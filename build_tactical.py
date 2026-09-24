import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SVG_TACTICAL_DIR = os.path.join(BASE_DIR, "svg", "tactical")
DIST_DIR = os.path.join(BASE_DIR, "dist")
os.makedirs(SVG_TACTICAL_DIR, exist_ok=True)
os.makedirs(DIST_DIR, exist_ok=True)

# Tactical Cyber / Chiseled Amber & Slate SVG Icons
# Inspired by the reference design:
# - Bold dark slate/charcoal outlines & structural bevels (#0f172a / #1e293b)
# - Golden amber highlights and focal planes (var(--wf-accent, #f59e0b) / #fbbf24)
# - Chiseled low-poly and shaded slate facets (#334155 / #475569)
# - Crisp white / light details (#ffffff)

A = 'var(--wf-accent, #f59e0b)'
AL = 'var(--wf-accent-light, #fbbf24)'
AD = 'var(--wf-accent-dark, #d97706)'
SD = '#1e293b'
SM = '#334155'
SL = '#475569'
BD = '#0f172a'
W = '#ffffff'

TACTICAL_ICONS = {
    # 1. Navigation
    "wf-arrow-up": f'''<polygon points="12 2 20 10 15 10 15 21 9 21 9 10 4 10" fill="{A}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="12 2 12 21 9 21 9 10 4 10" fill="{AL}" opacity="0.35"/>
<polygon points="15 10 20 10 15 21" fill="{SM}" opacity="0.4"/>
<line x1="12" y1="2" x2="12" y2="21" stroke="{BD}" stroke-width="1.2"/>''',

    "wf-arrow-right": f'''<polygon points="22 12 14 4 14 9 3 9 3 15 14 15 14 20" fill="{A}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="22 12 3 12 3 9 14 9 14 4" fill="{AL}" opacity="0.4"/>
<polygon points="14 15 22 12 14 20" fill="{SM}" opacity="0.5"/>
<line x1="3" y1="12" x2="22" y2="12" stroke="{BD}" stroke-width="1.2"/>''',

    "wf-arrow-down": f'''<polygon points="12 22 4 14 9 14 9 3 15 3 15 14 20 14" fill="{A}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="12 22 12 3 9 3 9 14 4 14" fill="{AL}" opacity="0.4"/>
<polygon points="15 14 12 22 15 3" fill="{SM}" opacity="0.5"/>
<line x1="12" y1="3" x2="12" y2="22" stroke="{BD}" stroke-width="1.2"/>''',

    "wf-arrow-left": f'''<path d="M18 5A8 8 0 0 0 6 12l-3-3v8h8l-3-3a6 6 0 0 1 10-2z" fill="{A}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="6 12 3 9 3 17 11 17 8 14" fill="{AL}"/>
<polygon points="19 2 20.5 5 23.5 6.5 20.5 8 19 11 17.5 8 14.5 6.5 17.5 5" fill="{AL}" stroke="{BD}" stroke-width="0.8"/>''',

    "wf-arrow-up-right": f'''<polygon points="6 20 15 11 15 17 21 17 21 3 7 3 7 9 13 9 4 18" fill="{A}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="7 3 21 3 15 9 7 9" fill="{AL}" opacity="0.45"/>
<polygon points="15 11 21 17 15 17" fill="{SM}" opacity="0.5"/>
<line x1="6" y1="20" x2="19" y2="5" stroke="{BD}" stroke-width="1.2"/>''',

    "wf-arrow-up-left": f'''<polygon points="18 20 9 11 9 17 3 17 3 3 17 3 17 9 11 9 20 18" fill="{A}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="17 3 3 3 9 9 17 9" fill="{AL}" opacity="0.45"/>
<polygon points="9 11 3 17 9 17" fill="{SM}" opacity="0.5"/>
<line x1="18" y1="20" x2="5" y2="5" stroke="{BD}" stroke-width="1.2"/>''',

    "wf-u-turn": f'''<path d="M8 18l-4-4h3A7 7 0 0 1 14 7a7 7 0 0 1 7 7v7h-4v-7a3 3 0 0 0-3-3 3 3 0 0 0-3 3h3z" fill="{A}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<path d="M8 18l-4-4h3a7 7 0 0 1 7-7v4a3 3 0 0 0-3 3h3z" fill="{AL}" opacity="0.4"/>
<rect x="17" y="14" width="4" height="7" fill="{SM}"/>''',

    "wf-signpost": f'''<rect x="11" y="2" width="2" height="20" fill="{SM}" stroke="{BD}" stroke-width="1.5"/>
<polygon points="4 5 11 5 13 7.5 11 10 4 10" fill="{SL}" stroke="{BD}" stroke-width="1.5" stroke-linejoin="round"/>
<polygon points="13 11 20 11 22 13.5 20 16 13 16" fill="{A}" stroke="{BD}" stroke-width="1.5" stroke-linejoin="round"/>
<polygon points="13 11 17 11 18 13.5 16 16 13 16" fill="{AL}" opacity="0.4"/>''',

    "wf-pin": f'''<polygon points="12 2 19 6 19 14 12 22 5 14 5 6" fill="{SD}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="12 2 19 6 12 10 5 6" fill="{SL}"/>
<polygon points="12 10 19 6 19 14 12 22" fill="{SM}"/>
<circle cx="12" cy="11" r="3.5" fill="{A}" stroke="{BD}" stroke-width="1"/>
<text x="12" y="12.5" font-size="3.5" font-weight="900" text-anchor="middle" fill="{BD}" font-family="sans-serif">YOU</text>''',

    "wf-facing": f'''<circle cx="12" cy="12" r="9.5" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<circle cx="12" cy="12" r="7" fill="{SM}"/>
<polygon points="12 4 15.5 12 12 10 8.5 12" fill="{A}" stroke="{BD}" stroke-width="1.2" stroke-linejoin="round"/>
<polygon points="12 4 12 10 8.5 12" fill="{AL}"/>
<circle cx="12" cy="16.5" r="1.5" fill="{A}"/>''',

    "wf-map": f'''<polygon points="3 7 9 3 9 17 3 21" fill="{SL}" stroke="{BD}" stroke-width="1.5" stroke-linejoin="round"/>
<polygon points="9 3 15 7 15 21 9 17" fill="{A}" stroke="{BD}" stroke-width="1.5" stroke-linejoin="round"/>
<polygon points="15 7 21 3 21 17 15 21" fill="{SM}" stroke="{BD}" stroke-width="1.5" stroke-linejoin="round"/>
<polygon points="9 3 15 7 12 12" fill="{AL}" opacity="0.5"/>
<polygon points="12 12 15 21 9 17" fill="{AD}" opacity="0.6"/>
<polygon points="3 7 9 10 3 14" fill="{A}" opacity="0.85"/>
<polygon points="15 7 21 10 18 14" fill="{A}" opacity="0.85"/>''',

    "wf-touch": f'''<polygon points="4 16 12 11 20 16 12 21" fill="{SL}" stroke="{BD}" stroke-width="1.5" stroke-linejoin="round"/>
<polygon points="4 16 12 11 12 21" fill="{A}" opacity="0.85"/>
<circle cx="12" cy="6" r="3.5" fill="{A}" stroke="{BD}" stroke-width="1.5"/>
<circle cx="12" cy="6" r="1.5" fill="{W}"/>
<path d="M12 9v5l2 2" fill="none" stroke="{BD}" stroke-width="2" stroke-linecap="round"/>''',

    # 2. Building
    "wf-entrance": f'''<polygon points="8 3 18 3 21 6 21 21 8 21" fill="{SD}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<rect x="11" y="6" width="7" height="15" fill="{SM}" stroke="{BD}" stroke-width="1.2"/>
<polygon points="3 13 8 9 8 12 13 12 13 14 8 14 8 17" fill="{A}" stroke="{BD}" stroke-width="1.5" stroke-linejoin="round"/>
<polygon points="3 13 8 9 8 13" fill="{AL}"/>''',

    "wf-exit": f'''<polygon points="12 2 19 6 19 18 12 22 5 18 5 6" fill="{SD}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="5 6 12 2 12 22 5 18" fill="{SM}"/>
<polygon points="6.5 7.5 11 4 11 20 6.5 16.5" fill="{A}"/>
<polygon points="17.5 7.5 13 4 13 20 17.5 16.5" fill="{A}"/>
<polygon points="6.5 7.5 11 4 11 12 6.5 12" fill="{AL}"/>
<polygon points="13 4 17.5 7.5 17.5 12 13 12" fill="{AL}"/>''',

    "wf-lift": f'''<rect x="3" y="3" width="18" height="18" rx="2" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<rect x="5.5" y="5.5" width="13" height="13" fill="{A}" stroke="{BD}" stroke-width="1.2"/>
<circle cx="9" cy="9.5" r="1.3" fill="{BD}"/>
<path d="M7.5 16v-3a1.5 1.5 0 0 1 3 0v3z" fill="{BD}"/>
<circle cx="15" cy="9.5" r="1.3" fill="{BD}"/>
<path d="M13.5 16v-3a1.5 1.5 0 0 1 3 0v3z" fill="{BD}"/>
<polygon points="12 2.5 10 4.5 14 4.5" fill="{A}" stroke="{BD}" stroke-width="0.8"/>
<polygon points="12 21.5 10 19.5 14 19.5" fill="{A}" stroke="{BD}" stroke-width="0.8"/>''',

    "wf-stairs": f'''<polygon points="3 20 8 20 8 16 13 16 13 12 18 12 18 8 22 8 22 20 3 20" fill="{SM}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="8 20 8 16 13 16 13 12 18 12 18 8 22 8 22 20" fill="{SD}"/>
<polyline points="3 20 8 20 8 16 13 16 13 12 18 12 18 8 22 8" fill="none" stroke="{A}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="5" y1="13" x2="19" y2="4" stroke="{AL}" stroke-width="2" stroke-linecap="round"/>''',

    "wf-escalator-up": f'''<path d="M3 6h4.5l8 11H21" fill="none" stroke="{SD}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M3 6h4.5l8 11H21" fill="none" stroke="{A}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="14 7 19 7 19 12" fill="{A}" stroke="{BD}" stroke-width="1"/>
<circle cx="9" cy="4" r="1.5" fill="{BD}"/>
<path d="M7 10l3-3 2 1" fill="none" stroke="{BD}" stroke-width="2" stroke-linecap="round"/>''',

    "wf-escalator-down": f'''<path d="M3 18h4.5l8-11H21" fill="none" stroke="{SD}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M3 18h4.5l8-11H21" fill="none" stroke="{A}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="10 17 5 17 5 12" fill="{A}" stroke="{BD}" stroke-width="1"/>
<circle cx="15" cy="4" r="1.5" fill="{BD}"/>
<path d="M17 10l-3-3-2 1" fill="none" stroke="{BD}" stroke-width="2" stroke-linecap="round"/>''',

    "wf-ramp": f'''<polygon points="2 20 22 20 22 9 2 20" fill="{SM}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="2 20 22 9 22 20" fill="{SD}"/>
<line x1="2" y1="20" x2="22" y2="9" stroke="{A}" stroke-width="3" stroke-linecap="round"/>
<circle cx="15" cy="6" r="1.6" fill="{A}"/>
<path d="M11 14a2.5 2.5 0 0 1 3-2l2-1.5" fill="none" stroke="{BD}" stroke-width="1.8" stroke-linecap="round"/>''',

    "wf-accessible": f'''<circle cx="12" cy="12" r="9.5" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<circle cx="12" cy="5" r="1.8" fill="{A}"/>
<path d="M10 9h3.5l1.5 5h3" fill="none" stroke="{A}" stroke-width="2.2" stroke-linecap="round"/>
<path d="M13 14a4 4 0 1 1-5-2.5" fill="none" stroke="{W}" stroke-width="2.2" stroke-linecap="round"/>
<polyline points="8 12 11 12 12 15" stroke="{A}" stroke-width="2" stroke-linecap="round"/>''',

    "wf-levels": f'''<polygon points="12 2 21 6.5 12 11 3 6.5" fill="{A}" stroke="{BD}" stroke-width="1.5" stroke-linejoin="round"/>
<polygon points="12 2 12 11 3 6.5" fill="{AL}" opacity="0.4"/>
<polygon points="12 7.5 21 12 12 16.5 3 12" fill="{SM}" stroke="{BD}" stroke-width="1.5" stroke-linejoin="round"/>
<polygon points="12 7.5 12 16.5 3 12" fill="{SL}" opacity="0.4"/>
<polygon points="12 13 21 17.5 12 22 3 17.5" fill="{SD}" stroke="{BD}" stroke-width="1.5" stroke-linejoin="round"/>''',

    "wf-no-entry": f'''<circle cx="12" cy="12" r="9.5" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<circle cx="12" cy="12" r="7.5" fill="{SM}"/>
<rect x="4.5" y="10" width="15" height="4" rx="1" fill="{A}" stroke="{BD}" stroke-width="1.2"/>
<rect x="4.5" y="10" width="15" height="2" fill="{AL}"/>''',

    "wf-prohibited": f'''<circle cx="12" cy="12" r="9.5" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<circle cx="12" cy="12" r="7" fill="{SM}"/>
<line x1="5.5" y1="5.5" x2="18.5" y2="18.5" stroke="{A}" stroke-width="3.5" stroke-linecap="round"/>
<line x1="5.5" y1="5.5" x2="18.5" y2="18.5" stroke="{AL}" stroke-width="1.5" stroke-linecap="round"/>''',

    "wf-staff-only": f'''<polygon points="12 2 19 5 17 14 12 20 7 14 5 5" fill="{SD}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="12 4 17 7 15 13 12 17 9 13 7 7" fill="{SM}"/>
<rect x="9.5" y="7" width="5" height="2.5" rx="0.5" fill="{A}"/>
<polygon points="12 11 14 13 12 16 10 13" fill="{A}"/>''',

    # 3. Amenities
    "wf-toilets": f'''<rect x="2" y="2" width="20" height="20" rx="3" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<line x1="12" y1="3" x2="12" y2="21" stroke="{A}" stroke-width="1.5"/>
<circle cx="7" cy="6" r="1.5" fill="{A}"/>
<path d="M5 10h4v6H8v4H6v-4H5z" fill="{W}"/>
<circle cx="17" cy="6" r="1.5" fill="{A}"/>
<polygon points="15 10 19 10 20 16 14 16" fill="{W}"/>
<rect x="15" y="16" width="1.5" height="4" fill="{W}"/>
<rect x="17.5" y="16" width="1.5" height="4" fill="{W}"/>''',

    "wf-toilet-male": f'''<circle cx="12" cy="12" r="9.5" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<circle cx="12" cy="5" r="1.8" fill="{A}"/>
<polygon points="10 8.5 14 8.5 15 15 13 15 13 20 11 20 11 15 9 15" fill="{W}" stroke="{BD}" stroke-width="1"/>
<polygon points="11.5 8.5 12.5 8.5 13 12 11 12" fill="{A}"/>''',

    "wf-toilet-female": f'''<circle cx="12" cy="12" r="9.5" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<circle cx="12" cy="5" r="1.8" fill="{A}"/>
<polygon points="10 8.5 14 8.5 16 16 8 16" fill="{W}" stroke="{BD}" stroke-width="1"/>
<rect x="9.5" y="16" width="2" height="4" fill="{W}"/>
<rect x="12.5" y="16" width="2" height="4" fill="{W}"/>
<polygon points="12 8.5 14 8.5 15 12 12 12" fill="{A}"/>''',

    "wf-toilet-accessible": f'''<polygon points="12 2 20 6 20 18 12 22 4 18 4 6" fill="{SD}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<circle cx="10" cy="6" r="1.6" fill="{A}"/>
<path d="M8 10h3l1.5 4h2.5" fill="none" stroke="{W}" stroke-width="1.8" stroke-linecap="round"/>
<path d="M11 14a3.5 3.5 0 1 1-5-2" fill="none" stroke="{A}" stroke-width="2" stroke-linecap="round"/>
<rect x="16" y="8" width="3" height="9" rx="0.5" fill="{SM}" stroke="{A}" stroke-width="1"/>''',

    "wf-baby-change": f'''<polygon points="3 17 21 17 19 20 5 20" fill="{SM}" stroke="{BD}" stroke-width="1.5" stroke-linejoin="round"/>
<line x1="2" y1="17" x2="22" y2="17" stroke="{A}" stroke-width="2.5" stroke-linecap="round"/>
<circle cx="7" cy="9" r="2.2" fill="{A}"/>
<path d="M10 13c2 0 4-2 6-2s4 2 5 2" fill="none" stroke="{W}" stroke-width="2" stroke-linecap="round"/>
<circle cx="15" cy="9" r="1.5" fill="{W}"/>''',

    "wf-cafe": f'''<path d="M5 8c-2 2-2 5 0 7s5 2 7 0l5-5c2-2 2-5 0-7s-5-2-7 0z" fill="{A}" stroke="{BD}" stroke-width="1.8"/>
<path d="M19 8c2 2 2 5 0 7s-5 2-7 0l-5-5c-2-2-2-5 0-7s5-2 7 0z" fill="{SM}" opacity="0.7" stroke="{BD}" stroke-width="1.8"/>
<line x1="8" y1="2" x2="8" y2="4" stroke="{A}" stroke-width="1.5" stroke-linecap="round"/>
<line x1="12" y1="1" x2="12" y2="3" stroke="{A}" stroke-width="1.5" stroke-linecap="round"/>
<line x1="16" y1="2" x2="16" y2="4" stroke="{A}" stroke-width="1.5" stroke-linecap="round"/>''',

    "wf-food": f'''<polygon points="18 2 20 2 19 14 19 22 17 22 17 14" fill="{W}" stroke="{BD}" stroke-width="1.5" stroke-linejoin="round"/>
<path d="M21 2c0 4-3 5-3 8" fill="none" stroke="{A}" stroke-width="1.8" stroke-linecap="round"/>
<path d="M4 2v6c0 2 1.5 3 3.5 3v11h2V11c2 0 3.5-1 3.5-3V2" fill="none" stroke="{W}" stroke-width="1.8" stroke-linecap="round"/>
<line x1="7.5" y1="2" x2="7.5" y2="7" stroke="{A}" stroke-width="1.5"/>''',

    "wf-retail": f'''<polygon points="5 8 19 8 18 21 6 21" fill="{SM}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="5 8 19 8 13 21 6 21" fill="{A}"/>
<polygon points="5 8 12 8 8 21 6 21" fill="{AL}"/>
<path d="M9 8V5a3 3 0 0 1 6 0v3" fill="none" stroke="{BD}" stroke-width="2" stroke-linecap="round"/>''',

    "wf-atm": f'''<rect x="4" y="3" width="16" height="18" rx="2" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<rect x="7" y="5.5" width="10" height="6.5" rx="1" fill="{SM}" stroke="{BD}" stroke-width="1"/>
<rect x="8.5" y="7" width="7" height="3.5" rx="0.5" fill="{A}"/>
<line x1="7" y1="15" x2="17" y2="15" stroke="{A}" stroke-width="2" stroke-linecap="round"/>
<rect x="13.5" y="17" width="4" height="2" fill="{W}"/>''',

    "wf-payment": f'''<polygon points="3 14 7 8 17 8 21 14" fill="{SM}" stroke="{BD}" stroke-width="1.5" stroke-linejoin="round"/>
<path d="M3 14c0 4.5 4 7 9 7s9-2.5 9-7z" fill="{SD}" stroke="{BD}" stroke-width="1.5"/>
<line x1="7" y1="6" x2="15" y2="13" stroke="{A}" stroke-width="2.5" stroke-linecap="round"/>
<circle cx="16" cy="5" r="2.5" fill="{A}" stroke="{BD}" stroke-width="1"/>''',

    "wf-pharmacy": f'''<path d="M4 11c0 5 3.5 8 8 8s8-3 8-8z" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<line x1="3" y1="11" x2="21" y2="11" stroke="{A}" stroke-width="2" stroke-linecap="round"/>
<line x1="16" y1="4" x2="10" y2="13" stroke="{A}" stroke-width="3" stroke-linecap="round"/>
<polygon points="12 14 13 14 13 15 14 15 14 16 13 16 13 17 12 17 12 16 11 16 11 15 12 15" fill="{A}" transform="scale(1.2) translate(-2,-2)"/>''',

    "wf-water": f'''<polygon points="12 2 17 8 17 15 12 21 7 15 7 8" fill="{SD}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="12 2 17 8 12 15 7 8" fill="{A}"/>
<polygon points="12 2 12 15 7 8" fill="{AL}"/>
<polyline points="8 12 11 15 16 9" stroke="{W}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>''',

    "wf-wifi": f'''<path d="M4 8a13 13 0 0 1 16 0" fill="none" stroke="{SD}" stroke-width="3" stroke-linecap="round"/>
<path d="M4 8a13 13 0 0 1 16 0" fill="none" stroke="{A}" stroke-width="1.5" stroke-linecap="round"/>
<path d="M7 12a8 8 0 0 1 10 0" fill="none" stroke="{SD}" stroke-width="3" stroke-linecap="round"/>
<path d="M7 12a8 8 0 0 1 10 0" fill="none" stroke="{A}" stroke-width="1.5" stroke-linecap="round"/>
<circle cx="12" cy="18" r="2.2" fill="{A}" stroke="{BD}" stroke-width="1.2"/>''',

    "wf-seating": f'''<polygon points="5 5 19 5 17 12 7 12" fill="{SM}" stroke="{BD}" stroke-width="1.5" stroke-linejoin="round"/>
<rect x="4" y="12" width="16" height="4.5" rx="1.5" fill="{A}" stroke="{BD}" stroke-width="1.5"/>
<line x1="6" y1="16.5" x2="4" y2="21" stroke="{SD}" stroke-width="2" stroke-linecap="round"/>
<line x1="18" y1="16.5" x2="20" y2="21" stroke="{SD}" stroke-width="2" stroke-linecap="round"/>''',

    # 4. Transit
    "wf-parking": f'''<polygon points="4 6 20 6 22 13 2 13" fill="{SM}" stroke="{BD}" stroke-width="1.5" stroke-linejoin="round"/>
<polygon points="2 13 22 13 20 18 4 18" fill="{SD}" stroke="{BD}" stroke-width="1.5" stroke-linejoin="round"/>
<circle cx="6.5" cy="18" r="2.2" fill="{A}" stroke="{BD}" stroke-width="1.2"/>
<circle cx="17.5" cy="18" r="2.2" fill="{A}" stroke="{BD}" stroke-width="1.2"/>
<polygon points="5 13 7 8 17 8 19 13" fill="{A}" opacity="0.85"/>''',

    "wf-car": f'''<polygon points="5 11 8 5 16 5 19 11" fill="{A}" stroke="{BD}" stroke-width="1.5" stroke-linejoin="round"/>
<rect x="3" y="11" width="18" height="6" rx="2" fill="{SD}" stroke="{BD}" stroke-width="1.5"/>
<circle cx="7" cy="17" r="2" fill="{A}" stroke="{BD}" stroke-width="1"/>
<circle cx="17" cy="17" r="2" fill="{A}" stroke="{BD}" stroke-width="1"/>
<line x1="3" y1="13" x2="6" y2="13" stroke="{AL}" stroke-width="1.5"/>
<line x1="18" y1="13" x2="21" y2="13" stroke="{AL}" stroke-width="1.5"/>''',

    "wf-bus": f'''<rect x="5" y="3" width="14" height="16" rx="3" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<rect x="7" y="5.5" width="10" height="2.5" rx="0.5" fill="{A}"/>
<rect x="7" y="9.5" width="10" height="4.5" rx="0.5" fill="{SM}"/>
<circle cx="8" cy="16" r="1.3" fill="{A}"/>
<circle cx="16" cy="16" r="1.3" fill="{A}"/>
<line x1="7" y1="19" x2="7" y2="21.5" stroke="{BD}" stroke-width="2"/>
<line x1="17" y1="19" x2="17" y2="21.5" stroke="{BD}" stroke-width="2"/>''',

    "wf-ev": f'''<polygon points="12 2 19 6 19 18 12 22 5 18 5 6" fill="{SD}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="12 2 19 6 12 11 5 6" fill="{SL}"/>
<polygon points="12 11 19 6 19 18 12 22" fill="{SM}"/>
<polygon points="12 5 8 12 12 12 11 18 16 11 12 11" fill="{A}" stroke="{BD}" stroke-width="0.8"/>''',

    # 5. Services
    "wf-info": f'''<circle cx="12" cy="12" r="9.5" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<circle cx="12" cy="12" r="7" fill="{SM}"/>
<path d="M12 5 A7 7 0 0 1 19 12 L12 12 Z" fill="{A}"/>
<circle cx="12" cy="12" r="3.5" fill="{SD}" stroke="{BD}" stroke-width="1.2"/>
<circle cx="12" cy="12" r="1.5" fill="{A}"/>''',

    "wf-help": f'''<polygon points="12 2 20 6.5 20 17.5 12 22 4 17.5 4 6.5" fill="{SD}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="12 4.5 18 8 18 16 12 19.5 6 16 6 8" fill="{SM}"/>
<path d="M10 8.5a2.5 2.5 0 0 1 4 1.5c0 1.5-2 2-2 3.5" fill="none" stroke="{A}" stroke-width="2.5" stroke-linecap="round"/>
<circle cx="12" cy="16.5" r="1.3" fill="{A}"/>''',

    "wf-reception": f'''<polygon points="4 14 20 14 18 19 6 19" fill="{SD}" stroke="{BD}" stroke-width="1.5" stroke-linejoin="round"/>
<rect x="3" y="14" width="18" height="2.5" rx="0.5" fill="{A}"/>
<circle cx="12" cy="6" r="2.5" fill="{A}" stroke="{BD}" stroke-width="1.2"/>
<path d="M9 14a3 3 0 0 1 6 0" fill="{SM}"/>''',

    "wf-security": f'''<rect x="5" y="5" width="14" height="9" rx="1.5" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<rect x="7" y="7" width="10" height="5" fill="{A}"/>
<polygon points="10 14 14 14 16 20 8 20" fill="{SM}" stroke="{BD}" stroke-width="1.5" stroke-linejoin="round"/>
<line x1="3" y1="20" x2="21" y2="20" stroke="{A}" stroke-width="2"/>''',

    "wf-phone": f'''<polygon points="12 2 20 6 18 16 12 21 6 16 4 6" fill="{SD}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="12 4 18 7.5 16.5 15 12 19 7.5 15 6 7.5" fill="{SM}"/>
<path d="M9 8h2l1 2.5-1.5 1.5a7 7 0 0 0 3 3l1.5-1.5 2.5 1v2a2 2 0 0 1-2 2A10 10 0 0 1 7 9a2 2 0 0 1 2-1" fill="{A}"/>''',

    "wf-intercom": f'''<circle cx="12" cy="12" r="9.5" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<circle cx="12" cy="12" r="7.5" fill="{SM}"/>
<circle cx="12" cy="12" r="6" fill="{SD}"/>
<text x="12" y="16.5" font-size="12" font-weight="900" text-anchor="middle" fill="{A}" font-family="sans-serif">H</text>''',

    # 6. Healthcare
    "wf-hospital": f'''<circle cx="12" cy="12" r="9.5" fill="{A}" stroke="{BD}" stroke-width="1.8"/>
<circle cx="12" cy="12" r="7.5" fill="{SD}"/>
<text x="12" y="16.5" font-size="12" font-weight="900" text-anchor="middle" fill="{A}" font-family="sans-serif">H</text>''',

    "wf-first-aid": f'''<rect x="3" y="6" width="18" height="15" rx="3" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<path d="M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2" fill="none" stroke="{A}" stroke-width="2"/>
<polygon points="10 11 10 9 14 9 14 11 16 11 16 15 14 15 14 17 10 17 10 15 8 15 8 11" fill="{A}" stroke="{BD}" stroke-width="1"/>''',

    "wf-consult": f'''<rect x="3" y="6" width="18" height="15" rx="3" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<polygon points="10 11 10 9 14 9 14 11 16 11 16 15 14 15 14 17 10 17 10 15 8 15 8 11" fill="{A}"/>
<line x1="8" y1="6" x2="16" y2="6" stroke="{A}" stroke-width="2.5" stroke-linecap="round"/>''',

    "wf-pathology": f'''<rect x="3" y="6" width="18" height="15" rx="3" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<polygon points="10 11 10 9 14 9 14 11 16 11 16 15 14 15 14 17 10 17 10 15 8 15 8 11" fill="{A}"/>
<circle cx="17.5" cy="8.5" r="1.5" fill="{W}"/>''',

    "wf-aed": f'''<polygon points="12 21 3 12 6 5 12 9 18 5 21 12" fill="{SD}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="12 19 5 12 7 7 12 10 17 7 19 12" fill="{SM}"/>
<polygon points="12 4 9 11 13 11 11 17 16 10 12 10" fill="{A}" stroke="{BD}" stroke-width="1"/>''',

    # 7. Campus
    "wf-student": f'''<polygon points="12 2 14.5 8 21 9 16 14 18 21 12 17 6 21 8 14 3 9 9.5 8" fill="{SD}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="12 2 14.5 8 12 12 9.5 8" fill="{A}"/>
<polygon points="21 9 16 14 12 12 14.5 8" fill="{SM}"/>
<polygon points="18 21 12 17 12 12 16 14" fill="{A}"/>
<polygon points="6 21 8 14 12 12 12 17" fill="{AL}"/>
<polygon points="3 9 9.5 8 12 12 8 14" fill="{A}"/>''',

    "wf-library": f'''<rect x="3" y="4" width="4" height="17" rx="0.5" fill="{SM}" stroke="{BD}" stroke-width="1.2"/>
<rect x="8" y="2" width="5" height="19" rx="0.5" fill="{SD}" stroke="{BD}" stroke-width="1.2"/>
<rect x="14" y="5" width="4" height="16" rx="0.5" fill="{A}" stroke="{BD}" stroke-width="1.2"/>
<rect x="19" y="8" width="3" height="13" rx="0.5" fill="{SL}" stroke="{BD}" stroke-width="1.2"/>
<line x1="9.5" y1="6" x2="11.5" y2="6" stroke="{A}" stroke-width="1.5"/>''',

    "wf-lecture": f'''<rect x="3" y="3" width="18" height="13" rx="1.5" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<rect x="5" y="5" width="14" height="9" fill="{SM}"/>
<polygon points="6 6 12 6 12 9 6 9" fill="{A}"/>
<line x1="6" y1="11" x2="18" y2="11" stroke="{W}" stroke-width="1.2"/>
<polygon points="9 16 15 16 17 21 7 21" fill="{A}" stroke="{BD}" stroke-width="1.5" stroke-linejoin="round"/>''',

    # 8. Safety
    "wf-emergency": f'''<polygon points="7 2 17 2 22 7 22 17 17 22 7 22 2 17 2 7" fill="{SD}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<circle cx="12" cy="12" r="7.5" fill="{SM}"/>
<line x1="12" y1="2" x2="12" y2="5" stroke="{A}" stroke-width="2"/>
<line x1="12" y1="19" x2="12" y2="22" stroke="{A}" stroke-width="2"/>
<line x1="2" y1="12" x2="5" y2="12" stroke="{A}" stroke-width="2"/>
<line x1="19" y1="12" x2="22" y2="12" stroke="{A}" stroke-width="2"/>
<polygon points="11 7 13 7 13 13 11 13" fill="{A}"/>
<circle cx="12" cy="16" r="1.3" fill="{A}"/>''',

    "wf-evacuate": f'''<polygon points="13 3 21 3 21 21 13 21" fill="{A}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="15 5 19 5 19 19 15 19" fill="{AL}"/>
<circle cx="7" cy="6" r="1.8" fill="{BD}"/>
<path d="M5 16l2-3 2 1.5 3-4.5h2" stroke="{BD}" stroke-width="2" stroke-linecap="round" fill="none"/>''',

    "wf-assembly": f'''<polygon points="12 2 14.5 7 20 5 18 10.5 23 13 18 15.5 20 21 14.5 19 12 24 9.5 19 4 21 6 15.5 1 13 6 10.5 4 5 9.5 7" fill="{SD}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="12 2 14.5 7 12 13 9.5 7" fill="{A}"/>
<polygon points="20 5 18 10.5 12 13 14.5 7" fill="{SM}"/>
<polygon points="23 13 18 15.5 12 13 18 10.5" fill="{A}"/>
<polygon points="20 21 14.5 19 12 13 18 15.5" fill="{AL}"/>
<polygon points="12 24 9.5 19 12 13 14.5 19" fill="{A}"/>
<polygon points="4 21 6 15.5 12 13 9.5 19" fill="{SM}"/>
<polygon points="1 13 6 10.5 12 13 6 15.5" fill="{A}"/>
<polygon points="4 5 9.5 7 12 13 6 10.5" fill="{AL}"/>''',

    "wf-fire": f'''<polygon points="12 2 15 8.5 22 9.5 17 14.5 18.5 21.5 12 18 5.5 21.5 7 14.5 2 9.5 9 8.5" fill="{SD}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="12 2 15 8.5 12 14 9 8.5" fill="{A}"/>
<polygon points="22 9.5 17 14.5 12 14 15 8.5" fill="{AL}"/>
<polygon points="18.5 21.5 12 18 12 14 17 14.5" fill="{AD}"/>
<polygon points="5.5 21.5 7 14.5 12 14 12 18" fill="{A}"/>
<polygon points="2 9.5 9 8.5 12 14 7 14.5" fill="{AL}"/>''',

    "wf-warning": f'''<polygon points="12 2 23 20 1 20" fill="{SD}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="12 5 20.5 18.5 3.5 18.5" fill="{A}" stroke="{BD}" stroke-width="1.2" stroke-linejoin="round"/>
<polygon points="12 5 20.5 18.5 12 18.5" fill="{AL}" opacity="0.4"/>
<line x1="12" y1="9" x2="12" y2="13.5" stroke="{BD}" stroke-width="2.5" stroke-linecap="round"/>
<circle cx="12" cy="16.5" r="1.3" fill="{BD}"/>''',

    "wf-construction": f'''<polygon points="12 2 23 20 1 20" fill="{A}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="12 2 12 20 1 20" fill="{AL}" opacity="0.35"/>
<line x1="6" y1="16" x2="18" y2="16" stroke="{BD}" stroke-width="2.5"/>
<line x1="8" y1="12" x2="16" y2="12" stroke="{BD}" stroke-width="2.5"/>
<polygon points="12 5 15 10 9 10" fill="{SD}"/>''',

    # 9. UI
    "wf-home": f'''<polygon points="12 2 22 10 19 10 19 21 5 21 5 10 2 10" fill="{SD}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="12 2 22 10 19 10 12 4.5 5 10 2 10" fill="{A}" stroke="{BD}" stroke-width="1.2" stroke-linejoin="round"/>
<polygon points="12 2 22 10 19 10 12 4.5" fill="{AL}"/>
<rect x="9.5" y="13" width="5" height="8" fill="{A}" stroke="{BD}" stroke-width="1.2"/>''',

    "wf-search": f'''<circle cx="10.5" cy="10.5" r="7.5" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<circle cx="10.5" cy="10.5" r="5.5" fill="{SM}"/>
<path d="M7 7 A5 5 0 0 1 14 7" stroke="{A}" stroke-width="2" stroke-linecap="round" fill="none"/>
<polygon points="15 15 21 21 22 20 16 14" fill="{A}" stroke="{BD}" stroke-width="1.5" stroke-linejoin="round"/>''',

    "wf-menu": f'''<rect x="3" y="4" width="18" height="3.5" rx="1.5" fill="{A}" stroke="{BD}" stroke-width="1.5"/>
<rect x="3" y="10.25" width="18" height="3.5" rx="1.5" fill="{SD}" stroke="{BD}" stroke-width="1.5"/>
<rect x="3" y="16.5" width="18" height="3.5" rx="1.5" fill="{A}" stroke="{BD}" stroke-width="1.5"/>''',

    "wf-back": f'''<polygon points="16 3 6 12 16 21 19 18 11 12 19 6" fill="{A}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="16 3 6 12 11 12 19 6" fill="{AL}"/>''',

    "wf-close": f'''<polygon points="6 3 12 9 18 3 21 6 15 12 21 18 18 21 12 15 6 21 3 18 9 12 3 6" fill="{A}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="6 3 12 9 15 12 9 12 3 6" fill="{AL}"/>''',

    "wf-hours": f'''<circle cx="12" cy="12" r="9.5" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<circle cx="12" cy="12" r="7.5" fill="{SM}"/>
<path d="M12 4.5 A7.5 7.5 0 0 1 19.5 12 L12 12 Z" fill="{A}"/>
<line x1="12" y1="6" x2="12" y2="12" stroke="{BD}" stroke-width="2" stroke-linecap="round"/>
<line x1="12" y1="12" x2="16" y2="12" stroke="{BD}" stroke-width="2" stroke-linecap="round"/>''',

    "wf-timetable": f'''<rect x="3" y="4" width="18" height="17" rx="2" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<rect x="3" y="4" width="18" height="5" fill="{A}" stroke="{BD}" stroke-width="1.2"/>
<circle cx="8" cy="13" r="1.3" fill="{W}"/>
<circle cx="12" cy="13" r="1.3" fill="{W}"/>
<circle cx="16" cy="13" r="1.3" fill="{W}"/>
<circle cx="8" cy="17" r="1.3" fill="{W}"/>
<circle cx="12" cy="17" r="1.3" fill="{A}"/>''',

    "wf-events": f'''<rect x="3" y="4" width="18" height="17" rx="2" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<rect x="3" y="4" width="18" height="5" fill="{SM}" stroke="{BD}" stroke-width="1.2"/>
<polygon points="12 10 13.5 13 17 13.5 14.5 16 15 19.5 12 18 9 19.5 9.5 16 7 13.5 10.5 13" fill="{A}" stroke="{BD}" stroke-width="1"/>''',

    "wf-news": f'''<polygon points="3 4 19 4 21 7 21 21 3 21" fill="{SM}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="19 4 21 7 19 7" fill="{SL}"/>
<rect x="5.5" y="6.5" width="6" height="5" fill="{A}" stroke="{BD}" stroke-width="1"/>
<line x1="13.5" y1="7" x2="18.5" y2="7" stroke="{W}" stroke-width="1.5"/>
<line x1="13.5" y1="10" x2="18.5" y2="10" stroke="{W}" stroke-width="1.5"/>
<line x1="5.5" y1="14" x2="18.5" y2="14" stroke="{W}" stroke-width="1.5"/>
<line x1="5.5" y1="17.5" x2="15.5" y2="17.5" stroke="{A}" stroke-width="1.5"/>''',

    "wf-announce": f'''<polygon points="4 9 13 4 13 20 4 15" fill="{SD}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="4 9 13 4 13 12 4 12" fill="{SM}"/>
<path d="M16 8a5 5 0 0 1 0 8" stroke="{A}" stroke-width="2.5" stroke-linecap="round" fill="none"/>
<path d="M19 5a9 9 0 0 1 0 14" stroke="{A}" stroke-width="2.5" stroke-linecap="round" fill="none"/>
<path d="M6 15v4a2 2 0 0 0 2 2h2" fill="none" stroke="{BD}" stroke-width="2"/>''',

    # 10. Media
    "wf-share": f'''<polygon points="14 3 22 9 14 15 14 11 4 11 4 7 14 7" fill="{SD}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="14 3 22 9 14 9" fill="{A}"/>
<circle cx="6" cy="18" r="2.5" fill="{A}" stroke="{BD}" stroke-width="1.2"/>
<line x1="8.5" y1="17" x2="17" y2="13" stroke="{A}" stroke-width="1.8"/>''',

    "wf-chat": f'''<path d="M4 5h14a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2H8l-5 4V7a2 2 0 0 1 2-2z" fill="{SD}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<path d="M4 5h14a2 2 0 0 1 2 2v3H4z" fill="{SM}"/>
<circle cx="8" cy="11" r="1.3" fill="{A}"/>
<circle cx="12" cy="11" r="1.3" fill="{A}"/>
<circle cx="16" cy="11" r="1.3" fill="{A}"/>''',

    "wf-like": f'''<path d="M13 9V4a2 2 0 0 0-2-2l-3 7v12h10a2 2 0 0 0 2-1.7l1.3-8.5a2 2 0 0 0-2-2.3H13z" fill="{SD}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<rect x="3" y="9" width="5" height="12" rx="1" fill="{A}" stroke="{BD}" stroke-width="1.8"/>
<line x1="8" y1="9" x2="8" y2="21" stroke="{BD}" stroke-width="1.5"/>
<path d="M13 9V4a2 2 0 0 0-2-2l-3 7h5z" fill="{AL}"/>''',

    "wf-camera": f'''<polygon points="4 7 7 4 17 4 20 7 21 7 21 20 3 20 3 7" fill="{SD}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<circle cx="12" cy="13.5" r="4.5" fill="{SM}" stroke="{BD}" stroke-width="1.5"/>
<circle cx="12" cy="13.5" r="2.5" fill="{A}"/>
<circle cx="18" cy="8" r="1.2" fill="{AL}"/>''',

    "wf-video": f'''<rect x="2" y="6" width="13" height="12" rx="2" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<polygon points="15 10 22 6 22 18 15 14" fill="{A}" stroke="{BD}" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="15 10 22 6 15 14" fill="{AL}"/>
<circle cx="6" cy="9.5" r="1.5" fill="{AL}"/>''',

    "wf-qr": f'''<rect x="2" y="2" width="20" height="20" rx="3" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<rect x="4" y="4" width="6.5" height="6.5" fill="{W}" stroke="{BD}" stroke-width="1.2"/>
<rect x="5.5" y="5.5" width="3.5" height="3.5" fill="{A}"/>
<rect x="13.5" y="4" width="6.5" height="6.5" fill="{W}" stroke="{BD}" stroke-width="1.2"/>
<rect x="15" y="5.5" width="3.5" height="3.5" fill="{A}"/>
<rect x="4" y="13.5" width="6.5" height="6.5" fill="{W}" stroke="{BD}" stroke-width="1.2"/>
<rect x="5.5" y="15" width="3.5" height="3.5" fill="{A}"/>
<rect x="13.5" y="13.5" width="3" height="3" fill="{A}"/>
<rect x="17" y="17" width="3" height="3" fill="{A}"/>
<rect x="13.5" y="17" width="3" height="3" fill="{W}"/>''',

    "wf-email": f'''<rect x="2" y="4" width="20" height="16" rx="2" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<polygon points="2 5 12 13 22 5" fill="{SM}" stroke="{BD}" stroke-width="1.2"/>
<polygon points="2 5 12 13 7 13" fill="{A}"/>
<polygon points="22 5 12 13 17 13" fill="{AL}"/>''',

    "wf-web": f'''<circle cx="12" cy="12" r="9.5" fill="{SD}" stroke="{BD}" stroke-width="1.8"/>
<ellipse cx="12" cy="12" rx="4.5" ry="9.5" fill="{SM}" stroke="{A}" stroke-width="1.5"/>
<line x1="2.5" y1="12" x2="21.5" y2="12" stroke="{A}" stroke-width="1.8"/>
<circle cx="12" cy="12" r="2.2" fill="{A}"/>'''
}

print(f"Total Tactical icons defined: {len(TACTICAL_ICONS)}")

# 1. Generate individual SVG files in svg/tactical/<id>.svg
for icon_id, paths in TACTICAL_ICONS.items():
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="wf-icon wf-icon-tactical {icon_id}">
  {paths}
</svg>
'''
    file_path = os.path.join(SVG_TACTICAL_DIR, f"{icon_id}.svg")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

print(f"Wrote 80 individual SVGs to {SVG_TACTICAL_DIR}")

# 2. Generate SVG Sprite dist/wayfinding-icons-tactical.svg
sprite_symbols = []
for icon_id, paths in TACTICAL_ICONS.items():
    sym = f'  <symbol id="{icon_id}" viewBox="0 0 24 24">\n    {paths}\n  </symbol>'
    sprite_symbols.append(sym)

sprite_content = f'''<svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
{os.linesep.join(sprite_symbols)}
</svg>
'''
sprite_path = os.path.join(DIST_DIR, "wayfinding-icons-tactical.svg")
with open(sprite_path, "w", encoding="utf-8") as f:
    f.write(sprite_content)
print(f"Wrote sprite to {sprite_path}")

# 3. Update dist/wayfinding-icons.json with paths_tactical
json_path = os.path.join(DIST_DIR, "wayfinding-icons.json")
with open(json_path, "r", encoding="utf-8") as f:
    metadata = json.load(f)

for item in metadata:
    item_id = item["id"]
    if item_id in TACTICAL_ICONS:
        item["paths_tactical"] = TACTICAL_ICONS[item_id]

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2, ensure_ascii=False)
print("Updated dist/wayfinding-icons.json with paths_tactical")

# 4. Update dist/wayfinding-icons.js with WAYFINDING_TACTICAL export and web component support
js_path = os.path.join(DIST_DIR, "wayfinding-icons.js")
with open(js_path, "r", encoding="utf-8") as f:
    js_text = f.read()

tactical_js_entries = []
for k, v in TACTICAL_ICONS.items():
    escaped_v = v.replace('"', '\\"').replace('\n', '\\n')
    tactical_js_entries.append(f'  "{k}": "{escaped_v}"')
tactical_js_dict = "export const WAYFINDING_TACTICAL = {\n" + ",\n".join(tactical_js_entries) + "\n};\n\n"

if "export const WAYFINDING_TACTICAL" not in js_text:
    target_needle = "export const WAYFINDING_DUOTONE = {"
    idx = js_text.find(target_needle)
    if idx != -1:
        js_text = js_text[:idx] + tactical_js_dict + js_text[idx:]
    else:
        js_text = tactical_js_dict + js_text

# Update getWayfindingIcon and render
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
  } else if (set === 'tactical') {
    paths = WAYFINDING_TACTICAL[iconId] || '';
    if (!paths) return '';
    return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" class="wf-icon wf-icon-tactical ${iconId} ${className}">${paths}</svg>`;
  }
  paths = WAYFINDING_LINE[iconId] || '';
  if (!paths) return '';
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${strokeWidth}" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-line ${iconId} ${className}">${paths}</svg>`;
}"""

new_render = """  render() {
    const name = this.getAttribute('name') || 'wf-pin';
    const set = this.getAttribute('set') || 'line';
    const size = this.getAttribute('size') || '24';
    const strokeWidth = this.getAttribute('stroke-width') || '2';
    const color = this.getAttribute('color');

    if (color) {
      this.style.color = color;
      this.style.setProperty('--wf-accent', color);
    }

    if (set === 'solid') {
      const paths = WAYFINDING_SOLID[name] || '';
      this.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" fill="currentColor" class="wf-icon wf-icon-solid ${name}">${paths}</svg>`;
    } else if (set === 'duotone') {
      const paths = WAYFINDING_DUOTONE[name] || '';
      this.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" class="wf-icon wf-icon-duotone ${name}">${paths}</svg>`;
    } else if (set === 'tactical') {
      const paths = WAYFINDING_TACTICAL[name] || '';
      this.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" class="wf-icon wf-icon-tactical ${name}">${paths}</svg>`;
    } else {
      const paths = WAYFINDING_LINE[name] || '';
      this.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${strokeWidth}" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-line ${name}">${paths}</svg>`;
    }
  }"""

import re
js_text = re.sub(r'export function getWayfindingIcon\(iconId, options = \{\}\) \{[\s\S]*?^\}', new_get_icon, js_text, flags=re.MULTILINE)
js_text = re.sub(r'  render\(\) \{[\s\S]*?^\  \}', new_render, js_text, flags=re.MULTILINE)

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_text)

print("Updated dist/wayfinding-icons.js with WAYFINDING_TACTICAL & Web Component support")
