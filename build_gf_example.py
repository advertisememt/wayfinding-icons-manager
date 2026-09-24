import os
import json
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SVG_GF_DIR = os.path.join(BASE_DIR, "svg", "gf-example")
DIST_DIR = os.path.join(BASE_DIR, "dist")

# Load existing metadata
json_path = os.path.join(DIST_DIR, "wayfinding-icons.json")
with open(json_path, "r", encoding="utf-8") as f:
    metadata = json.load(f)

# The mapping verified earlier
from verify_and_build_gf import GF_MAPPING

gf_paths = {}
for icon_id, symbol in GF_MAPPING.items():
    svg_file = os.path.join(SVG_GF_DIR, f"{icon_id}.svg")
    with open(svg_file, "r", encoding="utf-8") as f:
        content = f.read()
    # Extract path or inner contents of svg
    match = re.search(r'<svg[^>]*>(.*?)</svg>', content, re.DOTALL)
    if match:
        inner = match.group(1).strip()
    else:
        inner = content
    gf_paths[icon_id] = inner

# 1. Update metadata with gf_symbol and paths_gf_example
for item in metadata:
    icon_id = item["id"]
    item["gf_symbol"] = GF_MAPPING.get(icon_id, "")
    item["paths_gf_example"] = gf_paths.get(icon_id, "")

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2)
print("Updated wayfinding-icons.json with gf_symbol and paths_gf_example")

# 2. Build SVG sprite sheet: dist/wayfinding-icons-gf-example.svg
sprite_path = os.path.join(DIST_DIR, "wayfinding-icons-gf-example.svg")
with open(sprite_path, "w", encoding="utf-8") as f:
    f.write('<svg xmlns="http://www.w3.org/2000/svg" style="display: none;">\n')
    for icon_id, symbol in GF_MAPPING.items():
        inner = gf_paths.get(icon_id, '')
        f.write(f'  <symbol id="{icon_id}" viewBox="0 -960 960 960">\n    {inner}\n  </symbol>\n')
    f.write('</svg>\n')
print(f"Generated {sprite_path}")

# 3. Update dist/wayfinding-icons.js
js_path = os.path.join(DIST_DIR, "wayfinding-icons.js")
with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

# Add export const WAYFINDING_GF_EXAMPLE and mapping
gf_dict_str = json.dumps(gf_paths, indent=2)
mapping_dict_str = json.dumps(GF_MAPPING, indent=2)

gf_export_code = f"""
export const GOOGLE_FONTS_SYMBOL_MAPPING = {mapping_dict_str};

export const WAYFINDING_GF_EXAMPLE = {gf_dict_str};
"""

# Insert before WAYFINDING_TACTICAL or at end of exports
if "export const WAYFINDING_GF_EXAMPLE" not in js_content:
    # insert before renderWayfindingIcon
    marker = "export function renderWayfindingIcon"
    idx = js_content.find(marker)
    if idx != -1:
        js_content = js_content[:idx] + gf_export_code + "\n" + js_content[idx:]
    else:
        js_content += gf_export_code

# Update renderWayfindingIcon to handle 'gf-example'
old_render = 'if (set === \'tactical\') {'
new_render = """if (set === 'gf-example') {
    const paths = WAYFINDING_GF_EXAMPLE[iconId] || '';
    return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 -960 960 960" fill="currentColor" class="wf-icon wf-icon-gf ${iconId} ${className}">${paths}</svg>`;
  }
  if (set === 'tactical') {"""
if old_render in js_content and "set === 'gf-example'" not in js_content:
    js_content = js_content.replace(old_render, new_render, 1)

# Update Web Component to handle 'gf-example'
old_wc = "} else if (set === 'tactical') {"
new_wc = """} else if (set === 'gf-example') {
      const paths = WAYFINDING_GF_EXAMPLE[name] || '';
      this.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 -960 960 960" fill="currentColor" class="wf-icon wf-icon-gf ${name}">${paths}</svg>`;
    } else if (set === 'tactical') {"""
if old_wc in js_content and "set === 'gf-example'" not in js_content:
    js_content = js_content.replace(old_wc, new_wc, 1)

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_content)
print("Updated wayfinding-icons.js with WAYFINDING_GF_EXAMPLE")

# 4. Update dist/wayfinding-icons.css
css_path = os.path.join(DIST_DIR, "wayfinding-icons.css")
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

if ".wf-icon-gf" not in css_content:
    css_append = """
/* Google Fonts Material Symbols Outlined Set */
.wf-icon-gf {
  display: inline-block;
  width: 1em;
  height: 1em;
  fill: currentColor;
  vertical-align: -0.15em;
}

.material-symbols-outlined {
  font-family: 'Material Symbols Outlined';
  font-weight: normal;
  font-style: normal;
  font-size: 24px;
  line-height: 1;
  letter-spacing: normal;
  text-transform: none;
  display: inline-block;
  white-space: nowrap;
  word-wrap: normal;
  direction: ltr;
  -webkit-font-feature-settings: 'liga';
  -webkit-font-smoothing: antialiased;
}
"""
    with open(css_path, "a", encoding="utf-8") as f:
        f.write(css_append)
    print("Updated wayfinding-icons.css with .wf-icon-gf and .material-symbols-outlined")
