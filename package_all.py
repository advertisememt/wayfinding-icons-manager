import os
import zipfile
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIST_DIR = os.path.join(BASE_DIR, "dist")
ZIP_PATH = os.path.join(DIST_DIR, "wayfinding-icons.zip")

print("Packaging all 10 sets into wayfinding-icons.zip...")

file_count = 0
with zipfile.ZipFile(ZIP_PATH, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # 1. SVGs: line, solid, duotone, tactical, gf-example, m3, lucide, tabler
    for folder in ['line', 'solid', 'duotone', 'tactical', 'gf-example', 'm3', 'lucide', 'tabler']:
        svg_files = glob.glob(os.path.join(BASE_DIR, 'svg', folder, '*.svg'))
        for f in svg_files:
            rel = os.path.relpath(f, BASE_DIR).replace('\\', '/')
            zipf.write(f, arcname=rel)
            file_count += 1
            
    # 2. PNGs: png (squircle) and png-circle (puck)
    for folder in ['png', 'png-circle']:
        png_files = glob.glob(os.path.join(BASE_DIR, folder, '*.png'))
        for f in png_files:
            rel = os.path.relpath(f, BASE_DIR).replace('\\', '/')
            zipf.write(f, arcname=rel)
            file_count += 1

    # 3. Dist assets: sprites, css, js, json
    dist_files = [
        'wayfinding-icons-line.svg',
        'wayfinding-icons-solid.svg',
        'wayfinding-icons-duotone.svg',
        'wayfinding-icons-tactical.svg',
        'wayfinding-icons-gf-example.svg',
        'wayfinding-icons-m3.svg',
        'wayfinding-icons-lucide.svg',
        'wayfinding-icons-tabler.svg',
        'wayfinding-icons.svg',
        'wayfinding-icons.css',
        'wayfinding-icons.js',
        'wayfinding-icons.json'
    ]
    for df in dist_files:
        p = os.path.join(DIST_DIR, df)
        if os.path.exists(p):
            zipf.write(p, arcname=f"dist/{df}")
            file_count += 1

    # 4. Docs & showcase
    for doc in ['README.md', 'index.html']:
        p = os.path.join(BASE_DIR, doc)
        if os.path.exists(p):
            zipf.write(p, arcname=doc)
            file_count += 1

size_kb = os.path.getsize(ZIP_PATH) / 1024
print(f"Packaged {file_count} files into {ZIP_PATH} ({size_kb:.1f} KB)")
