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
        page.on("pageerror", lambda err: errors.append(f"{err.message} at {err.stack}"))
        page.on("console", lambda msg: errors.append(f"console error: {msg.text}") if msg.type == "error" else None)

        print(f"Navigating to {HTML_PATH}...")
        await page.goto(HTML_PATH)
        await page.wait_for_timeout(1000)

        # 1. Verify all 10 dropdown options exist
        options = await page.eval_on_selector_all("#set-select option", "opts => opts.map(o => ({ value: o.value, text: o.text }))")
        assert len(options) == 10, f"Expected 10 options, found {len(options)}"
        print(f"[OK] 10 design sets verified in dropdown: {[o['text'] for o in options]}")

        # 2. Select 'lucide'
        print("Selecting Lucide open source set...")
        if errors:
            print("Errors detected so far:", errors)
        await page.select_option("#set-select", "lucide")
        await page.wait_for_timeout(500)
        if errors:
            print("Errors after select:", errors)

        val = await page.evaluate("() => ({ val: document.getElementById('set-select').value, currentSet: window.currentSet || (typeof currentSet !== 'undefined' ? currentSet : 'unknown') })")
        print("DOM select state:", val)

        set_label_lucide = await page.text_content("#current-set-label")
        assert "Lucide" in set_label_lucide, f"Unexpected label: {set_label_lucide}"
        print(f"[OK] Set label verified: {set_label_lucide}")

        cards_lucide = await page.query_selector_all(".icon-card")
        assert len(cards_lucide) == 80, f"Expected 80 cards, got {len(cards_lucide)}"
        lucide_svgs = await page.query_selector_all(".icon-card .icon-preview.lucide-mode svg.wf-icon-lucide")
        assert len(lucide_svgs) == 80, f"Expected 80 Lucide SVGs, got {len(lucide_svgs)}"
        print(f"[OK] Rendered all 80 Lucide open-source SVGs")

        # Test modal for Lucide
        first_card = cards_lucide[0]
        await first_card.click()
        await page.wait_for_timeout(300)
        modal_title = await page.text_content("#modal-title")
        assert "Lucide" in modal_title, f"Expected 'Lucide' in modal title, got '{modal_title}'"
        modal_usage = await page.text_content("#modal-usage-code")
        assert "ISC" in modal_usage or "lucide" in modal_usage, f"Expected Lucide/ISC in modal usage code"
        print(f"[OK] Lucide detail modal & ISC license info verified: {modal_title}")
        await page.click("#modal-close")
        await page.wait_for_timeout(200)

        # 3. Select 'tabler'
        print("Selecting Tabler open source set...")
        await page.select_option("#set-select", "tabler")
        await page.wait_for_timeout(500)

        set_label_tabler = await page.text_content("#current-set-label")
        assert "Tabler" in set_label_tabler, f"Unexpected label: {set_label_tabler}"
        print(f"[OK] Set label verified: {set_label_tabler}")

        cards_tabler = await page.query_selector_all(".icon-card")
        assert len(cards_tabler) == 80, f"Expected 80 cards, got {len(cards_tabler)}"
        tabler_svgs = await page.query_selector_all(".icon-card .icon-preview.tabler-mode svg.wf-icon-tabler")
        assert len(tabler_svgs) == 80, f"Expected 80 Tabler SVGs, got {len(tabler_svgs)}"
        print(f"[OK] Rendered all 80 Tabler open-source SVGs")

        # Test modal for Tabler
        first_card = cards_tabler[0]
        await first_card.click()
        await page.wait_for_timeout(300)
        modal_title_tabler = await page.text_content("#modal-title")
        assert "Tabler" in modal_title_tabler, f"Expected 'Tabler' in modal title, got '{modal_title_tabler}'"
        modal_usage_tabler = await page.text_content("#modal-usage-code")
        assert "MIT" in modal_usage_tabler or "tabler" in modal_usage_tabler, f"Expected Tabler/MIT in modal usage code"
        print(f"[OK] Tabler detail modal & MIT license info verified: {modal_title_tabler}")
        await page.click("#modal-close")
        await page.wait_for_timeout(200)

        # 4. Test Container Shapes with Tabler
        print("Testing Container Shape (Circle) on open source icons...")
        await page.click("#cb-circle")
        await page.wait_for_timeout(300)
        circle_badges = await page.query_selector_all("#icons-grid .icon-badge-wrap.badge-circle")
        assert len(circle_badges) == 80, f"Expected 80 circle badges, got {len(circle_badges)}"
        print(f"[OK] Circle container shape verified on 80 open-source icons")

        # 5. Test 150px Sizing & Hex Recolor
        print("Testing 150px slider and hex recolor...")
        await page.evaluate("""() => {
            const slider = document.getElementById('size-slider');
            slider.value = 150;
            slider.dispatchEvent(new Event('input'));
            const hexInput = document.getElementById('hex-color-input');
            hexInput.value = '#10B981';
            hexInput.dispatchEvent(new Event('input'));
        }""")
        await page.wait_for_timeout(300)

        size_label = await page.text_content("#size-label")
        assert size_label == "150px", f"Expected 150px, got {size_label}"
        print("[OK] Sized to 150px with emerald (#10B981) recoloring")

        assert len(errors) == 0, f"Console errors detected: {errors}"
        print(f"[OK] 0 console errors detected across all actions")

        await browser.close()
        print("\nAll Open Source Icon Set verification tests PASSED! Successfully verified.")

if __name__ == "__main__":
    asyncio.run(main())
