import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SVG_DUOTONE_DIR = os.path.join(BASE_DIR, "svg", "duotone")
DIST_DIR = os.path.join(BASE_DIR, "dist")
os.makedirs(SVG_DUOTONE_DIR, exist_ok=True)
os.makedirs(DIST_DIR, exist_ok=True)

# 80 DUOTONE WAYFINDING ICONS
# Designed with two semantic layers:
# Layer 1 (Secondary): opacity="0.25" fill="currentColor" (backing disc, contextual frame, wash, shadow or envelope)
# Layer 2 (Primary): opacity="1.0" fill="currentColor" (crisp focal silhouette, directional arrow, critical indicator)
DUOTONE_ICONS = {
    # 1. Navigation
    "wf-arrow-up": '<circle cx="12" cy="12" r="9" opacity="0.25" fill="currentColor"/><path d="M12 4.5l6 6h-4v9h-4v-9H6z" fill="currentColor"/>',
    "wf-arrow-right": '<circle cx="12" cy="12" r="9" opacity="0.25" fill="currentColor"/><path d="M19.5 12l-6-6v4H4.5v4h9v4z" fill="currentColor"/>',
    "wf-arrow-down": '<circle cx="12" cy="12" r="9" opacity="0.25" fill="currentColor"/><path d="M12 19.5l-6-6h4v-9h4v9h4z" fill="currentColor"/>',
    "wf-arrow-left": '<circle cx="12" cy="12" r="9" opacity="0.25" fill="currentColor"/><path d="M4.5 12l6 6v-4h9v-4h-9V6z" fill="currentColor"/>',
    "wf-arrow-up-right": '<circle cx="12" cy="12" r="9" opacity="0.25" fill="currentColor"/><path d="M19.07 4.93 7.76 4.93 11.29 8.46 2.81 16.95 7.05 21.19 15.54 12.71 19.07 16.24Z" fill="currentColor"/>',
    "wf-arrow-up-left": '<circle cx="12" cy="12" r="9" opacity="0.25" fill="currentColor"/><path d="M4.93 4.93 16.24 4.93 12.71 8.46 21.19 16.95 16.95 21.19 8.46 12.71 4.93 16.24Z" fill="currentColor"/>',
    "wf-u-turn": '<circle cx="12" cy="12" r="9" opacity="0.25" fill="currentColor"/><path d="M9 18l-5-5h3.5A7.5 7.5 0 0 1 15 5.5a7.5 7.5 0 0 1 7.5 7.5v6h-4v-6a3.5 3.5 0 0 0-3.5-3.5A3.5 3.5 0 0 0 11.5 13H15z" fill="currentColor"/>',
    "wf-signpost": '<path d="M12 12H5a1 1 0 0 1-1-1V8a1 1 0 0 1 1-1h7l2 2.5-2 2.5z" opacity="0.25" fill="currentColor"/><rect x="11" y="2" width="2" height="20" rx="1" fill="currentColor"/><path d="M12 5h7a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-7l-2-2.5 2-2.5z" fill="currentColor"/>',
    "wf-pin": '<ellipse cx="12" cy="20.5" rx="5.5" ry="1.75" opacity="0.25" fill="currentColor"/><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 12 7 12s7-6.75 7-12c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z" fill="currentColor"/>',
    "wf-facing": '<circle cx="12" cy="12" r="9" opacity="0.25" fill="currentColor"/><polygon points="12 4 16 13 12 11 8 13" fill="currentColor"/><circle cx="12" cy="17" r="1.2" fill="currentColor"/>',
    "wf-map": '<polygon points="3 6 9 3 9 18 3 21" opacity="0.25" fill="currentColor"/><polygon points="15 6 21 3 21 18 15 21" opacity="0.25" fill="currentColor"/><polygon points="9 3 15 6 15 21 9 18" fill="currentColor"/><circle cx="12" cy="11" r="2" fill="currentColor"/>',
    "wf-touch": '<circle cx="12" cy="4" r="5" opacity="0.2" fill="currentColor"/><circle cx="12" cy="4" r="2.5" opacity="0.3" fill="currentColor"/><path d="M12 11V6a1.5 1.5 0 0 1 3 0v5" fill="currentColor"/><path d="M15 9.5a1.5 1.5 0 0 1 3 0V12a1.5 1.5 0 0 1 3 0v3a6 6 0 0 1-6 6h-2a6 6 0 0 1-4.24-1.76L5 15.4a1.5 1.5 0 0 1 2.2-2L9.5 15V6a1.5 1.5 0 0 1 3 0v5" fill="currentColor"/>',

    # 2. Building
    "wf-entrance": '<path d="M10 2h11a1 1 0 0 1 1 1v17a1 1 0 0 1-1 1h-11v-2h9V4h-9V2z" opacity="0.25" fill="currentColor"/><path d="m19 4-6 2.5v11l6 2.5V4z" opacity="0.35" fill="currentColor"/><rect x="1" y="21" width="22" height="2" rx="0.5" opacity="0.25" fill="currentColor"/><path d="M1 10.5h5V7.5l5.5 4.5-5.5 4.5v-3H1z" fill="currentColor"/>',
    "wf-exit": '<path d="M14 2H3a1 1 0 0 0-1 1v17a1 1 0 0 0 1 1h11v-2H5V4h9V2z" opacity="0.25" fill="currentColor"/><path d="m5 4 6 2.5v11L5 20V4z" opacity="0.35" fill="currentColor"/><rect x="1" y="21" width="22" height="2" rx="0.5" opacity="0.25" fill="currentColor"/><path d="M12.5 10.5h5V7.5l5.5 4.5-5.5 4.5v-3h-5z" fill="currentColor"/>',
    "wf-lift": '<rect x="2" y="2" width="13" height="20" rx="3" opacity="0.25" fill="currentColor"/><circle cx="6" cy="7.5" r="1.5" fill="currentColor"/><path d="M4 16v-3a2 2 0 0 1 4 0v3H4z" fill="currentColor"/><circle cx="11" cy="7.5" r="1.5" fill="currentColor"/><path d="M9 16v-3a2 2 0 0 1 4 0v3H9z" fill="currentColor"/><polygon points="19.5 4 16 8.5 23 8.5" fill="currentColor"/><polygon points="19.5 20 16 15.5 23 15.5" fill="currentColor"/><rect x="18.5" y="10.5" width="2" height="3" rx="0.5" fill="currentColor"/>',
    "wf-stairs": '<path d="M4 19h4v-4h4v-4h4V7h4v12H4z" opacity="0.25" fill="currentColor"/><circle cx="7" cy="5.5" r="1.8" fill="currentColor"/><path d="M5 14l3-3 2 1.5 3-4.5h3v2h-2l-2.5 3.5L10 12l-3 4.5H5z" fill="currentColor"/>',
    "wf-escalator-up": '<path d="M2 7h4.5l7 10H22v3H13.5l-7-10H2V7z" opacity="0.25" fill="currentColor"/><circle cx="8" cy="4.5" r="1.8" fill="currentColor"/><path d="M6 13l2.5-3 2 1.5 2.5-3.5h2v1.5h-1.2l-2 2.8-2-1.5-2 3H6z" fill="currentColor"/><polygon points="18 13 18 18 22 15.5" fill="currentColor"/>',
    "wf-escalator-down": '<path d="M2 17h4.5l7-10H22V4H13.5l-7 10H2v3z" opacity="0.25" fill="currentColor"/><circle cx="16" cy="4.5" r="1.8" fill="currentColor"/><path d="M18 13l-2.5-3-2 1.5-2.5-3.5h-2v1.5h1.2l2 2.8 2-1.5 2 3h1.8z" fill="currentColor"/><polygon points="6 13 6 18 2 15.5" fill="currentColor"/>',
    "wf-ramp": '<polygon points="2 19 22 19 22 11 2 19" opacity="0.25" fill="currentColor"/><circle cx="14" cy="6.5" r="1.8" fill="currentColor"/><path d="M10 11.5a3 3 0 0 1 4-1.2l1.5-1.5 1.4 1-1.5 2a3 3 0 1 1-5.4-.3zm2 3.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z" fill="currentColor"/>',
    "wf-accessible": '<circle cx="12" cy="12" r="9.5" opacity="0.22" fill="currentColor"/><circle cx="12" cy="4.5" r="2" fill="currentColor"/><path d="M10 9h3.5l1.5 5h3" fill="none" stroke="currentColor" stroke-width="2"/><path d="M13.5 14A4 4 0 1 1 8 11.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M8 12h3" fill="none" stroke="currentColor" stroke-width="2"/>',
    "wf-levels": '<polygon points="3 12 12 16.5 21 12 12 16.5" opacity="0.25" fill="currentColor"/><polygon points="3 16.5 12 21 21 16.5 12 21" opacity="0.2" fill="currentColor"/><polygon points="12 3 21 7.5 12 12 3 7.5 12 3" fill="currentColor"/><polyline points="3 12 12 16.5 21 12" fill="none" stroke="currentColor" stroke-width="2"/><polyline points="3 16.5 12 21 21 16.5" fill="none" stroke="currentColor" stroke-width="2"/>',
    "wf-no-entry": '<circle cx="12" cy="12" r="9" opacity="0.25" fill="currentColor"/><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z" fill="currentColor"/><rect x="5.5" y="10.25" width="13" height="3.5" rx="1" fill="currentColor"/>',
    "wf-prohibited": '<circle cx="12" cy="12" r="8" opacity="0.25" fill="currentColor"/><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm-8 10a7.9 7.9 0 0 1 1.77-5.06l11.29 11.29A7.9 7.9 0 0 1 4 12zm14.23 5.06L6.94 5.77A7.9 7.9 0 0 1 18.23 12a7.9 7.9 0 0 1-2.23 5.06z" fill="currentColor"/>',
    "wf-staff-only": '<rect x="4" y="7" width="16" height="14" rx="3" opacity="0.25" fill="currentColor"/><circle cx="12" cy="12" r="2.5" fill="currentColor"/><path d="M8 18c0-2.2 1.8-4 4-4s4 1.8 4 4H8z" fill="currentColor"/><path d="M8 7V5a4 4 0 0 1 8 0v2h-2V5a2 2 0 0 0-4 0v2H8z" fill="currentColor"/>',

    # 3. Amenities
    "wf-toilets": '<rect x="2" y="2" width="20" height="20" rx="4" opacity="0.2" fill="currentColor"/><circle cx="7" cy="5" r="1.5" fill="currentColor"/><path d="M5 9h4v6H8v5H6v-5H5V9z" fill="currentColor"/><circle cx="17" cy="5" r="1.5" fill="currentColor"/><path d="M15 15l-1-6h6l-1 6h-4z" fill="currentColor"/><path d="M16 15v5h2v-5" fill="currentColor"/>',
    "wf-toilet-male": '<circle cx="12" cy="12" r="9.5" opacity="0.22" fill="currentColor"/><circle cx="12" cy="4" r="2" fill="currentColor"/><path d="M9 8h6a1 1 0 0 1 1 1v6h-2v6h-4v-6H8V9a1 1 0 0 1 1-1z" fill="currentColor"/>',
    "wf-toilet-female": '<circle cx="12" cy="12" r="9.5" opacity="0.22" fill="currentColor"/><circle cx="12" cy="4" r="2" fill="currentColor"/><path d="M9.5 8h5l2.5 8h-4v5h-2v-5H7l2.5-8z" fill="currentColor"/>',
    "wf-toilet-accessible": '<circle cx="12" cy="12" r="9.5" opacity="0.22" fill="currentColor"/><circle cx="10" cy="5" r="1.8" fill="currentColor"/><path d="M8 9h3l1.5 4h2.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M11 13a3.5 3.5 0 1 1-5-2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M17 9h4v11h-4" fill="none" stroke="currentColor" stroke-width="2"/><path d="M19 12v3" fill="none" stroke="currentColor" stroke-width="2"/>',
    "wf-baby-change": '<rect x="2" y="17" width="20" height="2.5" rx="1" opacity="0.25" fill="currentColor"/><circle cx="6.5" cy="8.5" r="2.5" fill="currentColor"/><path d="M9.5 12.5c1.5 0 3-1 4-2 1.5 1.5 3.5 1.5 5 1" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 4v4" stroke="currentColor" stroke-width="2"/><path d="m10 6 4 0" stroke="currentColor" stroke-width="2"/>',
    "wf-cafe": '<path d="M2 8h14v6a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z" opacity="0.25" fill="currentColor"/><path d="M16 8h1a4 4 0 0 1 0 8h-1" fill="none" stroke="currentColor" stroke-width="2"/><path d="M2 8h14v6a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z" fill="none" stroke="currentColor" stroke-width="2"/><line x1="6" y1="2" x2="6" y2="5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="10" y1="2" x2="10" y2="5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="14" y1="2" x2="14" y2="5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "wf-food": '<circle cx="12" cy="12" r="9.5" opacity="0.25" fill="currentColor"/><path d="M18 2v20" fill="none" stroke="currentColor" stroke-width="2"/><path d="M21 2c0 4-3 5-3 8" fill="none" stroke="currentColor" stroke-width="2"/><path d="M4 2v6c0 1.7 1.3 3 3 3v11" fill="none" stroke="currentColor" stroke-width="2"/><path d="M7 2v6" fill="none" stroke="currentColor" stroke-width="2"/><path d="M10 2v6c0 1.7-1.3 3-3 3" fill="none" stroke="currentColor" stroke-width="2"/>',
    "wf-retail": '<rect x="4" y="8" width="16" height="13" rx="2.5" opacity="0.25" fill="currentColor"/><path d="M8 8V6a4 4 0 0 1 8 0v2" fill="none" stroke="currentColor" stroke-width="2"/><rect x="4" y="8" width="16" height="13" rx="2.5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="9" cy="13" r="1.2" fill="currentColor"/><circle cx="15" cy="13" r="1.2" fill="currentColor"/>',
    "wf-atm": '<rect x="3" y="3" width="18" height="18" rx="3" opacity="0.25" fill="currentColor"/><rect x="3" y="3" width="18" height="18" rx="3" fill="none" stroke="currentColor" stroke-width="2"/><line x1="7" y1="8" x2="17" y2="8" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="7" y1="12" x2="12" y2="12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><rect x="14" y="11" width="3.5" height="4.5" rx="0.5" fill="currentColor"/>',
    "wf-payment": '<rect x="2" y="5" width="20" height="14" rx="3" opacity="0.25" fill="currentColor"/><rect x="2" y="5" width="20" height="14" rx="3" fill="none" stroke="currentColor" stroke-width="2"/><rect x="2" y="9" width="20" height="3" fill="currentColor"/><circle cx="7" cy="15" r="1.5" fill="currentColor"/><circle cx="11" cy="15" r="1.5" fill="currentColor"/>',
    "wf-pharmacy": '<circle cx="12" cy="12" r="9.5" opacity="0.25" fill="currentColor"/><path d="M10 3h4v6h6v4h-6v6h-4v-6H4V9h6z" fill="currentColor"/>',
    "wf-water": '<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z" opacity="0.25" fill="currentColor"/><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 18a4 4 0 0 0 4-4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "wf-wifi": '<path d="M5 12.55a11 11 0 0 1 14.08 0" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" opacity="0.3"/><path d="M1.42 9a16 16 0 0 1 21.16 0" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/><path d="M8.53 16.11a6 6 0 0 1 6.95 0" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/><circle cx="12" cy="19.5" r="1.5" fill="currentColor"/>',
    "wf-seating": '<rect x="3" y="11" width="18" height="5" rx="1.5" opacity="0.25" fill="currentColor"/><path d="M5 11V6a3 3 0 0 1 6 0v5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M13 11V6a3 3 0 0 1 6 0v5" fill="none" stroke="currentColor" stroke-width="2"/><rect x="3" y="11" width="18" height="5" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M5 16v5" stroke="currentColor" stroke-width="2"/><path d="M19 16v5" stroke="currentColor" stroke-width="2"/>',

    # 4. Transit
    "wf-parking": '<rect x="2" y="2" width="20" height="20" rx="4" opacity="0.25" fill="currentColor"/><path d="M8 19V5h5a4 4 0 0 1 0 8H8" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "wf-car": '<path d="M4 11l2-4.5A2 2 0 0 1 7.8 5h8.4a2 2 0 0 1 1.8 1.5L20 11v6H4v-6z" opacity="0.25" fill="currentColor"/><path d="M3 16h18v-4l-2-5H5l-2 5v4z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="7" cy="16.5" r="2" fill="currentColor"/><circle cx="17" cy="16.5" r="2" fill="currentColor"/>',
    "wf-bus": '<rect x="4" y="3" width="16" height="15" rx="3" opacity="0.25" fill="currentColor"/><rect x="4" y="3" width="16" height="15" rx="3" fill="none" stroke="currentColor" stroke-width="2"/><line x1="4" y1="10" x2="20" y2="10" stroke="currentColor" stroke-width="2"/><circle cx="8" cy="14" r="1.5" fill="currentColor"/><circle cx="16" cy="14" r="1.5" fill="currentColor"/><path d="M6 18v3" stroke="currentColor" stroke-width="2"/><path d="M18 18v3" stroke="currentColor" stroke-width="2"/>',
    "wf-ev": '<rect x="3" y="4" width="12" height="16" rx="2.5" opacity="0.25" fill="currentColor"/><rect x="3" y="4" width="12" height="16" rx="2.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="m8 9 2-3v4h2l-3 4v-3H7l2-2" fill="currentColor"/><path d="M15 9h3a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2h-1" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17" cy="17" r="1" fill="currentColor"/>',

    # 5. Services
    "wf-info": '<circle cx="12" cy="12" r="9.5" opacity="0.25" fill="currentColor"/><circle cx="12" cy="7.5" r="1.5" fill="currentColor"/><rect x="10.5" y="11" width="3" height="6" rx="0.75" fill="currentColor"/>',
    "wf-help": '<circle cx="12" cy="12" r="9.5" opacity="0.25" fill="currentColor"/><path d="M9.5 9a2.5 2.5 0 0 1 5 0c0 1.5-2 2.5-2 3.5" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/><circle cx="12" cy="16.5" r="1.5" fill="currentColor"/>',
    "wf-reception": '<rect x="3" y="14" width="18" height="6" rx="1.5" opacity="0.25" fill="currentColor"/><path d="M8 8a4 4 0 0 1 8 0H8z" fill="currentColor"/><line x1="12" y1="4" x2="12" y2="8" stroke="currentColor" stroke-width="2"/><rect x="3" y="14" width="18" height="6" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><line x1="2" y1="20" x2="22" y2="20" stroke="currentColor" stroke-width="2"/>',
    "wf-security": '<path d="M12 2s7 2.5 7 8c0 5.5-5 9.5-7 11-2-1.5-7-5.5-7-11 0-5.5 7-8 7-8z" opacity="0.25" fill="currentColor"/><path d="M12 2s7 2.5 7 8c0 5.5-5 9.5-7 11-2-1.5-7-5.5-7-11 0-5.5 7-8 7-8z" fill="none" stroke="currentColor" stroke-width="2"/><path d="m9 12 2 2 4-4" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>',
    "wf-phone": '<circle cx="12" cy="12" r="9.5" opacity="0.22" fill="currentColor"/><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z" fill="currentColor"/>',
    "wf-intercom": '<rect x="5" y="3" width="14" height="18" rx="3" opacity="0.25" fill="currentColor"/><rect x="5" y="3" width="14" height="18" rx="3" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="8" r="2.5" fill="currentColor"/><line x1="9" y1="13" x2="15" y2="13" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="17" r="1.5" fill="currentColor"/>',

    # 6. Healthcare
    "wf-hospital": '<rect x="4" y="3" width="16" height="18" rx="2" opacity="0.25" fill="currentColor"/><path d="M4 21V5a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v16H4z" fill="none" stroke="currentColor" stroke-width="2"/><path d="M10 7h4v3h3v4h-3v3h-4v-3H7v-4h3z" fill="currentColor"/><rect x="10" y="17" width="4" height="4" fill="currentColor"/>',
    "wf-first-aid": '<rect x="3" y="7" width="18" height="14" rx="3" opacity="0.25" fill="currentColor"/><rect x="3" y="7" width="18" height="14" rx="3" fill="none" stroke="currentColor" stroke-width="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M10.5 10h3v2h2v3h-2v2h-3v-2h-2v-3h2z" fill="currentColor"/>',
    "wf-consult": '<circle cx="12" cy="12" r="9.5" opacity="0.22" fill="currentColor"/><path d="M6 3v5a6 6 0 0 0 12 0V3" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="6" cy="3" r="1.2" fill="currentColor"/><circle cx="18" cy="3" r="1.2" fill="currentColor"/><path d="M12 14v4a3 3 0 0 0 6 0v-2" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="18" cy="16" r="2" fill="currentColor"/>',
    "wf-pathology": '<path d="M6.5 19.5h11l-3.5-7.5H10l-3.5 7.5z" opacity="0.3" fill="currentColor"/><path d="M9 3h6" stroke="currentColor" stroke-width="2"/><path d="M10 3v5l-4.5 9A2 2 0 0 0 7.3 20h9.4a2 2 0 0 0 1.8-3L14 8V3" fill="none" stroke="currentColor" stroke-width="2"/><line x1="7.5" y1="15" x2="16.5" y2="15" stroke="currentColor" stroke-width="2"/>',
    "wf-aed": '<path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" opacity="0.25" fill="currentColor"/><polygon points="12.5 5 9 12 13 12 11 18 16 11 12 11 12.5 5" fill="currentColor"/>',

    # 7. Campus
    "wf-student": '<polygon points="12 3 22 8.5 12 14 2 8.5" opacity="0.25" fill="currentColor"/><polygon points="12 3 22 8.5 12 14 2 8.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M6 10.7v5.3c0 2.2 2.7 4 6 4s6-1.8 6-4v-5.3" fill="none" stroke="currentColor" stroke-width="2"/><path d="M22 8.5v6" stroke="currentColor" stroke-width="2"/>',
    "wf-library": '<path d="M3 6.5A3.5 3.5 0 0 1 6.5 3H12v15H6.5A3.5 3.5 0 0 0 3 21.5V6.5z" opacity="0.25" fill="currentColor"/><path d="M21 6.5A3.5 3.5 0 0 0 17.5 3H12v15h5.5A3.5 3.5 0 0 1 21 21.5V6.5z" opacity="0.25" fill="currentColor"/><path d="M3 6.5A3.5 3.5 0 0 1 6.5 3H12v15H6.5A3.5 3.5 0 0 0 3 21.5V6.5z" fill="none" stroke="currentColor" stroke-width="2"/><path d="M21 6.5A3.5 3.5 0 0 0 17.5 3H12v15h5.5A3.5 3.5 0 0 1 21 21.5V6.5z" fill="none" stroke="currentColor" stroke-width="2"/>',
    "wf-lecture": '<rect x="3" y="3" width="18" height="12" rx="1.5" opacity="0.25" fill="currentColor"/><rect x="3" y="3" width="18" height="12" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="9" cy="8" r="1.5" fill="currentColor"/><line x1="13" y1="6" x2="18" y2="6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="13" y1="9" x2="16" y2="9" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path d="M12 15v6m-4 0h8" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',

    # 8. Safety
    "wf-emergency": '<polygon points="7.86 2 16.14 2 22 7.86 22 16.14 16.14 22 7.86 22 2 16.14 2 7.86" opacity="0.25" fill="currentColor"/><polygon points="7.86 2 16.14 2 22 7.86 22 16.14 16.14 22 7.86 22 2 16.14 2 7.86" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 7v6" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><circle cx="12" cy="17" r="1.5" fill="currentColor"/>',
    "wf-evacuate": '<rect x="13" y="3" width="8" height="18" rx="1.5" opacity="0.25" fill="currentColor"/><rect x="13" y="3" width="8" height="18" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="8" cy="6" r="1.8" fill="currentColor"/><path d="M6 16l2-3 2 1.5 3-4.5h2v1.5h-1.2l-2.5 3.5-2-1.5-2 4.5H6z" fill="currentColor"/>',
    "wf-assembly": '<circle cx="12" cy="12" r="9.5" opacity="0.22" fill="currentColor"/><path d="M4 12h5m-2.5-2.5L9 12l-2.5 2.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M20 12h-5m2.5-2.5L15 12l2.5 2.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M12 4v5m-2.5-2.5L12 9l2.5-2.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M12 20v-5m-2.5 2.5L12 15l2.5 2.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="12" cy="12" r="1.5" fill="currentColor"/>',
    "wf-fire": '<path d="M12 2C9 7 5 9 5 15a7 7 0 0 0 14 0c0-6-4-8-7-13z" opacity="0.25" fill="currentColor"/><path d="M12 2C9 7 5 9 5 15a7 7 0 0 0 14 0c0-6-4-8-7-13z" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 18a3 3 0 0 0 3-3c0-2-1.5-3-3-5-1.5 2-3 3-3 5a3 3 0 0 0 3 3z" fill="currentColor"/>',
    "wf-warning": '<polygon points="12 2 22 20 2 20" opacity="0.25" fill="currentColor"/><polygon points="12 2 22 20 2 20" fill="none" stroke="currentColor" stroke-width="2"/><line x1="12" y1="9" x2="12" y2="13" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><circle cx="12" cy="17" r="1.5" fill="currentColor"/>',
    "wf-construction": '<polygon points="7 19 17 19 14 5 10 5" opacity="0.25" fill="currentColor"/><polygon points="7 19 17 19 14 5 10 5" fill="none" stroke="currentColor" stroke-width="2"/><line x1="4" y1="21" x2="20" y2="21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="8.5" y1="14" x2="15.5" y2="14" stroke="currentColor" stroke-width="2"/><line x1="9.5" y1="9" x2="14.5" y2="9" stroke="currentColor" stroke-width="2"/>',

    # 9. UI
    "wf-home": '<path d="M4 10v10a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1V10l-8-6-8 6z" opacity="0.25" fill="currentColor"/><path d="M3 10l9-7 9 7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><rect x="9" y="13" width="6" height="8" rx="0.5" fill="currentColor"/>',
    "wf-search": '<circle cx="10.5" cy="10.5" r="7" opacity="0.25" fill="currentColor"/><circle cx="10.5" cy="10.5" r="7" fill="none" stroke="currentColor" stroke-width="2"/><line x1="15.5" y1="15.5" x2="21" y2="21" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    "wf-menu": '<rect x="3" y="3" width="18" height="18" rx="4" opacity="0.22" fill="currentColor"/><line x1="7" y1="8" x2="17" y2="8" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/><line x1="7" y1="12" x2="17" y2="12" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/><line x1="7" y1="16" x2="17" y2="16" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>',
    "wf-back": '<circle cx="12" cy="12" r="9.5" opacity="0.22" fill="currentColor"/><path d="M14 7l-5 5 5 5" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
    "wf-close": '<circle cx="12" cy="12" r="9.5" opacity="0.22" fill="currentColor"/><line x1="8" y1="8" x2="16" y2="16" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/><line x1="16" y1="8" x2="8" y2="16" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>',
    "wf-hours": '<circle cx="12" cy="12" r="9" opacity="0.25" fill="currentColor"/><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><polyline points="12 7 12 12 15.5 12" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>',
    "wf-timetable": '<rect x="3" y="4" width="18" height="17" rx="2.5" opacity="0.25" fill="currentColor"/><rect x="3" y="4" width="18" height="17" rx="2.5" fill="none" stroke="currentColor" stroke-width="2"/><line x1="3" y1="9" x2="21" y2="9" stroke="currentColor" stroke-width="2"/><line x1="8" y1="2" x2="8" y2="5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="16" y1="2" x2="16" y2="5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="8" cy="13" r="1.2" fill="currentColor"/><circle cx="12" cy="13" r="1.2" fill="currentColor"/><circle cx="16" cy="13" r="1.2" fill="currentColor"/><circle cx="8" cy="17" r="1.2" fill="currentColor"/><circle cx="12" cy="17" r="1.2" fill="currentColor"/>',
    "wf-events": '<rect x="3" y="4" width="18" height="17" rx="2.5" opacity="0.25" fill="currentColor"/><rect x="3" y="4" width="18" height="17" rx="2.5" fill="none" stroke="currentColor" stroke-width="2"/><line x1="3" y1="9" x2="21" y2="9" stroke="currentColor" stroke-width="2"/><line x1="8" y1="2" x2="8" y2="5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="16" y1="2" x2="16" y2="5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><polygon points="12 11 13.5 14 16.5 14.5 14.2 16.8 14.8 20 12 18.2 9.2 20 9.8 16.8 7.5 14.5 10.5 14" fill="currentColor"/>',
    "wf-news": '<rect x="3" y="4" width="18" height="16" rx="2" opacity="0.25" fill="currentColor"/><rect x="3" y="4" width="18" height="16" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><rect x="6" y="7" width="5" height="4" fill="currentColor"/><line x1="13" y1="7" x2="18" y2="7" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><line x1="13" y1="10" x2="18" y2="10" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><line x1="6" y1="14" x2="18" y2="14" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><line x1="6" y1="17" x2="15" y2="17" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>',
    "wf-announce": '<polygon points="4 9 12 5 12 17 4 13" opacity="0.25" fill="currentColor"/><polygon points="4 9 12 5 12 17 4 13" fill="none" stroke="currentColor" stroke-width="2"/><path d="M6 13v4a2 2 0 0 0 2 2h1v-6" fill="none" stroke="currentColor" stroke-width="2"/><path d="M16 8a4 4 0 0 1 0 8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path d="M19 6a8 8 0 0 1 0 12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',

    # 10. Media
    "wf-share": '<circle cx="12" cy="12" r="9.5" opacity="0.22" fill="currentColor"/><line x1="8.6" y1="13.5" x2="15.4" y2="17.5" stroke="currentColor" stroke-width="2"/><line x1="15.4" y1="6.5" x2="8.6" y2="10.5" stroke="currentColor" stroke-width="2"/><circle cx="18" cy="5" r="2.5" fill="currentColor"/><circle cx="6" cy="12" r="2.5" fill="currentColor"/><circle cx="18" cy="19" r="2.5" fill="currentColor"/>',
    "wf-chat": '<path d="M17 11h1a3 3 0 0 0 3-3V5a3 3 0 0 0-3-3H9a3 3 0 0 0-3 3v1" opacity="0.25" fill="currentColor"/><path d="M14 16H6l-3 4V7a3 3 0 0 1 3-3h8a3 3 0 0 1 3 3v6a3 3 0 0 1-3 3z" fill="currentColor"/><circle cx="6.5" cy="10" r="1" fill="#fff"/><circle cx="10" cy="10" r="1" fill="#fff"/><circle cx="13.5" cy="10" r="1" fill="#fff"/>',
    "wf-like": '<circle cx="12" cy="12" r="9.5" opacity="0.22" fill="currentColor"/><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3H14zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3" fill="currentColor"/>',
    "wf-camera": '<rect x="3" y="7" width="18" height="14" rx="3" opacity="0.25" fill="currentColor"/><rect x="3" y="7" width="18" height="14" rx="3" fill="none" stroke="currentColor" stroke-width="2"/><path d="M8 7l1.5-2.5h5L16 7" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="14" r="3.5" fill="currentColor"/><circle cx="17.5" cy="10" r="0.8" fill="currentColor"/>',
    "wf-video": '<rect x="2" y="6" width="14" height="12" rx="2.5" opacity="0.25" fill="currentColor"/><rect x="2" y="6" width="14" height="12" rx="2.5" fill="none" stroke="currentColor" stroke-width="2"/><polygon points="22 7 16 11 16 13 22 17 22 7" fill="currentColor"/><polygon points="7.5 9.5 11.5 12 7.5 14.5" fill="currentColor"/>',
    "wf-qr": '<rect x="2" y="2" width="20" height="20" rx="3" opacity="0.22" fill="currentColor"/><rect x="4" y="4" width="6" height="6" rx="1" fill="currentColor"/><rect x="14" y="4" width="6" height="6" rx="1" fill="currentColor"/><rect x="4" y="14" width="6" height="6" rx="1" fill="currentColor"/><rect x="5.5" y="5.5" width="3" height="3" fill="#fff"/><rect x="15.5" y="5.5" width="3" height="3" fill="#fff"/><rect x="5.5" y="15.5" width="3" height="3" fill="#fff"/><rect x="14" y="14" width="2.5" height="2.5" fill="currentColor"/><rect x="17.5" y="17.5" width="2.5" height="2.5" fill="currentColor"/><rect x="14" y="17.5" width="2.5" height="2.5" fill="currentColor"/>',
    "wf-email": '<rect x="2" y="4" width="20" height="16" rx="2.5" opacity="0.25" fill="currentColor"/><rect x="2" y="4" width="20" height="16" rx="2.5" fill="none" stroke="currentColor" stroke-width="2"/><polyline points="22,6 12,13 2,6" fill="none" stroke="currentColor" stroke-width="2"/>',
    "wf-web": '<circle cx="12" cy="12" r="9" opacity="0.25" fill="currentColor"/><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><line x1="3" y1="12" x2="21" y2="12" stroke="currentColor" stroke-width="2"/><ellipse cx="12" cy="12" rx="4.5" ry="9" fill="none" stroke="currentColor" stroke-width="2"/>'
}

print(f"Total Duotone icons defined: {len(DUOTONE_ICONS)}")

# 1. Generate individual SVG files in svg/duotone/<id>.svg
for icon_id, paths in DUOTONE_ICONS.items():
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="wf-icon wf-icon-duotone {icon_id}">
  {paths}
</svg>
'''
    file_path = os.path.join(SVG_DUOTONE_DIR, f"{icon_id}.svg")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

print(f"Wrote 80 individual SVGs to {SVG_DUOTONE_DIR}")

# 2. Generate SVG Sprite dist/wayfinding-icons-duotone.svg
sprite_symbols = []
for icon_id, paths in DUOTONE_ICONS.items():
    sym = f'  <symbol id="{icon_id}" viewBox="0 0 24 24">\n    {paths}\n  </symbol>'
    sprite_symbols.append(sym)

sprite_content = f'''<svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
{os.linesep.join(sprite_symbols)}
</svg>
'''
sprite_path = os.path.join(DIST_DIR, "wayfinding-icons-duotone.svg")
with open(sprite_path, "w", encoding="utf-8") as f:
    f.write(sprite_content)
print(f"Wrote sprite to {sprite_path}")

# 3. Update dist/wayfinding-icons.json with paths_duotone
json_path = os.path.join(DIST_DIR, "wayfinding-icons.json")
with open(json_path, "r", encoding="utf-8") as f:
    metadata = json.load(f)

for item in metadata:
    item_id = item["id"]
    if item_id in DUOTONE_ICONS:
        item["paths_duotone"] = DUOTONE_ICONS[item_id]

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2, ensure_ascii=False)
print("Updated dist/wayfinding-icons.json with paths_duotone")

# 4. Update dist/wayfinding-icons.js with WAYFINDING_DUOTONE export and web component support
js_path = os.path.join(DIST_DIR, "wayfinding-icons.js")
with open(js_path, "r", encoding="utf-8") as f:
    js_text = f.read()

# Build duotone dict JS code
duotone_js_entries = []
for k, v in DUOTONE_ICONS.items():
    escaped_v = v.replace('"', '\\"')
    duotone_js_entries.append(f'  "{k}": "{escaped_v}"')
duotone_js_dict = "export const WAYFINDING_DUOTONE = {\n" + ",\n".join(duotone_js_entries) + "\n};\n\n"

# Insert WAYFINDING_DUOTONE before WAYFINDING_SOLID or near exports
if "export const WAYFINDING_DUOTONE" not in js_text:
    target_needle = "export const WAYFINDING_SOLID = {"
    idx = js_text.find(target_needle)
    if idx != -1:
        js_text = js_text[:idx] + duotone_js_dict + js_text[idx:]
    else:
        js_text = duotone_js_dict + js_text

# Update getWayfindingIcon in JS
new_get_icon = """export function getWayfindingIcon(iconId, options = {}) {
  const {
    set = 'line',
    size = 24,
    strokeWidth = 2,
    className = ''
  } = options;

  let paths = '';
  if (set === 'solid') {
    paths = WAYFINDING_SOLID[iconId] || '';
    if (!paths) return '';
    return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" fill="currentColor" class="wf-icon wf-icon-solid ${iconId} ${className}">${paths}</svg>`;
  } else if (set === 'duotone') {
    paths = WAYFINDING_DUOTONE[iconId] || '';
    if (!paths) return '';
    return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" class="wf-icon wf-icon-duotone ${iconId} ${className}">${paths}</svg>`;
  }
  paths = WAYFINDING_LINE[iconId] || '';
  if (!paths) return '';
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${strokeWidth}" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-line ${iconId} ${className}">${paths}</svg>`;
}"""

# Update custom component render in JS
new_render = """  render() {
    const name = this.getAttribute('name') || 'wf-pin';
    const set = this.getAttribute('set') || 'line';
    const size = this.getAttribute('size') || '24';
    const strokeWidth = this.getAttribute('stroke-width') || '2';
    const color = this.getAttribute('color');

    if (color) {
      this.style.color = color;
    }

    if (set === 'solid') {
      const paths = WAYFINDING_SOLID[name] || '';
      this.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" fill="currentColor" class="wf-icon wf-icon-solid ${name}">${paths}</svg>`;
    } else if (set === 'duotone') {
      const paths = WAYFINDING_DUOTONE[name] || '';
      this.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" class="wf-icon wf-icon-duotone ${name}">${paths}</svg>`;
    } else {
      const paths = WAYFINDING_LINE[name] || '';
      this.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${strokeWidth}" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-line ${name}">${paths}</svg>`;
    }
  }"""

# Replace in js_text
import re
js_text = re.sub(r'export function getWayfindingIcon\(iconId, options = \{\}\) \{[\s\S]*?^\}', new_get_icon, js_text, flags=re.MULTILINE)
js_text = re.sub(r'  render\(\) \{[\s\S]*?^\  \}', new_render, js_text, flags=re.MULTILINE)

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_text)

print("Updated dist/wayfinding-icons.js with WAYFINDING_DUOTONE & Web Component support")
