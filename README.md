# Wayfinding Icons Manager (10 Design Sets • 800 Icons)

A comprehensive suite of **800 icons across 10 distinct design sets** (8 SVG/Vector sets + 2 PNG raster sets) crafted specifically for **touchscreen wayfinding kiosks**, directional totems, overhead signage, airports, campuses, and healthcare facilities.

All vector and raster sets are **100% open-source and free for commercial and personal use**.

---

## 10 Unique Design Sets

1. **Lucide Icons (Open Source - ISC/MIT License)** *(New!)*:
   - **Format:** Pure vector SVG on 24 × 24 dp canvas (`viewBox="0 0 24 24"`).
   - **License:** ISC License (Permissive open-source, 100% free for commercial & personal products).
   - **Design Aesthetic:** Community-driven evolution of Feather Icons. Ultra-clean, geometric, 2px stroke outlines with round linecaps and linejoins.
   - **Location:** `svg/lucide/` (80 files).

2. **Tabler Icons (Open Source - MIT License)** *(New!)*:
   - **Format:** Pure vector SVG on 24 × 24 dp canvas (`viewBox="0 0 24 24"`).
   - **License:** MIT License (100% free for commercial use).
   - **Design Aesthetic:** Crisp, highly consistent, rounded fillets and comprehensive wayfinding/facility coverage.
   - **Location:** `svg/tabler/` (80 files).

3. **Material Design 3 (M3 Clean Vector SVG)**:
   - **Format:** Pure vector SVG on standard 24 × 24 dp canvas with 20 × 20 dp live area (`viewBox="0 0 24 24"`).
   - **Design Aesthetic:** Strictly adheres to official Google Material 3 icon design principles with 2.0 dp standard stroke weight, keyline geometry, and interactive **Fill Axis toggle** (Outline FILL=0 vs. Filled FILL=1).
   - **Location:** `svg/m3/` (80 files).

4. **GF example icons (Google Fonts Material Symbols)**:
   - **Format:** Google Fonts Web Font (`Material Symbols Outlined`) & Vector SVG (`viewBox="0 -960 960 960"`).
   - **Design Aesthetic:** Official Google Fonts Material Symbols Outlined icons matched to all 80 wayfinding concepts.
   - **Location:** `svg/gf-example/` (80 files).

5. **Tactical Cyber / Chiseled Amber (Faceted SVG)**:
   - **Format:** Pure vector SVG with multifaceted geometric geometry (`viewBox="0 0 24 24"`).
   - **Design Aesthetic:** Low-poly faceted industrial wayfinding aesthetic inspired by chiseled dark slate bevels, gunmetal facet planes, and energetic radiant amber gold focal faces (`--wf-accent`).
   - **Location:** `svg/tactical/` (80 files).

6. **Duotone Pictograms (Two-Tone SVG)**:
   - **Format:** Pure vector SVG with semantic two-tone layering (`viewBox="0 0 24 24"`).
   - **Design Aesthetic:** Architectural dual-tone hierarchy featuring soft translucent tinting (`opacity="0.25"`) for contextual backplates and high-contrast foreground pictograms.
   - **Location:** `svg/duotone/` (80 files).

7. **3D Circular Pucks (PNG Images)**:
   - **Resolution:** 256 × 256 px 32-bit RGBA PNGs with transparent background.
   - **Design Aesthetic:** Circular touch hardware pucks with outer chamfer bezel ring, radial convex curvature, and top gloss dome highlight.
   - **Location:** `png-circle/` (80 files).

8. **3D Squircle Badges (PNG Images)**:
   - **Resolution:** 256 × 256 px 32-bit RGBA PNGs with transparent background.
   - **Design Aesthetic:** Continuous-corner squircle tiles, specular glossy reflection, inner rim highlight, and realistic drop shadow.
   - **Location:** `png/` (80 files).

9. **Solid Signage (Filled Silhouette SVG)**:
   - **Format:** Pure vector SVG with solid silhouette fills.
   - **Design Aesthetic:** High-contrast, bold, ISO/AIGA-inspired signage iconography optimized for long-distance legibility.
   - **Location:** `svg/solid/` (80 files).

10. **Modern Line (Outline SVG)**:
    - **Format:** 24 × 24 grid SVG with 2px stroke width, rounded caps, and joins.
    - **Design Aesthetic:** Contemporary, airy, minimalist vector style for interactive maps and dense UI layouts.
    - **Location:** `svg/line/` (80 files).

---

## Interactive Controls & Customization Engine

- **Container Shapes:** Frame any icon in **None**, **Tile** (rounded-rect tint), **Outline** (circular ring), or **Circle** (solid filled badge with white glyph).
- **Fill Axis (M3):** Toggle between **Outline** (FILL=0) and **Filled** (FILL=1) states.
- **Display Size Scaler:** Continuous slider from **24px to 150px**.
- **Stroke Width Slider:** Continuous stroke adjustment from **1.5px to 3.5px**.
- **Live Color & Hex Engine:** Swatches + custom 6-digit hex code picker + canvas PNG generator for live custom PNG downloads.
- **Search & Category Filtering:** Instant multi-field filtering across 10 categories and 80 icons.

---

## Directory Structure

```
wayfinding-icons-manager/
├── dist/
│   ├── wayfinding-icons-lucide.svg     # Lucide SVG Sprite (80 symbols)
│   ├── wayfinding-icons-tabler.svg     # Tabler SVG Sprite (80 symbols)
│   ├── wayfinding-icons-m3.svg         # M3 SVG Sprite (80 symbols)
│   ├── wayfinding-icons-gf-example.svg # Google Fonts SVG Sprite (80 symbols)
│   ├── wayfinding-icons-tactical.svg   # Tactical Cyber SVG Sprite (80 symbols)
│   ├── wayfinding-icons-duotone.svg    # Duotone SVG Sprite (80 symbols)
│   ├── wayfinding-icons-solid.svg      # Solid SVG Sprite (80 symbols)
│   ├── wayfinding-icons-line.svg       # Modern Line SVG Sprite (80 symbols)
│   ├── wayfinding-icons.css            # Styles & custom properties
│   ├── wayfinding-icons.js             # Web Component & JS Module
│   ├── wayfinding-icons.json           # Master metadata (80 icons x 10 sets)
│   └── wayfinding-icons.zip            # Complete distribution bundle (814 files)
├── svg/
│   ├── lucide/                         # 80 individual Lucide SVGs (ISC)
│   ├── tabler/                         # 80 individual Tabler SVGs (MIT)
│   ├── m3/                             # 80 individual Material 3 SVGs
│   ├── gf-example/                     # 80 individual Google Fonts SVGs
│   ├── tactical/                       # 80 individual Tactical Cyber SVGs
│   ├── duotone/                        # 80 individual Duotone SVGs
│   ├── solid/                          # 80 individual Solid Signage SVGs
│   └── line/                           # 80 individual Modern Line SVGs
├── png/                                # 80 3D Squircle Badges (256x256 PNG)
├── png-circle/                         # 80 3D Circular Pucks (256x256 PNG)
├── index.html                          # Interactive Wayfinding Showcase UI
└── README.md
```

---

## Commercial License Summary

All icon assets in this repository are **free for commercial and personal use**:
- **Lucide Icons**: ISC License
- **Tabler Icons**: MIT License
- **Google Fonts Material Symbols**: Apache License 2.0
- **Wayfinding Custom Sets**: MIT License
