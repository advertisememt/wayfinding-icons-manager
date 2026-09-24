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
        
        # Check title
        title = await page.title()
        print(f"Page title: {title}")
        
        # Check set select options
        options = await page.eval_on_selector_all("#set-select option", "opts => opts.map(o => ({ value: o.value, text: o.text }))")
        print(f"Dropdown options: {options}")
        tactical_opt = next((o for o in options if o["value"] == "tactical"), None)
        assert tactical_opt is not None, "Tactical option not found in dropdown!"
        
        # Switch to tactical
        print("Selecting 'tactical' set...")
        await page.select_option("#set-select", "tactical")
        await page.wait_for_timeout(500)
        
        # Verify count
        visible_count = await page.text_content("#visible-count")
        print(f"Visible icons count: {visible_count}")
        assert visible_count == "80", f"Expected 80 icons, got {visible_count}"
        
        # Verify tactical svg elements exist in cards
        cards_count = await page.locator(".icon-card").count()
        print(f"Rendered cards: {cards_count}")
        assert cards_count == 80
        
        first_svg = page.locator(".icon-card svg.wf-icon-tactical").first
        assert await first_svg.count() > 0, "wf-icon-tactical not rendered in cards!"
        
        # Take full showcase screenshot with tactical icons
        screenshot_path = os.path.join(BASE_DIR, "tactical_showcase.png")
        await page.screenshot(path=screenshot_path)
        print(f"Saved showcase screenshot to {screenshot_path}")
        
        # Test custom hex recolor: change color to #10b981 (Emerald)
        print("Testing custom hex recoloring (#10B981)...")
        await page.fill("#hex-color-input", "#10B981")
        await page.wait_for_timeout(500)
        
        # Verify --wf-accent on first card
        style_attr = await page.locator(".icon-card svg.wf-icon-tactical").first.get_attribute("style")
        print(f"First card style: {style_attr}")
        assert "#10b981" in style_attr.lower(), f"Expected #10b981 in style, got {style_attr}"
        
        # Test 150px slider
        print("Testing size slider to 150px...")
        await page.evaluate("""() => {
            const slider = document.getElementById('size-slider');
            slider.value = 120;
            slider.dispatchEvent(new Event('input'));
        }""")
        await page.wait_for_timeout(500)
        
        size_label = await page.text_content("#size-label")
        print(f"Size label: {size_label}")
        
        # Screenshot with large size and green accent
        screenshot_large_path = os.path.join(BASE_DIR, "tactical_large.png")
        await page.screenshot(path=screenshot_large_path)
        print(f"Saved large screenshot to {screenshot_large_path}")
        
        # Reset slider back to 48px and color to default (#f59e0b)
        await page.evaluate("""() => {
            const slider = document.getElementById('size-slider');
            slider.value = 48;
            slider.dispatchEvent(new Event('input'));
            const defaultSwatch = document.querySelector('.color-swatch[data-color="default"]');
            if (defaultSwatch) defaultSwatch.click();
        }""")
        await page.wait_for_timeout(500)
        
        # Test modal opening
        print("Testing modal click on first card (wf-arrow-up)...")
        await page.locator(".icon-card").first.click()
        await page.wait_for_timeout(500)
        
        modal_active = await page.eval_on_selector("#modal-overlay", "el => el.classList.contains('active')")
        assert modal_active, "Modal did not open!"
        
        modal_title = await page.text_content("#modal-title")
        modal_svg_code = await page.text_content("#modal-svg-code")
        modal_usage_code = await page.text_content("#modal-usage-code")
        print(f"Modal title: {modal_title}")
        print(f"Usage tag snippet: {modal_usage_code[:80]}...")
        assert "Tactical Cyber" in modal_title
        assert 'set="tactical"' in modal_usage_code
        assert "wf-icon-tactical" in modal_svg_code
        
        # Screenshot modal
        modal_screenshot_path = os.path.join(BASE_DIR, "tactical_modal.png")
        await page.screenshot(path=modal_screenshot_path)
        print(f"Saved modal screenshot to {modal_screenshot_path}")
        
        await page.click("#modal-close")
        await page.wait_for_timeout(300)
        
        # Check errors
        print(f"Total console/page errors: {len(errors)}")
        if errors:
            print("Errors encountered:", errors)
            raise AssertionError(f"Console/page errors found: {errors}")
            
        print("ALL TESTS PASSED SUCCESSFULLY!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
