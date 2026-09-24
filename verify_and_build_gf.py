import os
import json
import urllib.request
import urllib.error
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SVG_GF_DIR = os.path.join(BASE_DIR, "svg", "gf-example")
os.makedirs(SVG_GF_DIR, exist_ok=True)

# Complete 80 Wayfinding to Google Fonts Material Symbols Outlined mapping
GF_MAPPING = {
    "wf-arrow-up": "arrow_upward",
    "wf-arrow-right": "arrow_forward",
    "wf-arrow-down": "arrow_downward",
    "wf-arrow-left": "arrow_back",
    "wf-arrow-up-right": "north_east",
    "wf-arrow-up-left": "north_west",
    "wf-u-turn": "u_turn_left",
    "wf-signpost": "signpost",
    "wf-pin": "location_on",
    "wf-facing": "explore",
    "wf-map": "map",
    "wf-touch": "touch_app",
    "wf-entrance": "login",
    "wf-exit": "logout",
    "wf-lift": "elevator",
    "wf-stairs": "stairs",
    "wf-escalator-up": "escalator",
    "wf-escalator-down": "escalator_warning",
    "wf-ramp": "ramp_right",
    "wf-accessible": "accessible",
    "wf-levels": "layers",
    "wf-no-entry": "do_not_disturb_on",
    "wf-prohibited": "cancel",
    "wf-staff-only": "badge",
    "wf-toilets": "wc",
    "wf-toilet-male": "man",
    "wf-toilet-female": "woman",
    "wf-toilet-accessible": "accessible_forward",
    "wf-baby-change": "baby_changing_station",
    "wf-cafe": "local_cafe",
    "wf-food": "restaurant",
    "wf-retail": "shopping_bag",
    "wf-atm": "atm",
    "wf-payment": "payments",
    "wf-pharmacy": "local_pharmacy",
    "wf-water": "water_drop",
    "wf-wifi": "wifi",
    "wf-seating": "chair",
    "wf-parking": "local_parking",
    "wf-car": "directions_car",
    "wf-bus": "directions_bus",
    "wf-ev": "ev_charger",
    "wf-info": "info",
    "wf-help": "help",
    "wf-reception": "desk",
    "wf-security": "shield",
    "wf-phone": "call",
    "wf-intercom": "contact_emergency",
    "wf-hospital": "local_hospital",
    "wf-first-aid": "medical_services",
    "wf-consult": "stethoscope",
    "wf-pathology": "biotech",
    "wf-aed": "cardiology",
    "wf-student": "school",
    "wf-library": "local_library",
    "wf-lecture": "co_present",
    "wf-emergency": "emergency",
    "wf-evacuate": "directions_run",
    "wf-assembly": "groups",
    "wf-fire": "local_fire_department",
    "wf-warning": "warning",
    "wf-construction": "construction",
    "wf-home": "home",
    "wf-search": "search",
    "wf-menu": "menu",
    "wf-back": "arrow_back",
    "wf-close": "close",
    "wf-hours": "schedule",
    "wf-timetable": "calendar_month",
    "wf-events": "event",
    "wf-news": "newspaper",
    "wf-announce": "campaign",
    "wf-share": "share",
    "wf-chat": "chat",
    "wf-like": "thumb_up",
    "wf-camera": "photo_camera",
    "wf-video": "videocam",
    "wf-qr": "qr_code_scanner",
    "wf-email": "mail",
    "wf-web": "language"
}

print(f"Total icons to verify: {len(GF_MAPPING)}")

verified = {}
failures = []

for icon_id, symbol in GF_MAPPING.items():
    # Try fetching 24px outlined SVG from google material design icons
    url = f"https://raw.githubusercontent.com/google/material-design-icons/master/symbols/web/{symbol}/materialsymbolsoutlined/{symbol}_24px.svg"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            content = response.read().decode('utf-8')
            # Extract the inner SVG paths
            # Content looks like: <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24"><path d="..."/></svg>
            verified[icon_id] = {
                "symbol": symbol,
                "svg": content,
                "url": url
            }
            # Write individual file
            with open(os.path.join(SVG_GF_DIR, f"{icon_id}.svg"), "w", encoding="utf-8") as f:
                f.write(content)
            print(f"OK: {icon_id} -> {symbol}")
    except Exception as e:
        print(f"FAIL: {icon_id} -> {symbol}: {e}")
        failures.append((icon_id, symbol, str(e)))

print(f"\nDone: {len(verified)} verified, {len(failures)} failed.")
if failures:
    print("Failures:", failures)
