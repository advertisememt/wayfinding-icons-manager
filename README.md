# Wayfinding Kiosk Icon Library (8 Design Sets)

A comprehensive suite of **640 icons across 8 distinct design sets** (6 SVG/Vector sets + 2 PNG raster sets) crafted specifically for **touchscreen wayfinding kiosks**, directional totems, overhead signage, airports, campuses, and healthcare facilities.

---

## 8 Unique Design Sets

1. **Material Design 3 (M3 Clean Vector SVG)** *(New!)*:
   - **Format:** Pure vector SVG on standard 24 × 24 dp canvas with 20 × 20 dp live area (`viewBox="0 0 24 24"`).
   - **Design Aesthetic:** Strictly adheres to official Google Material 3 icon design principles (`https://m3.material.io/styles/icons/designing-icons`):
     - **Grid & Keylines:** Precise 24×24 dp canvas, 2 dp trim padding, circular keylines (Ø20), square keylines (18×18 rx=2), and rectangular keylines (20×14 and 14×20).
     - **Stroke & Geometry:** 2.0 dp standard stroke weight for lines, interior counters, and terminal gaps.
     - **Corners & Terminals:** Systematic 2.0 dp corner radii on exterior vertices; interior vertices sharp or minimal fillet. Rounded terminal caps (`stroke-linecap="round" stroke-linejoin="round"`).
     - **Visual Balance:** Uncluttered geometric clarity, minimal extraneous detail, and optical consistency across all 80 wayfinding concepts.
   - **Usage:** Embed via `<wf-icon name="..." set="m3" size="32"></wf-icon>` or SVG sprite `<svg class="wf-icon wf-icon-m3"><use href="dist/wayfinding-icons-m3.svg#wf-..."></use></svg>`. Scales cleanly from 24px to 150px and supports full live stroke and hex recoloring.
   - **Location:** `svg/m3/` (80 files).

2. **GF example icons (Google Fonts Material Symbols)**:
   - **Format:** Google Fonts Web Font (`Material Symbols Outlined`) & Vector SVG (`viewBox="0 -960 960 960"`).
   - **Design Aesthetic:** Official Google Fonts Material Symbols Outlined icons matched to all 80 wayfinding concepts (e.g. `wf-lift` -> `elevator`, `wf-arrow-up` -> `arrow_upward`, `wf-entrance` -> `login`, `wf-exit` -> `logout`, `wf-toilets` -> `wc`).
   - **Usage:** Embed seamlessly via Google Fonts `<span class="material-symbols-outlined">elevator</span>` or as SVG vector assets. Supports optical size scaling up to 150px and color customizer (including `#e3e3e3` and `#000000`).
   - **Location:** `svg/gf-example/` (80 files).

3. **Tactical Cyber / Chiseled Amber (Faceted SVG)**:
   - **Format:** Pure vector SVG with multifaceted geometric geometry (`viewBox="0 0 24 24"`).
   - **Design Aesthetic:** Tactical / low-poly faceted industrial wayfinding aesthetic inspired by chiseled dark slate bevels, gunmetal facet planes, and energetic radiant amber gold focal faces. Features sharp mitered angles, high-contrast white passenger glyphs, and dynamic CSS variable support (`--wf-accent`) for live theme recoloring.
   - **Location:** `svg/tactical/` (80 files).

4. **Duotone Pictograms (Two-Tone SVG)**:
   - **Format:** Pure vector SVG with semantic two-tone layering (`viewBox="0 0 24 24"`).
   - **Design Aesthetic:** Architectural dual-tone hierarchy featuring soft translucent tinting (`opacity="0.25"`) for contextual backplates, doorway thresholds, halos, and bases, combined with high-contrast 100% foreground pictograms and directional arrows. Fully dynamic with `currentColor` and custom hex re-shading.
   - **Location:** `svg/duotone/` (80 files).

5. **3D Circular Pucks (PNG Images)**:
   - **Resolution:** 256 × 256 px 32-bit RGBA PNGs with transparent background.
   - **Design Aesthetic:** Circular touch hardware pucks with outer chamfer bezel ring, radial convex curvature, top gloss dome highlight, and embossed solid white pictograms.
   - **Location:** `png-circle/` (80 files).

6. **3D Squircle Badges (PNG Images)**:
   - **Resolution:** 256 × 256 px 32-bit RGBA PNGs with transparent background.
   - **Design Aesthetic:** Continuous-corner squircle tiles, specular glossy reflection, inner rim highlight, and realistic drop shadow.
   - **Location:** `png/` (80 files).

7. **Solid Signage (Filled Silhouette SVG)**:
   - **Format:** Pure vector SVG with solid silhouette fills.
   - **Design Aesthetic:** High-contrast, bold, ISO/AIGA-inspired signage iconography optimized for long-distance legibility on public transit and overhead displays.
   - **Location:** `svg/solid/` (80 files).

8. **Modern Line (Outline SVG)**:
   - **Format:** 24 × 24 grid SVG with 2px stroke width, rounded caps, and joins.
   - **Design Aesthetic:** Contemporary, airy, minimalist vector style for interactive maps and dense UI layouts.
   - **Location:** `svg/line/` (80 files).

---

## Dynamic Color Customizer (Black & Custom Hex Codes)

The interactive showcase (`index.html`) includes a **real-time Color & Hex engine**:
- **Black Swatch:** Instant Obsidian Black (`#000000`) mode with graphite shading and specular silver gloss.
- **Custom Hex Code Input & Color Picker:** Enter any 6-digit hex code (e.g. `#FF0055`, `#10B981`, `#FF6B00`) or pick any color.
- **Real-Time Dynamic Recolor:**
  - Recolor **Modern Line** stroke outlines.
  - Recolor **Solid Signage** silhouette fills.
  - Re-shade **3D Squircle Badges** with matching computed gradients and shadows.
  - Re-shade **3D Circular Pucks** with radial depth and matching shadows.
  - **Live Custom PNG Download:** Download custom-colored 256×256 PNG images on the fly!

---

## Icon Catalog (80 Unique Wayfinding Identifiers)

| Icon ID | Name | Category | Squircle Badge | Circular Puck |
| :--- | :--- | :--- | :--- | :--- |
| `wf-arrow-up` | **Ahead** | Navigation | `png/wf-arrow-up.png` | `png-circle/wf-arrow-up.png` |
| `wf-arrow-right` | **Right** | Navigation | `png/wf-arrow-right.png` | `png-circle/wf-arrow-right.png` |
| `wf-arrow-down` | **Down / behind** | Navigation | `png/wf-arrow-down.png` | `png-circle/wf-arrow-down.png` |
| `wf-arrow-left` | **Left** | Navigation | `png/wf-arrow-left.png` | `png-circle/wf-arrow-left.png` |
| `wf-arrow-up-right` | **Ahead right** | Navigation | `png/wf-arrow-up-right.png` | `png-circle/wf-arrow-up-right.png` |
| `wf-arrow-up-left` | **Ahead left** | Navigation | `png/wf-arrow-up-left.png` | `png-circle/wf-arrow-up-left.png` |
| `wf-u-turn` | **Turn around** | Navigation | `png/wf-u-turn.png` | `png-circle/wf-u-turn.png` |
| `wf-signpost` | **Directions** | Navigation | `png/wf-signpost.png` | `png-circle/wf-signpost.png` |
| `wf-pin` | **You are here** | Navigation | `png/wf-pin.png` | `png-circle/wf-pin.png` |
| `wf-facing` | **Facing this way** | Navigation | `png/wf-facing.png` | `png-circle/wf-facing.png` |
| `wf-map` | **Map** | Navigation | `png/wf-map.png` | `png-circle/wf-map.png` |
| `wf-touch` | **Touch here** | Navigation | `png/wf-touch.png` | `png-circle/wf-touch.png` |
| `wf-entrance` | **Entrance** | Building | `png/wf-entrance.png` | `png-circle/wf-entrance.png` |
| `wf-exit` | **Exit** | Building | `png/wf-exit.png` | `png-circle/wf-exit.png` |
| `wf-lift` | **Lift** | Building | `png/wf-lift.png` | `png-circle/wf-lift.png` |
| `wf-stairs` | **Stairs** | Building | `png/wf-stairs.png` | `png-circle/wf-stairs.png` |
| `wf-escalator-up` | **Escalator up** | Building | `png/wf-escalator-up.png` | `png-circle/wf-escalator-up.png` |
| `wf-escalator-down` | **Escalator down** | Building | `png/wf-escalator-down.png` | `png-circle/wf-escalator-down.png` |
| `wf-ramp` | **Ramp** | Building | `png/wf-ramp.png` | `png-circle/wf-ramp.png` |
| `wf-accessible` | **Accessible** | Building | `png/wf-accessible.png` | `png-circle/wf-accessible.png` |
| `wf-levels` | **Levels** | Building | `png/wf-levels.png` | `png-circle/wf-levels.png` |
| `wf-no-entry` | **No entry** | Building | `png/wf-no-entry.png` | `png-circle/wf-no-entry.png` |
| `wf-prohibited` | **Not permitted** | Building | `png/wf-prohibited.png` | `png-circle/wf-prohibited.png` |
| `wf-staff-only` | **Staff only** | Building | `png/wf-staff-only.png` | `png-circle/wf-staff-only.png` |
| `wf-toilets` | **Toilets** | Amenities | `png/wf-toilets.png` | `png-circle/wf-toilets.png` |
| `wf-toilet-male` | **Male toilet** | Amenities | `png/wf-toilet-male.png` | `png-circle/wf-toilet-male.png` |
| `wf-toilet-female` | **Female toilet** | Amenities | `png/wf-toilet-female.png` | `png-circle/wf-toilet-female.png` |
| `wf-toilet-accessible` | **Accessible toilet** | Amenities | `png/wf-toilet-accessible.png` | `png-circle/wf-toilet-accessible.png` |
| `wf-baby-change` | **Baby change** | Amenities | `png/wf-baby-change.png` | `png-circle/wf-baby-change.png` |
| `wf-cafe` | **Café** | Amenities | `png/wf-cafe.png` | `png-circle/wf-cafe.png` |
| `wf-food` | **Food** | Amenities | `png/wf-food.png` | `png-circle/wf-food.png` |
| `wf-retail` | **Retail** | Amenities | `png/wf-retail.png` | `png-circle/wf-retail.png` |
| `wf-atm` | **ATM** | Amenities | `png/wf-atm.png` | `png-circle/wf-atm.png` |
| `wf-payment` | **Cashier / pay** | Amenities | `png/wf-payment.png` | `png-circle/wf-payment.png` |
| `wf-pharmacy` | **Pharmacy** | Amenities | `png/wf-pharmacy.png` | `png-circle/wf-pharmacy.png` |
| `wf-water` | **Drinking water** | Amenities | `png/wf-water.png` | `png-circle/wf-water.png` |
| `wf-wifi` | **Free Wi-Fi** | Amenities | `png/wf-wifi.png` | `png-circle/wf-wifi.png` |
| `wf-seating` | **Waiting area** | Amenities | `png/wf-seating.png` | `png-circle/wf-seating.png` |
| `wf-parking` | **Car park** | Transit | `png/wf-parking.png` | `png-circle/wf-parking.png` |
| `wf-car` | **Drop-off** | Transit | `png/wf-car.png` | `png-circle/wf-car.png` |
| `wf-bus` | **Bus / shuttle** | Transit | `png/wf-bus.png` | `png-circle/wf-bus.png` |
| `wf-ev` | **EV charging** | Transit | `png/wf-ev.png` | `png-circle/wf-ev.png` |
| `wf-info` | **Information** | Services | `png/wf-info.png` | `png-circle/wf-info.png` |
| `wf-help` | **Help** | Services | `png/wf-help.png` | `png-circle/wf-help.png` |
| `wf-reception` | **Reception** | Services | `png/wf-reception.png` | `png-circle/wf-reception.png` |
| `wf-security` | **Security** | Services | `png/wf-security.png` | `png-circle/wf-security.png` |
| `wf-phone` | **Phone** | Services | `png/wf-phone.png` | `png-circle/wf-phone.png` |
| `wf-intercom` | **Help point** | Services | `png/wf-intercom.png` | `png-circle/wf-intercom.png` |
| `wf-hospital` | **Hospital** | Healthcare | `png/wf-hospital.png` | `png-circle/wf-hospital.png` |
| `wf-first-aid` | **First aid** | Healthcare | `png/wf-first-aid.png` | `png-circle/wf-first-aid.png` |
| `wf-consult` | **Consulting / GP** | Healthcare | `png/wf-consult.png` | `png-circle/wf-consult.png` |
| `wf-pathology` | **Pathology** | Healthcare | `png/wf-pathology.png` | `png-circle/wf-pathology.png` |
| `wf-aed` | **Defibrillator** | Healthcare | `png/wf-aed.png` | `png-circle/wf-aed.png` |
| `wf-student` | **Student hub** | Campus | `png/wf-student.png` | `png-circle/wf-student.png` |
| `wf-library` | **Library** | Campus | `png/wf-library.png` | `png-circle/wf-library.png` |
| `wf-lecture` | **Lecture room** | Campus | `png/wf-lecture.png` | `png-circle/wf-lecture.png` |
| `wf-emergency` | **Emergency** | Safety | `png/wf-emergency.png` | `png-circle/wf-emergency.png` |
| `wf-evacuate` | **Emergency exit** | Safety | `png/wf-evacuate.png` | `png-circle/wf-evacuate.png` |
| `wf-assembly` | **Assembly point** | Safety | `png/wf-assembly.png` | `png-circle/wf-assembly.png` |
| `wf-fire` | **Fire** | Safety | `png/wf-fire.png` | `png-circle/wf-fire.png` |
| `wf-warning` | **Caution** | Safety | `png/wf-warning.png` | `png-circle/wf-warning.png` |
| `wf-construction` | **Under construction** | Safety | `png/wf-construction.png` | `png-circle/wf-construction.png` |
| `wf-home` | **Home** | UI | `png/wf-home.png` | `png-circle/wf-home.png` |
| `wf-search` | **Search** | UI | `png/wf-search.png` | `png-circle/wf-search.png` |
| `wf-menu` | **Menu** | UI | `png/wf-menu.png` | `png-circle/wf-menu.png` |
| `wf-back` | **Back** | UI | `png/wf-back.png` | `png-circle/wf-back.png` |
| `wf-close` | **Close** | UI | `png/wf-close.png` | `png-circle/wf-close.png` |
| `wf-hours` | **Opening hours** | UI | `png/wf-hours.png` | `png-circle/wf-hours.png` |
| `wf-timetable` | **Timetable** | UI | `png/wf-timetable.png` | `png-circle/wf-timetable.png` |
| `wf-events` | **Events** | UI | `png/wf-events.png` | `png-circle/wf-events.png` |
| `wf-news` | **News** | UI | `png/wf-news.png` | `png-circle/wf-news.png` |
| `wf-announce` | **Announcements** | UI | `png/wf-announce.png` | `png-circle/wf-announce.png` |
| `wf-share` | **Share / social** | Media | `png/wf-share.png` | `png-circle/wf-share.png` |
| `wf-chat` | **Chat** | Media | `png/wf-chat.png` | `png-circle/wf-chat.png` |
| `wf-like` | **Like / feedback** | Media | `png/wf-like.png` | `png-circle/wf-like.png` |
| `wf-camera` | **Photos** | Media | `png/wf-camera.png` | `png-circle/wf-camera.png` |
| `wf-video` | **Video** | Media | `png/wf-video.png` | `png-circle/wf-video.png` |
| `wf-qr` | **Scan QR** | Media | `png/wf-qr.png` | `png-circle/wf-qr.png` |
| `wf-email` | **Email** | Media | `png/wf-email.png` | `png-circle/wf-email.png` |
| `wf-web` | **Website** | Media | `png/wf-web.png` | `png-circle/wf-web.png` |

---

## Directory Structure
```
wayfinding-icons/
├── svg/
│   ├── m3/                          # 80 Material Design 3 (M3) SVGs (New!)
│   ├── gf-example/                  # 80 Google Fonts Material Symbols SVGs
│   ├── tactical/                    # 80 Tactical Cyber Chiseled Amber SVGs
│   ├── duotone/                     # 80 Duotone Two-Tone SVGs
│   ├── line/                        # 80 Modern Line SVGs
│   └── solid/                       # 80 Solid Signage SVGs
├── png-circle/                      # 80 3D Circular Pucks (256x256 RGBA)
│   ├── wf-arrow-up.png
│   └── ... (80 files)
├── png/                             # 80 3D Squircle Badges (256x256 RGBA)
│   ├── wf-arrow-up.png
│   └── ... (80 files)
├── dist/
│   ├── wayfinding-icons.zip         # All 640 assets bundled (.ZIP)
│   ├── wayfinding-icons.json        # Unified metadata catalog with all 8 sets + GF mapping
│   ├── wayfinding-icons-m3.svg      # Combined Material 3 SVG sprite sheet
│   ├── wayfinding-icons-gf-example.svg # Combined Google Fonts SVG sprite sheet
│   ├── wayfinding-icons-tactical.svg# Combined Tactical SVG sprite sheet
│   ├── wayfinding-icons-duotone.svg # Combined Duotone SVG sprite sheet
│   ├── wayfinding-icons-line.svg    # Combined Line SVG sprite sheet
│   ├── wayfinding-icons-solid.svg   # Combined Solid SVG sprite sheet
│   ├── wayfinding-icons.css         # Styling, sizing utilities & M3 / Google Fonts classes
│   └── wayfinding-icons.js          # Web component (<wf-icon>) supporting all 8 sets
├── index.html                       # Interactive 8-way showcase with color customizer
├── build_m3.py                      # Material 3 SVG generator & asset builder
├── build_gf_example.py              # Google Fonts Material Symbols builder
├── build_tactical.py                # Tactical Cyber SVG generator script
├── build_duotone.py                 # Duotone SVG generator script
├── generate_png_icons.py            # Squircle badge generator
├── generate_puck_icons.py           # Circular puck generator
└── update_showcase.py               # Showcase generator script
```
