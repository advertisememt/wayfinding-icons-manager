"""
Build Script for Tabler Open Source Icon Set
License: MIT License (100% Free for Commercial & Personal Use)
https://tabler-icons.io / https://github.com/tabler/tabler-icons
All icons designed on 24x24 viewBox, stroke-width 2, round linecaps and linejoins.
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SVG_DIR = os.path.join(BASE_DIR, "svg", "tabler")
DIST_DIR = os.path.join(BASE_DIR, "dist")
os.makedirs(SVG_DIR, exist_ok=True)
os.makedirs(DIST_DIR, exist_ok=True)

TABLER_ICONS = {
    # ----------------------------------------------------
    # Category 1: Navigation (12 icons)
    # ----------------------------------------------------
    "wf-arrow-up": '<path d="M12 5l0 14"/><path d="M18 11l-6 -6"/><path d="M6 11l6 -6"/>',
    "wf-arrow-right": '<path d="M5 12l14 0"/><path d="M13 18l6 -6"/><path d="M13 6l6 6"/>',
    "wf-arrow-down": '<path d="M12 5l0 14"/><path d="M18 13l-6 6"/><path d="M6 13l6 6"/>',
    "wf-arrow-left": '<path d="M5 12l14 0"/><path d="M5 12l6 6"/><path d="M5 12l6 -6"/>',
    "wf-arrow-up-right": '<path d="M17 7l-10 10"/><path d="M8 7l9 0l0 9"/>',
    "wf-arrow-up-left": '<path d="M7 7l10 10"/><path d="M16 7l-9 0l0 9"/>',
    "wf-u-turn": '<path d="M7 16v-6a5 5 0 0 1 10 0v10"/><path d="M10 13l-3 3l-3 -3"/>',
    "wf-signpost": '<path d="M10.5 21h3"/><path d="M12 3v18"/><path d="M6 5h10a2 2 0 0 1 2 2v0a2 2 0 0 1 -2 2h-10l-2 -2z"/><path d="M8 12h10l2 2l-2 2h-10a2 2 0 0 1 -2 -2v0a2 2 0 0 1 2 -2z"/>',
    "wf-pin": '<path d="M9 11a3 3 0 1 0 6 0a3 3 0 0 0 -6 0"/><path d="M17.657 16.657l-4.243 4.243a2 2 0 0 1 -2.827 0l-4.244 -4.243a8 8 0 1 1 11.314 0z"/>',
    "wf-facing": '<path d="M8 16l2 -6l6 -2l-2 6l-6 2"/><path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0"/>',
    "wf-map": '<path d="M3 7l6 -3l6 3l6 -3v13l-6 3l-6 -3l-6 3v-13"/><path d="M9 4v13"/><path d="M15 7v13"/>',
    "wf-touch": '<path d="M8 13v-8.5a1.5 1.5 0 0 1 3 0v7.5"/><path d="M11 11.5v-2a1.5 1.5 0 0 1 3 0v2.5"/><path d="M14 10.5a1.5 1.5 0 0 1 3 0v1.5"/><path d="M17 11.5a1.5 1.5 0 0 1 3 0v4.5a6 6 0 0 1 -6 6h-2h.208a6 6 0 0 1 -5.012 -2.7l-.196 -.3c-.312 -.479 -1.407 -2.388 -3.286 -5.728a1.5 1.5 0 0 1 .536 -2.022a1.867 1.867 0 0 1 2.28 .28l1.47 1.47"/>',

    # ----------------------------------------------------
    # Category 2: Building (12 icons)
    # ----------------------------------------------------
    "wf-entrance": '<path d="M14 8v-2a2 2 0 0 0 -2 -2h-7a2 2 0 0 0 -2 2v12a2 2 0 0 0 2 2h7a2 2 0 0 0 2 -2v-2"/><path d="M20 12h-13l3 -3m0 6l-3 -3"/>',
    "wf-exit": '<path d="M14 8v-2a2 2 0 0 0 -2 -2h-7a2 2 0 0 0 -2 2v12a2 2 0 0 0 2 2h7a2 2 0 0 0 2 -2v-2"/><path d="M9 12h12l-3 -3m0 6l3 -3"/>',
    "wf-lift": '<path d="M5 4m0 1a1 1 0 0 1 1 -1h12a1 1 0 0 1 1 1v14a1 1 0 0 1 -1 1h-12a1 1 0 0 1 -1 -1z"/><path d="M10 10l2 -2l2 2"/><path d="M10 14l2 2l2 -2"/>',
    "wf-stairs": '<path d="M20 5v4h-4v4h-4v4h-4v4h-4"/>',
    "wf-escalator-up": '<path d="M4 19h4.5l7 -10h4.5"/><path d="M16 5h4v4"/><circle cx="10" cy="7" r="1.5"/>',
    "wf-escalator-down": '<path d="M4 5h4.5l7 10h4.5"/><path d="M16 19h4v-4"/><circle cx="10" cy="17" r="1.5"/>',
    "wf-ramp": '<path d="M3 19h18l-18 -8v8z"/><circle cx="11" cy="7" r="1.5"/>',
    "wf-accessible": '<path d="M12 4m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0"/><path d="M10 9h3l3 7h2"/><path d="M13 14v4l3 2"/><path d="M10 19a5 5 0 1 0 -2 -9.5"/>',
    "wf-levels": '<path d="M12 4l-8 4l8 4l8 -4l-8 -4"/><path d="M4 12l8 4l8 -4"/><path d="M4 16l8 4l8 -4"/>',
    "wf-no-entry": '<path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0"/><path d="M6 12h12"/>',
    "wf-prohibited": '<path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0"/><path d="M5.7 5.7l12.6 12.6"/>',
    "wf-staff-only": '<path d="M8 7a4 4 0 1 0 8 0a4 4 0 0 0 -8 0"/><path d="M6 21v-2a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4v2"/><path d="M19 11l2 2l4 -4"/>',

    # ----------------------------------------------------
    # Category 3: Amenities (14 icons)
    # ----------------------------------------------------
    "wf-toilets": '<path d="M10 5a2 2 0 1 0 4 0a2 2 0 0 0 -4 0"/><path d="M4 17l1.5 -5a2 2 0 0 1 2 -1.5h1a2 2 0 0 1 2 1.5l1.5 5"/><path d="M7 11v7"/><path d="M14 17l1.5 -5a2 2 0 0 1 2 -1.5h1a2 2 0 0 1 2 1.5l1.5 5"/><path d="M17 11v7"/>',
    "wf-toilet-male": '<path d="M12 5a2 2 0 1 0 0 -4a2 2 0 0 0 0 4z"/><path d="M9 20h6v-7a1 1 0 0 0 -1 -1h-4a1 1 0 0 0 -1 1v7z"/>',
    "wf-toilet-female": '<path d="M12 5a2 2 0 1 0 0 -4a2 2 0 0 0 0 4z"/><path d="M10 20l2 -8l2 8"/><path d="M8 12h8"/>',
    "wf-toilet-accessible": '<path d="M12 4m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0"/><path d="M10 9h3l3 7h2"/><path d="M10 19a5 5 0 1 0 -2 -9.5"/>',
    "wf-baby-change": '<path d="M4 19h16"/><path d="M7 14h5a2 2 0 0 0 2 -2v-3a2 2 0 0 0 -2 -2h-4"/><circle cx="8" cy="6" r="1.5"/>',
    "wf-cafe": '<path d="M3 14c.83 .642 2.077 1.017 3.5 1c1.423 .017 2.67 -.358 3.5 -1c.83 -.642 2.077 -1.017 3.5 -1c1.423 -.017 2.67 .358 3.5 1"/><path d="M8 3a2.4 2.4 0 0 0 -1 2a2.4 2.4 0 0 0 1 2"/><path d="M12 3a2.4 2.4 0 0 0 -1 2a2.4 2.4 0 0 0 1 2"/><path d="M3 10h14v5a6 6 0 0 1 -6 6h-2a6 6 0 0 1 -6 -6v-5z"/><path d="M17 11h1a3 3 0 0 1 3 3v1a3 3 0 0 1 -3 3h-1"/>',
    "wf-food": '<path d="M19 3v12h-5c-.023 -3.681 .184 -7.406 5 -12zm0 12v6h-1v-3m-10 -15v6m3 -6v6m-3 -3h3m-2 3v12h-2v-12"/>',
    "wf-retail": '<path d="M6.331 8h11.339a2 2 0 0 1 1.977 2.304l-1.255 8.152a3 3 0 0 1 -2.966 2.544h-6.852a3 3 0 0 1 -2.965 -2.544l-1.255 -8.152a2 2 0 0 1 1.977 -2.304z"/><path d="M9 11v-5a3 3 0 0 1 6 0v5"/>',
    "wf-atm": '<path d="M3 6a2 2 0 0 1 2 -2h14a2 2 0 0 1 2 2v12a2 2 0 0 1 -2 2h-14a2 2 0 0 1 -2 -2v-12z"/><path d="M3 10h18"/><path d="M7 15h4"/><path d="M16 15h1"/>',
    "wf-payment": '<path d="M17 8v-3a1 1 0 0 0 -1 -1h-10a2 2 0 0 0 0 4h12a1 1 0 0 1 1 1v3m0 4v3a1 1 0 0 1 -1 1h-12a2 2 0 0 1 -2 -2v-12"/><path d="M20 12v4h-4a2 2 0 0 1 0 -4h4"/>',
    "wf-pharmacy": '<path d="M3 6a3 3 0 0 1 3 -3h12a3 3 0 0 1 3 3v12a3 3 0 0 1 -3 3h-12a3 3 0 0 1 -3 -3v-12z"/><path d="M12 8v8"/><path d="M8 12h8"/>',
    "wf-water": '<path d="M6.8 11a6 6 0 1 0 10.396 0l-5.197 -8l-5.2 8z"/>',
    "wf-wifi": '<path d="M12 18l.01 0"/><path d="M9.172 15.172a4 4 0 0 1 5.656 0"/><path d="M6.343 12.343a8 8 0 0 1 11.314 0"/><path d="M3.515 9.515c4.686 -4.687 12.284 -4.687 17 0"/>',
    "wf-seating": '<path d="M5 11a2 2 0 0 1 2 2v2h10v-2a2 2 0 1 1 4 0v4a2 2 0 0 1 -2 2h-14a2 2 0 0 1 -2 -2v-4a2 2 0 0 1 2 -2z"/><path d="M5 11v-5a3 3 0 0 1 3 -3h8a3 3 0 0 1 3 3v5"/><path d="M6 19v2"/><path d="M18 19v2"/>',

    # ----------------------------------------------------
    # Category 4: Transit (4 icons)
    # ----------------------------------------------------
    "wf-parking": '<path d="M3 5a2 2 0 0 1 2 -2h14a2 2 0 0 1 2 2v14a2 2 0 0 1 -2 2h-14a2 2 0 0 1 -2 -2v-14z"/><path d="M10 16v-8h3.334a2 2 0 0 1 1.666 3.111a2 2 0 0 1 -1.666 1.889h-3.334"/>',
    "wf-car": '<path d="M7 17m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0"/><path d="M17 17m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0"/><path d="M5 17h-2v-6l2 -5h9l4 5h1a2 2 0 0 1 2 2v4h-2m-4 0h-6"/><path d="M6 10h11"/>',
    "wf-bus": '<path d="M6 17m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0"/><path d="M18 17m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0"/><path d="M4 17h-2v-11a1 1 0 0 1 1 -1h14a5 5 0 0 1 5 5v7h-2m-4 0h-8"/><path d="M16 5l1.5 7h4.5"/><path d="M2 10h15"/>',
    "wf-ev": '<path d="M3 5a2 2 0 0 1 2 -2h8a2 2 0 0 1 2 2v14a2 2 0 0 1 -2 2h-8a2 2 0 0 1 -2 -2v-14z"/><path d="M15 9h2a2 2 0 0 1 2 2v4a2 2 0 0 0 2 2h0a2 2 0 0 0 2 -2v-5"/><path d="M9 8l-2 5h4l-2 5"/>',

    # ----------------------------------------------------
    # Category 5: Services (6 icons)
    # ----------------------------------------------------
    "wf-info": '<path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0"/><path d="M12 8l.01 0"/><path d="M11 12h1v4h1"/>',
    "wf-help": '<path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0"/><path d="M12 17l.01 0"/><path d="M12 13.5a1.5 1.5 0 0 1 1 -1.5a2.6 2.6 0 1 0 -3 -4"/>',
    "wf-reception": '<path d="M4 18h16a1 1 0 0 0 1 -1v-1a4 4 0 0 0 -4 -4h-10a4 4 0 0 0 -4 4v1a1 1 0 0 0 1 1z"/><path d="M12 8a4 4 0 1 0 0 -8a4 4 0 0 0 0 8z"/><path d="M2 21h20"/>',
    "wf-security": '<path d="M12 3a12 12 0 0 0 8.5 3a12 12 0 0 1 -8.5 15a12 12 0 0 1 -8.5 -15a12 12 0 0 0 8.5 -3"/><path d="M9 12l2 2l4 -4"/>',
    "wf-phone": '<path d="M5 4h4l2 5l-2.5 1.5a11 11 0 0 0 5 5l1.5 -2.5l5 2v4a2 2 0 0 1 -2 2a16 16 0 0 1 -15 -15a2 2 0 0 1 2 -2"/>',
    "wf-intercom": '<path d="M4 12v-3a8 8 0 1 1 16 0v3"/><path d="M4 12m0 1a1 1 0 0 1 1 -1h2a1 1 0 0 1 1 1v4a1 1 0 0 1 -1 1h-2a1 1 0 0 1 -1 -1z"/><path d="M16 12m0 1a1 1 0 0 1 1 -1h2a1 1 0 0 1 1 1v4a1 1 0 0 1 -1 1h-2a1 1 0 0 1 -1 -1z"/>',

    # ----------------------------------------------------
    # Category 6: Healthcare (5 icons)
    # ----------------------------------------------------
    "wf-hospital": '<path d="M3 21l18 0"/><path d="M5 21v-16a2 2 0 0 1 2 -2h10a2 2 0 0 1 2 2v16"/><path d="M9 21v-4a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v4"/><path d="M10 9l4 0"/><path d="M12 7l0 4"/>',
    "wf-first-aid": '<path d="M3 8m0 2a2 2 0 0 1 2 -2h14a2 2 0 0 1 2 2v8a2 2 0 0 1 -2 2h-14a2 2 0 0 1 -2 -2z"/><path d="M8 8v-3a2 2 0 0 1 2 -2h4a2 2 0 0 1 2 2v3"/><path d="M12 11v6"/><path d="M9 14h6"/>',
    "wf-consult": '<path d="M6 4h-1a2 2 0 0 0 -2 2v3.5h0a5.5 5.5 0 0 0 11 0v-3.5a2 2 0 0 0 -2 -2h-1"/><path d="M8 15a6 6 0 0 0 12 0v-3"/><circle cx="20" cy="10" r="2"/>',
    "wf-pathology": '<path d="M9 3l6 0"/><path d="M10 9l4 0"/><path d="M10 3v6l-4 11a.7 .7 0 0 0 .5 1h13a.7 .7 0 0 0 .5 -1l-4 -11v-6"/>',
    "wf-aed": '<path d="M19.5 12.572l-7.5 7.428l-7.5 -7.428a5 5 0 1 1 7.5 -6.566a5 5 0 1 1 7.5 6.572"/><path d="M12 7l-2 4h3l-2 4"/>',

    # ----------------------------------------------------
    # Category 7: Campus (3 icons)
    # ----------------------------------------------------
    "wf-student": '<path d="M22 9l-10 -4l-10 4l10 4l10 -4v6"/><path d="M6 10.6v5.4a6 3 0 0 0 12 0v-5.4"/>',
    "wf-library": '<path d="M3 19l18 0"/><path d="M5 6m0 1a1 1 0 0 1 1 -1h2a1 1 0 0 1 1 1v11a1 1 0 0 1 -1 1h-2a1 1 0 0 1 -1 -1z"/><path d="M9 6m0 1a1 1 0 0 1 1 -1h2a1 1 0 0 1 1 1v11a1 1 0 0 1 -1 1h-2a1 1 0 0 1 -1 -1z"/><path d="M14 8l3 10l2 -1l-3 -10z"/>',
    "wf-lecture": '<path d="M3 4h18v11h-18z"/><path d="M4 15l-1 6"/><path d="M20 15l1 6"/><path d="M12 15v6"/>',

    # ----------------------------------------------------
    # Category 8: Safety (6 icons)
    # ----------------------------------------------------
    "wf-emergency": '<path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0"/><path d="M12 9v4"/><path d="M12 16v.01"/><path d="M12 3v-1"/><path d="M12 22v-1"/><path d="M3 12h-1"/><path d="M22 12h-1"/>',
    "wf-evacuate": '<path d="M13 12v.01"/><path d="M3 21h18"/><path d="M5 21v-16a2 2 0 0 1 2 -2h6m4 10.5v7.5"/><path d="M21 7h-7m3 -3l-3 3l3 3"/>',
    "wf-assembly": '<path d="M12 12m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0"/><path d="M4 8v-2a2 2 0 0 1 2 -2h2"/><path d="M4 16v2a2 2 0 0 0 2 2h2"/><path d="M16 4h2a2 2 0 0 1 2 2v2"/><path d="M16 20h2a2 2 0 0 0 2 -2v-2"/>',
    "wf-fire": '<path d="M12 12c2 -2.96 0 -7 -1 -8c0 3.038 -1.773 4.741 -3 6c-1.226 1.26 -2 3.24 -2 5a6 6 0 1 0 12 0c0 -1.532 -1.056 -3.94 -2 -5c-1.786 3 -2.791 3 -4 2z"/>',
    "wf-warning": '<path d="M12 9v4"/><path d="M12 16v.01"/><path d="M5 19h14a2 2 0 0 0 1.84 -2.75l-7.1 -12.25a2 2 0 0 0 -3.5 0l-7.1 12.25a2 2 0 0 0 1.75 2.75"/>',
    "wf-construction": '<path d="M4 20h16"/><path d="M4 20l10 -14h4l-10 14"/><path d="M14 20l4 -6"/>',

    # ----------------------------------------------------
    # Category 9: UI (10 icons)
    # ----------------------------------------------------
    "wf-home": '<path d="M5 12l-2 0l9 -9l9 9l-2 0"/><path d="M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2 -2v-7"/><path d="M9 21v-6a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v6"/>',
    "wf-search": '<path d="M10 10m-7 0a7 7 0 1 0 14 0a7 7 0 1 0 -14 0"/><path d="M21 21l-6 -6"/>',
    "wf-menu": '<path d="M4 6l16 0"/><path d="M4 12l16 0"/><path d="M4 18l16 0"/>',
    "wf-back": '<path d="M15 6l-6 6l6 6"/>',
    "wf-close": '<path d="M18 6l-12 12"/><path d="M6 6l12 12"/>',
    "wf-hours": '<path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0"/><path d="M12 7v5l3 3"/>',
    "wf-timetable": '<path d="M4 5m0 2a2 2 0 0 1 2 -2h12a2 2 0 0 1 2 2v12a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2z"/><path d="M16 3v4"/><path d="M8 3v4"/><path d="M4 11h16"/><path d="M11 15h1"/>',
    "wf-events": '<path d="M4 5m0 2a2 2 0 0 1 2 -2h12a2 2 0 0 1 2 2v12a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2z"/><path d="M16 3v4"/><path d="M8 3v4"/><path d="M4 11h16"/><path d="M12 13l1 2l2 .5l-1.5 1.5l.5 2l-2 -1l-2 1l.5 -2l-1.5 -1.5l2 -.5z"/>',
    "wf-news": '<path d="M16 6h3a1 1 0 0 1 1 1v11a2 2 0 0 1 -4 0v-13a1 1 0 0 0 -1 -1h-10a1 1 0 0 0 -1 1v12a3 3 0 0 0 3 3h11"/><path d="M8 8h4"/><path d="M8 12h4"/><path d="M8 16h4"/>',
    "wf-announce": '<path d="M18 8a3 3 0 0 1 0 6"/><path d="M10 8v11a1 1 0 0 1 -1 1h-1a1 1 0 0 1 -1 -1v-5"/><path d="M12 8h0l4.524 -3.77a.9 .9 0 0 1 1.476 .692v12.156a.9 .9 0 0 1 -1.476 .692l-4.524 -3.77h-8a1 1 0 0 1 -1 -1v-4a1 1 0 0 1 1 -1h8"/>',

    # ----------------------------------------------------
    # Category 10: Media (8 icons)
    # ----------------------------------------------------
    "wf-share": '<path d="M6 12m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0"/><path d="M18 6m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0"/><path d="M18 18m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0"/><path d="M8.7 10.7l6.6 -3.4"/><path d="M8.7 13.3l6.6 3.4"/>',
    "wf-chat": '<path d="M3 20l1.3 -3.9a9 8 0 1 1 3.4 2.9l-4.7 1"/>',
    "wf-like": '<path d="M7 11v8a1 1 0 0 1 -1 1h-2a1 1 0 0 1 -1 -1v-7a1 1 0 0 1 1 -1h3a4 4 0 0 0 4 -4v-1a2 2 0 0 1 4 0v1.4a3 3 0 0 0 3 3h1a2 2 0 0 1 2 2l-1.5 6h-10.5"/>',
    "wf-camera": '<path d="M5 7h1a2 2 0 0 0 2 -2a1 1 0 0 1 1 -1h6a1 1 0 0 1 1 1a2 2 0 0 0 2 2h1a2 2 0 0 1 2 2v9a2 2 0 0 1 -2 2h-14a2 2 0 0 1 -2 -2v-9a2 2 0 0 1 2 -2"/><path d="M9 13a3 3 0 1 0 6 0a3 3 0 0 0 -6 0"/>',
    "wf-video": '<path d="M15 10l4.553 -2.276a1 1 0 0 1 1.447 .894v6.764a1 1 0 0 1 -1.447 .894l-4.553 -2.276v-4z"/><path d="M3 6m0 2a2 2 0 0 1 2 -2h8a2 2 0 0 1 2 2v8a2 2 0 0 1 -2 2h-8a2 2 0 0 1 -2 -2z"/>',
    "wf-qr": '<path d="M4 4m0 1a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v4a1 1 0 0 1 -1 1h-4a1 1 0 0 1 -1 -1z"/><path d="M7 17l0 .01"/><path d="M14 4m0 1a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v4a1 1 0 0 1 -1 1h-4a1 1 0 0 1 -1 -1z"/><path d="M4 14m0 1a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v4a1 1 0 0 1 -1 1h-4a1 1 0 0 1 -1 -1z"/><path d="M14 14h1v1h-1z"/><path d="M14 18h2v2h-2z"/><path d="M18 14h2v2h-2z"/>',
    "wf-email": '<path d="M3 7a2 2 0 0 1 2 -2h14a2 2 0 0 1 2 2v10a2 2 0 0 1 -2 2h-14a2 2 0 0 1 -2 -2v-10z"/><path d="M3 7l9 6l9 -6"/>',
    "wf-web": '<path d="M3 12a9 9 0 1 0 18 0a9 9 0 0 0 -18 0"/><path d="M3.6 9h16.8"/><path d="M3.6 15h16.8"/><path d="M11.5 3a17 17 0 0 0 0 18"/><path d="M12.5 3a17 17 0 0 1 0 18"/>'
}

assert len(TABLER_ICONS) == 80, f"Expected 80 icons, found {len(TABLER_ICONS)}"

def generate_svg_files():
    print(f"Generating {len(TABLER_ICONS)} Tabler SVGs in {SVG_DIR}...")
    for icon_id, paths in TABLER_ICONS.items():
        svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-tabler {icon_id}">
  {paths}
</svg>
'''
        with open(os.path.join(SVG_DIR, f"{icon_id}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_content)
    print("Tabler SVGs generated successfully.")

def build_sprite():
    sprite_path = os.path.join(DIST_DIR, "wayfinding-icons-tabler.svg")
    print(f"Building sprite sheet {sprite_path}...")
    with open(sprite_path, "w", encoding="utf-8") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" style="display: none;">\n')
        for icon_id, paths in TABLER_ICONS.items():
            f.write(f'  <symbol id="{icon_id}" viewBox="0 0 24 24">\n    <g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n      {paths}\n    </g>\n  </symbol>\n')
        f.write('</svg>\n')
    print("Tabler sprite generated.")

def update_metadata():
    json_path = os.path.join(DIST_DIR, "wayfinding-icons.json")
    print(f"Updating {json_path} with paths_tabler...")
    with open(json_path, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    for item in metadata:
        icon_id = item["id"]
        item["paths_tabler"] = TABLER_ICONS.get(icon_id, "")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)
    print("Metadata updated with Tabler paths.")

def update_js():
    js_path = os.path.join(DIST_DIR, "wayfinding-icons.js")
    print(f"Updating {js_path}...")
    with open(js_path, "r", encoding="utf-8") as f:
        js = f.read()

    tabler_json = json.dumps(TABLER_ICONS, indent=2)
    export_stmt = f"\nexport const WAYFINDING_TABLER = {tabler_json};\n"

    if "export const WAYFINDING_TABLER" not in js:
        idx = js.find("export function renderWayfindingIcon")
        if idx != -1:
            js = js[:idx] + export_stmt + "\n" + js[idx:]
        else:
            js += export_stmt

    if "set === 'tabler'" not in js:
        target = "if (set === 'lucide') {"
        replacement = """if (set === 'tabler') {
    const paths = WAYFINDING_TABLER[iconId] || '';
    return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-tabler ${iconId} ${className}">${paths}</svg>`;
  }
  if (set === 'lucide') {"""
        js = js.replace(target, replacement, 1)

    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js)
    print("wayfinding-icons.js updated.")

def update_css():
    css_path = os.path.join(DIST_DIR, "wayfinding-icons.css")
    print(f"Updating {css_path}...")
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    tabler_css = """
/* Tabler Open Source Icons (MIT License) */
.wf-icon-tabler {
  fill: none;
  stroke: currentColor;
  stroke-width: var(--live-stroke, 2px);
  stroke-linecap: round;
  stroke-linejoin: round;
}
"""
    if ".wf-icon-tabler" not in css:
        css += tabler_css
        with open(css_path, "w", encoding="utf-8") as f:
            f.write(css)
        print("wayfinding-icons.css updated.")

if __name__ == "__main__":
    generate_svg_files()
    build_sprite()
    update_metadata()
    update_js()
    update_css()
    print("All Tabler assets generated successfully!")
