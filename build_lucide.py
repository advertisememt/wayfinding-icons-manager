"""
Build Script for Lucide Open Source Icon Set
License: ISC License (100% Free for Commercial & Personal Use)
https://lucide.dev / https://github.com/lucide-icons/lucide
All icons designed on 24x24 viewBox, stroke-width 2, round linecaps and linejoins.
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SVG_DIR = os.path.join(BASE_DIR, "svg", "lucide")
DIST_DIR = os.path.join(BASE_DIR, "dist")
os.makedirs(SVG_DIR, exist_ok=True)
os.makedirs(DIST_DIR, exist_ok=True)

LUCIDE_ICONS = {
    # ----------------------------------------------------
    # Category 1: Navigation (12 icons)
    # ----------------------------------------------------
    "wf-arrow-up": '<path d="m5 12 7-7 7 7"/><path d="M12 19V5"/>',
    "wf-arrow-right": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    "wf-arrow-down": '<path d="M12 5v14"/><path d="m19 12-7 7-7-7"/>',
    "wf-arrow-left": '<path d="m12 19-7-7 7-7"/><path d="M19 12H5"/>',
    "wf-arrow-up-right": '<path d="M7 7h10v10"/><path d="M7 17 17 7"/>',
    "wf-arrow-up-left": '<path d="M17 7H7v10"/><path d="M17 17 7 7"/>',
    "wf-u-turn": '<path d="M9 10v5a3 3 0 0 0 6 0v-8"/><path d="m9 14-3-3 3-3"/>',
    "wf-signpost": '<path d="M10 9H4L2 7l2-2h6"/><path d="M14 5h6l2 2-2 2h-6"/><path d="M10 22V2"/><path d="M14 22V2"/>',
    "wf-pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    "wf-facing": '<circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/>',
    "wf-map": '<polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"/><line x1="9" x2="9" y1="3" y2="18"/><line x1="15" x2="15" y1="6" y2="21"/>',
    "wf-touch": '<path d="m3 3 7.07 16.97 2.51-7.39 7.39-2.51L3 3z"/><path d="m13 13 6 6"/>',

    # ----------------------------------------------------
    # Category 2: Building (12 icons)
    # ----------------------------------------------------
    "wf-entrance": '<path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"/><polyline points="10 17 15 12 10 7"/><line x1="15" x2="3" y1="12" y2="12"/>',
    "wf-exit": '<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/>',
    "wf-lift": '<rect width="18" height="18" x="3" y="3" rx="2"/><polyline points="7 10 10 7 13 10"/><polyline points="7 14 10 17 13 14"/><line x1="17" y1="3" x2="17" y2="21"/>',
    "wf-stairs": '<path d="M19 5v4h-4v4h-4v4H7v4H3"/>',
    "wf-escalator-up": '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M6 17h3l6-8h3"/><polyline points="13 6 18 6 18 11"/>',
    "wf-escalator-down": '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M6 7h3l6 8h3"/><polyline points="13 18 18 18 18 13"/>',
    "wf-ramp": '<path d="M3 19h18L3 10v9z"/><circle cx="10" cy="7" r="2"/>',
    "wf-accessible": '<circle cx="16" cy="4" r="1"/><path d="m18 19 1-7-6 1"/><path d="m5 8 3-3 5.5 3-2.36 3.5"/><path d="M4.24 14.5a5 5 0 0 0 6.88 6"/><path d="M13.76 17.5a5 5 0 0 0-4-7.5"/>',
    "wf-levels": '<path d="m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z"/><path d="m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65"/><path d="m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65"/>',
    "wf-no-entry": '<circle cx="12" cy="12" r="10"/><line x1="4.93" x2="19.07" y1="4.93" y2="19.07"/>',
    "wf-prohibited": '<circle cx="12" cy="12" r="10"/><line x1="4.93" x2="19.07" y1="19.07" y2="4.93"/>',
    "wf-staff-only": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><polyline points="16 11 18 13 22 9"/>',

    # ----------------------------------------------------
    # Category 3: Amenities (14 icons)
    # ----------------------------------------------------
    "wf-toilets": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "wf-toilet-male": '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    "wf-toilet-female": '<circle cx="12" cy="5" r="2"/><path d="m9 20 3-6 3 6"/><path d="m6 8 6 2 6-2"/><path d="M12 10v4"/>',
    "wf-toilet-accessible": '<circle cx="16" cy="4" r="1.5"/><path d="m18 19 1-7-6 1"/><path d="m5 8 3-3 5.5 3-2.36 3.5"/><path d="M4.24 14.5a5 5 0 0 0 6.88 6"/>',
    "wf-baby-change": '<path d="M9 12h.01"/><path d="M15 12h.01"/><path d="M10 16c.5.3 1.2.5 2 .5s1.5-.2 2-.5"/><path d="M19 6.3a9 9 0 0 1 1.8 3.9 2 2 0 0 1 0 3.6 9 9 0 0 1-17.6 0 2 2 0 0 1 0-3.6A9 9 0 0 1 12 3c2 0 3.5 1.1 3.5 2.5s-.9 2.5-2 2.5c-.8 0-1.5-.4-1.5-1"/>',
    "wf-cafe": '<path d="M17 8h1a4 4 0 1 1 0 8h-1"/><path d="M3 8h14v9a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4Z"/><line x1="6" x2="6" y1="2" y2="4"/><line x1="10" x2="10" y1="2" y2="4"/><line x1="14" x2="14" y1="2" y2="4"/>',
    "wf-food": '<path d="M18 2v6a3 3 0 0 1-3 3 3 3 0 0 1-3-3V2"/><path d="M15 2v14a3 3 0 0 1-3 3H9"/><line x1="15" x2="15" y1="8" y2="22"/><path d="M6 2v20"/><path d="M3 2v6a3 3 0 0 0 6 0V2"/>',
    "wf-retail": '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/>',
    "wf-atm": '<rect width="20" height="14" x="2" y="5" rx="2"/><line x1="2" x2="22" y1="10" y2="10"/><path d="M7 15h4"/><rect width="3" height="3" x="15" y="13" rx="0.5"/>',
    "wf-payment": '<path d="M19 7V4a1 1 0 0 0-1-1H5a2 2 0 0 0 0 4h15a1 1 0 0 1 1 1v4h-3a2 2 0 0 0 0 4h3a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1"/><path d="M3 5v14a2 2 0 0 0 2 2h15a1 1 0 0 0 1-1v-4"/>',
    "wf-pharmacy": '<rect width="18" height="18" x="3" y="3" rx="3"/><line x1="12" x2="12" y1="8" y2="16"/><line x1="8" x2="16" y1="12" y2="12"/>',
    "wf-water": '<path d="M7 16.3c2.2 0 4-1.83 4-4.05 0-1.16-.57-2.26-1.71-3.19S7.29 6.75 7 5.3c-.29 1.45-1.14 2.84-2.29 3.76S3 11.1 3 12.25c0 2.22 1.8 4.05 4 4.05z"/><path d="M12.56 6.6A10.97 10.97 0 0 0 14 3.02c.5 2.5 2 4.9 4 6.5s3 3.5 3 5.5a6.98 6.98 0 0 1-11.91 4.97"/>',
    "wf-wifi": '<path d="M12 20h.01"/><path d="M2 8.82a15 15 0 0 1 20 0"/><path d="M5 12.86a10 10 0 0 1 14 0"/><path d="M8.5 16.43a5 5 0 0 1 7 0"/>',
    "wf-seating": '<path d="M19 9V6a2 2 0 0 0-2-2H7a2 2 0 0 0-2 2v3"/><path d="M3 16a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-5a2 2 0 0 0-4 0v2H7v-2a2 2 0 0 0-4 0Z"/><path d="M5 18v2"/><path d="M19 18v2"/>',

    # ----------------------------------------------------
    # Category 4: Transit (4 icons)
    # ----------------------------------------------------
    "wf-parking": '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M9 17V7h4a3 3 0 0 1 0 6H9"/>',
    "wf-car": '<path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2"/><circle cx="7" cy="17" r="2"/><path d="M9 17h6"/><circle cx="17" cy="17" r="2"/>',
    "wf-bus": '<path d="M8 6v6"/><path d="M15 6v6"/><path d="M2 12h19.6"/><path d="M18 18h3s.5-1.7.8-2.8c.1-.4.2-.8.2-1.2 0-.4-.1-.8-.2-1.2l-1.4-5C20.1 6.8 19.1 6 18 6H4a2 2 0 0 0-2 2v10h3"/><circle cx="7" cy="18" r="2"/><path d="M9 18h5"/><circle cx="16" cy="18" r="2"/>',
    "wf-ev": '<rect width="12" height="18" x="3" y="3" rx="2"/><path d="M15 8h2a2 2 0 0 1 2 2v5a2 2 0 0 0 2 2v0a2 2 0 0 0 2-2V9"/><path d="m8 10 2-4-3 7h3l-2 4"/>',

    # ----------------------------------------------------
    # Category 5: Services (6 icons)
    # ----------------------------------------------------
    "wf-info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>',
    "wf-help": '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>',
    "wf-reception": '<path d="M2 18a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v2H2v-2Z"/><path d="M20 16a8 8 0 1 0-16 0"/><path d="M12 4v4"/><path d="M10 4h4"/>',
    "wf-security": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
    "wf-phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "wf-intercom": '<path d="M4.9 19.1C1 15.2 1 8.8 4.9 4.9"/><path d="M7.8 16.2c-2.3-2.3-2.3-6.1 0-8.5"/><circle cx="12" cy="12" r="2"/><path d="M16.2 7.8c2.3 2.3 2.3 6.1 0 8.5"/><path d="M19.1 4.9C23 8.8 23 15.1 19.1 19"/>',

    # ----------------------------------------------------
    # Category 6: Healthcare (5 icons)
    # ----------------------------------------------------
    "wf-hospital": '<path d="M12 6v4"/><path d="M14 8h-4"/><path d="M18 18h2a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h2"/><path d="M6 14h12v8H6z"/>',
    "wf-first-aid": '<path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><rect width="20" height="14" x="2" y="7" rx="2"/><path d="M12 11v6"/><path d="M9 14h6"/>',
    "wf-consult": '<path d="M4.8 2.3A.3.3 0 1 0 5 2H4a2 2 0 0 0-2 2v5a6 6 0 0 0 6 6v0a6 6 0 0 0 6-6V4a2 2 0 0 0-2-2h-1a.2.2 0 1 0 .3.3"/><path d="M8 15v1a6 6 0 0 0 6 6v0a6 6 0 0 0 6-6v-4"/><circle cx="20" cy="10" r="2"/>',
    "wf-pathology": '<path d="M10 2v7.527a2 2 0 0 1-.211.896L4.72 20.55a1 1 0 0 0 .9 1.45h12.76a1 1 0 0 0 .9-1.45l-5.069-10.127A2 2 0 0 1 14 9.527V2"/><path d="M8.5 2h7"/><path d="M7 16h10"/>',
    "wf-aed": '<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/><path d="M3.22 12H9.5l.5-1 2 4.5 2-7 1.5 3.5h5.27"/>',

    # ----------------------------------------------------
    # Category 7: Campus (3 icons)
    # ----------------------------------------------------
    "wf-student": '<path d="M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z"/><path d="M22 10v6"/><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"/>',
    "wf-library": '<path d="m16 6 4 14"/><path d="M12 6v14"/><path d="M8 8v12"/><path d="M4 4v16"/><path d="M2 20h20"/>',
    "wf-lecture": '<path d="M2 3h20"/><path d="M21 3v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V3"/><path d="m7 21 5-5 5 5"/>',

    # ----------------------------------------------------
    # Category 8: Safety (6 icons)
    # ----------------------------------------------------
    "wf-emergency": '<path d="M7 18v-6a5 5 0 1 1 10 0v6"/><path d="M5 21a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-1a2 2 0 0 0-2-2H7a2 2 0 0 0-2 2z"/><path d="M21 12h1"/><path d="M18.5 4.5 18 5"/><path d="M2 12h1"/><path d="M12 2v1"/><path d="m4.929 4.929.707.707"/><path d="M12 12v6"/>',
    "wf-evacuate": '<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/><circle cx="16" cy="5" r="1.5"/>',
    "wf-assembly": '<circle cx="12" cy="12" r="3"/><path d="M3 7V5a2 2 0 0 1 2-2h2"/><path d="M17 3h2a2 2 0 0 1 2 2v2"/><path d="M21 17v2a2 2 0 0 1-2 2h-2"/><path d="M7 21H5a2 2 0 0 1-2-2v-2"/>',
    "wf-fire": '<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/>',
    "wf-warning": '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" x2="12" y1="9" y2="13"/><line x1="12" x2="12.01" y1="17" y2="17"/>',
    "wf-construction": '<path d="m8 2 1.88 18h4.24L16 2Z"/><path d="M9 9h6"/><path d="M8.5 15h7"/><path d="M2 22h20"/>',

    # ----------------------------------------------------
    # Category 9: UI (10 icons)
    # ----------------------------------------------------
    "wf-home": '<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>',
    "wf-search": '<circle cx="11" cy="11" r="8"/><line x1="21" x2="16.65" y1="21" y2="16.65"/>',
    "wf-menu": '<line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/>',
    "wf-back": '<path d="m15 18-6-6 6-6"/>',
    "wf-close": '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    "wf-hours": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    "wf-timetable": '<rect width="18" height="18" x="3" y="4" rx="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/>',
    "wf-events": '<rect width="18" height="18" x="3" y="4" rx="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/><path d="m12 13 1 2 2.5.5-2 1.5.5 2.5-2-1-2 1 .5-2.5-2-1.5 2.5-.5Z"/>',
    "wf-news": '<path d="M4 22h16a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v16a2 2 0 0 1-2 2Zm0 0a2 2 0 0 1-2-2v-9c0-1.1.9-2 2-2h2"/><path d="M18 14h-8"/><path d="M15 18h-5"/><path d="M10 6h8v4h-8V6Z"/>',
    "wf-announce": '<path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>',

    # ----------------------------------------------------
    # Category 10: Media (8 icons)
    # ----------------------------------------------------
    "wf-share": '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" x2="15.42" y1="13.51" y2="17.49"/><line x1="15.41" x2="8.59" y1="6.51" y2="10.49"/>',
    "wf-chat": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "wf-like": '<path d="M7 10v12"/><path d="M15 5.88 14 10h5.83a2 2 0 0 1 1.92 2.56l-2.33 8A2 2 0 0 1 17.5 22H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h3"/>',
    "wf-camera": '<path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/>',
    "wf-video": '<path d="m22 8-6 4 6 4V8Z"/><rect width="14" height="12" x="2" y="6" rx="2"/>',
    "wf-qr": '<rect width="5" height="5" x="3" y="3" rx="1"/><rect width="5" height="5" x="16" y="3" rx="1"/><rect width="5" height="5" x="3" y="16" rx="1"/><path d="M21 16h-3a2 2 0 0 0-2 2v3"/><path d="M21 21v.01"/><path d="M12 7v3a2 2 0 0 1-2 2H7"/><path d="M3 12h.01"/><path d="M12 3h.01"/><path d="M12 16v.01"/><path d="M16 12h1"/><path d="M21 12v.01"/><path d="M12 21v-1"/>',
    "wf-email": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    "wf-web": '<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>'
}

assert len(LUCIDE_ICONS) == 80, f"Expected 80 icons, found {len(LUCIDE_ICONS)}"

def generate_svg_files():
    print(f"Generating {len(LUCIDE_ICONS)} Lucide SVGs in {SVG_DIR}...")
    for icon_id, paths in LUCIDE_ICONS.items():
        svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-lucide {icon_id}">
  {paths}
</svg>
'''
        with open(os.path.join(SVG_DIR, f"{icon_id}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_content)
    print("Lucide SVGs generated successfully.")

def build_sprite():
    sprite_path = os.path.join(DIST_DIR, "wayfinding-icons-lucide.svg")
    print(f"Building sprite sheet {sprite_path}...")
    with open(sprite_path, "w", encoding="utf-8") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" style="display: none;">\n')
        for icon_id, paths in LUCIDE_ICONS.items():
            f.write(f'  <symbol id="{icon_id}" viewBox="0 0 24 24">\n    <g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n      {paths}\n    </g>\n  </symbol>\n')
        f.write('</svg>\n')
    print("Lucide sprite generated.")

def update_metadata():
    json_path = os.path.join(DIST_DIR, "wayfinding-icons.json")
    print(f"Updating {json_path} with paths_lucide...")
    with open(json_path, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    for item in metadata:
        icon_id = item["id"]
        item["paths_lucide"] = LUCIDE_ICONS.get(icon_id, "")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)
    print("Metadata updated with Lucide paths.")

def update_js():
    js_path = os.path.join(DIST_DIR, "wayfinding-icons.js")
    print(f"Updating {js_path}...")
    with open(js_path, "r", encoding="utf-8") as f:
        js = f.read()

    lucide_json = json.dumps(LUCIDE_ICONS, indent=2)
    export_stmt = f"\nexport const WAYFINDING_LUCIDE = {lucide_json};\n"

    if "export const WAYFINDING_LUCIDE" not in js:
        idx = js.find("export function renderWayfindingIcon")
        if idx != -1:
            js = js[:idx] + export_stmt + "\n" + js[idx:]
        else:
            js += export_stmt

    if "set === 'lucide'" not in js:
        target = "if (set === 'm3') {"
        replacement = """if (set === 'lucide') {
    const paths = WAYFINDING_LUCIDE[iconId] || '';
    return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-lucide ${iconId} ${className}">${paths}</svg>`;
  }
  if (set === 'm3') {"""
        js = js.replace(target, replacement, 1)

    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js)
    print("wayfinding-icons.js updated.")

def update_css():
    css_path = os.path.join(DIST_DIR, "wayfinding-icons.css")
    print(f"Updating {css_path}...")
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    lucide_css = """
/* Lucide Open Source Icons (ISC License) */
.wf-icon-lucide {
  fill: none;
  stroke: currentColor;
  stroke-width: var(--live-stroke, 2px);
  stroke-linecap: round;
  stroke-linejoin: round;
}
"""
    if ".wf-icon-lucide" not in css:
        css += lucide_css
        with open(css_path, "w", encoding="utf-8") as f:
            f.write(css)
        print("wayfinding-icons.css updated.")

if __name__ == "__main__":
    generate_svg_files()
    build_sprite()
    update_metadata()
    update_js()
    update_css()
    print("All Lucide assets generated successfully!")
