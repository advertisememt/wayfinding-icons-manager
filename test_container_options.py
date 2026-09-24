"""Playwright test for Container Shape selection: Tile, Outline, Circle."""
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel="chrome", headless=True)
        page = await browser.new_page()

        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)

        file_url = "file:///C:/Users/Marco/.gemini/antigravity/scratch/wayfinding-icons/index.html"
        await page.goto(file_url, wait_until="networkidle")

        # 1. Verify container buttons exist
        cb_none = page.locator("#cb-none")
        cb_tile = page.locator("#cb-tile")
        cb_outline = page.locator("#cb-outline")
        cb_circle = page.locator("#cb-circle")

        assert await cb_none.count() == 1, "None button not found"
        assert await cb_tile.count() == 1, "Tile button not found"
        assert await cb_outline.count() == 1, "Outline button not found"
        assert await cb_circle.count() == 1, "Circle button not found"
        print("[OK] All 4 container buttons exist")

        # 2. Select M3 set
        await page.select_option("#set-select", "m3")
        await page.wait_for_timeout(300)

        # 3. Click Tile
        await cb_tile.click()
        await page.wait_for_timeout(300)
        tile_badges = await page.locator("#icons-grid .icon-badge-wrap.badge-tile").count()
        assert tile_badges == 80, f"Expected 80 tile badges, found {tile_badges}"
        print(f"[OK] Tile container verified: {tile_badges} badges rendered")

        # 4. Click Outline
        await cb_outline.click()
        await page.wait_for_timeout(300)
        outline_badges = await page.locator("#icons-grid .icon-badge-wrap.badge-outline").count()
        assert outline_badges == 80, f"Expected 80 outline badges, found {outline_badges}"
        print(f"[OK] Outline container verified: {outline_badges} badges rendered")

        # 5. Click Circle
        await cb_circle.click()
        await page.wait_for_timeout(300)
        circle_badges = await page.locator("#icons-grid .icon-badge-wrap.badge-circle").count()
        assert circle_badges == 80, f"Expected 80 circle badges, found {circle_badges}"
        print(f"[OK] Circle container verified: {circle_badges} badges rendered")

        # 6. Test with GF Example icons
        await page.select_option("#set-select", "gf-example")
        await page.wait_for_timeout(300)
        gf_circle_badges = await page.locator("#icons-grid .icon-badge-wrap.badge-circle").count()
        assert gf_circle_badges == 80, f"Expected 80 circle badges on GF set, found {gf_circle_badges}"
        print(f"[OK] Container shape works across sets (GF Example verified)")

        # 7. Test with Modern Line SVG
        await page.select_option("#set-select", "line")
        await cb_tile.click()
        await page.wait_for_timeout(300)
        line_tile_badges = await page.locator("#icons-grid .icon-badge-wrap.badge-tile").count()
        assert line_tile_badges == 80, f"Expected 80 tile badges on Line set, found {line_tile_badges}"
        print(f"[OK] Container shape works on Modern Line set")

        # 8. Test Modal preview
        first_card = page.locator(".icon-card").first
        await first_card.click()
        await page.wait_for_timeout(300)
        modal_overlay = page.locator("#modal-overlay")
        assert await modal_overlay.is_visible(), "Modal did not open"
        modal_badge = await page.locator("#modal-preview .icon-badge-wrap.badge-tile").count()
        assert modal_badge == 1, "Modal preview does not have container badge"
        print("[OK] Modal preview with container verified")

        # Close modal
        await page.click("#modal-close")
        await page.wait_for_timeout(200)

        # 9. Click None to return to uncontained
        await cb_none.click()
        await page.wait_for_timeout(300)
        none_badges = await page.locator("#icons-grid .icon-badge-wrap").count()
        assert none_badges == 0, f"Expected 0 badges in None mode, found {none_badges}"
        print("[OK] Reset to None container verified")

        assert len(errors) == 0, f"Console errors detected: {errors}"
        print(f"[OK] 0 console errors detected")

        await browser.close()
        print("\nAll Container Shape tests PASSED! Successfully verified.")

if __name__ == "__main__":
    asyncio.run(main())
