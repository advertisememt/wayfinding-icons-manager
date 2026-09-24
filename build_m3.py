"""
Build Script for Material Design 3 (M3) Wayfinding Icon Set
Adheres to official Material Design 3 icon design principles:
- Canvas: 24×24 dp, 20×20 dp live area with 2 dp margin
- Standard stroke weight: 2.0 dp
- Corner radii: 2.0 dp exterior fillets
- Terminals: stroke-linecap="round", stroke-linejoin="round"
- Keyline geometry: clean circles (r=10), squares (18×18 rx=2), rectangles (20×14, 14×20)
- Visual balance: simplified, uncluttered geometric silhouettes
"""

import os
import json
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SVG_M3_DIR = os.path.join(BASE_DIR, "svg", "m3")
DIST_DIR = os.path.join(BASE_DIR, "dist")
os.makedirs(SVG_M3_DIR, exist_ok=True)
os.makedirs(DIST_DIR, exist_ok=True)

# 80 Icons in M3 Design Language (24x24 viewBox, stroke-width 2, round caps/corners)
M3_ICONS = {
    # ----------------------------------------------------
    # Category 1: Navigation (12 icons)
    # ----------------------------------------------------
    "wf-arrow-up": '<line x1="12" y1="20" x2="12" y2="4"/><polyline points="5 11 12 4 19 11"/>',
    "wf-arrow-right": '<line x1="4" y1="12" x2="20" y2="12"/><polyline points="13 5 20 12 13 19"/>',
    "wf-arrow-down": '<line x1="12" y1="4" x2="12" y2="20"/><polyline points="5 13 12 20 19 13"/>',
    "wf-arrow-left": '<line x1="20" y1="12" x2="4" y2="12"/><polyline points="11 5 4 12 11 19"/>',
    "wf-arrow-up-right": '<line x1="6" y1="18" x2="18" y2="6"/><polyline points="9 6 18 6 18 15"/>',
    "wf-arrow-up-left": '<line x1="18" y1="18" x2="6" y2="6"/><polyline points="15 6 6 6 6 15"/>',
    "wf-u-turn": '<path d="M7 18V11a5 5 0 0 1 10 0v9"/><polyline points="3.5 14.5 7 18 10.5 14.5"/>',
    "wf-signpost": '<line x1="12" y1="3" x2="12" y2="21"/><path d="M6 5h9l3 2.5-3 2.5H6z"/><path d="M18 13H9l-3 2.5 3 2.5h9z"/>',
    "wf-pin": '<path d="M12 21.5c-4.2-4.5-7-8.8-7-12a7 7 0 1 1 14 0c0 3.2-2.8 7.5-7 12z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "wf-facing": '<circle cx="12" cy="12" r="9.5"/><polygon points="12 4 15 12 12 10.5 9 12" fill="currentColor" stroke="none"/><circle cx="12" cy="16.5" r="1.2" fill="currentColor" stroke="none"/>',
    "wf-map": '<polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"/><line x1="9" y1="3" x2="9" y2="18"/><line x1="15" y1="6" x2="15" y2="21"/>',
    "wf-touch": '<path d="M12 3a9 9 0 0 1 9 9"/><path d="M12 7a5 5 0 0 1 5 5"/><path d="M9 14.5V8a1.5 1.5 0 0 1 3 0v6.5"/><path d="M12 11.5a1.5 1.5 0 0 1 3 0V14"/><path d="M15 12.5a1.5 1.5 0 0 1 3 0V15a6 6 0 0 1-6 6h-2a6 6 0 0 1-4.2-1.8L5 15.4a1.5 1.5 0 0 1 2.2-2l1.8 1.6"/>',

    # ----------------------------------------------------
    # Category 2: Building (12 icons)
    # ----------------------------------------------------
    "wf-entrance": '<rect x="9" y="3" width="12" height="18" rx="2"/><polyline points="15 3 9 5.5 9 18.5 15 21"/><path d="M2 12h8"/><polyline points="6.5 8.5 10 12 6.5 15.5"/>',
    "wf-exit": '<rect x="3" y="3" width="12" height="18" rx="2"/><polyline points="9 3 15 5.5 15 18.5 9 21"/><path d="M12 12h10"/><polyline points="18.5 8.5 22 12 18.5 15.5"/>',
    "wf-lift": '<rect x="4" y="3" width="16" height="18" rx="2"/><line x1="12" y1="3" x2="12" y2="21"/><polygon points="8 10 6 13 10 13" fill="currentColor" stroke="none"/><polygon points="16 14 14 11 18 11" fill="currentColor" stroke="none"/>',
    "wf-stairs": '<path d="M3 19h5v-4h5v-4h5V7h3"/><path d="M5 6l4-2"/><circle cx="12" cy="4" r="1.5" fill="currentColor" stroke="none"/><path d="M10 8l3 3-2 4"/>',
    "wf-escalator-up": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M6 17h3l6-8h3"/><polyline points="13 6 18 6 18 11"/><circle cx="9.5" cy="7.5" r="1.5" fill="currentColor" stroke="none"/>',
    "wf-escalator-down": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M6 7h3l6 8h3"/><polyline points="13 18 18 18 18 13"/><circle cx="9.5" cy="16.5" r="1.5" fill="currentColor" stroke="none"/>',
    "wf-ramp": '<path d="M3 19h18L3 11z"/><circle cx="10" cy="8" r="1.5" fill="currentColor" stroke="none"/><path d="M9 11l2 2 3-3"/>',
    "wf-accessible": '<circle cx="12" cy="4" r="2" fill="currentColor" stroke="none"/><path d="M9 20a5 5 0 1 0 0-10 5 5 0 0 0-1.5.2"/><path d="M9 10h4l2.5 5H19"/><path d="M12 14v4l3 2"/>',
    "wf-levels": '<path d="M12 3L3 7.5 12 12l9-4.5L12 3z"/><path d="M3 12l9 4.5 9-4.5"/><path d="M3 16.5l9 4.5 9-4.5"/>',
    "wf-no-entry": '<circle cx="12" cy="12" r="9.5"/><line x1="6.5" y1="12" x2="17.5" y2="12" stroke-width="2.8"/>',
    "wf-prohibited": '<circle cx="12" cy="12" r="9.5"/><line x1="5.3" y1="5.3" x2="18.7" y2="18.7" stroke-width="2.5"/>',
    "wf-staff-only": '<rect x="5" y="4" width="14" height="17" rx="2"/><circle cx="12" cy="10" r="2.5"/><path d="M8 17a4 4 0 0 1 8 0"/><line x1="10" y1="2" x2="14" y2="2"/>',

    # ----------------------------------------------------
    # Category 3: Amenities (14 icons)
    # ----------------------------------------------------
    "wf-toilets": '<circle cx="7.5" cy="5" r="1.5" fill="currentColor" stroke="none"/><path d="M5.5 9h4v6h-1v4h-2v-4h-1z"/><circle cx="16.5" cy="5" r="1.5" fill="currentColor" stroke="none"/><path d="M14 9h5l1.5 5h-2l-1 5h-2l-1-5h-2z"/><line x1="12" y1="3" x2="12" y2="21" stroke-dasharray="2 2"/>',
    "wf-toilet-male": '<circle cx="12" cy="4.5" r="2" fill="currentColor" stroke="none"/><path d="M9 9.5h6a1 1 0 0 1 1 1v5h-2v5.5a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5V15.5H8v-5a1 1 0 0 1 1-1z"/>',
    "wf-toilet-female": '<circle cx="12" cy="4.5" r="2" fill="currentColor" stroke="none"/><path d="M9.5 9.5h5l2.5 6.5h-3v4.5a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5V16h-3z"/>',
    "wf-toilet-accessible": '<circle cx="13" cy="4.5" r="2" fill="currentColor" stroke="none"/><path d="M9.5 19.5a5 5 0 1 0 0-10 5 5 0 0 0-1.5.2"/><path d="M9.5 9.5h4.5l2.5 5H20"/><path d="M13 14v4l3 2"/>',
    "wf-baby-change": '<circle cx="7" cy="8" r="1.5" fill="currentColor" stroke="none"/><path d="M5.5 12h3l2 3h4"/><line x1="3" y1="19" x2="21" y2="19"/><path d="M17 11a2.5 2.5 0 0 0-2.5-2.5H13"/>',
    "wf-cafe": '<path d="M4 8h12v7a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4V8z"/><path d="M16 10h2.5a2.5 2.5 0 0 1 0 5H16"/><line x1="2" y1="21" x2="18" y2="21"/><path d="M7 3c0 1.5 1 2 1 3"/><path d="M11 3c0 1.5 1 2 1 3"/>',
    "wf-food": '<path d="M6 3v6a3 3 0 0 0 3 3v9"/><line x1="6" y1="3" x2="6" y2="9"/><line x1="9" y1="3" x2="9" y2="6"/><path d="M18 3c0 4-3 5-3 9v9"/><path d="M15 3h3"/>',
    "wf-retail": '<path d="M6 7V5a3 3 0 0 1 3-3h6a3 3 0 0 1 3 3v2"/><rect x="4" y="7" width="16" height="14" rx="2"/><circle cx="12" cy="13" r="2"/>',
    "wf-atm": '<rect x="3" y="4" width="18" height="16" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="7" y1="14" x2="12" y2="14"/><rect x="15" y="13" width="3" height="3" rx="0.5"/>',
    "wf-payment": '<rect x="3" y="5" width="18" height="14" rx="2"/><line x1="3" y1="10" x2="21" y2="10"/><circle cx="7.5" cy="15" r="1.5" fill="currentColor" stroke="none"/><circle cx="11.5" cy="15" r="1.5" fill="currentColor" stroke="none"/>',
    "wf-pharmacy": '<rect x="3" y="5" width="18" height="15" rx="3"/><line x1="12" y1="9" x2="12" y2="16"/><line x1="8.5" y1="12.5" x2="15.5" y2="12.5"/>',
    "wf-water": '<path d="M5 20h14"/><path d="M6 16h8a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2H9"/><path d="M9 6V4"/><path d="M12 12c0 1.7-1.3 3-1.3 3s-1.3-1.3-1.3-3a1.3 1.3 0 0 1 2.6 0z" fill="currentColor"/>',
    "wf-wifi": '<path d="M3 8a13 13 0 0 1 18 0"/><path d="M6.5 12a8.5 8.5 0 0 1 11 0"/><path d="M10 16a3.5 3.5 0 0 1 4 0"/><circle cx="12" cy="19" r="1" fill="currentColor" stroke="none"/>',
    "wf-seating": '<path d="M5 5v10a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2"/><line x1="5" y1="17" x2="5" y2="21"/><line x1="19" y1="17" x2="19" y2="21"/><line x1="5" y1="13" x2="19" y2="13"/>',

    # ----------------------------------------------------
    # Category 4: Transit (4 icons)
    # ----------------------------------------------------
    "wf-parking": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M9 17V7h4.5a3.5 3.5 0 0 1 0 7H9"/>',
    "wf-car": '<path d="M5 11l2-5h10l2 5"/><rect x="3" y="11" width="18" height="7" rx="2"/><circle cx="7" cy="16" r="1.5" fill="currentColor" stroke="none"/><circle cx="17" cy="16" r="1.5" fill="currentColor" stroke="none"/><line x1="5" y1="18" x2="5" y2="20"/><line x1="19" y1="18" x2="19" y2="20"/>',
    "wf-bus": '<rect x="4" y="3" width="16" height="15" rx="3"/><line x1="4" y1="9" x2="20" y2="9"/><circle cx="8" cy="14.5" r="1.5" fill="currentColor" stroke="none"/><circle cx="16" cy="14.5" r="1.5" fill="currentColor" stroke="none"/><line x1="6" y1="18" x2="6" y2="21"/><line x1="18" y1="18" x2="18" y2="21"/>',
    "wf-ev": '<rect x="3" y="4" width="12" height="16" rx="2"/><polyline points="15 8 18 8 18 16 21 16"/><line x1="19.5" y1="16" x2="19.5" y2="18.5"/><polygon points="9 8 7 12 10 12 8 16" fill="currentColor" stroke="none"/>',

    # ----------------------------------------------------
    # Category 5: Services (6 icons)
    # ----------------------------------------------------
    "wf-info": '<circle cx="12" cy="12" r="9.5"/><circle cx="12" cy="7.5" r="1.2" fill="currentColor" stroke="none"/><line x1="12" y1="11" x2="12" y2="16.5"/><line x1="10.5" y1="11" x2="12" y2="11"/>',
    "wf-help": '<circle cx="12" cy="12" r="9.5"/><path d="M9.5 9a2.5 2.5 0 0 1 5 0c0 1.5-1.5 2-2.5 2.8v1"/><circle cx="12" cy="16.5" r="1.2" fill="currentColor" stroke="none"/>',
    "wf-reception": '<circle cx="12" cy="6" r="2" fill="currentColor" stroke="none"/><path d="M9 12a3 3 0 0 1 6 0"/><line x1="3" y1="15" x2="21" y2="15"/><line x1="4" y1="15" x2="4" y2="20"/><line x1="20" y1="15" x2="20" y2="20"/>',
    "wf-security": '<path d="M12 3l8 3v6c0 5-3.5 9.5-8 10.5C7.5 21.5 4 17 4 12V6l8-3z"/><polyline points="9 12 11.5 14.5 15.5 10"/>',
    "wf-phone": '<path d="M5 4h3.5l1.5 3.5L8 9.5a13 13 0 0 0 6.5 6.5l2-2 3.5 1.5V19a2 2 0 0 1-2 2A17 17 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
    "wf-intercom": '<rect x="6" y="3" width="12" height="18" rx="2.5"/><circle cx="12" cy="8" r="2.5"/><line x1="12" y1="14" x2="12" y2="17"/><path d="M2 9a14 14 0 0 1 0 6"/><path d="M22 9a14 14 0 0 0 0 6"/>',

    # ----------------------------------------------------
    # Category 6: Healthcare (5 icons)
    # ----------------------------------------------------
    "wf-hospital": '<rect x="4" y="3" width="16" height="18" rx="2"/><line x1="12" y1="7" x2="12" y2="13"/><line x1="9" y1="10" x2="15" y2="10"/><rect x="10" y="17" width="4" height="4"/>',
    "wf-first-aid": '<rect x="3" y="6" width="18" height="15" rx="2.5"/><path d="M9 6V4a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2"/><line x1="12" y1="10.5" x2="12" y2="16.5"/><line x1="9" y1="13.5" x2="15" y2="13.5"/>',
    "wf-consult": '<circle cx="12" cy="5" r="2" fill="currentColor" stroke="none"/><path d="M8 12a4 4 0 0 1 8 0v2H8z"/><path d="M6 14v2a6 6 0 0 0 12 0v-2"/><circle cx="18" cy="14" r="1.5" fill="currentColor" stroke="none"/>',
    "wf-pathology": '<path d="M9 3h6"/><line x1="12" y1="3" x2="12" y2="7"/><path d="M10 7L4.5 18A2 2 0 0 0 6.2 21h11.6a2 2 0 0 0 1.7-3L14 7H10z"/><line x1="7.5" y1="15" x2="16.5" y2="15"/><circle cx="10" cy="18" r="1" fill="currentColor" stroke="none"/><circle cx="14" cy="17.5" r="1" fill="currentColor" stroke="none"/>',
    "wf-aed": '<path d="M12 21.5L4 13.5a5.5 5.5 0 0 1 0-7.8 5.5 5.5 0 0 1 7.8 0L12 6l.2-.3a5.5 5.5 0 0 1 7.8 7.8L12 21.5z"/><polygon points="12.5 7 10 12 12.5 12 11.5 16 14.5 11 12 11" fill="currentColor" stroke="none"/>',

    # ----------------------------------------------------
    # Category 7: Campus (3 icons)
    # ----------------------------------------------------
    "wf-student": '<polygon points="12 3 2 8 12 13 22 8"/><path d="M6 10.5v5c0 2.5 3 4.5 6 4.5s6-2 6-4.5v-5"/><line x1="22" y1="8" x2="22" y2="15"/>',
    "wf-library": '<rect x="4" y="4" width="4" height="16" rx="1"/><rect x="9.5" y="4" width="4" height="16" rx="1"/><path d="M16 4.5l3.8 14.5a1 1 0 0 1-.7 1.2l-.3.1-3.8-1a1 1 0 0 1-.7-1.2L16 4.5z"/><line x1="2" y1="21" x2="22" y2="21"/>',
    "wf-lecture": '<rect x="4" y="3" width="16" height="10" rx="1.5"/><circle cx="12" cy="17" r="1.5" fill="currentColor" stroke="none"/><path d="M9 22l3-3 3 3"/><line x1="12" y1="13" x2="12" y2="15.5"/>',

    # ----------------------------------------------------
    # Category 8: Safety (6 icons)
    # ----------------------------------------------------
    "wf-emergency": '<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/><line x1="12" y1="2" x2="12" y2="4"/><line x1="4.5" y1="4.5" x2="6" y2="6"/><line x1="19.5" y1="4.5" x2="18" y2="6"/>',
    "wf-evacuate": '<rect x="3" y="3" width="9" height="18" rx="1.5"/><circle cx="17.5" cy="5" r="1.8" fill="currentColor" stroke="none"/><path d="M14 9l3 2-2 4 4 3"/><path d="M15 11l-3 3-3-1"/>',
    "wf-assembly": '<polyline points="7 4 3 4 3 8"/><line x1="3" y1="4" x2="8" y2="9"/><polyline points="17 4 21 4 21 8"/><line x1="21" y1="4" x2="16" y2="9"/><polyline points="7 20 3 20 3 16"/><line x1="3" y1="20" x2="8" y2="15"/><polyline points="17 20 21 20 21 16"/><line x1="21" y1="20" x2="16" y2="15"/><circle cx="12" cy="12" r="2" fill="currentColor" stroke="none"/>',
    "wf-fire": '<path d="M12 2c0 3.5-3 5.5-3 9a6 6 0 0 0 12 0c0-4-3-6-4-8-.5 2-1.5 3-2.5 3.5C14.5 5.5 13 3.5 12 2z"/><path d="M12 13a2.5 2.5 0 0 0 2.5 2.5c0 1.5-1 2.5-2.5 2.5s-2.5-1-2.5-2.5A2.5 2.5 0 0 1 12 13z" fill="currentColor"/>',
    "wf-warning": '<path d="M12 3.2L2.5 19.8A1.5 1.5 0 0 0 3.8 22h16.4a1.5 1.5 0 0 0 1.3-2.2L12 3.2z"/><line x1="12" y1="9" x2="12" y2="14.5"/><circle cx="12" cy="18" r="1.2" fill="currentColor" stroke="none"/>',
    "wf-construction": '<polygon points="12 3 5 19 19 19"/><line x1="2" y1="21" x2="22" y2="21"/><line x1="8.5" y1="14" x2="15.5" y2="14"/><line x1="10" y1="10" x2="14" y2="10"/>',

    # ----------------------------------------------------
    # Category 9: UI (10 icons)
    # ----------------------------------------------------
    "wf-home": '<path d="M3 10.5L12 3l9 7.5V20a1.5 1.5 0 0 1-1.5 1.5H4.5A1.5 1.5 0 0 1 3 20V10.5z"/><path d="M9 21.5v-7a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v7"/>',
    "wf-search": '<circle cx="11" cy="11" r="7"/><line x1="16.5" y1="16.5" x2="21.5" y2="21.5"/>',
    "wf-menu": '<line x1="4" y1="6" x2="20" y2="6"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="18" x2="20" y2="18"/>',
    "wf-back": '<polyline points="15 19 8 12 15 5"/>',
    "wf-close": '<line x1="5" y1="5" x2="19" y2="19"/><line x1="19" y1="5" x2="5" y2="19"/>',
    "wf-hours": '<circle cx="12" cy="12" r="9.5"/><polyline points="12 7 12 12 16 14"/>',
    "wf-timetable": '<rect x="3" y="4" width="18" height="17" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="8" y1="2" x2="8" y2="5"/><line x1="16" y1="2" x2="16" y2="5"/><line x1="7.5" y1="14" x2="10.5" y2="14"/><line x1="13.5" y1="14" x2="16.5" y2="14"/>',
    "wf-events": '<rect x="3" y="4" width="18" height="17" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="8" y1="2" x2="8" y2="5"/><line x1="16" y1="2" x2="16" y2="5"/><polygon points="12 11.5 13 13.8 15.5 14 13.5 15.6 14.2 18 12 16.7 9.8 18 10.5 15.6 8.5 14 11 13.8" fill="currentColor" stroke="none"/>',
    "wf-news": '<rect x="3" y="4" width="18" height="16" rx="2"/><line x1="7" y1="8" x2="17" y2="8"/><rect x="7" y="11" width="4" height="4" rx="0.5"/><line x1="13" y1="12" x2="17" y2="12"/><line x1="13" y1="15" x2="17" y2="15"/>',
    "wf-announce": '<path d="M3 11v2a2 2 0 0 0 2 2h2l5 4V5L7 9H5a2 2 0 0 0-2 2z"/><path d="M16 8.5a5 5 0 0 1 0 7"/><path d="M19 6a9 9 0 0 1 0 12"/>',

    # ----------------------------------------------------
    # Category 10: Media (8 icons)
    # ----------------------------------------------------
    "wf-share": '<circle cx="18" cy="5" r="2.5"/><circle cx="6" cy="12" r="2.5"/><circle cx="18" cy="19" r="2.5"/><line x1="8.3" y1="10.9" x2="15.7" y2="6.1"/><line x1="8.3" y1="13.1" x2="15.7" y2="17.9"/>',
    "wf-chat": '<path d="M20 15a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h3v4l5-4h8z"/><circle cx="8" cy="9" r="1" fill="currentColor" stroke="none"/><circle cx="12" cy="9" r="1" fill="currentColor" stroke="none"/><circle cx="16" cy="9" r="1" fill="currentColor" stroke="none"/>',
    "wf-like": '<path d="M7 10v10H4a1 1 0 0 1-1-1v-8a1 1 0 0 1 1-1h3zm3 10h7a2 2 0 0 0 2-1.5l1.5-6A2 2 0 0 0 18.5 10H14V5a2 2 0 0 0-2-2l-2 7v10z"/>',
    "wf-camera": '<path d="M9 4.5l1.5-2h3l1.5 2H19a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-11a2 2 0 0 1 2-2h4z"/><circle cx="12" cy="13" r="3.5"/><circle cx="18" cy="8.5" r="0.8" fill="currentColor" stroke="none"/>',
    "wf-video": '<rect x="3" y="5" width="13" height="14" rx="2"/><polygon points="16 10 21 6.5 21 17.5 16 14"/>',
    "wf-qr": '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="5.5" y="5.5" width="2" height="2" fill="currentColor" stroke="none"/><rect x="16.5" y="5.5" width="2" height="2" fill="currentColor" stroke="none"/><rect x="5.5" y="16.5" width="2" height="2" fill="currentColor" stroke="none"/><path d="M14 14h3v3h-3z" fill="currentColor" stroke="none"/><path d="M18 18h3v3h-3z" fill="currentColor" stroke="none"/><path d="M18 14h3v1h-3z" fill="currentColor" stroke="none"/>',
    "wf-email": '<rect x="3" y="5" width="18" height="14" rx="2"/><polyline points="3 7 12 13 21 7"/>',
    "wf-web": '<circle cx="12" cy="12" r="9.5"/><line x1="2.5" y1="12" x2="21.5" y2="12"/><ellipse cx="12" cy="12" rx="4.5" ry="9.5"/>'
}

# 80 Filled/Solid M3 variants — same 24×24 grid, pure fill="currentColor", no strokes.
# Each icon is the "filled" state as per Material Design 3 Fill axis (FILL=1).
M3_ICONS_FILLED = {
    # --- Category 1: Navigation ---
    "wf-arrow-up":       '<polygon points="12 3 20 20 12 15 4 20" fill="currentColor"/>',
    "wf-arrow-right":    '<polygon points="21 12 4 4 9 12 4 20" fill="currentColor"/>',
    "wf-arrow-down":     '<polygon points="12 21 4 4 12 9 20 4" fill="currentColor"/>',
    "wf-arrow-left":     '<polygon points="3 12 20 4 15 12 20 20" fill="currentColor"/>',
    "wf-arrow-up-right": '<path d="M8 5h11v11l-3-3-5 5-5-5 5-5z" fill="currentColor"/>',
    "wf-arrow-up-left":  '<path d="M16 5H5v11l3-3 5 5 5-5-5-5z" fill="currentColor"/>',
    "wf-u-turn":         '<path d="M17 18V11a5 5 0 0 0-10 0v7H5V11a7 7 0 0 1 14 0v7zm-3.5-3.5L7 18l-3.5-6.5h7z" fill="currentColor"/>',
    "wf-signpost":       '<path d="M11 3h2v18h-2zM6 5h9l3 2.5-3 2.5H6zM9 13h9l3 2.5-3 2.5H9z" fill="currentColor"/>',
    "wf-pin":            '<path d="M12 2a8 8 0 0 0-8 8c0 5 5.5 10.5 7.5 12.2a1 1 0 0 0 1 0C14.5 20.5 20 15 20 10a8 8 0 0 0-8-8zm0 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6z" fill="currentColor"/>',
    "wf-facing":         '<path d="M12 2a10 10 0 1 0 0 20A10 10 0 0 0 12 2zm0 2l4 9-4-2-4 2z" fill="currentColor"/><circle cx="12" cy="16.5" r="1.5" fill="currentColor"/>',
    "wf-map":            '<path d="M9 3.5L3 6.3v13.4l6-2.6 6 2.6 6-2.6V3.7L15 6.3zM9 5.2l6 2.6v11.6L9 16.8zm-2 12.4L3 19V7.8l4-1.7zm10-9.2V20l4-2V6.2z" fill="currentColor"/>',
    "wf-touch":          '<path d="M12 2a10 10 0 0 1 10 10h-2a8 8 0 0 0-8-8zm0 4a6 6 0 0 1 6 6h-2a4 4 0 0 0-4-4zm-3 8V8.5a1.5 1.5 0 0 1 3 0V13a1.5 1.5 0 0 1 1.5-1.5A1.5 1.5 0 0 1 15 13v.5a1.5 1.5 0 0 1 3 0V15a6 6 0 0 1-6 6h-2a6 6 0 0 1-4.2-1.8L5 15.4a1.5 1.5 0 1 1 2-2.2l2 1.8z" fill="currentColor"/>',

    # --- Category 2: Building ---
    "wf-entrance":       '<path d="M9 3h12v18H9zm2 9H7.5l2.5 3v-2h4v-2h-4v-2l-2.5 3zm3-9v18l6-3V6z" fill="currentColor"/>',
    "wf-exit":           '<path d="M3 3h12v18H3zm11 0v18l7-3.5V6.5zm-5 9h7v-2l3 3-3 3v-2H9v-2z" fill="currentColor"/>',
    "wf-lift":           '<path d="M4 3h7v18H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2zm7 0h9a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-9zM6 10l2 3h-4zm10 4l-2-3h4z" fill="currentColor"/>',
    "wf-stairs":         '<path d="M3 19h5v-4h5v-4h5V7h3v-2h-5v4h-5v4H6v4H1v2z" fill="currentColor"/>',
    "wf-escalator-up":   '<path d="M3 3h18a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2zm6 4a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm3 3l-6 8h4l6-8zm3-3h4v4l-4-4z" fill="currentColor"/>',
    "wf-escalator-down": '<path d="M3 3h18a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2zm6 11a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm3-11L6 13h4l6-8zm3 13h4v-4l-4 4z" fill="currentColor"/>',
    "wf-ramp":           '<path d="M3 19L3 10l18 9zm8-8a2 2 0 1 0 0-4 2 2 0 0 0 0 4z" fill="currentColor"/>',
    "wf-accessible":     '<circle cx="12" cy="4" r="2.5" fill="currentColor"/><path d="M9 9h6l2 4h-3v3l3 2H9a5 5 0 1 1-2-4l1-3z" fill="currentColor"/>',
    "wf-levels":         '<path d="M12 2L3 6.5 12 11l9-4.5zm0 5.5L5 11l7 3.5 7-3.5zm0 5L5 16l7 3.5 7-3.5z" fill="currentColor"/>',
    "wf-no-entry":       '<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.5 11H7.5v-2h9v2z" fill="currentColor"/>',
    "wf-prohibited":     '<path d="M12 2a10 10 0 1 0 0 20A10 10 0 0 0 12 2zM4 12a8 8 0 0 1 12.9-6.3l-11.2 11.2A7.96 7.96 0 0 1 4 12zm8 8a8 8 0 0 1-4.9-1.7l11.2-11.2A8 8 0 0 1 20 12a8 8 0 0 1-8 8z" fill="currentColor"/>',
    "wf-staff-only":     '<path d="M5 2h14a2 2 0 0 1 2 2v17H3V4a2 2 0 0 1 2-2zm7 3a4 4 0 1 0 0 8 4 4 0 0 0 0-8zm-4 9a6 6 0 0 0-2 4h12a6 6 0 0 0-2-4z" fill="currentColor"/>',

    # --- Category 3: Amenities ---
    "wf-toilets":        '<circle cx="7.5" cy="5" r="2" fill="currentColor"/><path d="M5.5 8.5h4v7h-1v4H6v-4H5v-7z" fill="currentColor"/><circle cx="16.5" cy="5" r="2" fill="currentColor"/><path d="M14 8.5h5l1.5 5.5h-2.5l-1 5h-1l-1-5H12.5z" fill="currentColor"/>',
    "wf-toilet-male":    '<circle cx="12" cy="4.5" r="2.5" fill="currentColor"/><path d="M9 9.5a1 1 0 0 0-1 1v5h2v5h4v-5h2v-5a1 1 0 0 0-1-1z" fill="currentColor"/>',
    "wf-toilet-female":  '<circle cx="12" cy="4.5" r="2.5" fill="currentColor"/><path d="M9.5 9.5l-2.5 7h3.5v4h3v-4h3.5l-2.5-7z" fill="currentColor"/>',
    "wf-toilet-accessible": '<circle cx="13" cy="4.5" r="2.5" fill="currentColor"/><path d="M9.5 9.5h5l2.5 5.5h-3v3l3 1.5H9.5a5.5 5.5 0 1 1-2-4.5l1.5-3.5z" fill="currentColor"/>',
    "wf-baby-change":    '<circle cx="7" cy="8" r="2" fill="currentColor"/><path d="M3 19h18v-2H3zm3-4h6l1.5-4h3.5a3.5 3.5 0 0 0 0-7H13v2h3.5a1.5 1.5 0 0 1 0 3H13l-1.5 4H5z" fill="currentColor"/>',
    "wf-cafe":           '<path d="M4 8v7a4 4 0 0 0 4 4h4a4 4 0 0 0 4-4v-3h2a3 3 0 0 0 0-6h-2V8zm12 3h2a1 1 0 0 1 0 2h-2zM2 21h18v-1H2z" fill="currentColor"/>',
    "wf-food":           '<path d="M5.5 3v7.5a3.5 3.5 0 0 0 3 3.4V21h2v-7a3.5 3.5 0 0 0 3-3.4V3h-2v6h-1V3h-1v6h-1V3zm12.5 0v18h-2V10.5a3.5 3.5 0 0 1-2-3.2V3h1v4h1V3z" fill="currentColor"/>',
    "wf-retail":         '<path d="M6 7V5a3 3 0 0 1 3-3h6a3 3 0 0 1 3 3v2h2a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V9a2 2 0 0 1 2-2zm3-2v2h6V5a1 1 0 0 0-1-1H10a1 1 0 0 0-1 1zm3 7a3 3 0 1 0 0 6 3 3 0 0 0 0-6z" fill="currentColor"/>',
    "wf-atm":            '<path d="M3 4h18a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2zm0 5h18v-2H3zm4 5h5v-2H7zm8 0h3a1 1 0 0 0 1-1v-1a1 1 0 0 0-1-1h-3a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1z" fill="currentColor"/>',
    "wf-payment":        '<path d="M3 5h18a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2zm0 5h18v-3H3zm2 5a2 2 0 1 0 0-4 2 2 0 0 0 0 4zm4 0a2 2 0 1 0 0-4 2 2 0 0 0 0 4z" fill="currentColor"/>',
    "wf-pharmacy":       '<path d="M3 5h18a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3H3a3 3 0 0 1-3-3V8a3 3 0 0 1 3-3zm8 3v3H8v2h3v3h2v-3h3v-2h-3V8z" fill="currentColor"/>',
    "wf-water":          '<path d="M5 20h14v-2H5zm3-4h8a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2H9v-2H7v2H6a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2zm5-9v2H9V7zm-2 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3z" fill="currentColor"/>',
    "wf-wifi":           '<path d="M12 6C7 6 2.8 8.7 0 12.7L2 15A14 14 0 0 1 22 15l2-2.3A17 17 0 0 0 12 6zm0 4a10 10 0 0 1 7.5 3.4l-2 2A7 7 0 0 0 12 13a7 7 0 0 0-5.5 2.4l-2-2A10 10 0 0 1 12 10zm0 4a5 5 0 0 1 3.5 1.4l-2 2a2.5 2.5 0 0 0-3 0l-2-2A5 5 0 0 1 12 14zm0 4a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3z" fill="currentColor"/>',
    "wf-seating":        '<path d="M5 3h2v11H5zm12 0h2v11h-2zm-9 9h8v10h-2v-4H8v4H6V12zm0 2v2h8v-2zm-4 8v-2h16v2z" fill="currentColor"/>',

    # --- Category 4: Transit ---
    "wf-parking":        '<path d="M4 3h16a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2zm5 4v10h2v-3h3.5a4 4 0 0 0 0-8H9zm2 2h3.5a2 2 0 0 1 0 4H11z" fill="currentColor"/>',
    "wf-car":            '<path d="M4.8 10L7 5h10l2.2 5H21a1 1 0 0 1 1 1v7h-2v2h-4v-2H8v2H4v-2H2v-7a1 1 0 0 1 1-1zm2.2 1a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm10 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4z" fill="currentColor"/>',
    "wf-bus":            '<path d="M4 3h16a3 3 0 0 1 3 3v12a3 3 0 0 1-3 3H4a3 3 0 0 1-3-3V6a3 3 0 0 1 3-3zm0 6h16V6H4zm4 4a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm8 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4zM6 18v3h2v-3zm10 0v3h2v-3z" fill="currentColor"/>',
    "wf-ev":             '<path d="M3 4h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2zm6 3L7 12h3l-2 5 6-7h-3l2-4zm6 1h3a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2h-1v3h-2z" fill="currentColor"/>',

    # --- Category 5: Services ---
    "wf-info":           '<path d="M12 2a10 10 0 1 0 0 20A10 10 0 0 0 12 2zm0 5a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3zm-1 5h2v7h-2z" fill="currentColor"/>',
    "wf-help":           '<path d="M12 2a10 10 0 1 0 0 20A10 10 0 0 0 12 2zm0 16.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm1.5-6c0 .5-.5 1-1 1.5a2 2 0 0 0-.5 1v.5h-2V14a3 3 0 0 1 .8-2c.5-.5 1.2-1 1.2-1.5a1.5 1.5 0 0 0-3 0H7a3.5 3.5 0 0 1 7 0z" fill="currentColor"/>',
    "wf-reception":      '<path d="M12 3a4 4 0 1 1 0 8 4 4 0 0 1 0-8zm0 2a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm0 7a7 7 0 0 1 7 7H5a7 7 0 0 1 7-7zm-9 9h18v2H3z" fill="currentColor"/>',
    "wf-security":       '<path d="M12 2l9 3.4V12c0 5.2-3.8 10-9 11.5C6.8 22 3 17.2 3 12V5.4zm3 8l-4.5 4.5L8 12l-1.5 1.5 4 4L16.5 11z" fill="currentColor"/>',
    "wf-phone":          '<path d="M6 3.8C5 3 4 3 3.3 3.7L2 5C1 6 1 9.5 6 14.5S18 23 19 22l1.3-1.3c.7-.7.7-1.7-.1-2.7l-2-2.5c-.8-.9-1.8-.7-2.3-.2l-1 1c-.2.2-1 .1-2-.7s-2-2.2-2.7-3.3-.7-2-.4-2.3l1-1c.5-.5.7-1.5-.2-2.3z" fill="currentColor"/>',
    "wf-intercom":       '<path d="M6 3h12a3 3 0 0 1 3 3v12a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3V6a3 3 0 0 1 3-3zm6 3a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7zm0 9h-1v4h2v-4zm-8-7a15 15 0 0 0 0 8h2a13 13 0 0 1 0-8zm14 0h-2a13 13 0 0 1 0 8h2a15 15 0 0 0 0-8z" fill="currentColor"/>',

    # --- Category 6: Healthcare ---
    "wf-hospital":       '<path d="M4 3h16a2 2 0 0 1 2 2v16a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2zm7 4v4H7v2h4v4h2v-4h4v-2h-4V7zm2 14v-3H9v3z" fill="currentColor"/>',
    "wf-first-aid":      '<path d="M3 6h18a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2zm6-3h6a1 1 0 0 1 1 1v2H8V4a1 1 0 0 1 1-1zm2 6v3H8v2h3v3h2v-3h3v-2h-3V9z" fill="currentColor"/>',
    "wf-consult":        '<circle cx="12" cy="5" r="3" fill="currentColor"/><path d="M8 12a4 4 0 0 1 8 0v2H8zm-2 2v2a6 6 0 0 0 12 0v-2z" fill="currentColor"/><circle cx="18" cy="14" r="2" fill="currentColor"/>',
    "wf-pathology":      '<path d="M9 3h6v4H9zM10 7l-6 12a2 2 0 0 0 1.8 2.9h12.4a2 2 0 0 0 1.8-2.9L14 7zm2 7a2 2 0 1 1 0 4 2 2 0 0 1 0-4zm-2 5h4v1h-4z" fill="currentColor"/>',
    "wf-aed":            '<path d="M12 2a10 10 0 1 0 0 20A10 10 0 0 0 12 2zm1 3L9.5 12H12l-1 5 5-7H13z" fill="currentColor"/>',

    # --- Category 7: Campus ---
    "wf-student":        '<path d="M12 2L2 7.5 12 13 22 7.5zm-6 7v5a7 7 0 0 0 12 0V9l-6 3zm12 7.5v-1l2-1v3.5h-2z" fill="currentColor"/>',
    "wf-library":        '<path d="M4 3h4a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1zm5.5 0h4a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1h-4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1zm5.3 1l3.8 14.8a1 1 0 0 1-.7 1.2L16 21.3a1 1 0 0 1-1.2-.7L11 5.8zM2 21h20v2H2z" fill="currentColor"/>',
    "wf-lecture":        '<path d="M4 3h16a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-7v2a2 2 0 1 1 2 2H9a2 2 0 1 1 2-2v-2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2zm7 16a1 1 0 1 0 0-2 1 1 0 0 0 0 2z" fill="currentColor"/>',

    # --- Category 8: Safety ---
    "wf-emergency":      '<path d="M12 1.5L13.5 3l-1.5.6V5.5l2-2 1.5 1.5-2 2V11h-2V7l-2-2 1.5-1.5 2 2V3.5zm-4 6.5h8a4 4 0 0 0-8 0zm-2 2h12v11a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2z" fill="currentColor"/>',
    "wf-evacuate":       '<path d="M3 3h9a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2zm16 0a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zm-4 5l2 2-3 4 5 4-1.5 1.5-5-3.5-3 2.5v-2l5-6z" fill="currentColor"/>',
    "wf-assembly":       '<path d="M4 4H8v4l-4-4zm12 0h4l-4 4zm-4 4a4 4 0 1 0 0 8 4 4 0 0 0 0-8zM4 20l4-4H4zm16 0v-4l-4 4z" fill="currentColor"/>',
    "wf-fire":           '<path d="M12 2c0 4-4 6.5-4 10a7 7 0 0 0 14 0c0-4-3-6.5-4-8.5-1 2-2 3-3 4-.5-2.5-.5-4.5-3-5.5zm0 12.5a2 2 0 1 1 0-4 2 2 0 0 1 0 4z" fill="currentColor"/>',
    "wf-warning":        '<path d="M13 3L23 21H1zm-1 9v4h2v-4zm0 6h2v2h-2z" fill="currentColor"/>',
    "wf-construction":   '<path d="M12 2L3 20h18zm0 5l5.5 11H6.5zM11 14h2v3h-2zm-1.5-2h5v1.5h-5z" fill="currentColor"/>',

    # --- Category 9: UI ---
    "wf-home":           '<path d="M3 10.5L12 3l9 7.5V20a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-9.5zm7 11v-7h4v7z" fill="currentColor"/>',
    "wf-search":         '<path d="M11 2a9 9 0 1 0 5.6 16l4.7 4.7 1.4-1.4L18 16.6A9 9 0 0 0 11 2zm0 2a7 7 0 1 1 0 14A7 7 0 0 1 11 4z" fill="currentColor"/>',
    "wf-menu":           '<path d="M3 5h18v2H3zm0 6h18v2H3zm0 6h18v2H3z" fill="currentColor"/>',
    "wf-back":           '<path d="M16 4l-8 8 8 8V4z" fill="currentColor"/>',
    "wf-close":          '<path d="M4.3 4.3l15.4 15.4-1.4 1.4L2.9 5.7zm15.4 0l1.4 1.4L5.7 21.1l-1.4-1.4z" fill="currentColor"/>',
    "wf-hours":          '<path d="M12 2a10 10 0 1 0 0 20A10 10 0 0 0 12 2zm0 2a8 8 0 0 1 0 16A8 8 0 0 1 12 4zm-1 5v6l5 3-1 1.7-6-3.7V9z" fill="currentColor"/>',
    "wf-timetable":      '<path d="M3 4h18a2 2 0 0 1 2 2v15a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2zm5-3h2v3H8zm8 0h2v3h-2zm-11 8h16v-2H5zm2 4h4v-2H7zm6 0h4v-2h-4z" fill="currentColor"/>',
    "wf-events":         '<path d="M3 4h18a2 2 0 0 1 2 2v15a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2zm5-3h2v3H8zm8 0h2v3h-2zM5 10h14v-2H5zm7 2l1.5 3.5 3.5.5-2.5 2.5.5 3.5-3-1.5-3 1.5.5-3.5L7 16l3.5-.5z" fill="currentColor"/>',
    "wf-news":           '<path d="M3 4h18a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2zm2 4h14v-2H5zm0 3h6v5H5zm8 0h6v2h-6zm0 3h6v2h-6z" fill="currentColor"/>',
    "wf-announce":       '<path d="M3 11h4L13 5v14l-6-6H3a1 1 0 0 1-1-1v-1zm14-2.5a5 5 0 0 1 0 7l-1.4-1.4a3 3 0 0 0 0-4.2zm2.5-2.5a9 9 0 0 1 0 12.5l-1.4-1.4a7 7 0 0 0 0-9.7z" fill="currentColor"/>',

    # --- Category 10: Media ---
    "wf-share":          '<path d="M18 16a3 3 0 0 0-2.4 1.2L8.9 13.5a3 3 0 0 0 0-3L15.6 6.8A3 3 0 1 0 14.5 5l-6.7 3.7a3 3 0 1 0 0 6.6L14.5 19A3 3 0 1 0 18 16z" fill="currentColor"/>',
    "wf-chat":           '<path d="M2 5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-7l-5 4v-4H4a2 2 0 0 1-2-2zm6 4a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm4 0a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm4 0a1 1 0 1 0 0 2 1 1 0 0 0 0-2z" fill="currentColor"/>',
    "wf-like":           '<path d="M14 2c-1 0-2 .7-2 2v4H7a2 2 0 0 0-2 1.6l-1 8A2 2 0 0 0 6 20h13a2 2 0 0 0 2-2v-8a2 2 0 0 0-2-2h-3V4c0-1.1-.9-2-2-2zM4 10H1v10h3z" fill="currentColor"/>',
    "wf-camera":         '<path d="M8.6 4l-1.4 2H5a2 2 0 0 0-2 2v11a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-2.2L15.4 4zm3.4 5a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9zm5.5 1a1 1 0 1 1 0 2 1 1 0 0 1 0-2z" fill="currentColor"/>',
    "wf-video":          '<path d="M3 5h13a2 2 0 0 1 2 2v1.5l5-3.5v14l-5-3.5V17a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2z" fill="currentColor"/>',
    "wf-qr":             '<path d="M3 3h7v7H3zm1 1v5h5V4zm1 1h3v3H5zm7-2h7v7h-7zm1 1v5h5V4zm1 1h3v3h-3zM3 14h7v7H3zm1 1v5h5v-5zm1 1h3v3H5zm7-1h3v3h-3zm4 0h3v1.5h-3zm0 2.5h3V20h-3zM14 18h3v3h-3z" fill="currentColor"/>',
    "wf-email":          '<path d="M3 5h18a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2zm9 7.5L3.5 7h17z" fill="currentColor"/>',
    "wf-web":            '<path d="M12 2a10 10 0 1 0 0 20A10 10 0 0 0 12 2zm0 2c1 0 2.5 2 3.2 6H8.8C9.5 6 11 4 12 4zm-8 8a8 8 0 0 1 .3-2h3.4a24 24 0 0 0 0 4H4.3A8 8 0 0 1 4 12zm4 6.7a8 8 0 0 1-3.5-4.7h3a14 14 0 0 0 .5 4.7zm0-4.7h8a14 14 0 0 1-.8 4.7 8 8 0 0 1-6.4 0A14 14 0 0 1 8 14zm9.7 0h3a8 8 0 0 1-3.5 4.7 14 14 0 0 0 .5-4.7zm3-2h-3.4a24 24 0 0 0 0-4h3.4a8 8 0 0 1 0 4zm-5.5-4H8.8a12 12 0 0 1 6.4 0z" fill="currentColor"/>',
}

assert len(M3_ICONS_FILLED) == 80, f"Expected 80 filled icons, got {len(M3_ICONS_FILLED)}"


def generate_svg_files():
    print(f"Generating {len(M3_ICONS)} M3 SVGs in {SVG_M3_DIR}...")
    for icon_id, paths in M3_ICONS.items():
        svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-m3 {icon_id}">
  {paths}
</svg>
'''
        file_path = os.path.join(SVG_M3_DIR, f"{icon_id}.svg")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
    print("M3 SVG files generated successfully.")

def build_sprite():
    sprite_path = os.path.join(DIST_DIR, "wayfinding-icons-m3.svg")
    print(f"Building sprite sheet {sprite_path}...")
    with open(sprite_path, "w", encoding="utf-8") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" style="display: none;">\n')
        for icon_id, paths in M3_ICONS.items():
            f.write(f'  <symbol id="{icon_id}" viewBox="0 0 24 24">\n    <g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n      {paths}\n    </g>\n  </symbol>\n')
        f.write('</svg>\n')
    print("M3 SVG sprite generated.")

def update_metadata():
    json_path = os.path.join(DIST_DIR, "wayfinding-icons.json")
    print(f"Updating {json_path} with paths_m3 and paths_m3_filled...")
    with open(json_path, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    for item in metadata:
        icon_id = item["id"]
        item["paths_m3"] = M3_ICONS.get(icon_id, "")
        item["paths_m3_filled"] = M3_ICONS_FILLED.get(icon_id, "")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)
    print("wayfinding-icons.json updated successfully.")

def update_js():
    js_path = os.path.join(DIST_DIR, "wayfinding-icons.js")
    print(f"Updating {js_path}...")
    with open(js_path, "r", encoding="utf-8") as f:
        js = f.read()

    # 1. Export WAYFINDING_M3
    m3_json = json.dumps(M3_ICONS, indent=2)
    export_stmt = f"\nexport const WAYFINDING_M3 = {m3_json};\n"

    if "export const WAYFINDING_M3" not in js:
        # Insert before renderWayfindingIcon
        idx = js.find("export function renderWayfindingIcon")
        if idx != -1:
            js = js[:idx] + export_stmt + "\n" + js[idx:]
        else:
            js += export_stmt

    # 2. Update renderWayfindingIcon for 'm3'
    if "set === 'm3'" not in js:
        target = "if (set === 'gf-example') {"
        replacement = """if (set === 'm3') {
    const paths = WAYFINDING_M3[iconId] || '';
    return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-m3 ${iconId} ${className}">${paths}</svg>`;
  }
  if (set === 'gf-example') {"""
        js = js.replace(target, replacement, 1)

    # 3. Update Web Component for 'm3'
    if "set === 'm3'" not in js:
        wc_target = "} else if (set === 'gf-example') {"
        wc_replacement = """} else if (set === 'm3') {
      const paths = WAYFINDING_M3[name] || '';
      this.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-m3 ${name}">${paths}</svg>`;
    } else if (set === 'gf-example') {"""
        js = js.replace(wc_target, wc_replacement, 1)

    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js)
    print("wayfinding-icons.js updated successfully.")

def update_css():
    css_path = os.path.join(DIST_DIR, "wayfinding-icons.css")
    print(f"Updating {css_path}...")
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    m3_css = """
/* Material Design 3 (M3) Outlined Vector Signage */
.wf-icon-m3 {
  fill: none;
  stroke: currentColor;
  stroke-width: var(--live-stroke, 2px);
  stroke-linecap: round;
  stroke-linejoin: round;
}
.wf-icon-m3 [fill="currentColor"] {
  fill: currentColor;
}
.wf-icon-m3 [stroke="none"] {
  stroke: none;
}
"""
    if ".wf-icon-m3" not in css:
        css += m3_css
        with open(css_path, "w", encoding="utf-8") as f:
            f.write(css)
        print("wayfinding-icons.css updated successfully.")
    else:
        print(".wf-icon-m3 already present in CSS.")

if __name__ == "__main__":
    assert len(M3_ICONS) == 80, f"Expected 80 icons, found {len(M3_ICONS)}"
    generate_svg_files()
    build_sprite()
    update_metadata()
    update_js()
    update_css()
    print("All M3 icon assets built successfully!")
