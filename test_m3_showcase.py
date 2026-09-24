import asyncio
import os
from playwright.async_api import async_playwright

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_URL = f"file:///{os.path.join(BASE_DIR, 'index.html').replace(os.sep, '/')}"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel="chrome", headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 1000})

        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)

        print(f"Loading {INDEX_URL}...")
        await page.goto(INDEX_URL)
        await page.wait_for_selector(".icon-card")

        # 1. Verify all 10 options in #set-select
        options = await page.eval_on_selector_all("#set-select option", "opts => opts.map(o => ({ value: o.value, text: o.text }))")
        print(f"Found {len(options)} options in #set-select:")
        for o in options:
            print(f"  - {o['value']}: {o['text']}")
        assert len(options) == 10, f"Expected 10 options, got {len(options)}"
        m3_opt = next((o for o in options if o["value"] == "m3"), None)
        assert m3_opt is not None, "Missing 'm3' option in dropdown!"
        print("M3 option verified in dropdown.")

        # 2. Select 'm3'
        print("Selecting 'm3' style set...")
        await page.select_option("#set-select", "m3")
        await page.wait_for_timeout(300)

        # Verify set label
        set_label = await page.text_content("#current-set-label")
        print(f"Current set label: {set_label}")
        assert "Material 3" in set_label, f"Unexpected set label: {set_label}"

        # Verify card count
        cards = await page.query_selector_all(".icon-card")
        print(f"Card count for M3 set: {len(cards)}")
        assert len(cards) == 80, f"Expected 80 cards, got {len(cards)}"

        # Verify SVGs inside cards
        m3_svgs = await page.query_selector_all(".icon-card .icon-preview.m3-mode svg.wf-icon-m3")
        print(f"M3 SVGs rendered: {len(m3_svgs)}")
        assert len(m3_svgs) == 80, f"Expected 80 M3 SVGs, got {len(m3_svgs)}"

        # Verify stroke control is active
        stroke_opacity = await page.eval_on_selector("#stroke-control-group", "el => window.getComputedStyle(el).opacity")
        print(f"Stroke control opacity for M3: {stroke_opacity}")
        assert stroke_opacity == "1", f"Expected stroke control opacity 1, got {stroke_opacity}"

        # Take screenshot of M3 showcase at default 40px
        await page.screenshot(path=os.path.join(BASE_DIR, "m3_showcase.png"))
        print("Saved m3_showcase.png")

        # 3. Test Display Size scaling to 150px
        print("Testing 150px slider scaling...")
        await page.evaluate("""() => {
            const slider = document.getElementById('size-slider');
            slider.value = 150;
            slider.dispatchEvent(new Event('input'));
        }""")
        await page.wait_for_timeout(300)

        size_label = await page.text_content("#size-label")
        print(f"Size label: {size_label}")
        assert size_label == "150px", f"Expected 150px, got {size_label}"

        # Recolor with an emerald green hex
        print("Testing hex recolor to #10b981...")
        await page.evaluate("""() => {
            const input = document.getElementById('hex-color-input');
            input.value = '#10B981';
            input.dispatchEvent(new Event('input'));
        }""")
        await page.wait_for_timeout(300)

        await page.screenshot(path=os.path.join(BASE_DIR, "m3_150px_recolored.png"))
        print("Saved m3_150px_recolored.png")

        # Reset size back to 48px
        await page.evaluate("""() => {
            const slider = document.getElementById('size-slider');
            slider.value = 48;
            slider.dispatchEvent(new Event('input'));
        }""")
        await page.wait_for_timeout(200)

        # 4. Test Modal dialog
        print("Testing card modal click...")
        # Re-query card after recolor re-render
        target_card = await page.query_selector(".icon-card")
        await target_card.click()
        await page.wait_for_selector(".modal-overlay.active")

        modal_title = await page.text_content("#modal-title")
        modal_id = await page.text_content("#modal-id")
        modal_code1 = await page.text_content("#modal-svg-code")
        modal_code2 = await page.text_content("#modal-usage-code")
        modal_download = await page.get_attribute("#modal-download", "href")

        print(f"Modal title: {modal_title}")
        print(f"Modal ID: {modal_id}")
        print(f"Modal download href: {modal_download}")
        assert "Material 3" in modal_title or "Material 3" in modal_id
        assert "dist/wayfinding-icons-m3.svg" in modal_code2
        assert "set=\"m3\"" in modal_code2
        assert modal_download.startswith("svg/m3/")

        await page.screenshot(path=os.path.join(BASE_DIR, "m3_modal.png"))
        print("Saved m3_modal.png")

        # Close modal
        await page.click("#modal-close")
        await page.wait_for_timeout(200)

        # Check for any console errors
        print(f"Console errors recorded: {len(console_errors)}")
        if console_errors:
            print("Errors:", console_errors)
        assert len(console_errors) == 0, f"Expected 0 console errors, got {len(console_errors)}"

        await browser.close()
        print("\nALL PLAYWRIGHT TESTS PASSED FOR MATERIAL 3 ICON SET!")

if __name__ == "__main__":
    asyncio.run(main())
