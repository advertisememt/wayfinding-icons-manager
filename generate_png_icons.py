import os
import json
import time
import re
from playwright.sync_api import sync_playwright

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, "dist", "wayfinding-icons.json")
out_dir = os.path.join(BASE_DIR, "png")
os.makedirs(out_dir, exist_ok=True)

with open(json_path, "r", encoding="utf-8") as f:
    icons = json.load(f)

THEMES = {
    "Navigation": {
        "c1": "#0284c7", "c2": "#0369a1", "c3": "#075985",
        "shadow": "rgba(2, 132, 199, 0.45)"
    },
    "Building": {
        "c1": "#0d9488", "c2": "#0f766e", "c3": "#115e59",
        "shadow": "rgba(13, 148, 136, 0.45)"
    },
    "ExitGreen": {
        "c1": "#10b981", "c2": "#059669", "c3": "#047857",
        "shadow": "rgba(16, 185, 129, 0.45)"
    },
    "Amenities": {
        "c1": "#6366f1", "c2": "#4f46e5", "c3": "#3730a3",
        "shadow": "rgba(99, 102, 241, 0.45)"
    },
    "Dining": {
        "c1": "#ea580c", "c2": "#c2410c", "c3": "#9a3412",
        "shadow": "rgba(234, 88, 12, 0.45)"
    },
    "Transit": {
        "c1": "#0891b2", "c2": "#0e7490", "c3": "#155e75",
        "shadow": "rgba(8, 145, 178, 0.45)"
    },
    "Healthcare": {
        "c1": "#2563eb", "c2": "#1d4ed8", "c3": "#1e40af",
        "shadow": "rgba(37, 99, 235, 0.45)"
    },
    "Safety": {
        "c1": "#dc2626", "c2": "#b91c1c", "c3": "#991b1b",
        "shadow": "rgba(220, 38, 38, 0.45)"
    },
    "Caution": {
        "c1": "#d97706", "c2": "#b45309", "c3": "#92400e",
        "shadow": "rgba(217, 119, 6, 0.45)"
    },
    "Services": {
        "c1": "#7c3aed", "c2": "#6d28d9", "c3": "#5b21b6",
        "shadow": "rgba(124, 58, 237, 0.45)"
    },
    "Campus": {
        "c1": "#0284c7", "c2": "#0369a1", "c3": "#075985",
        "shadow": "rgba(2, 132, 199, 0.45)"
    },
    "UI": {
        "c1": "#334155", "c2": "#1e293b", "c3": "#0f172a",
        "shadow": "rgba(15, 23, 42, 0.55)"
    },
    "Media": {
        "c1": "#475569", "c2": "#334155", "c3": "#1e293b",
        "shadow": "rgba(30, 41, 59, 0.55)"
    }
}

def get_theme(icon):
    cid = icon["id"]
    cat = icon.get("category", "Navigation")
    if cid == "wf-exit":
        return THEMES["ExitGreen"]
    if cid in ["wf-cafe", "wf-food"]:
        return THEMES["Dining"]
    if cid in ["wf-warning", "wf-construction"]:
        return THEMES["Caution"]
    if cid in ["wf-emergency", "wf-evacuate", "wf-fire", "wf-no-entry", "wf-prohibited", "wf-staff-only"]:
        return THEMES["Safety"]
    return THEMES.get(cat, THEMES["Navigation"])

def generate_all():
    print(f"Generating 3D tactile PNG badges for {len(icons)} wayfinding icons...")

    batch_size = 40
    total_time = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)
        page = browser.new_page(viewport={"width": 2400, "height": 3000}, device_scale_factor=1)

        for batch_idx in range(0, len(icons), batch_size):
            batch = icons[batch_idx:batch_idx + batch_size]
            t0 = time.time()

            badges_html = []
            for icon in batch:
                theme = get_theme(icon)
                # Replace white contrast/cutout elements with the badge's dark base color
                paths = icon["paths_solid"]
                paths = re.sub(r'fill=["\']#fff(fff)?["\']', f'fill="{theme["c3"]}"', paths, flags=re.IGNORECASE)
                paths = re.sub(r'fill=["\']white["\']', f'fill="{theme["c3"]}"', paths, flags=re.IGNORECASE)
                paths = re.sub(r'stroke=["\']#fff(fff)?["\']', f'stroke="{theme["c3"]}"', paths, flags=re.IGNORECASE)
                paths = re.sub(r'stroke=["\']white["\']', f'stroke="{theme["c3"]}"', paths, flags=re.IGNORECASE)

                badges_html.append(f'''
                <div id="wrap-{icon['id']}" class="badge-wrapper">
                  <div class="badge" style="background: linear-gradient(145deg, {theme['c1']} 0%, {theme['c2']} 55%, {theme['c3']} 100%); box-shadow: 0 16px 34px -4px {theme['shadow']}, 0 6px 14px -2px rgba(0, 0, 0, 0.4), inset 0 2px 2px rgba(255, 255, 255, 0.7), inset 0 -2px 4px rgba(0, 0, 0, 0.4);">
                    <div class="gloss"></div>
                    <div class="glyph">
                      <svg viewBox="0 0 24 24" fill="#ffffff">{paths}</svg>
                    </div>
                  </div>
                </div>''')

            html_content = f'''<!DOCTYPE html>
            <html>
            <head>
            <meta charset="UTF-8">
            <style>
            body {{ margin: 0; background: transparent; padding: 0; display: flex; flex-wrap: wrap; }}
            .badge-wrapper {{
              width: 256px;
              height: 256px;
              display: flex;
              align-items: center;
              justify-content: center;
              background: transparent;
              position: relative;
            }}
            .badge {{
              width: 204px;
              height: 204px;
              border-radius: 48px;
              position: relative;
              overflow: hidden;
              display: flex;
              align-items: center;
              justify-content: center;
            }}
            .gloss {{
              position: absolute;
              top: 0; left: 0; right: 0; height: 50%;
              background: linear-gradient(180deg, rgba(255,255,255,0.42) 0%, rgba(255,255,255,0.08) 75%, transparent 100%);
              border-radius: 48px 48px 120px 120px / 48px 48px 32px 32px;
              pointer-events: none;
            }}
            .glyph {{
              width: 104px;
              height: 104px;
              color: #ffffff;
              filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.35)) drop-shadow(0 -1px 0 rgba(255, 255, 255, 0.3));
              position: relative;
              z-index: 2;
              display: flex;
              align-items: center;
              justify-content: center;
            }}
            .glyph svg {{
              width: 100%;
              height: 100%;
            }}
            </style>
            </head>
            <body>
            {''.join(badges_html)}
            </body>
            </html>'''

            temp_html = os.path.join(BASE_DIR, "png", f"_batch_{batch_idx}.html")
            with open(temp_html, "w", encoding="utf-8") as f:
                f.write(html_content)

            page.goto(f"file:///{temp_html.replace(chr(92), '/')}")

            for icon in batch:
                target_png = os.path.join(out_dir, f"{icon['id']}.png")
                page.locator(f"#wrap-{icon['id']}").screenshot(path=target_png, omit_background=True)

            try:
                os.remove(temp_html)
            except Exception:
                pass

            dt = time.time() - t0
            total_time += dt
            print(f"Batch {batch_idx // batch_size + 1}: {len(batch)} icons rendered in {dt:.2f}s")

        browser.close()

    print(f"Successfully generated all {len(icons)} PNG icons in {total_time:.2f}s!")

if __name__ == "__main__":
    generate_all()
