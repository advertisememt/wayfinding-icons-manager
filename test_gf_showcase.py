import asyncio
import os
from playwright.async_api import async_playwright

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = f"file:///{os.path.join(BASE_DIR, 'index.html').replace('\\', '/')}"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, channel="chrome")
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        
        errors = []
        page.on("pageerror", lambda err: errors.append(str(err)))
        page.on("console", lambda msg: errors.append(f"console error: {msg.text}") if msg.type == "error" else None)
        
        print("Navigating to index.html...")
        await page.goto(HTML_PATH)
        await page.wait_for_timeout(1000)
        
        title = await page.title()
        print(f"Page title: {title}")
        
        # Check dropdown options
        options = await page.eval_on_selector_all("#set-select option", "opts => opts.map(o => ({ value: o.value, text: o.text }))")
        print(f"Dropdown options: {[o['text'] for o in options]}")
        gf_opt = next((o for o in options if o["value"] == "gf-example"), None)
        assert gf_opt is not None, "GF example icons option not found!"
        assert "GF example icons" in gf_opt["text"]
        
        # Select GF example icons
        print("Selecting 'gf-example'...")
        await page.select_option("#set-select", "gf-example")
        await page.wait_for_timeout(800)
        
        # Check visible count
        visible_count = await page.text_content("#visible-count")
        print(f"Visible count: {visible_count}")
        assert visible_count == "80"
        
        # Check cards count and material-symbols-outlined element
        cards_count = await page.locator(".icon-card").count()
        assert cards_count == 80
        symbols_count = await page.locator(".icon-card .material-symbols-outlined").count()
        assert symbols_count == 80
        print(f"Rendered {symbols_count} material symbols across 80 cards")
        
        # Locate wf-lift card specifically
        lift_card = page.locator(".icon-card:has(.icon-id:has-text('wf-lift'))")
        assert await lift_card.count() > 0, "wf-lift card not found!"
        lift_symbol = await lift_card.locator(".material-symbols-outlined").text_content()
        lift_id_label = await lift_card.locator(".icon-id").text_content()
        print(f"wf-lift rendered symbol: '{lift_symbol}', label: '{lift_id_label}'")
        assert lift_symbol == "elevator", f"Expected elevator for lift, got {lift_symbol}"
        assert "GF: elevator" in lift_id_label
        
        # Take showcase screenshot in default mode
        screenshot_path = os.path.join(BASE_DIR, "gf_showcase.png")
        await page.screenshot(path=screenshot_path)
        print(f"Saved GF showcase screenshot to {screenshot_path}")
        
        # Test color swatches: Click Platinum #E3E3E3 swatch (from user URL)
        print("Testing #e3e3e3 swatch...")
        e3_swatch = page.locator(".color-swatch[data-color='#e3e3e3']")
        assert await e3_swatch.count() > 0, "#e3e3e3 swatch not found!"
        await e3_swatch.click()
        await page.wait_for_timeout(400)
        
        # Test size slider up to 150px (from user URL: icon.size=150)
        print("Testing size slider to 150px...")
        await page.evaluate("""() => {
            const slider = document.getElementById('size-slider');
            slider.value = 150;
            slider.dispatchEvent(new Event('input'));
        }""")
        await page.wait_for_timeout(500)
        
        size_label = await page.text_content("#size-label")
        print(f"Size label: {size_label}")
        assert size_label == "150px"
        
        # Take screenshot of 150px size with #e3e3e3 color
        screenshot_150px = os.path.join(BASE_DIR, "gf_150px_e3e3e3.png")
        await page.screenshot(path=screenshot_150px)
        print(f"Saved 150px screenshot to {screenshot_150px}")
        
        # Test clicking wf-lift card to open modal
        print("Opening modal for wf-lift...")
        await lift_card.click()
        await page.wait_for_timeout(500)
        
        modal_active = await page.eval_on_selector("#modal-overlay", "el => el.classList.contains('active')")
        assert modal_active
        
        modal_title = await page.text_content("#modal-title")
        modal_id = await page.text_content("#modal-id")
        modal_svg_code = await page.text_content("#modal-svg-code")
        modal_usage_code = await page.text_content("#modal-usage-code")
        
        print(f"Modal title: {modal_title}")
        print(f"Modal ID label: {modal_id}")
        print(f"Modal tag code: {modal_svg_code}")
        print(f"Modal usage code:\n{modal_usage_code}")
        
        assert "elevator" in modal_title
        assert '<span class="material-symbols-outlined">elevator</span>' == modal_svg_code
        assert "Material+Symbols+Outlined:elevator" in modal_usage_code
        
        # Take modal screenshot
        screenshot_modal = os.path.join(BASE_DIR, "gf_modal.png")
        await page.screenshot(path=screenshot_modal)
        print(f"Saved GF modal screenshot to {screenshot_modal}")
        
        await page.click("#modal-close")
        await page.wait_for_timeout(300)
        
        print(f"Total console/page errors: {len(errors)}")
        if errors:
            print("Errors encountered:", errors)
            raise AssertionError(f"Errors found: {errors}")
            
        print("ALL GF TESTS PASSED WITH 0 ERRORS!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
