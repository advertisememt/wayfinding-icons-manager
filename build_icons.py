"""
Wayfinding Kiosk Icon Library Generator (Dual Sets: Modern Line & Solid Signage)
Generates:
- 80 Line SVGs in svg/line/
- 80 Solid SVGs in svg/solid/
- 80 Default SVGs in svg/
- SVG Sprite Sheets (dist/wayfinding-icons-line.svg, dist/wayfinding-icons-solid.svg, dist/wayfinding-icons.svg)
- CSS classes (dist/wayfinding-icons.css)
- JavaScript module & Web Component (dist/wayfinding-icons.js)
- JSON metadata (dist/wayfinding-icons.json)
- Complete ZIP bundle (dist/wayfinding-icons.zip)
- Interactive Showcase & Explorer Web App with Design Set Dropdown (index.html)
- Documentation (README.md)
"""

import os
import json
import zipfile

# 1. MODERN LINE (OUTLINE) ICONS
ICONS_LINE = [
    # Navigation
    {
        "id": "wf-arrow-up",
        "name": "Ahead",
        "category": "Navigation",
        "keywords": ["ahead", "forward", "straight", "north", "up", "arrow", "direction"],
        "paths": '<path d="M12 19V5"/><path d="m5 12 7-7 7 7"/>'
    },
    {
        "id": "wf-arrow-right",
        "name": "Right",
        "category": "Navigation",
        "keywords": ["right", "east", "turn right", "arrow", "direction"],
        "paths": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>'
    },
    {
        "id": "wf-arrow-down",
        "name": "Down / behind",
        "category": "Navigation",
        "keywords": ["down", "behind", "reverse", "south", "backwards", "arrow", "direction"],
        "paths": '<path d="M12 5v14"/><path d="m19 12-7 7-7-7"/>'
    },
    {
        "id": "wf-arrow-left",
        "name": "Left",
        "category": "Navigation",
        "keywords": ["left", "west", "turn left", "arrow", "direction"],
        "paths": '<path d="M19 12H5"/><path d="m12 19-7-7 7-7"/>'
    },
    {
        "id": "wf-arrow-up-right",
        "name": "Ahead right",
        "category": "Navigation",
        "keywords": ["ahead right", "diagonal right", "bear right", "northeast", "arrow"],
        "paths": '<path d="M7 17 17 7"/><path d="M8 7h9v9"/>'
    },
    {
        "id": "wf-arrow-up-left",
        "name": "Ahead left",
        "category": "Navigation",
        "keywords": ["ahead left", "diagonal left", "bear left", "northwest", "arrow"],
        "paths": '<path d="m17 17-10-10"/><path d="M16 7H7v9"/>'
    },
    {
        "id": "wf-u-turn",
        "name": "Turn around",
        "category": "Navigation",
        "keywords": ["turn around", "u-turn", "reverse", "loop", "opposite direction"],
        "paths": '<path d="M9 10v7"/><path d="m5 13 4 4 4-4"/><path d="M9 10a5 5 0 0 1 10 0v8"/>'
    },
    {
        "id": "wf-signpost",
        "name": "Directions",
        "category": "Navigation",
        "keywords": ["directions", "signpost", "guide", "guidepost", "which way", "directory"],
        "paths": '<path d="M12 3v18"/><path d="M12 5H5a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h7l2-2.5L12 5z"/><path d="M12 12h7a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-7l-2-2.5 2-2.5z"/>'
    },
    {
        "id": "wf-pin",
        "name": "You are here",
        "category": "Navigation",
        "keywords": ["you are here", "location", "marker", "pin", "current position", "destination"],
        "paths": '<path d="M12 21s-6-5.686-6-10a6 6 0 0 1 12 0c0 4.314-6 10-6 10z"/><circle cx="12" cy="11" r="2.5"/>'
    },
    {
        "id": "wf-facing",
        "name": "Facing this way",
        "category": "Navigation",
        "keywords": ["facing this way", "orientation", "bearing", "heading", "compass", "view angle"],
        "paths": '<circle cx="12" cy="12" r="9"/><polygon points="12 4 15 12 12 10 9 12 12 4" fill="currentColor"/><circle cx="12" cy="17" r="1" fill="currentColor"/>'
    },
    {
        "id": "wf-map",
        "name": "Map",
        "category": "Navigation",
        "keywords": ["map", "floor plan", "overview", "layout", "directory", "concourse"],
        "paths": '<polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"/><line x1="9" y1="3" x2="9" y2="18"/><line x1="15" y1="6" x2="15" y2="21"/>'
    },
    {
        "id": "wf-touch",
        "name": "Touch here",
        "category": "Navigation",
        "keywords": ["touch here", "tap", "finger", "interact", "touchscreen", "press", "kiosk"],
        "paths": '<path d="M12 11V6a1.5 1.5 0 0 1 3 0v5"/><path d="M15 9.5a1.5 1.5 0 0 1 3 0V12a1.5 1.5 0 0 1 3 0v3a6 6 0 0 1-6 6h-2a6 6 0 0 1-4.24-1.76L5 15.4a1.5 1.5 0 0 1 2.2-2L9.5 15V6a1.5 1.5 0 0 1 3 0v5"/><path d="M12 3a9 9 0 0 1 9 9"/><path d="M12 6a6 6 0 0 1 6 6"/>'
    },

    # Building
    {
        "id": "wf-entrance",
        "name": "Entrance",
        "category": "Building",
        "keywords": ["entrance", "enter", "entry", "door", "ingress", "main entrance", "doorway"],
        "paths": '<path d="M14 20V4a1 1 0 0 1 1-1h5a1 1 0 0 1 1 1v16"/><path d="m14 4-7 2.5v12l7 1.5"/><circle cx="10" cy="12" r="0.75" fill="currentColor"/><line x1="2" y1="20" x2="22" y2="20"/><path d="M2 11h8"/><path d="m7 7.5 3.5 3.5-3.5 3.5"/>'
    },
    {
        "id": "wf-exit",
        "name": "Exit",
        "category": "Building",
        "keywords": ["exit", "egress", "way out", "door", "leave", "outdoor"],
        "paths": '<path d="M10 20V4a1 1 0 0 0-1-1H4a1 1 0 0 0-1 1v16"/><path d="m10 4 7 2.5v12l-7 1.5"/><circle cx="14" cy="12" r="0.75" fill="currentColor"/><line x1="2" y1="20" x2="22" y2="20"/><path d="M14 11h8"/><path d="m18.5 7.5 3.5 3.5-3.5 3.5"/>'
    },
    {
        "id": "wf-lift",
        "name": "Lift",
        "category": "Building",
        "keywords": ["lift", "elevator", "floors", "vertical", "accessible lift"],
        "paths": '<rect x="3" y="3" width="12" height="18" rx="2"/><circle cx="6.5" cy="8" r="1.4"/><path d="M4.5 16.5v-2a1.8 1.8 0 0 1 3.6 0v2"/><circle cx="11.5" cy="8" r="1.4"/><path d="M9.7 16.5v-2a1.8 1.8 0 0 1 3.6 0v2"/><polygon points="18.5 4.5 15.5 8.5 21.5 8.5" fill="currentColor"/><polygon points="18.5 19.5 15.5 15.5 21.5 15.5" fill="currentColor"/><line x1="18.5" y1="11" x2="18.5" y2="13"/>'
    },
    {
        "id": "wf-stairs",
        "name": "Stairs",
        "category": "Building",
        "keywords": ["stairs", "staircase", "steps", "walk up", "stairwell"],
        "paths": '<path d="M4 19h4v-4h4v-4h4V7h4"/><circle cx="7" cy="6" r="2"/><path d="m11 11-2-2.5-3 1.5"/>'
    },
    {
        "id": "wf-escalator-up",
        "name": "Escalator up",
        "category": "Building",
        "keywords": ["escalator up", "moving stairs", "up", "level up", "transit"],
        "paths": '<path d="M3 7h4l7 10h7"/><path d="m5 17 4-4"/><path d="M5 13h4v4"/><circle cx="6" cy="4" r="1.5"/><path d="m8 9-2-2-3 2"/>'
    },
    {
        "id": "wf-escalator-down",
        "name": "Escalator down",
        "category": "Building",
        "keywords": ["escalator down", "moving stairs", "down", "level down", "transit"],
        "paths": '<path d="M3 17h4l7-10h7"/><path d="m19 17-4-4"/><path d="M15 17h4v-4"/><circle cx="18" cy="4" r="1.5"/><path d="m16 9 2-2 3 2"/>'
    },
    {
        "id": "wf-ramp",
        "name": "Ramp",
        "category": "Building",
        "keywords": ["ramp", "incline", "slope", "accessible route", "step free"],
        "paths": '<polygon points="3 19 21 19 21 11 3 19"/><circle cx="14" cy="7" r="1.5"/><path d="M12 14a2.5 2.5 0 0 1 3-2.4l1.5-1.6"/>'
    },
    {
        "id": "wf-accessible",
        "name": "Accessible",
        "category": "Building",
        "keywords": ["accessible", "wheelchair", "disabled", "disability", "step free", "accessibility"],
        "paths": '<circle cx="12" cy="4.5" r="2"/><path d="M10 9h3.5l1.5 5h3"/><path d="M13.5 14A4 4 0 1 1 8 11.5"/><path d="M8 12h3"/>'
    },
    {
        "id": "wf-levels",
        "name": "Levels",
        "category": "Building",
        "keywords": ["levels", "floors", "stories", "multi-level", "stack", "building layout"],
        "paths": '<polygon points="12 3 21 7.5 12 12 3 7.5 12 3"/><polyline points="3 12 12 16.5 21 12"/><polyline points="3 16.5 12 21 21 16.5"/>'
    },
    {
        "id": "wf-no-entry",
        "name": "No entry",
        "category": "Building",
        "keywords": ["no entry", "do not enter", "restricted", "stop", "forbidden", "closed"],
        "paths": '<circle cx="12" cy="12" r="9"/><line x1="6" y1="12" x2="18" y2="12" stroke-width="3"/>'
    },
    {
        "id": "wf-prohibited",
        "name": "Not permitted",
        "category": "Building",
        "keywords": ["not permitted", "prohibited", "banned", "forbidden", "slash", "restriction"],
        "paths": '<circle cx="12" cy="12" r="9"/><line x1="5.6" y1="5.6" x2="18.4" y2="18.4"/>'
    },
    {
        "id": "wf-staff-only",
        "name": "Staff only",
        "category": "Building",
        "keywords": ["staff only", "employees", "authorized personnel", "restricted access", "badge", "id"],
        "paths": '<rect x="5" y="8" width="14" height="13" rx="2"/><circle cx="12" cy="13" r="2.5"/><path d="M9 19c0-1.7 1.3-3 3-3s3 1.3 3 3"/><path d="M9 8V5a3 3 0 0 1 6 0v3"/>'
    },

    # Amenities
    {
        "id": "wf-toilets",
        "name": "Toilets",
        "category": "Amenities",
        "keywords": ["toilets", "restroom", "wc", "washroom", "bathroom", "amenities"],
        "paths": '<line x1="12" y1="4" x2="12" y2="20"/><circle cx="7" cy="5" r="1.5"/><path d="M5 9h4v6H8v5H6v-5H5V9z"/><circle cx="17" cy="5" r="1.5"/><path d="M15 15l-1-6h6l-1 6h-4z"/><path d="M16 15v5h2v-5"/>'
    },
    {
        "id": "wf-toilet-male",
        "name": "Male toilet",
        "category": "Amenities",
        "keywords": ["male toilet", "men", "gents", "male restroom", "man"],
        "paths": '<circle cx="12" cy="4" r="2"/><path d="M9 8h6a1 1 0 0 1 1 1v6h-2v6h-4v-6H8V9a1 1 0 0 1 1-1z"/>'
    },
    {
        "id": "wf-toilet-female",
        "name": "Female toilet",
        "category": "Amenities",
        "keywords": ["female toilet", "women", "ladies", "female restroom", "woman"],
        "paths": '<circle cx="12" cy="4" r="2"/><path d="M9.5 8h5l2.5 8h-4v5h-2v-5H7l2.5-8z"/>'
    },
    {
        "id": "wf-toilet-accessible",
        "name": "Accessible toilet",
        "category": "Amenities",
        "keywords": ["accessible toilet", "wheelchair toilet", "disabled wc", "accessible bathroom"],
        "paths": '<circle cx="10" cy="5" r="1.8"/><path d="M8 9h3l1.5 4h2.5"/><path d="M11 13a3.5 3.5 0 1 1-5-2"/><path d="M17 9h4v11h-4"/><path d="M19 12v3"/>'
    },
    {
        "id": "wf-baby-change",
        "name": "Baby change",
        "category": "Amenities",
        "keywords": ["baby change", "parents room", "nappy change", "infant care", "baby care"],
        "paths": '<line x1="3" y1="18" x2="21" y2="18"/><circle cx="7" cy="9" r="2.5"/><path d="M10 13c1.5 0 3-1 4-2 1.5 1.5 3.5 1.5 5 1"/><path d="M12 4v4"/><path d="m10 6 4 0"/>'
    },
    {
        "id": "wf-cafe",
        "name": "Café",
        "category": "Amenities",
        "keywords": ["cafe", "coffee", "tea", "espresso", "beverage", "drinks", "cafeteria"],
        "paths": '<path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v7a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="2" x2="6" y2="5"/><line x1="10" y1="2" x2="10" y2="5"/><line x1="14" y1="2" x2="14" y2="5"/>'
    },
    {
        "id": "wf-food",
        "name": "Food",
        "category": "Amenities",
        "keywords": ["food", "dining", "restaurant", "food court", "cutlery", "eat", "meal"],
        "paths": '<path d="M18 2v20"/><path d="M21 2c0 4-3 5-3 8"/><path d="M3 2v6c0 1.7 1.3 3 3 3v11"/><path d="M6 2v6"/><path d="M9 2v6c0 1.7-1.3 3-3 3"/>'
    },
    {
        "id": "wf-retail",
        "name": "Retail",
        "category": "Amenities",
        "keywords": ["retail", "shopping", "store", "shop", "boutique", "mall", "bag"],
        "paths": '<path d="M6 8V6a6 6 0 0 1 12 0v2"/><rect x="4" y="8" width="16" height="13" rx="2"/><circle cx="9" cy="13" r="1" fill="currentColor"/><circle cx="15" cy="13" r="1" fill="currentColor"/>'
    },
    {
        "id": "wf-atm",
        "name": "ATM",
        "category": "Amenities",
        "keywords": ["atm", "cash machine", "cashpoint", "money", "withdraw", "bank"],
        "paths": '<rect x="3" y="4" width="18" height="16" rx="2"/><line x1="7" y1="9" x2="17" y2="9"/><line x1="7" y1="13" x2="12" y2="13"/><rect x="14" y="12" width="3" height="4" rx="0.5"/>'
    },
    {
        "id": "wf-payment",
        "name": "Cashier / pay",
        "category": "Amenities",
        "keywords": ["cashier", "pay", "payment", "card", "checkout", "credit card", "pos"],
        "paths": '<rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/><circle cx="7" cy="15" r="1.5"/><circle cx="11" cy="15" r="1.5"/>'
    },
    {
        "id": "wf-pharmacy",
        "name": "Pharmacy",
        "category": "Amenities",
        "keywords": ["pharmacy", "chemist", "dispensary", "prescription", "medicine", "drugs"],
        "paths": '<path d="M12 3v18"/><path d="M3 12h18"/><circle cx="12" cy="12" r="9"/>'
    },
    {
        "id": "wf-water",
        "name": "Drinking water",
        "category": "Amenities",
        "keywords": ["drinking water", "water fountain", "refill", "hydration", "tap", "bottle refill"],
        "paths": '<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/><path d="M12 18a4 4 0 0 0 4-4"/>'
    },
    {
        "id": "wf-wifi",
        "name": "Free Wi-Fi",
        "category": "Amenities",
        "keywords": ["wifi", "free wifi", "internet", "wireless", "network", "hotspot"],
        "paths": '<path d="M5 12.55a11 11 0 0 1 14.08 0"/><path d="M1.42 9a16 16 0 0 1 21.16 0"/><path d="M8.53 16.11a6 6 0 0 1 6.95 0"/><circle cx="12" cy="19.5" r="1.2" fill="currentColor"/>'
    },
    {
        "id": "wf-seating",
        "name": "Waiting area",
        "category": "Amenities",
        "keywords": ["waiting area", "seating", "lounge", "rest", "chairs", "waiting room"],
        "paths": '<path d="M5 11V6a3 3 0 0 1 6 0v5"/><path d="M13 11V6a3 3 0 0 1 6 0v5"/><rect x="3" y="11" width="18" height="5" rx="1.5"/><path d="M5 16v5"/><path d="M19 16v5"/>'
    },

    # Transit
    {
        "id": "wf-parking",
        "name": "Car park",
        "category": "Transit",
        "keywords": ["car park", "parking", "garage", "p", "vehicle parking", "bays"],
        "paths": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M9 17V7h4.5a3.5 3.5 0 0 1 0 7H9"/>'
    },
    {
        "id": "wf-car",
        "name": "Drop-off",
        "category": "Transit",
        "keywords": ["drop-off", "pick-up", "car", "taxi", "passenger", "vehicle", "rideshare"],
        "paths": '<path d="M4 17h16"/><path d="M5 17l1.5-6h11l1.5 6"/><circle cx="7.5" cy="17" r="2"/><circle cx="16.5" cy="17" r="2"/><path d="M7 11l1.5-4.5a1.5 1.5 0 0 1 1.4-1h4.2a1.5 1.5 0 0 1 1.4 1L17 11"/>'
    },
    {
        "id": "wf-bus",
        "name": "Bus / shuttle",
        "category": "Transit",
        "keywords": ["bus", "shuttle", "coach", "public transport", "transit", "stop"],
        "paths": '<rect x="4" y="3" width="16" height="15" rx="3"/><line x1="4" y1="10" x2="20" y2="10"/><circle cx="8" cy="14" r="1.5"/><circle cx="16" cy="14" r="1.5"/><path d="M6 18v3"/><path d="M18 18v3"/><line x1="9" y1="6" x2="15" y2="6"/>'
    },
    {
        "id": "wf-ev",
        "name": "EV charging",
        "category": "Transit",
        "keywords": ["ev charging", "electric vehicle", "charger", "plug", "clean energy"],
        "paths": '<rect x="3" y="4" width="12" height="16" rx="2"/><path d="m8 9 2-3v4h2l-3 4v-3H7l2-2"/><path d="M15 9h3a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2h-1"/><circle cx="17" cy="17" r="1"/>'
    },

    # Services
    {
        "id": "wf-info",
        "name": "Information",
        "category": "Services",
        "keywords": ["information", "info", "help desk", "inquiries", "directory", "about"],
        "paths": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="8" r="1.2" fill="currentColor"/><path d="M11 12h2v5h-2z"/>'
    },
    {
        "id": "wf-help",
        "name": "Help",
        "category": "Services",
        "keywords": ["help", "assistance", "support", "question", "faq"],
        "paths": '<circle cx="12" cy="12" r="9"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><circle cx="12" cy="17" r="1" fill="currentColor"/>'
    },
    {
        "id": "wf-reception",
        "name": "Reception",
        "category": "Services",
        "keywords": ["reception", "front desk", "concierge", "check-in", "counter", "lobby"],
        "paths": '<path d="M4 19h16"/><path d="M4 15h16"/><path d="M12 4v4"/><path d="M8 8a4 4 0 0 1 8 0H8z"/><path d="M10 15v-3h4v3"/>'
    },
    {
        "id": "wf-security",
        "name": "Security",
        "category": "Services",
        "keywords": ["security", "guard", "protection", "safe", "shield", "patrol"],
        "paths": '<path d="M12 3s7 2.5 7 8c0 5.5-5 9.5-7 10-2-.5-7-4.5-7-10 0-5.5 7-8 7-8z"/><path d="m9 12 2 2 4-4"/>'
    },
    {
        "id": "wf-phone",
        "name": "Phone",
        "category": "Services",
        "keywords": ["phone", "telephone", "call", "public phone", "contact"],
        "paths": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>'
    },
    {
        "id": "wf-intercom",
        "name": "Help point",
        "category": "Services",
        "keywords": ["help point", "intercom", "call button", "emergency intercom", "pillar", "speaker"],
        "paths": '<rect x="6" y="3" width="12" height="18" rx="2"/><circle cx="12" cy="8" r="2"/><line x1="9" y1="13" x2="15" y2="13"/><circle cx="12" cy="17" r="1.5" fill="currentColor"/>'
    },

    # Healthcare
    {
        "id": "wf-hospital",
        "name": "Hospital",
        "category": "Healthcare",
        "keywords": ["hospital", "clinic", "medical center", "infirmary", "health", "ward"],
        "paths": '<path d="M3 21h18"/><path d="M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16"/><path d="M12 7v6"/><path d="M9 10h6"/><rect x="9.5" y="16" width="5" height="5"/>'
    },
    {
        "id": "wf-first-aid",
        "name": "First aid",
        "category": "Healthcare",
        "keywords": ["first aid", "emergency care", "medical kit", "cross", "treatment"],
        "paths": '<rect x="3" y="7" width="18" height="14" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><path d="M12 11v6"/><path d="M9 14h6"/>'
    },
    {
        "id": "wf-consult",
        "name": "Consulting / GP",
        "category": "Healthcare",
        "keywords": ["consulting", "gp", "doctor", "physician", "clinic", "stethoscope", "appointment"],
        "paths": '<path d="M6 3v5a6 6 0 0 0 12 0V3"/><circle cx="6" cy="3" r="1" fill="currentColor"/><circle cx="18" cy="3" r="1" fill="currentColor"/><path d="M12 14v4a3 3 0 0 0 6 0v-2"/><circle cx="18" cy="16" r="2"/>'
    },
    {
        "id": "wf-pathology",
        "name": "Pathology",
        "category": "Healthcare",
        "keywords": ["pathology", "lab", "laboratory", "blood test", "specimen", "microscope"],
        "paths": '<path d="M9 3h6"/><path d="M10 3v5l-4.5 9A2 2 0 0 0 7.3 20h9.4a2 2 0 0 0 1.8-3L14 8V3"/><line x1="7.5" y1="15" x2="16.5" y2="15"/>'
    },
    {
        "id": "wf-aed",
        "name": "Defibrillator",
        "category": "Healthcare",
        "keywords": ["defibrillator", "aed", "cardiac", "resuscitation", "heart", "shock", "emergency"],
        "paths": '<path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/><polygon points="12.5 6 9.5 12 13 12 11.5 17 15.5 11 12 11 12.5 6" fill="currentColor"/>'
    },

    # Campus
    {
        "id": "wf-student",
        "name": "Student hub",
        "category": "Campus",
        "keywords": ["student hub", "student services", "campus center", "union", "graduation cap", "alumni"],
        "paths": '<polygon points="12 3 22 8.5 12 14 2 8.5 12 3"/><path d="M6 10.7v5.3c0 2.2 2.7 4 6 4s6-1.8 6-4v-5.3"/><path d="M22 8.5v6"/>'
    },
    {
        "id": "wf-library",
        "name": "Library",
        "category": "Campus",
        "keywords": ["library", "books", "study", "reading", "learning", "quiet zone"],
        "paths": '<path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5z"/><path d="M4 6h16"/><line x1="8" y1="10" x2="16" y2="10"/><line x1="8" y1="14" x2="14" y2="14"/>'
    },
    {
        "id": "wf-lecture",
        "name": "Lecture room",
        "category": "Campus",
        "keywords": ["lecture room", "theatre", "auditorium", "classroom", "presentation", "seminar"],
        "paths": '<rect x="3" y="4" width="18" height="12" rx="2"/><line x1="3" y1="12" x2="21" y2="12"/><path d="M9 16l-2 5"/><path d="M15 16l2 5"/><circle cx="12" cy="8" r="2"/>'
    },

    # Safety
    {
        "id": "wf-emergency",
        "name": "Emergency",
        "category": "Safety",
        "keywords": ["emergency", "alarm", "alert", "danger", "urgent", "critical"],
        "paths": '<polygon points="12 2 21.5 7.5 21.5 16.5 12 22 2.5 16.5 2.5 7.5 12 2"/><line x1="12" y1="8" x2="12" y2="13"/><circle cx="12" cy="16.5" r="1" fill="currentColor"/>'
    },
    {
        "id": "wf-evacuate",
        "name": "Emergency exit",
        "category": "Safety",
        "keywords": ["emergency exit", "evacuate", "escape", "running man", "fire exit", "safety"],
        "paths": '<path d="M19 3v18h-6"/><circle cx="7.5" cy="5.5" r="1.5"/><path d="M5 10l3-2 3 2.5v4"/><path d="m8 10-3 5"/><path d="m8 14 3 6"/><path d="m11 10.5 4-1.5"/>'
    },
    {
        "id": "wf-assembly",
        "name": "Assembly point",
        "category": "Safety",
        "keywords": ["assembly point", "muster point", "meeting point", "evacuation assembly", "safe area"],
        "paths": '<circle cx="12" cy="12" r="3"/><path d="M4 4l4 4"/><path d="M4 8V4h4"/><path d="M20 4l-4 4"/><path d="M20 8V4h-4"/><path d="M4 20l4-4"/><path d="M4 16v4h4"/><path d="M20 20l-4-4"/><path d="M20 16v4h-4"/>'
    },
    {
        "id": "wf-fire",
        "name": "Fire",
        "category": "Safety",
        "keywords": ["fire", "flame", "hose", "hydrant", "extinguisher", "fire safety"],
        "paths": '<path d="M12 2c1 3 4 5 4 9a6 6 0 0 1-12 0c0-3.5 2.5-6.5 4-8 1 2 2 3 4-1z"/><path d="M12 13a2.5 2.5 0 0 0-2.5 2.5c0 1.38 1.12 2.5 2.5 2.5s2.5-1.12 2.5-2.5c0-1-.8-1.8-1.5-2.2-.3.3-.6.5-1 .2z"/>'
    },
    {
        "id": "wf-warning",
        "name": "Caution",
        "category": "Safety",
        "keywords": ["caution", "warning", "hazard", "attention", "careful", "notice"],
        "paths": '<path d="m10.29 3.86-8.57 14.85A2 2 0 0 0 3.45 22h17.1a2 2 0 0 0 1.73-3.29L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="14"/><circle cx="12" cy="18" r="1" fill="currentColor"/>'
    },
    {
        "id": "wf-construction",
        "name": "Under construction",
        "category": "Safety",
        "keywords": ["under construction", "work in progress", "maintenance", "cone", "barrier", "renovation"],
        "paths": '<polygon points="12 2 17 19 7 19 12 2"/><line x1="3" y1="21" x2="21" y2="21"/><line x1="8.5" y1="14" x2="15.5" y2="14"/><line x1="10" y1="9" x2="14" y2="9"/>'
    },

    # UI
    {
        "id": "wf-home",
        "name": "Home",
        "category": "UI",
        "keywords": ["home", "main screen", "start", "homepage", "welcome"],
        "paths": '<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V9z"/><polyline points="9 22 9 12 15 12 15 22"/>'
    },
    {
        "id": "wf-search",
        "name": "Search",
        "category": "UI",
        "keywords": ["search", "find", "lookup", "explore", "magnifier", "query"],
        "paths": '<circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>'
    },
    {
        "id": "wf-menu",
        "name": "Menu",
        "category": "UI",
        "keywords": ["menu", "hamburger", "navigation", "options", "list"],
        "paths": '<line x1="4" y1="6" x2="20" y2="6"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="18" x2="20" y2="18"/>'
    },
    {
        "id": "wf-back",
        "name": "Back",
        "category": "UI",
        "keywords": ["back", "previous", "return", "left arrow", "undo"],
        "paths": '<polyline points="15 18 9 12 15 6"/>'
    },
    {
        "id": "wf-close",
        "name": "Close",
        "category": "UI",
        "keywords": ["close", "dismiss", "exit modal", "cancel", "x"],
        "paths": '<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>'
    },
    {
        "id": "wf-hours",
        "name": "Opening hours",
        "category": "UI",
        "keywords": ["opening hours", "trading hours", "times", "clock", "schedule", "open"],
        "paths": '<circle cx="12" cy="12" r="9"/><polyline points="12 6 12 12 16 14"/>'
    },
    {
        "id": "wf-timetable",
        "name": "Timetable",
        "category": "UI",
        "keywords": ["timetable", "schedule", "departures", "timesheet", "planner", "calendar"],
        "paths": '<rect x="3" y="4" width="18" height="17" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="7" y1="13" x2="17" y2="13"/><line x1="7" y1="17" x2="13" y2="17"/>'
    },
    {
        "id": "wf-events",
        "name": "Events",
        "category": "UI",
        "keywords": ["events", "what's on", "calendar", "activities", "happenings", "starred"],
        "paths": '<rect x="3" y="4" width="18" height="17" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="16" y1="2" x2="16" y2="6"/><polygon points="12 12 13.2 14.5 16 14.9 14 16.8 14.5 19.5 12 18.2 9.5 19.5 10 16.8 8 14.9 10.8 14.5 12 12" fill="currentColor"/>'
    },
    {
        "id": "wf-news",
        "name": "News",
        "category": "UI",
        "keywords": ["news", "updates", "newspaper", "bulletin", "articles", "press"],
        "paths": '<path d="M4 20h14a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2z"/><line x1="6" y1="6" x2="14" y2="6"/><line x1="6" y1="10" x2="18" y2="10"/><line x1="6" y1="14" x2="18" y2="14"/>'
    },
    {
        "id": "wf-announce",
        "name": "Announcements",
        "category": "UI",
        "keywords": ["announcements", "broadcast", "megaphone", "bullhorn", "notices", "alerts"],
        "paths": '<path d="m3 11 15-5v12L3 13v-2z"/><path d="M11 13.5V19a2 2 0 0 1-2 2H8"/><path d="M19 9a4 4 0 0 1 0 6"/>'
    },

    # Media
    {
        "id": "wf-share",
        "name": "Share / social",
        "category": "Media",
        "keywords": ["share", "social", "send", "connect", "forward", "nodes"],
        "paths": '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/>'
    },
    {
        "id": "wf-chat",
        "name": "Chat",
        "category": "Media",
        "keywords": ["chat", "message", "conversation", "talk", "feedback", "bubble"],
        "paths": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>'
    },
    {
        "id": "wf-like",
        "name": "Like / feedback",
        "category": "Media",
        "keywords": ["like", "feedback", "thumbs up", "satisfaction", "survey", "rate", "positive"],
        "paths": '<path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3H14z"/><path d="M7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"/>'
    },
    {
        "id": "wf-camera",
        "name": "Photos",
        "category": "Media",
        "keywords": ["photos", "camera", "pictures", "images", "snapshots", "photography"],
        "paths": '<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>'
    },
    {
        "id": "wf-video",
        "name": "Video",
        "category": "Media",
        "keywords": ["video", "camcorder", "record", "clip", "stream", "film"],
        "paths": '<polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2"/>'
    },
    {
        "id": "wf-qr",
        "name": "Scan QR",
        "category": "Media",
        "keywords": ["scan qr", "qr code", "mobile scan", "barcode", "transfer to phone"],
        "paths": '<rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="15" y="15" width="2" height="2"/><rect x="19" y="15" width="2" height="2"/><rect x="15" y="19" width="6" height="2"/><path d="M6 6h1v1H6z" fill="currentColor"/><path d="M17 6h1v1h-1z" fill="currentColor"/><path d="M6 17h1v1H6z" fill="currentColor"/>'
    },
    {
        "id": "wf-email",
        "name": "Email",
        "category": "Media",
        "keywords": ["email", "mail", "envelope", "contact", "send to email", "newsletter"],
        "paths": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 7L2 7"/>'
    },
    {
        "id": "wf-web",
        "name": "Website",
        "category": "Media",
        "keywords": ["website", "web", "internet", "browser", "url", "online", "portal"],
        "paths": '<circle cx="12" cy="12" r="9"/><line x1="3" y1="12" x2="21" y2="12"/><path d="M12 3a15 15 0 0 1 4 9 15 15 0 0 1-4 9 15 15 0 0 1-4-9 15 15 0 0 1 4-9z"/>'
    }
]

# 2. SOLID SIGNAGE (FILLED SILHOUETTES) ICONS
ICONS_SOLID = [
    # Navigation
    {
        "id": "wf-arrow-up",
        "name": "Ahead",
        "category": "Navigation",
        "keywords": ["ahead", "forward", "straight", "north", "up", "arrow", "direction"],
        "paths": '<path d="M12 2.5l7 7h-4.5v12h-5v-12H5z" fill="currentColor"/>'
    },
    {
        "id": "wf-arrow-right",
        "name": "Right",
        "category": "Navigation",
        "keywords": ["right", "east", "turn right", "arrow", "direction"],
        "paths": '<path d="M21.5 12l-7-7v4.5H2.5v5h12v4.5z" fill="currentColor"/>'
    },
    {
        "id": "wf-arrow-down",
        "name": "Down / behind",
        "category": "Navigation",
        "keywords": ["down", "behind", "reverse", "south", "backwards", "arrow", "direction"],
        "paths": '<path d="M12 21.5l-7-7h4.5V2.5h5v12H19z" fill="currentColor"/>'
    },
    {
        "id": "wf-arrow-left",
        "name": "Left",
        "category": "Navigation",
        "keywords": ["left", "west", "turn left", "arrow", "direction"],
        "paths": '<path d="M2.5 12l7 7v-4.5h12v-5h-12V5z" fill="currentColor"/>'
    },
    {
        "id": "wf-arrow-up-right",
        "name": "Ahead right",
        "category": "Navigation",
        "keywords": ["ahead right", "diagonal right", "bear right", "northeast", "arrow"],
        "paths": '<path d="M7 3.5h13.5V17l-4.2-4.2-9 9-2.8-2.8 9-9z" fill="currentColor"/>'
    },
    {
        "id": "wf-arrow-up-left",
        "name": "Ahead left",
        "category": "Navigation",
        "keywords": ["ahead left", "diagonal left", "bear left", "northwest", "arrow"],
        "paths": '<path d="M17 3.5H3.5V17l4.2-4.2 9 9 2.8-2.8-9-9z" fill="currentColor"/>'
    },
    {
        "id": "wf-u-turn",
        "name": "Turn around",
        "category": "Navigation",
        "keywords": ["turn around", "u-turn", "reverse", "loop", "opposite direction"],
        "paths": '<path d="M9 18l-5-5h3.5A7.5 7.5 0 0 1 15 5.5a7.5 7.5 0 0 1 7.5 7.5v6h-4v-6a3.5 3.5 0 0 0-3.5-3.5A3.5 3.5 0 0 0 11.5 13H15z" fill="currentColor"/>'
    },
    {
        "id": "wf-signpost",
        "name": "Directions",
        "category": "Navigation",
        "keywords": ["directions", "signpost", "guide", "guidepost", "which way", "directory"],
        "paths": '<path d="M10.5 2h3v2h5.5l2 2.5-2 2.5H13.5v2H19a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1h-5.5v5h-3v-5H5a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1h5.5V9H5L3 6.5 5 4h5.5z" fill="currentColor"/>'
    },
    {
        "id": "wf-pin",
        "name": "You are here",
        "category": "Navigation",
        "keywords": ["you are here", "location", "marker", "pin", "current position", "destination"],
        "paths": '<path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z" fill="currentColor"/>'
    },
    {
        "id": "wf-facing",
        "name": "Facing this way",
        "category": "Navigation",
        "keywords": ["facing this way", "orientation", "bearing", "heading", "compass", "view angle"],
        "paths": '<circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2.5"/><polygon points="12 4 16 13 12 11 8 13 12 4" fill="currentColor"/><circle cx="12" cy="17" r="1.5" fill="currentColor"/>'
    },
    {
        "id": "wf-map",
        "name": "Map",
        "category": "Navigation",
        "keywords": ["map", "floor plan", "overview", "layout", "directory", "concourse"],
        "paths": '<path d="M3 6.2l5.7-2.3 6.6 2.6L21 4.2v13.6l-5.7 2.3-6.6-2.6L3 19.8V6.2zm7.2.3v10.9l3.6 1.4V7.9l-3.6-1.4z" fill="currentColor"/>'
    },
    {
        "id": "wf-touch",
        "name": "Touch here",
        "category": "Navigation",
        "keywords": ["touch here", "tap", "finger", "interact", "touchscreen", "press", "kiosk"],
        "paths": '<path d="M11 1.5a1.5 1.5 0 0 1 3 0V9.2a3 3 0 0 1 3.5 3v3.5a5.5 5.5 0 0 1-5.5 5.5H10a5.5 5.5 0 0 1-3.9-1.6l-3.5-3.5 1.5-1.5 2.9 1.7V1.5z" fill="currentColor"/><path d="M12.5 0a7 7 0 0 1 7 7h-2a5 5 0 0 0-5-5V0z" fill="currentColor"/>'
    },

    # Building
    {
        "id": "wf-entrance",
        "name": "Entrance",
        "category": "Building",
        "keywords": ["entrance", "enter", "entry", "door", "ingress", "main entrance", "doorway"],
        "paths": '<path d="M13 2h8a1 1 0 0 1 1 1v17a1 1 0 0 1-1 1h-8v-2h6V4h-6V2z" fill="currentColor"/><path d="m13 3-8 3v12l8 3V3z" fill="currentColor"/><circle cx="8" cy="12" r="1" fill="#fff"/><path d="M1 11h7v-3l4 4-4 4v-3H1z" fill="currentColor"/><rect x="1" y="21" width="22" height="2" rx="0.5" fill="currentColor"/>'
    },
    {
        "id": "wf-exit",
        "name": "Exit",
        "category": "Building",
        "keywords": ["exit", "egress", "way out", "door", "leave", "outdoor"],
        "paths": '<path d="M11 2H3a1 1 0 0 0-1 1v17a1 1 0 0 0 1 1h8v-2H5V4h6V2z" fill="currentColor"/><path d="m11 3 8 3v12l-8 3V3z" fill="currentColor"/><circle cx="16" cy="12" r="1" fill="#fff"/><path d="M15 11h4v-3l4 4-4 4v-3h-4z" fill="currentColor"/><rect x="1" y="21" width="22" height="2" rx="0.5" fill="currentColor"/>'
    },
    {
        "id": "wf-lift",
        "name": "Lift",
        "category": "Building",
        "keywords": ["lift", "elevator", "floors", "vertical", "accessible lift"],
        "paths": '<rect x="2" y="2" width="13" height="20" rx="3" fill="currentColor"/><circle cx="6" cy="7.5" r="1.5" fill="#fff"/><path d="M4 16v-3a2 2 0 0 1 4 0v3H4z" fill="#fff"/><circle cx="11" cy="7.5" r="1.5" fill="#fff"/><path d="M9 16v-3a2 2 0 0 1 4 0v3H9z" fill="#fff"/><polygon points="19.5 4 16 8.5 23 8.5" fill="currentColor"/><polygon points="19.5 20 16 15.5 23 15.5" fill="currentColor"/><rect x="18.5" y="10.5" width="2" height="3" rx="0.5" fill="currentColor"/>'
    },
    {
        "id": "wf-stairs",
        "name": "Stairs",
        "category": "Building",
        "keywords": ["stairs", "staircase", "steps", "walk up", "stairwell"],
        "paths": '<polygon points="4 20 20 20 20 6 16 6 16 10 12 10 12 14 8 14 8 18 4 18 4 20" fill="currentColor"/><circle cx="8" cy="5" r="2" fill="currentColor"/><path d="m11.5 10-2-2.5-2.5 1.5 1 2 2-1z" fill="currentColor"/>'
    },
    {
        "id": "wf-escalator-up",
        "name": "Escalator up",
        "category": "Building",
        "keywords": ["escalator up", "moving stairs", "up", "level up", "transit"],
        "paths": '<polygon points="3 8 8 8 15 18 21 18 21 20 14 20 7 10 3 10" fill="currentColor"/><polygon points="6 14 6 17 9 17 9 14" fill="currentColor"/><path d="M3 17l4-4 1.4 1.4-2.6 2.6H9v2H3z" fill="currentColor"/><circle cx="7" cy="4" r="1.8" fill="currentColor"/><path d="m9 9.5-2-2.5-2 1.5.8 1.8 1.7-.8z" fill="currentColor"/>'
    },
    {
        "id": "wf-escalator-down",
        "name": "Escalator down",
        "category": "Building",
        "keywords": ["escalator down", "moving stairs", "down", "level down", "transit"],
        "paths": '<polygon points="3 18 8 18 15 8 21 8 21 6 14 6 7 16 3 16" fill="currentColor"/><path d="M19 14l-4 4-1.4-1.4 2.6-2.6H13v-2h6z" fill="currentColor"/><circle cx="17" cy="4" r="1.8" fill="currentColor"/><path d="m15 9.5 2-2.5 2 1.5-.8 1.8-1.7-.8z" fill="currentColor"/>'
    },
    {
        "id": "wf-ramp",
        "name": "Ramp",
        "category": "Building",
        "keywords": ["ramp", "incline", "slope", "accessible route", "step free"],
        "paths": '<polygon points="2 20 22 20 22 10 2 20" fill="currentColor"/><circle cx="14" cy="5.5" r="1.8" fill="currentColor"/><path d="M11.5 13a2.8 2.8 0 1 1 3.5-3.3l1.8-1.8 1.4 1.4-2.4 2.4-1.5-.5a1.5 1.5 0 0 0-1.8 1.8z" fill="currentColor"/>'
    },
    {
        "id": "wf-accessible",
        "name": "Accessible",
        "category": "Building",
        "keywords": ["accessible", "wheelchair", "disabled", "disability", "step free", "accessibility"],
        "paths": '<circle cx="12" cy="4" r="2" fill="currentColor"/><path d="M10 8h4.5l1.6 5.5h2.9v2h-4.2l-1.3-4.5H11v3.5a4.5 4.5 0 1 1-5-4.4V8h4zm-1.5 6a2.5 2.5 0 1 0 2.5 2.5V14H8.5z" fill="currentColor"/>'
    },
    {
        "id": "wf-levels",
        "name": "Levels",
        "category": "Building",
        "keywords": ["levels", "floors", "stories", "multi-level", "stack", "building layout"],
        "paths": '<polygon points="12 2 21 6.5 12 11 3 6.5" fill="currentColor"/><polygon points="12 7.5 21 12 12 16.5 3 12" fill="currentColor"/><polygon points="12 13 21 17.5 12 22 3 17.5" fill="currentColor"/>'
    },
    {
        "id": "wf-no-entry",
        "name": "No entry",
        "category": "Building",
        "keywords": ["no entry", "do not enter", "restricted", "stop", "forbidden", "closed"],
        "paths": '<path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm6 11.5H6v-3h12v3z" fill="currentColor"/>'
    },
    {
        "id": "wf-prohibited",
        "name": "Not permitted",
        "category": "Building",
        "keywords": ["not permitted", "prohibited", "banned", "forbidden", "slash", "restriction"],
        "paths": '<path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 2a7.95 7.95 0 0 1 5.36 2.06L6.06 17.36A8 8 0 0 1 12 4zm0 16a7.95 7.95 0 0 1-5.36-2.06L17.94 6.64A8 8 0 0 1 12 20z" fill="currentColor"/>'
    },
    {
        "id": "wf-staff-only",
        "name": "Staff only",
        "category": "Building",
        "keywords": ["staff only", "employees", "authorized personnel", "restricted access", "badge", "id"],
        "paths": '<rect x="4" y="7" width="16" height="15" rx="3" fill="currentColor"/><path d="M9 7V4a3 3 0 0 1 6 0v3h-2V4a1 1 0 0 0-2 0v3H9z" fill="currentColor"/><circle cx="12" cy="12" r="2" fill="#fff"/><path d="M9 19c0-1.7 1.3-3 3-3s3 1.3 3 3H9z" fill="#fff"/>'
    },

    # Amenities
    {
        "id": "wf-toilets",
        "name": "Toilets",
        "category": "Amenities",
        "keywords": ["toilets", "restroom", "wc", "washroom", "bathroom", "amenities"],
        "paths": '<circle cx="7" cy="4" r="1.8" fill="currentColor"/><path d="M4.5 8h5a1 1 0 0 1 1 1v6h-2v5H6.5v-5h-2V9a1 1 0 0 1 1-1z" fill="currentColor"/><circle cx="17" cy="4" r="1.8" fill="currentColor"/><path d="M14.5 8h5l2.2 7h-3.2v5h-2v-5h-3.2l2.2-7z" fill="currentColor"/><line x1="12" y1="3" x2="12" y2="21" stroke="currentColor" stroke-width="1.5"/>'
    },
    {
        "id": "wf-toilet-male",
        "name": "Male toilet",
        "category": "Amenities",
        "keywords": ["male toilet", "men", "gents", "male restroom", "man"],
        "paths": '<circle cx="12" cy="4" r="2.2" fill="currentColor"/><path d="M8.5 8.5h7a1.5 1.5 0 0 1 1.5 1.5V16h-2.5v5.5h-5V16H7v-6a1.5 1.5 0 0 1 1.5-1.5z" fill="currentColor"/>'
    },
    {
        "id": "wf-toilet-female",
        "name": "Female toilet",
        "category": "Amenities",
        "keywords": ["female toilet", "women", "ladies", "female restroom", "woman"],
        "paths": '<circle cx="12" cy="4" r="2.2" fill="currentColor"/><path d="M9 8.5h6l3 8.5h-4.5v4.5h-3V17H6l3-8.5z" fill="currentColor"/>'
    },
    {
        "id": "wf-toilet-accessible",
        "name": "Accessible toilet",
        "category": "Amenities",
        "keywords": ["accessible toilet", "wheelchair toilet", "disabled wc", "accessible bathroom"],
        "paths": '<circle cx="9" cy="4.5" r="1.8" fill="currentColor"/><path d="M7 8h4.5l1.6 5h2.9v1.8h-4.2l-1.3-4H8.5v3a4 4 0 1 1-4.5-3.9V8H7z" fill="currentColor"/><rect x="17" y="5" width="4" height="15" rx="1" fill="currentColor"/><rect x="15" y="14" width="4" height="2" fill="currentColor"/>'
    },
    {
        "id": "wf-baby-change",
        "name": "Baby change",
        "category": "Amenities",
        "keywords": ["baby change", "parents room", "nappy change", "infant care", "baby care"],
        "paths": '<rect x="2" y="17" width="20" height="2.5" rx="1" fill="currentColor"/><circle cx="6.5" cy="8.5" r="2.2" fill="currentColor"/><path d="M9.5 13a4 4 0 0 0 4-2.5 3.5 3.5 0 0 1 5 1.5v3H9.5z" fill="currentColor"/><path d="M12 4v4m-2-2h4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>'
    },
    {
        "id": "wf-cafe",
        "name": "Café",
        "category": "Amenities",
        "keywords": ["cafe", "coffee", "tea", "espresso", "beverage", "drinks", "cafeteria"],
        "paths": '<path d="M18 7h1a4 4 0 0 1 0 8h-1v-8zm2 6a2 2 0 0 0 0-4v4z" fill="currentColor"/><path d="M2 7h15v7a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V7zm0 12h17a1 1 0 0 1 0 2H2a1 1 0 0 1 0-2z" fill="currentColor"/><path d="M5 2v3m4-3v3m4-3v3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>'
    },
    {
        "id": "wf-food",
        "name": "Food",
        "category": "Amenities",
        "keywords": ["food", "dining", "restaurant", "food court", "cutlery", "eat", "meal"],
        "paths": '<path d="M18 2v20h2V2h-2zm-12 0v7a2 2 0 0 1-2 2v11h2V11a2 2 0 0 1-2-2V2h2zm4 0v7a2 2 0 0 1-2 2v11h2V11a2 2 0 0 0 2-2V2h-2z" fill="currentColor"/>'
    },
    {
        "id": "wf-retail",
        "name": "Retail",
        "category": "Amenities",
        "keywords": ["retail", "shopping", "store", "shop", "boutique", "mall", "bag"],
        "paths": '<path d="M6 7V5a6 6 0 0 1 12 0v2h3a1 1 0 0 1 1 1l-1.5 13A2 2 0 0 1 18.5 22H5.5a2 2 0 0 1-2-1.8L2 8a1 1 0 0 1 1-1h3zm2 0h8V5a4 4 0 0 0-8 0v2z" fill="currentColor"/>'
    },
    {
        "id": "wf-atm",
        "name": "ATM",
        "category": "Amenities",
        "keywords": ["atm", "cash machine", "cashpoint", "money", "withdraw", "bank"],
        "paths": '<rect x="3" y="3" width="18" height="18" rx="3" fill="currentColor"/><rect x="6" y="6" width="12" height="3" rx="0.5" fill="#fff"/><rect x="6" y="11" width="6" height="2" fill="#fff"/><rect x="14" y="11" width="4" height="6" rx="1" fill="#fff"/>'
    },
    {
        "id": "wf-payment",
        "name": "Cashier / pay",
        "category": "Amenities",
        "keywords": ["cashier", "pay", "payment", "card", "checkout", "credit card", "pos"],
        "paths": '<rect x="2" y="4" width="20" height="16" rx="3" fill="currentColor"/><rect x="2" y="8" width="20" height="3.5" fill="#fff"/><circle cx="7" cy="15.5" r="1.8" fill="#fff"/><circle cx="11.5" cy="15.5" r="1.8" fill="#fff"/>'
    },
    {
        "id": "wf-pharmacy",
        "name": "Pharmacy",
        "category": "Amenities",
        "keywords": ["pharmacy", "chemist", "dispensary", "prescription", "medicine", "drugs"],
        "paths": '<rect x="2" y="2" width="20" height="20" rx="4" fill="currentColor"/><path d="M10 6h4v4h4v4h-4v4h-4v-4H6v-4h4V6z" fill="#fff"/>'
    },
    {
        "id": "wf-water",
        "name": "Drinking water",
        "category": "Amenities",
        "keywords": ["drinking water", "water fountain", "refill", "hydration", "tap", "bottle refill"],
        "paths": '<path d="M12 2.5C12 2.5 5 10.5 5 15.5a7 7 0 0 0 14 0c0-5-7-13-7-13zm0 16a4.5 4.5 0 0 1-4.5-4.5c0-.6.4-1 1-1s1 .4 1 1A2.5 2.5 0 0 0 12 16.5c.6 0 1 .4 1 1s-.4 1-1 1z" fill="currentColor"/>'
    },
    {
        "id": "wf-wifi",
        "name": "Free Wi-Fi",
        "category": "Amenities",
        "keywords": ["wifi", "free wifi", "internet", "wireless", "network", "hotspot"],
        "paths": '<path d="M12 4a14.8 14.8 0 0 1 9.9 3.9l-2.1 2.1A11.8 11.8 0 0 0 12 7c-3 0-5.8 1.1-7.8 3L2.1 7.9A14.8 14.8 0 0 1 12 4zm0 6a8.8 8.8 0 0 1 5.8 2.2l-2.1 2.1A5.8 5.8 0 0 0 12 13c-1.4 0-2.8.5-3.7 1.3L6.2 12.2A8.8 8.8 0 0 1 12 10zm0 6a3 3 0 0 1 2 1l-2 2-2-2a3 3 0 0 1 2-1z" fill="currentColor"/>'
    },
    {
        "id": "wf-seating",
        "name": "Waiting area",
        "category": "Amenities",
        "keywords": ["waiting area", "seating", "lounge", "rest", "chairs", "waiting room"],
        "paths": '<path d="M4 5a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v9h-2V5H6v9H4V5zm-2 9h20a1 1 0 0 1 1 1v4a2 2 0 0 1-2 2h-1v-2H4v2H2a2 2 0 0 1-2-2v-4a1 1 0 0 1 1-1z" fill="currentColor"/>'
    },

    # Transit
    {
        "id": "wf-parking",
        "name": "Car park",
        "category": "Transit",
        "keywords": ["car park", "parking", "garage", "p", "vehicle parking", "bays"],
        "paths": '<rect x="3" y="3" width="18" height="18" rx="4" fill="currentColor"/><path d="M9 17V7h4.5a3.5 3.5 0 0 1 0 7H11v3H9zm2-5h2.5a1.5 1.5 0 0 0 0-3H11v3z" fill="#fff"/>'
    },
    {
        "id": "wf-car",
        "name": "Drop-off",
        "category": "Transit",
        "keywords": ["drop-off", "pick-up", "car", "taxi", "passenger", "vehicle", "rideshare"],
        "paths": '<path d="M18.9 6.8A2 2 0 0 0 17.3 6H6.7a2 2 0 0 0-1.6.8L3 11v8a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-1h12v1a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-8l-2.1-4.2zM7.5 15a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm9 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zM6 10l1.3-3h9.4l1.3 3H6z" fill="currentColor"/>'
    },
    {
        "id": "wf-bus",
        "name": "Bus / shuttle",
        "category": "Transit",
        "keywords": ["bus", "shuttle", "coach", "public transport", "transit", "stop"],
        "paths": '<rect x="4" y="3" width="16" height="16" rx="3" fill="currentColor"/><rect x="6" y="6" width="12" height="4.5" rx="1" fill="#fff"/><circle cx="8" cy="14" r="1.5" fill="#fff"/><circle cx="16" cy="14" r="1.5" fill="#fff"/><rect x="5.5" y="19" width="3" height="3" rx="0.5" fill="currentColor"/><rect x="15.5" y="19" width="3" height="3" rx="0.5" fill="currentColor"/>'
    },
    {
        "id": "wf-ev",
        "name": "EV charging",
        "category": "Transit",
        "keywords": ["ev charging", "electric vehicle", "charger", "plug", "clean energy"],
        "paths": '<rect x="2" y="4" width="13" height="17" rx="3" fill="currentColor"/><path d="M8 8l-2 4h3l-1 4 4-5h-3l2-3H8z" fill="#fff"/><path d="M15 9h2a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2h-1v-2h1v-4h-2V9zm4 1v2h2v-2h-2z" fill="currentColor"/>'
    },

    # Services
    {
        "id": "wf-info",
        "name": "Information",
        "category": "Services",
        "keywords": ["information", "info", "help desk", "inquiries", "directory", "about"],
        "paths": '<circle cx="12" cy="12" r="10" fill="currentColor"/><circle cx="12" cy="7.5" r="1.5" fill="#fff"/><path d="M10.5 11h3v6h-3z" fill="#fff"/>'
    },
    {
        "id": "wf-help",
        "name": "Help",
        "category": "Services",
        "keywords": ["help", "assistance", "support", "question", "faq"],
        "paths": '<circle cx="12" cy="12" r="10" fill="currentColor"/><path d="M9.5 9a2.5 2.5 0 0 1 4.9.8c0 1.5-2.4 2-2.4 3.7h-2c0-2.3 2.5-2.8 2.5-3.7a.7.7 0 0 0-.7-.7.9.9 0 0 0-.9.9H9.5z" fill="#fff"/><circle cx="11" cy="16.5" r="1.2" fill="#fff"/>'
    },
    {
        "id": "wf-reception",
        "name": "Reception",
        "category": "Services",
        "keywords": ["reception", "front desk", "concierge", "check-in", "counter", "lobby"],
        "paths": '<rect x="2" y="15" width="20" height="6" rx="1.5" fill="currentColor"/><circle cx="12" cy="6" r="2.5" fill="currentColor"/><path d="M7 15v-1a5 5 0 0 1 10 0v1H7z" fill="currentColor"/>'
    },
    {
        "id": "wf-security",
        "name": "Security",
        "category": "Services",
        "keywords": ["security", "guard", "protection", "safe", "shield", "patrol"],
        "paths": '<path d="M12 2s8 3 8 9c0 6.5-6 10.5-8 11-2-.5-8-4.5-8-11 0-6 8-9 8-9zm-1 13l5-5-1.4-1.4-3.6 3.6-1.6-1.6L8 12l3 3z" fill="currentColor"/>'
    },
    {
        "id": "wf-phone",
        "name": "Phone",
        "category": "Services",
        "keywords": ["phone", "telephone", "call", "public phone", "contact"],
        "paths": '<path d="M20 15.5c-1.2 0-2.4-.2-3.6-.6-.4-.1-.8 0-1.1.3l-2.2 2.2a15 15 0 0 1-6.6-6.6l2.2-2.2c.3-.3.4-.7.2-1.1-.4-1.1-.6-2.3-.6-3.5 0-.6-.4-1-1-1H4c-.6 0-1 .4-1 1 0 9.4 7.6 17 17 17 .6 0 1-.4 1-1v-3.5c0-.6-.4-1-1-1z" fill="currentColor"/>'
    },
    {
        "id": "wf-intercom",
        "name": "Help point",
        "category": "Services",
        "keywords": ["help point", "intercom", "call button", "emergency intercom", "pillar", "speaker"],
        "paths": '<rect x="5" y="2" width="14" height="20" rx="3" fill="currentColor"/><circle cx="12" cy="7.5" r="2.5" fill="#fff"/><rect x="8" y="12" width="8" height="1.8" rx="0.5" fill="#fff"/><circle cx="12" cy="17" r="1.8" fill="#fff"/>'
    },

    # Healthcare
    {
        "id": "wf-hospital",
        "name": "Hospital",
        "category": "Healthcare",
        "keywords": ["hospital", "clinic", "medical center", "infirmary", "health", "ward"],
        "paths": '<rect x="3" y="3" width="18" height="19" rx="3" fill="currentColor"/><path d="M10 7h4v3h3v4h-3v3h-4v-3H7v-4h3V7z" fill="#fff"/>'
    },
    {
        "id": "wf-first-aid",
        "name": "First aid",
        "category": "Healthcare",
        "keywords": ["first aid", "emergency care", "medical kit", "cross", "treatment"],
        "paths": '<rect x="2" y="6" width="20" height="15" rx="3" fill="currentColor"/><path d="M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2h-2V4h-4v2H8zm2 4h4v3h3v4h-3v3h-4v-3H7v-4h3v-3z" fill="#fff"/>'
    },
    {
        "id": "wf-consult",
        "name": "Consulting / GP",
        "category": "Healthcare",
        "keywords": ["consulting", "gp", "doctor", "physician", "clinic", "stethoscope", "appointment"],
        "paths": '<path d="M6 3v6a6 6 0 0 0 12 0V3h-2v6a4 4 0 0 1-8 0V3H6zm6 12a3 3 0 0 0-3 3v2a3 3 0 0 0 6 0v-2a3 3 0 0 0-3-3zm6 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4z" fill="currentColor"/>'
    },
    {
        "id": "wf-pathology",
        "name": "Pathology",
        "category": "Healthcare",
        "keywords": ["pathology", "lab", "laboratory", "blood test", "specimen", "microscope"],
        "paths": '<path d="M9 2h6v2h-1v5.5l5.2 9.4A2 2 0 0 1 17.5 22H6.5a2 2 0 0 1-1.7-3.1L10 9.5V4H9V2zm2 9.5l-4 7.2a.5.5 0 0 0 .4.8h9.2a.5.5 0 0 0 .4-.8l-4-7.2h-2z" fill="currentColor"/>'
    },
    {
        "id": "wf-aed",
        "name": "Defibrillator",
        "category": "Healthcare",
        "keywords": ["defibrillator", "aed", "cardiac", "resuscitation", "heart", "shock", "emergency"],
        "paths": '<path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" fill="currentColor"/><polygon points="12.5 6 9.5 12 13 12 11.5 17 15.5 11 12 11 12.5 6" fill="#fff"/>'
    },

    # Campus
    {
        "id": "wf-student",
        "name": "Student hub",
        "category": "Campus",
        "keywords": ["student hub", "student services", "campus center", "union", "graduation cap", "alumni"],
        "paths": '<polygon points="12 2 22 7.5 12 13 2 7.5" fill="currentColor"/><path d="M6 10.5v5.5c0 2.2 2.7 4 6 4s6-1.8 6-4v-5.5l-6 3.3-6-3.3zm16-3v6h-2v-5l2-1z" fill="currentColor"/>'
    },
    {
        "id": "wf-library",
        "name": "Library",
        "category": "Campus",
        "keywords": ["library", "books", "study", "reading", "learning", "quiet zone"],
        "paths": '<path d="M4 3a2 2 0 0 1 2-2h13a1 1 0 0 1 1 1v20a1 1 0 0 1-1 1H6a2 2 0 0 1-2-2V3zm3 0v17h11V3H7zm2 4h7v2H9V7zm0 4h5v2H9v-2z" fill="currentColor"/>'
    },
    {
        "id": "wf-lecture",
        "name": "Lecture room",
        "category": "Campus",
        "keywords": ["lecture room", "theatre", "auditorium", "classroom", "presentation", "seminar"],
        "paths": '<rect x="2" y="3" width="20" height="13" rx="2" fill="currentColor"/><circle cx="12" cy="8" r="2" fill="#fff"/><polygon points="9 16 7 21 9 21 10.5 16" fill="currentColor"/><polygon points="15 16 17 21 15 21 13.5 16" fill="currentColor"/><rect x="8" y="15" width="8" height="2" rx="0.5" fill="currentColor"/>'
    },

    # Safety
    {
        "id": "wf-emergency",
        "name": "Emergency",
        "category": "Safety",
        "keywords": ["emergency", "alarm", "alert", "danger", "urgent", "critical"],
        "paths": '<polygon points="12 2 22 7.8 22 16.2 12 22 2 16.2 2 7.8" fill="currentColor"/><rect x="11" y="7" width="2" height="6" rx="0.5" fill="#fff"/><circle cx="12" cy="16" r="1.2" fill="#fff"/>'
    },
    {
        "id": "wf-evacuate",
        "name": "Emergency exit",
        "category": "Safety",
        "keywords": ["emergency exit", "evacuate", "escape", "running man", "fire exit", "safety"],
        "paths": '<rect x="16" y="2" width="6" height="20" rx="1" fill="currentColor"/><circle cx="8" cy="5.5" r="1.8" fill="currentColor"/><path d="M5 10l3.5-2 3.5 2.5v4h-2v-3l-2-1.5-3 5-1.5-1 2.5-4z" fill="currentColor"/><path d="m8 14 3 6-1.7 1-3.3-6.5L8 14z" fill="currentColor"/>'
    },
    {
        "id": "wf-assembly",
        "name": "Assembly point",
        "category": "Safety",
        "keywords": ["assembly point", "muster point", "meeting point", "evacuation assembly", "safe area"],
        "paths": '<circle cx="12" cy="12" r="3" fill="currentColor"/><polygon points="3 3 8 3 8 5 5.5 5 9 8.5 7.5 10 4 6.5 4 9 2 9 2 3" fill="currentColor"/><polygon points="21 3 21 9 19 9 19 6.5 15.5 10 14 8.5 17.5 5 15 5 15 3" fill="currentColor"/><polygon points="3 21 3 15 5 15 5 17.5 8.5 14 10 15.5 6.5 19 9 19 9 21" fill="currentColor"/><polygon points="21 21 15 21 15 19 17.5 19 14 15.5 15.5 14 19 17.5 19 15 21 15" fill="currentColor"/>'
    },
    {
        "id": "wf-fire",
        "name": "Fire",
        "category": "Safety",
        "keywords": ["fire", "flame", "hose", "hydrant", "extinguisher", "fire safety"],
        "paths": '<path d="M12 2c1.2 3.5 4.5 5.5 4.5 10a6.5 6.5 0 0 1-13 0c0-4 2.5-7 4.5-9 1 2 2.5 3 4-1z" fill="currentColor"/><path d="M12 13.5c1.2 0 2 1 2 2a2 2 0 0 1-4 0c0-1 .8-2 2-2z" fill="#fff"/>'
    },
    {
        "id": "wf-warning",
        "name": "Caution",
        "category": "Safety",
        "keywords": ["caution", "warning", "hazard", "attention", "careful", "notice"],
        "paths": '<path d="M12 2L1 21h22L12 2zm-1 7h2v6h-2V9zm1 10a1.2 1.2 0 1 1 0-2.4 1.2 1.2 0 0 1 0 2.4z" fill="currentColor"/>'
    },
    {
        "id": "wf-construction",
        "name": "Under construction",
        "category": "Safety",
        "keywords": ["under construction", "work in progress", "maintenance", "cone", "barrier", "renovation"],
        "paths": '<polygon points="12 2 18 19 6 19" fill="currentColor"/><rect x="2" y="20" width="20" height="2.5" rx="0.5" fill="currentColor"/><polygon points="10 8 14 8 15 12 9 12" fill="#fff"/><polygon points="8.5 14 15.5 14 16.5 17 7.5 17" fill="#fff"/>'
    },

    # UI
    {
        "id": "wf-home",
        "name": "Home",
        "category": "UI",
        "keywords": ["home", "main screen", "start", "homepage", "welcome"],
        "paths": '<polygon points="12 2 2 10 4 10 4 21 10 21 10 14 14 14 14 21 20 21 20 10 22 10" fill="currentColor"/>'
    },
    {
        "id": "wf-search",
        "name": "Search",
        "category": "UI",
        "keywords": ["search", "find", "lookup", "explore", "magnifier", "query"],
        "paths": '<path d="M15.5 14h-.8l-.3-.3a6.5 6.5 0 1 0-.7.7l.3.3v.8l5 5 1.5-1.5-5-5zm-6 0C7 14 5 12 5 9.5S7 5 9.5 5 14 7 14 9.5 12 14 9.5 14z" fill="currentColor"/>'
    },
    {
        "id": "wf-menu",
        "name": "Menu",
        "category": "UI",
        "keywords": ["menu", "hamburger", "navigation", "options", "list"],
        "paths": '<rect x="3" y="5" width="18" height="3" rx="1.5" fill="currentColor"/><rect x="3" y="11" width="18" height="3" rx="1.5" fill="currentColor"/><rect x="3" y="17" width="18" height="3" rx="1.5" fill="currentColor"/>'
    },
    {
        "id": "wf-back",
        "name": "Back",
        "category": "UI",
        "keywords": ["back", "previous", "return", "left arrow", "undo"],
        "paths": '<path d="M15.5 19l-7-7 7-7 1.8 1.8L12 12l5.3 5.2z" fill="currentColor"/>'
    },
    {
        "id": "wf-close",
        "name": "Close",
        "category": "UI",
        "keywords": ["close", "dismiss", "exit modal", "cancel", "x"],
        "paths": '<path d="M19 6.4L17.6 5 12 10.6 6.4 5 5 6.4l5.6 5.6L5 17.6 6.4 19l5.6-5.6 5.6 5.6 1.4-1.4-5.6-5.6z" fill="currentColor"/>'
    },
    {
        "id": "wf-hours",
        "name": "Opening hours",
        "category": "UI",
        "keywords": ["opening hours", "trading hours", "times", "clock", "schedule", "open"],
        "paths": '<circle cx="12" cy="12" r="10" fill="currentColor"/><path d="M11 6h2v5.5l3.5 2-1 1.7-4.5-2.7V6z" fill="#fff"/>'
    },
    {
        "id": "wf-timetable",
        "name": "Timetable",
        "category": "UI",
        "keywords": ["timetable", "schedule", "departures", "timesheet", "planner", "calendar"],
        "paths": '<rect x="3" y="4" width="18" height="17" rx="3" fill="currentColor"/><rect x="6" y="2" width="2" height="4" rx="0.5" fill="currentColor"/><rect x="16" y="2" width="2" height="4" rx="0.5" fill="currentColor"/><rect x="5" y="8" width="14" height="2" fill="#fff"/><rect x="6" y="12" width="12" height="1.8" fill="#fff"/><rect x="6" y="16" width="8" height="1.8" fill="#fff"/>'
    },
    {
        "id": "wf-events",
        "name": "Events",
        "category": "UI",
        "keywords": ["events", "what's on", "calendar", "activities", "happenings", "starred"],
        "paths": '<rect x="3" y="4" width="18" height="17" rx="3" fill="currentColor"/><rect x="6" y="2" width="2" height="4" rx="0.5" fill="currentColor"/><rect x="16" y="2" width="2" height="4" rx="0.5" fill="currentColor"/><rect x="5" y="8" width="14" height="2" fill="#fff"/><polygon points="12 11 13.2 13.5 16 13.9 14 15.8 14.5 18.5 12 17.2 9.5 18.5 10 15.8 8 13.9 10.8 13.5" fill="#fff"/>'
    },
    {
        "id": "wf-news",
        "name": "News",
        "category": "UI",
        "keywords": ["news", "updates", "newspaper", "bulletin", "articles", "press"],
        "paths": '<rect x="2" y="3" width="20" height="18" rx="2" fill="currentColor"/><rect x="5" y="6" width="7" height="2" fill="#fff"/><rect x="5" y="10" width="14" height="1.8" fill="#fff"/><rect x="5" y="13.5" width="14" height="1.8" fill="#fff"/><rect x="5" y="17" width="9" height="1.8" fill="#fff"/>'
    },
    {
        "id": "wf-announce",
        "name": "Announcements",
        "category": "UI",
        "keywords": ["announcements", "broadcast", "megaphone", "bullhorn", "notices", "alerts"],
        "paths": '<path d="M18 4l-9 4H4a1 1 0 0 0-1 1v6a1 1 0 0 0 1 1h5l9 4V4zm-9 15v3a2 2 0 0 1-2 2H5v-2h2a1 1 0 0 0 1-1v-2h1zm11.5-8.5a4 4 0 0 1 0 5v2a6 6 0 0 0 0-9v2z" fill="currentColor"/>'
    },

    # Media
    {
        "id": "wf-share",
        "name": "Share / social",
        "category": "Media",
        "keywords": ["share", "social", "send", "connect", "forward", "nodes"],
        "paths": '<path d="M18 16a3 3 0 0 0-2.4 1.2L8.9 13.7a3.3 3.3 0 0 0 0-3.4l6.7-3.5A3 3 0 1 0 15 5a3 3 0 0 0 .1.7L8.4 9.2a3 3 0 1 0 0 5.6l6.7 3.5c0 .2-.1.5-.1.7a3 3 0 1 0 3-3z" fill="currentColor"/>'
    },
    {
        "id": "wf-chat",
        "name": "Chat",
        "category": "Media",
        "keywords": ["chat", "message", "conversation", "talk", "feedback", "bubble"],
        "paths": '<path d="M20 2H4a2 2 0 0 0-2 2v18l4-4h14a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2z" fill="currentColor"/><circle cx="7" cy="10" r="1.5" fill="#fff"/><circle cx="12" cy="10" r="1.5" fill="#fff"/><circle cx="17" cy="10" r="1.5" fill="#fff"/>'
    },
    {
        "id": "wf-like",
        "name": "Like / feedback",
        "category": "Media",
        "keywords": ["like", "feedback", "thumbs up", "satisfaction", "survey", "rate", "positive"],
        "paths": '<path d="M1 21h4V9H1v12zm22-11a2 2 0 0 0-2-2h-6.3l1-4.6v-.3a1.5 1.5 0 0 0-.4-1.1L14.2 1 7.6 7.6A2 2 0 0 0 7 9v10a2 2 0 0 0 2 2h9c.8 0 1.5-.5 1.8-1.2l3-7.1c.1-.2.2-.5.2-.7v-2z" fill="currentColor"/>'
    },
    {
        "id": "wf-camera",
        "name": "Photos",
        "category": "Media",
        "keywords": ["photos", "camera", "pictures", "images", "snapshots", "photography"],
        "paths": '<path d="M20 4h-3.2L15 2H9L7.2 4H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm-8 14a5 5 0 1 1 0-10 5 5 0 0 1 0 10zm0-8a3 3 0 1 0 0 6 3 3 0 0 0 0-6z" fill="currentColor"/>'
    },
    {
        "id": "wf-video",
        "name": "Video",
        "category": "Media",
        "keywords": ["video", "camcorder", "record", "clip", "stream", "film"],
        "paths": '<rect x="2" y="5" width="14" height="14" rx="3" fill="currentColor"/><polygon points="18 8 23 4 23 20 18 16" fill="currentColor"/>'
    },
    {
        "id": "wf-qr",
        "name": "Scan QR",
        "category": "Media",
        "keywords": ["scan qr", "qr code", "mobile scan", "barcode", "transfer to phone"],
        "paths": '<rect x="2" y="2" width="8" height="8" rx="1.5" fill="currentColor"/><rect x="4" y="4" width="4" height="4" fill="#fff"/><rect x="5" y="5" width="2" height="2" fill="currentColor"/><rect x="14" y="2" width="8" height="8" rx="1.5" fill="currentColor"/><rect x="16" y="4" width="4" height="4" fill="#fff"/><rect x="17" y="5" width="2" height="2" fill="currentColor"/><rect x="2" y="14" width="8" height="8" rx="1.5" fill="currentColor"/><rect x="4" y="16" width="4" height="4" fill="#fff"/><rect x="5" y="17" width="2" height="2" fill="currentColor"/><rect x="14" y="14" width="3" height="3" fill="currentColor"/><rect x="19" y="14" width="3" height="3" fill="currentColor"/><rect x="14" y="19" width="8" height="3" fill="currentColor"/>'
    },
    {
        "id": "wf-email",
        "name": "Email",
        "category": "Media",
        "keywords": ["email", "mail", "envelope", "contact", "send to email", "newsletter"],
        "paths": '<path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" fill="currentColor"/>'
    },
    {
        "id": "wf-web",
        "name": "Website",
        "category": "Media",
        "keywords": ["website", "web", "internet", "browser", "url", "online", "portal"],
        "paths": '<circle cx="12" cy="12" r="10" fill="currentColor"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" fill="#fff"/><path d="M12 4a14 14 0 0 1 2 8 14 14 0 0 1-2 8 14 14 0 0 1-2-8 14 14 0 0 1 2-8z" fill="currentColor"/><line x1="2" y1="12" x2="22" y2="12" stroke="#fff" stroke-width="1.8"/>'
    }
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SVG_DIR = os.path.join(BASE_DIR, "svg")
SVG_LINE_DIR = os.path.join(SVG_DIR, "line")
SVG_SOLID_DIR = os.path.join(SVG_DIR, "solid")
DIST_DIR = os.path.join(BASE_DIR, "dist")

os.makedirs(SVG_LINE_DIR, exist_ok=True)
os.makedirs(SVG_SOLID_DIR, exist_ok=True)
os.makedirs(DIST_DIR, exist_ok=True)

def generate_line_svg(paths, icon_id):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-line {icon_id}">
  {paths}
</svg>'''

def generate_solid_svg(paths, icon_id):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="wf-icon wf-icon-solid {icon_id}">
  {paths}
</svg>'''

def main():
    print(f"Total icons configured per set: {len(ICONS_LINE)} Line, {len(ICONS_SOLID)} Solid")
    
    # 1. Generate individual Line SVGs (in svg/line/ and backward-compatible svg/)
    for icon in ICONS_LINE:
        svg_content = generate_line_svg(icon["paths"], icon["id"])
        with open(os.path.join(SVG_LINE_DIR, f"{icon['id']}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_content)
        with open(os.path.join(SVG_DIR, f"{icon['id']}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_content)
            
    # 2. Generate individual Solid SVGs (in svg/solid/)
    for icon in ICONS_SOLID:
        svg_content = generate_solid_svg(icon["paths"], icon["id"])
        with open(os.path.join(SVG_SOLID_DIR, f"{icon['id']}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_content)
            
    print(f"Generated SVGs in {SVG_LINE_DIR} and {SVG_SOLID_DIR}")

    # 3. Generate SVG Sprite Sheets
    # Line Sprite Sheet
    symbols_line = [f'  <symbol id="{i["id"]}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n    {i["paths"]}\n  </symbol>' for i in ICONS_LINE]
    sprite_line_path = os.path.join(DIST_DIR, "wayfinding-icons-line.svg")
    with open(sprite_line_path, "w", encoding="utf-8") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" style="display: none;">\n' + "\n".join(symbols_line) + '\n</svg>')

    # Solid Sprite Sheet
    symbols_solid = [f'  <symbol id="{i["id"]}" viewBox="0 0 24 24" fill="currentColor">\n    {i["paths"]}\n  </symbol>' for i in ICONS_SOLID]
    sprite_solid_path = os.path.join(DIST_DIR, "wayfinding-icons-solid.svg")
    with open(sprite_solid_path, "w", encoding="utf-8") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" style="display: none;">\n' + "\n".join(symbols_solid) + '\n</svg>')

    # Combined Sprite Sheet
    symbols_combined = symbols_line + [f'  <symbol id="{i["id"]}-solid" viewBox="0 0 24 24" fill="currentColor">\n    {i["paths"]}\n  </symbol>' for i in ICONS_SOLID]
    sprite_combined_path = os.path.join(DIST_DIR, "wayfinding-icons.svg")
    with open(sprite_combined_path, "w", encoding="utf-8") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" style="display: none;">\n' + "\n".join(symbols_combined) + '\n</svg>')

    # 4. Generate JSON metadata with both sets
    solid_map = {i["id"]: i["paths"] for i in ICONS_SOLID}
    combined_metadata = []
    for icon in ICONS_LINE:
        combined_metadata.append({
            "id": icon["id"],
            "name": icon["name"],
            "category": icon["category"],
            "keywords": icon["keywords"],
            "paths_line": icon["paths"],
            "paths_solid": solid_map.get(icon["id"], "")
        })
    json_path = os.path.join(DIST_DIR, "wayfinding-icons.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(combined_metadata, f, indent=2)

    # 5. Generate CSS stylesheet
    css_content = """/* Wayfinding Kiosk Icon Library CSS */
:root {
  --wf-icon-size: 24px;
  --wf-icon-stroke: 2px;
  --wf-icon-color: currentColor;
}

.wf-icon {
  display: inline-block;
  width: var(--wf-icon-size);
  height: var(--wf-icon-size);
  vertical-align: middle;
  flex-shrink: 0;
}

.wf-icon-line {
  stroke-width: var(--wf-icon-stroke);
  stroke: var(--wf-icon-color);
  fill: none;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.wf-icon-solid {
  fill: var(--wf-icon-color);
  stroke: none;
}

/* Preset Sizes for Kiosk Touch Interfaces */
.wf-icon-xs { width: 16px; height: 16px; }
.wf-icon-sm { width: 20px; height: 20px; }
.wf-icon-md { width: 24px; height: 24px; }
.wf-icon-lg { width: 32px; height: 32px; }
.wf-icon-xl { width: 48px; height: 48px; }
.wf-icon-2xl { width: 64px; height: 64px; }
.wf-icon-3xl { width: 96px; height: 96px; }

/* Kiosk Wayfinding Color Presets */
.wf-color-primary { color: #0284c7; }
.wf-color-success { color: #10b981; }
.wf-color-warning { color: #f59e0b; }
.wf-color-danger { color: #ef4444; }
.wf-color-dark { color: #0f172a; }
.wf-color-light { color: #f8fafc; }
.wf-color-accent { color: #8b5cf6; }
"""
    css_path = os.path.join(DIST_DIR, "wayfinding-icons.css")
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css_content)

    # 6. Generate JS Helper & Web Component
    line_dict = {i["id"]: i["paths"] for i in ICONS_LINE}
    solid_dict = {i["id"]: i["paths"] for i in ICONS_SOLID}
    js_content = f"""/**
 * Wayfinding Kiosk Icon Library (JavaScript / Web Component)
 * Supports both 'line' and 'solid' sets
 */

export const WAYFINDING_LINE = {json.dumps(line_dict, indent=2)};
export const WAYFINDING_SOLID = {json.dumps(solid_dict, indent=2)};
export const WAYFINDING_METADATA = {json.dumps(combined_metadata, indent=2)};

/**
 * Returns raw SVG string for an icon ID
 */
export function getWayfindingSvg(iconId, {{ set = 'line', size = 24, strokeWidth = 2, className = '' }} = {{}}) {{
  const isSolid = set === 'solid';
  const dict = isSolid ? WAYFINDING_SOLID : WAYFINDING_LINE;
  const paths = dict[iconId];
  if (!paths) {{
    console.warn(`Wayfinding icon "${{iconId}}" not found in ${{set}} set`);
    return '';
  }}
  if (isSolid) {{
    return `<svg xmlns="http://www.w3.org/2000/svg" width="${{size}}" height="${{size}}" viewBox="0 0 24 24" fill="currentColor" class="wf-icon wf-icon-solid ${{iconId}} ${{className}}">${{paths}}</svg>`;
  }}
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${{size}}" height="${{size}}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${{strokeWidth}}" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-line ${{iconId}} ${{className}}">${{paths}}</svg>`;
}}

/**
 * Custom Web Component <wf-icon name="wf-pin" set="solid" size="32"></wf-icon>
 */
class WayfindingIconElement extends HTMLElement {{
  static get observedAttributes() {{
    return ['name', 'set', 'size', 'stroke-width', 'color'];
  }}

  connectedCallback() {{
    this.render();
  }}

  attributeChangedCallback() {{
    this.render();
  }}

  render() {{
    const name = this.getAttribute('name') || 'wf-pin';
    const set = this.getAttribute('set') || 'line';
    const size = this.getAttribute('size') || '24';
    const strokeWidth = this.getAttribute('stroke-width') || '2';
    const color = this.getAttribute('color');
    const isSolid = set === 'solid';
    const dict = isSolid ? WAYFINDING_SOLID : WAYFINDING_LINE;
    const paths = dict[name] || '';

    if (color) {{
      this.style.color = color;
    }}

    if (isSolid) {{
      this.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="${{size}}" height="${{size}}" viewBox="0 0 24 24" fill="currentColor" class="wf-icon wf-icon-solid ${{name}}">${{paths}}</svg>`;
    }} else {{
      this.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="${{size}}" height="${{size}}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${{strokeWidth}}" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-line ${{name}}">${{paths}}</svg>`;
    }}
  }}
}}

if (typeof window !== 'undefined' && !customElements.get('wf-icon')) {{
  customElements.define('wf-icon', WayfindingIconElement);
}}
"""
    js_path = os.path.join(DIST_DIR, "wayfinding-icons.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_content)

    # 7. Generate README.md
    readme_content = f"""# Wayfinding Kiosk Icon Library (Dual Design Sets)

A comprehensive suite of **160 icons** (80 **Modern Line** + 80 **Solid Signage**) crafted for **touchscreen wayfinding kiosks**, directional totems, overhead signage, airports, campuses, and hospitals.

## Design Sets
1. **Modern Line (Outline)**: Contemporary 2px stroke, airy, minimalist, ideal for software UI and high-density maps.
2. **Solid Signage (Filled Silhouette)**: Bold, high-contrast, ISO/AIGA-inspired silhouettes with maximum visibility across busy public environments.

---

## Icon Catalog (80 Unique Wayfinding Identifiers)

| Icon ID | Name | Category |
| :--- | :--- | :--- |
""" + "\n".join([f"| `{icon['id']}` | **{icon['name']}** | {icon['category']} |" for icon in ICONS_LINE]) + """

---

## Directory Structure
```
wayfinding-icons/
├── svg/
│   ├── line/                 # 80 Line SVGs
│   └── solid/                # 80 Solid SVGs
├── dist/
│   ├── wayfinding-icons-line.svg    # Sprite sheet (Line)
│   ├── wayfinding-icons-solid.svg   # Sprite sheet (Solid)
│   ├── wayfinding-icons.svg         # Combined sprite sheet
│   ├── wayfinding-icons.css         # Sizing, color & reset utilities
│   ├── wayfinding-icons.js          # JS helper & Web Component
│   ├── wayfinding-icons.json        # Unified metadata & search index
│   └── wayfinding-icons.zip         # Complete release archive (both sets)
├── index.html                       # Interactive Showcase with Design Set Dropdown
├── build_icons.py                   # Generator script
└── README.md                        # Documentation
```
"""
    readme_path = os.path.join(BASE_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)

    # 8. Generate Showcase HTML
    import update_showcase
    print("Generated Showcase HTML via update_showcase")

    # 9. Create ZIP Package with Both Sets
    zip_path = os.path.join(DIST_DIR, "wayfinding-icons.zip")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for icon in ICONS_LINE:
            zipf.write(os.path.join(SVG_LINE_DIR, f"{icon['id']}.svg"), arcname=f"svg/line/{icon['id']}.svg")
        for icon in ICONS_SOLID:
            zipf.write(os.path.join(SVG_SOLID_DIR, f"{icon['id']}.svg"), arcname=f"svg/solid/{icon['id']}.svg")
        zipf.write(sprite_line_path, arcname="dist/wayfinding-icons-line.svg")
        zipf.write(sprite_solid_path, arcname="dist/wayfinding-icons-solid.svg")
        zipf.write(sprite_combined_path, arcname="dist/wayfinding-icons.svg")
        zipf.write(css_path, arcname="dist/wayfinding-icons.css")
        zipf.write(js_path, arcname="dist/wayfinding-icons.js")
        zipf.write(json_path, arcname="dist/wayfinding-icons.json")
        zipf.write(readme_path, arcname="README.md")
    print(f"Generated ZIP package: {zip_path}")

if __name__ == "__main__":
    main()
