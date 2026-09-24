import os
import json
import time
import re
from playwright.sync_api import sync_playwright

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, "dist", "wayfinding-icons.json")
out_dir = os.path.join(BASE_DIR, "png-circle")
os.makedirs(out_dir, exist_ok=True)

with open(json_path, "r", encoding="utf-8") as f:
    icons = json.load(f)

THEMES = {
    "Navigation": {
        "light": "#38bdf8", "mid": "#0284c7", "dark": "#075985",
        "shadow": "rgba(2, 132, 199, 0.5)"
    },
    "Building": {
        "light": "#14b8a6", "mid": "#0d9488", "dark": "#115e59",
        "shadow": "rgba(13, 148, 136, 0.5)"
    },
    "ExitGreen": {
        "light": "#34d399", "mid": "#10b981", "dark": "#064e3b",
        "shadow": "rgba(16, 185, 129, 0.5)"
    },
    "Amenities": {
        "light": "#818cf8", "mid": "#6366f1", "dark": "#3730a3",
        "shadow": "rgba(99, 102, 241, 0.5)"
    },
    "Dining": {
        "light": "#fb923c", "mid": "#ea580c", "dark": "#9a3412",
        "shadow": "rgba(234, 88, 12, 0.5)"
    },
    "Transit": {
        "light": "#22d3ee", "mid": "#0891b2", "dark": "#155e75",
        "shadow": "rgba(8, 145, 178, 0.5)"
    },
    "Healthcare": {
        "light": "#60a5fa", "mid": "#2563eb", "dark": "#1e40af",
        "shadow": "rgba(37, 99, 235, 0.5)"
    },
    "Safety": {
        "light": "#f87171", "mid": "#dc2626", "dark": "#991b1b",
        "shadow": "rgba(220, 38, 38, 0.5)"
    },
    "Caution": {
        "light": "#fbbf24", "mid": "#d97706", "dark": "#92400e",
        "shadow": "rgba(217, 119, 6, 0.5)"
    },
    "Services": {
        "light": "#a78bfa", "mid": "#7c3aed", "dark": "#5b21b6",
        "shadow": "rgba(124, 58, 237, 0.5)"
    },
    "Campus": {
        "light": "#38bdf8", "mid": "#0284c7", "dark": "#075985",
        "shadow": "rgba(2, 132, 199, 0.5)"
    },
    "UI": {
        "light": "#475569", "mid": "#1e293b", "dark": "#0f172a",
        "shadow": "rgba(15, 23, 42, 0.65)"
    },
    "Media": {
        "light": "#64748b", "mid": "#334155", "dark": "#1e293b",
        "shadow": "rgba(30, 41, 59, 0.65)"
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

def generate_all_pucks():
    print(f"Generating 3D Circular Kiosk Pucks for {len(icons)} wayfinding icons...")

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
                paths = icon["paths_solid"]
                paths = re.sub(r'fill=["\']#fff(fff)?["\']', f'fill="{theme["dark"]}"', paths, flags=re.IGNORECASE)
                paths = re.sub(r'fill=["\']white["\']', f'fill="{theme["dark"]}"', paths, flags=re.IGNORECASE)
                paths = re.sub(r'stroke=["\']#fff(fff)?["\']', f'stroke="{theme["dark"]}"', paths, flags=re.IGNORECASE)
                paths = re.sub(r'stroke=["\']white["\']', f'stroke="{theme["dark"]}"', paths, flags=re.IGNORECASE)

                badges_html.append(f'''
                <div id="wrap-{icon['id']}" class="puck-wrapper">
                  <div class="puck" style="background: radial-gradient(circle at 35% 25%, {theme['light']} 0%, {theme['mid']} 45%, {theme['dark']} 100%); box-shadow: 0 18px 36px -6px {theme['shadow']}, 0 8px 16px -4px rgba(0, 0, 0, 0.45), inset 0 2.5px 3px rgba(255, 255, 255, 0.8), inset 0 -3px 6px rgba(0, 0, 0, 0.5);">
                    <div class="gloss-dome"></div>
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
            .puck-wrapper {{
              width: 256px;
              height: 256px;
              display: flex;
              align-items: center;
              justify-content: center;
              background: transparent;
              position: relative;
            }}
            .puck {{
              width: 204px;
              height: 204px;
              border-radius: 50%;
              position: relative;
              overflow: hidden;
              display: flex;
              align-items: center;
              justify-content: center;
              border: 1.5px solid rgba(255, 255, 255, 0.3);
            }}
            .gloss-dome {{
              position: absolute;
              top: 4px; left: 14px; right: 14px; height: 48%;
              background: linear-gradient(180deg, rgba(255,255,255,0.5) 0%, rgba(255,255,255,0.08) 70%, transparent 100%);
              border-radius: 50% 50% 45% 45% / 70% 70% 30% 30%;
              pointer-events: none;
            }}
            .glyph {{
              width: 102px;
              height: 102px;
              color: #ffffff;
              filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.38)) drop-shadow(0 -1px 0 rgba(255, 255, 255, 0.3));
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

            temp_html = os.path.join(BASE_DIR, "png-circle", f"_batch_{batch_idx}.html")
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
            print(f"Batch {batch_idx // batch_size + 1}: {len(batch)} circular pucks rendered in {dt:.2f}s")

        browser.close()

    print(f"Successfully generated all {len(icons)} Circular Puck PNG icons in {total_time:.2f}s!")

if __name__ == "__main__":
    generate_all_pucks()
