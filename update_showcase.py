import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, "dist", "wayfinding-icons.json")

with open(json_path, "r", encoding="utf-8") as f:
    metadata = json.load(f)

categories = sorted(list(set(m["category"] for m in metadata)))

category_pills_html = '\n'.join([f'      <button class="pill" data-cat="{cat}">{cat}</button>' for cat in categories])

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Wayfinding Kiosk Icon Library (8 Sets: Material 3, GF example icons, Tactical, Duotone, Line, Solid & PNG)</title>
  <link rel="stylesheet" href="dist/wayfinding-icons.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200">
  <style>
    :root {
      --bg: #090d16;
      --surface: #111827;
      --surface-border: #1f293d;
      --surface-hover: #1e293b;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --primary: #0284c7;
      --primary-hover: #0369a1;
      --accent: #38bdf8;
      --card-bg: #131c2e;
      --card-border: #23314d;
      --live-size: 40px;
      --live-stroke: 2px;
      --live-color: #38bdf8;
      --font: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }

    [data-theme="light"] {
      --bg: #f1f5f9;
      --surface: #ffffff;
      --surface-border: #e2e8f0;
      --surface-hover: #f8fafc;
      --text: #0f172a;
      --text-muted: #64748b;
      --primary: #0284c7;
      --primary-hover: #0369a1;
      --accent: #0284c7;
      --card-bg: #ffffff;
      --card-border: #e2e8f0;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: var(--font);
      background-color: var(--bg);
      color: var(--text);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      transition: background-color 0.2s, color 0.2s;
    }

    header {
      background: var(--surface);
      border-bottom: 1px solid var(--surface-border);
      padding: 1.25rem 2rem;
      position: sticky;
      top: 0;
      z-index: 100;
    }

    .header-inner {
      max-width: 1400px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
      flex-wrap: wrap;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .brand-logo {
      width: 44px;
      height: 44px;
      background: linear-gradient(135deg, #0284c7, #38bdf8);
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-weight: 800;
      font-size: 1.1rem;
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.35);
    }

    .brand-text h1 {
      font-size: 1.25rem;
      font-weight: 700;
      letter-spacing: -0.02em;
    }

    .brand-text p {
      font-size: 0.825rem;
      color: var(--text-muted);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.5rem 1rem;
      border-radius: 8px;
      font-size: 0.875rem;
      font-weight: 600;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.15s ease;
      border: 1px solid transparent;
    }

    .btn-primary {
      background: var(--primary);
      color: #fff;
    }
    .btn-primary:hover {
      background: var(--primary-hover);
    }

    .btn-secondary {
      background: var(--surface-hover);
      color: var(--text);
      border-color: var(--surface-border);
    }
    .btn-secondary:hover {
      border-color: var(--primary);
    }

    main {
      max-width: 1400px;
      margin: 0 auto;
      padding: 2rem;
      flex: 1;
      width: 100%;
    }

    /* Controls Panel */
    .controls-panel {
      background: var(--surface);
      border: 1px solid var(--surface-border);
      border-radius: 14px;
      padding: 1.25rem;
      margin-bottom: 2rem;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 1.25rem;
      align-items: flex-end;
    }

    .control-group {
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
    }

    .control-group label {
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
    }

    .custom-select {
      width: 100%;
      background: var(--bg);
      border: 1px solid var(--surface-border);
      border-radius: 8px;
      padding: 0.6rem 0.85rem;
      color: var(--text);
      font-size: 0.9rem;
      font-weight: 600;
      outline: none;
      cursor: pointer;
      transition: border-color 0.15s;
    }
    .custom-select:focus {
      border-color: var(--primary);
    }

    .search-input {
      width: 100%;
      background: var(--bg);
      border: 1px solid var(--surface-border);
      border-radius: 8px;
      padding: 0.6rem 0.85rem;
      color: var(--text);
      font-size: 0.9rem;
      outline: none;
      transition: border-color 0.15s;
    }
    .search-input:focus {
      border-color: var(--primary);
    }

    .category-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-bottom: 1.5rem;
    }

    .pill {
      padding: 0.35rem 0.85rem;
      border-radius: 20px;
      font-size: 0.8rem;
      font-weight: 600;
      background: var(--surface);
      border: 1px solid var(--surface-border);
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .pill:hover {
      color: var(--text);
      border-color: var(--accent);
    }
    .pill.active {
      background: var(--primary);
      border-color: var(--primary);
      color: #fff;
    }

    .range-wrap {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }
    .range-wrap input[type="range"] {
      flex: 1;
      accent-color: var(--primary);
      cursor: pointer;
    }

    /* Colors and Hex */
    .color-controls-row {
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }

    .color-swatches {
      display: flex;
      gap: 0.45rem;
      align-items: center;
      flex-wrap: wrap;
    }

    .color-swatch {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      cursor: pointer;
      border: 2px solid transparent;
      transition: transform 0.15s, border-color 0.15s, box-shadow 0.15s;
      position: relative;
    }
    .color-swatch:hover {
      transform: scale(1.15);
    }
    .color-swatch.active {
      border-color: #fff;
      box-shadow: 0 0 0 2px var(--primary);
    }
    .color-swatch[data-color="#000000"] {
      border: 1px solid #475569;
    }
    .color-swatch[data-color="#000000"].active {
      border-color: #fff;
      box-shadow: 0 0 0 2px var(--primary);
    }

    .hex-input-group {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .hex-color-picker {
      -webkit-appearance: none;
      -moz-appearance: none;
      appearance: none;
      width: 32px;
      height: 32px;
      border: 1px solid var(--surface-border);
      border-radius: 8px;
      cursor: pointer;
      background: transparent;
      padding: 0;
      overflow: hidden;
    }
    .hex-color-picker::-webkit-color-swatch-wrapper {
      padding: 0;
    }
    .hex-color-picker::-webkit-color-swatch {
      border: none;
      border-radius: 6px;
    }

    .hex-text-input {
      width: 100px;
      background: var(--bg);
      border: 1px solid var(--surface-border);
      border-radius: 8px;
      padding: 0.45rem 0.65rem;
      color: var(--text);
      font-family: monospace;
      font-size: 0.85rem;
      font-weight: 600;
      outline: none;
      transition: border-color 0.15s;
    }
    .hex-text-input:focus {
      border-color: var(--primary);
    }

    /* Simulation Totem Banner */
    .kiosk-demo-banner {
      background: linear-gradient(135deg, rgba(2, 132, 199, 0.12), rgba(56, 189, 248, 0.05));
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 14px;
      padding: 1.25rem 1.75rem;
      margin-bottom: 2rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
      flex-wrap: wrap;
    }

    .kiosk-demo-sample {
      display: flex;
      align-items: center;
      gap: 1rem;
      flex-wrap: wrap;
    }

    .totem-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      background: rgba(2, 132, 199, 0.2);
      border: 1px solid rgba(56, 189, 248, 0.4);
      padding: 0.5rem 1rem;
      border-radius: 8px;
      font-weight: 600;
      font-size: 0.9rem;
      color: var(--accent);
    }

    /* Grid */
    .grid-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1rem;
    }
    .grid-count {
      font-size: 0.9rem;
      color: var(--text-muted);
    }

    .icons-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(max(140px, calc(var(--live-size, 40px) + 36px)), 1fr));
      gap: 1.25rem;
    }

    .icon-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 1.25rem 0.75rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      cursor: pointer;
      transition: all 0.15s ease;
      position: relative;
    }

    .icon-card:hover {
      transform: translateY(-2px);
      border-color: var(--primary);
      box-shadow: 0 8px 24px rgba(2, 132, 199, 0.12);
    }

    .icon-preview {
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: calc(var(--live-size, 40px) + 16px);
      margin-bottom: 0.75rem;
      color: var(--live-color, #38bdf8);
    }

    .icon-preview svg {
      width: var(--live-size, 40px);
      height: var(--live-size, 40px);
      transition: width 0.15s, height 0.15s;
    }

    /* --- Container Badge Shapes --- */
    .icon-badge-wrap {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      transition: background 0.2s, border-color 0.2s, box-shadow 0.2s;
    }
    /* Tile: rounded-rect tonal background */
    .icon-badge-wrap.badge-tile {
      background: var(--badge-bg, rgba(56,189,248,0.13));
      border-radius: calc(var(--live-size, 40px) * 0.28);
      padding: calc(var(--live-size, 40px) * 0.22);
    }
    /* Outline: circular border ring, transparent inside */
    .icon-badge-wrap.badge-outline {
      border: 2.5px solid var(--badge-color, #38bdf8);
      border-radius: 50%;
      padding: calc(var(--live-size, 40px) * 0.22);
    }
    /* Circle: filled solid circle, icon becomes white */
    .icon-badge-wrap.badge-circle {
      background: var(--badge-color, #38bdf8);
      border-radius: 50%;
      padding: calc(var(--live-size, 40px) * 0.22);
    }
    /* In circle mode, force icon to white */
    .icon-badge-wrap.badge-circle svg {
      filter: brightness(0) invert(1);
    }
    .icon-badge-wrap.badge-circle .material-symbols-outlined {
      color: #fff !important;
    }
    /* Container control group styles */
    #container-control-group {
      display: block;
    }
    .container-toggle-row {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .container-btn {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 5px 12px;
      border-radius: 20px;
      font-size: 11.5px;
      font-weight: 600;
      cursor: pointer;
      border: 2px solid var(--border);
      background: var(--card-bg);
      color: var(--text-muted);
      transition: all 0.18s;
      letter-spacing: 0.3px;
    }
    .container-btn:hover {
      border-color: var(--accent);
      color: var(--accent);
    }
    .container-btn.active {
      background: var(--accent);
      border-color: var(--accent);
      color: #fff;
    }
    .container-btn .cb-shape {
      width: 13px;
      height: 13px;
      border: 2px solid currentColor;
      flex-shrink: 0;
    }
    .container-btn.cb-none .cb-shape { border: none; background: transparent; opacity: 0; }
    .container-btn.cb-tile .cb-shape { border-radius: 3px; }
    .container-btn.cb-outline .cb-shape { border-radius: 50%; }
    .container-btn.cb-circle .cb-shape { border-radius: 50%; background: currentColor; border-color: transparent; }

    .icon-preview.line-mode svg {
      stroke-width: var(--live-stroke, 2px);
    }

        .icon-preview.lucide-mode svg,
    .icon-preview.tabler-mode svg {
      stroke-width: var(--live-stroke, 2px);
    }
    .icon-preview.m3-mode svg {
      stroke-width: var(--live-stroke, 2px);
    }

    .icon-preview.m3-filled-mode svg {
      fill: currentColor;
      stroke: none;
    }

    /* M3 Fill toggle control */
    #fill-toggle-group {
      display: none;
    }
    #fill-toggle-group.m3-active {
      display: block;
    }
    .fill-toggle-row {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .fill-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      border: 2px solid var(--border);
      background: var(--card-bg);
      color: var(--text);
      transition: all 0.18s;
      letter-spacing: 0.3px;
    }
    .fill-btn:hover {
      border-color: var(--accent);
      color: var(--accent);
    }
    .fill-btn.active {
      background: var(--accent);
      border-color: var(--accent);
      color: #fff;
    }
    .fill-btn .fill-btn-icon {
      width: 14px;
      height: 14px;
      border-radius: 2px;
    }
    .fill-btn.btn-outline .fill-btn-icon {
      border: 2px solid currentColor;
      background: transparent;
    }
    .fill-btn.btn-filled .fill-btn-icon {
      background: currentColor;
    }

    .icon-preview.gf-mode {
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .material-symbols-outlined {
      font-family: 'Material Symbols Outlined';
      font-weight: normal;
      font-style: normal;
      font-size: var(--live-size, 40px);
      line-height: 1;
      letter-spacing: normal;
      text-transform: none;
      display: inline-block;
      white-space: nowrap;
      word-wrap: normal;
      direction: ltr;
      -webkit-font-smoothing: antialiased;
      text-rendering: optimizeLegibility;
      font-feature-settings: 'liga';
      font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 48;
      user-select: none;
      transition: font-size 0.15s, color 0.15s;
    }

    .icon-preview img.wf-png-thumb {
      width: var(--live-size, 40px);
      height: var(--live-size, 40px);
      object-fit: contain;
      filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
      transition: width 0.15s, height 0.15s;
    }

    /* Dynamic HTML/CSS 3D Badges and Pucks when recolored */
    .dynamic-badge {
      width: var(--live-size, 40px);
      height: var(--live-size, 40px);
      border-radius: calc(var(--live-size, 40px) * 0.23);
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: width 0.15s, height 0.15s;
    }

    .dynamic-badge .gloss {
      position: absolute;
      top: 0; left: 0; right: 0; height: 50%;
      background: linear-gradient(180deg, rgba(255,255,255,0.42) 0%, rgba(255,255,255,0.08) 75%, transparent 100%);
      border-radius: calc(var(--live-size, 40px) * 0.23) calc(var(--live-size, 40px) * 0.23) 50% 50% / calc(var(--live-size, 40px) * 0.23) calc(var(--live-size, 40px) * 0.23) 25% 25%;
      pointer-events: none;
    }

    .dynamic-puck {
      width: var(--live-size, 40px);
      height: var(--live-size, 40px);
      border-radius: 50%;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid rgba(255, 255, 255, 0.3);
      transition: width 0.15s, height 0.15s;
    }

    .dynamic-puck .gloss-dome {
      position: absolute;
      top: 4%; left: 8%; right: 8%; height: 48%;
      background: linear-gradient(180deg, rgba(255,255,255,0.5) 0%, rgba(255,255,255,0.08) 70%, transparent 100%);
      border-radius: 50% 50% 45% 45% / 70% 70% 30% 30%;
      pointer-events: none;
    }

    .dynamic-glyph {
      width: 52%;
      height: 52%;
      color: #ffffff;
      filter: drop-shadow(0 2px 3px rgba(0, 0, 0, 0.4));
      position: relative;
      z-index: 2;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .dynamic-glyph svg {
      width: 100%;
      height: 100%;
      fill: currentColor;
    }

    .icon-name {
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text);
      margin-bottom: 0.25rem;
    }

    .icon-id {
      font-family: monospace;
      font-size: 0.75rem;
      color: var(--text-muted);
      background: var(--surface-hover);
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
    }

    .card-actions {
      display: flex;
      gap: 0.35rem;
      margin-top: 0.75rem;
      opacity: 0;
      transform: translateY(4px);
      transition: all 0.15s ease;
    }

    .icon-card:hover .card-actions {
      opacity: 1;
      transform: translateY(0);
    }

    .card-btn {
      background: var(--surface-border);
      border: none;
      color: var(--text);
      font-size: 0.7rem;
      padding: 0.25rem 0.5rem;
      border-radius: 4px;
      cursor: pointer;
      font-weight: 600;
    }
    .card-btn:hover {
      background: var(--primary);
      color: #fff;
    }

    /* Modal */
    .modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(6px);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 200;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s;
    }

    .modal-overlay.active {
      opacity: 1;
      pointer-events: auto;
    }

    .modal {
      background: var(--surface);
      border: 1px solid var(--surface-border);
      border-radius: 16px;
      max-width: 600px;
      width: 90%;
      padding: 1.75rem;
      position: relative;
      box-shadow: 0 20px 40px rgba(0,0,0,0.5);
    }

    .modal-close {
      position: absolute;
      top: 1rem;
      right: 1rem;
      background: none;
      border: none;
      font-size: 1.5rem;
      color: var(--text-muted);
      cursor: pointer;
    }
    .modal-close:hover {
      color: var(--text);
    }

    .modal-header {
      display: flex;
      align-items: center;
      gap: 1.25rem;
      margin-bottom: 1.5rem;
    }

    .modal-preview {
      width: 96px;
      height: 96px;
      background: var(--bg);
      border: 1px solid var(--surface-border);
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--accent);
    }

    .modal-preview svg {
      width: 56px;
      height: 56px;
    }

    .modal-preview img {
      width: 80px;
      height: 80px;
      object-fit: contain;
    }

    .modal-code-box {
      background: var(--bg);
      border: 1px solid var(--surface-border);
      border-radius: 8px;
      padding: 0.85rem;
      font-family: monospace;
      font-size: 0.75rem;
      overflow-x: auto;
      max-height: 120px;
      margin-top: 0.5rem;
      margin-bottom: 1.25rem;
      white-space: pre-wrap;
      word-break: break-all;
      color: var(--accent);
    }

    .modal-actions {
      display: flex;
      gap: 0.75rem;
      flex-wrap: wrap;
    }

    .toast {
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: var(--primary);
      color: #fff;
      padding: 0.75rem 1.25rem;
      border-radius: 8px;
      font-weight: 600;
      font-size: 0.875rem;
      box-shadow: 0 8px 24px rgba(0,0,0,0.3);
      opacity: 0;
      transform: translateY(10px);
      transition: all 0.2s ease;
      z-index: 300;
      pointer-events: none;
    }
    .toast.show {
      opacity: 1;
      transform: translateY(0);
    }
  </style>
</head>
<body>
  <header>
    <div class="header-inner">
      <div class="brand">
        <div class="brand-logo">WF</div>
        <div class="brand-text">
          <h1>Wayfinding Kiosk Icon Library</h1>
          <p>8 Design Sets: Material 3 (M3 Clean Vector SVG), GF example icons, Tactical Cyber, Duotone, Line, Solid, 3D Squircle Badges & 3D Circular Pucks with Color Customizer</p>
        </div>
      </div>
      <div class="header-actions">
        <a href="dist/wayfinding-icons.zip" class="btn btn-primary" download>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          Download All Sets (.ZIP)
        </a>
        <button class="btn btn-secondary" id="theme-toggle">Toggle Theme</button>
      </div>
    </div>
  </header>

  <main>
    <!-- Live Kiosk Interface Simulation Banner -->
    <div class="kiosk-demo-banner">
      <div>
        <div style="font-weight: 700; font-size: 1.1rem; color: #f8fafc; margin-bottom: 0.25rem;">Live Wayfinding Totem Simulation</div>
        <div style="font-size: 0.85rem; color: #94a3b8;">High-visibility directional totems, overhead signage & directory indicators</div>
      </div>
      <div class="kiosk-demo-sample" id="banner-samples"></div>
    </div>

    <!-- Controls Panel with Dropdown for Sets & Hex Color -->
    <div class="controls-panel">
      <!-- Design Set Dropdown -->
      <div class="control-group">
        <label>Design Style Set</label>
        <select id="set-select" class="custom-select">
          <option value="lucide">Lucide Icons (Open Source - ISC/MIT)</option>
          <option value="tabler">Tabler Icons (Open Source - MIT)</option>
          <option value="m3">Material 3 (M3 Clean Vector SVG)</option>
          <option value="gf-example">GF example icons</option>
          <option value="line">Modern Line (Outline SVG)</option>
          <option value="solid">Solid Signage (Filled Silhouette SVG)</option>
          <option value="duotone">Duotone Pictograms (Two-Tone SVG)</option>
          <option value="tactical">Tactical Cyber (Chiseled Amber SVG)</option>
          <option value="png" selected>3D Squircle Badges (PNG Images)</option>
          <option value="png-circle">3D Circular Pucks (PNG Images)</option>
        </select>
      </div>

      <div class="control-group">
        <label>Search 80 Icons</label>
        <input type="text" id="search-box" class="search-input" placeholder="Search by name, ID or keyword...">
      </div>

      <div class="control-group">
        <label>Display Size (<span id="size-label">40px</span>)</label>
        <div class="range-wrap">
          <input type="range" id="size-slider" min="24" max="150" value="40" step="2">
        </div>
      </div>

      <div class="control-group" id="stroke-control-group">
        <label>Stroke Width (<span id="stroke-label">2.0px</span>)</label>
        <div class="range-wrap">
          <input type="range" id="stroke-slider" min="1.5" max="3.5" value="2.0" step="0.25">
        </div>
      </div>

      <div class="control-group" id="fill-toggle-group">
        <label>Fill Style (M3 Design Axis)</label>
        <div class="fill-toggle-row">
          <button class="fill-btn btn-outline active" id="fill-btn-outline" title="Outline — unfilled stroke icons (FILL=0)">
            <span class="fill-btn-icon"></span> Outline
          </button>
          <button class="fill-btn btn-filled" id="fill-btn-filled" title="Filled — solid shape icons (FILL=1)">
            <span class="fill-btn-icon"></span> Filled
          </button>
        </div>
      </div>

      <div class="control-group" id="container-control-group">
        <label>Container Shape</label>
        <div class="container-toggle-row">
          <button class="container-btn cb-none active" id="cb-none" title="No container — bare icon">
            <span class="cb-shape"></span> None
          </button>
          <button class="container-btn cb-tile" id="cb-tile" title="Tile — rounded rectangle badge">
            <span class="cb-shape"></span> Tile
          </button>
          <button class="container-btn cb-outline" id="cb-outline" title="Outline — circular border ring">
            <span class="cb-shape"></span> Outline
          </button>
          <button class="container-btn cb-circle" id="cb-circle" title="Circle — filled circle badge">
            <span class="cb-shape"></span> Circle
          </button>
        </div>
      </div>

      <div class="control-group" id="color-control-group">
        <label>Signage Color & Hex</label>
        <div class="color-controls-row">
          <div class="color-swatches">
            <div class="color-swatch active" style="background: linear-gradient(135deg, #0284c7, #10b981, #ef4444);" data-color="default" title="Category Theme Default"></div>
            <div class="color-swatch" style="background: #000000;" data-color="#000000" title="Obsidian Black"></div>
            <div class="color-swatch" style="background: #e3e3e3;" data-color="#e3e3e3" title="GF Platinum (#E3E3E3)"></div>
            <div class="color-swatch" style="background: #38bdf8;" data-color="#38bdf8" title="Cyan"></div>
            <div class="color-swatch" style="background: #10b981;" data-color="#10b981" title="Green"></div>
            <div class="color-swatch" style="background: #ef4444;" data-color="#ef4444" title="Red"></div>
            <div class="color-swatch" style="background: #f59e0b;" data-color="#f59e0b" title="Amber"></div>
            <div class="color-swatch" style="background: #a855f7;" data-color="#a855f7" title="Purple"></div>
            <div class="color-swatch" style="background: #ffffff;" data-color="#ffffff" title="White"></div>
          </div>
          <div class="hex-input-group">
            <input type="color" id="hex-color-picker" class="hex-color-picker" value="#38bdf8" title="Pick any custom color">
            <input type="text" id="hex-color-input" class="hex-text-input" value="#38bdf8" placeholder="#000000" maxlength="7">
          </div>
        </div>
      </div>
    </div>

    <!-- Category Filter Pills -->
    <div class="category-pills" id="category-pills">
      <button class="pill active" data-cat="all">All Icons (80)</button>
__CATEGORY_PILLS__
    </div>

    <div class="grid-header">
      <div class="grid-count">Showing <span id="visible-count">80</span> of 80 icons in <span id="current-set-label" style="font-weight: 700; color: var(--accent);">3D Squircle Badges (PNG)</span> style</div>
    </div>

    <!-- Icons Grid -->
    <div class="icons-grid" id="icons-grid"></div>
  </main>

  <!-- Detail Modal -->
  <div class="modal-overlay" id="modal-overlay">
    <div class="modal">
      <button class="modal-close" id="modal-close">&times;</button>
      <div class="modal-header">
        <div class="modal-preview" id="modal-preview"></div>
        <div>
          <h2 id="modal-title" style="font-size: 1.25rem; font-weight: 700; margin-bottom: 0.25rem;"></h2>
          <div id="modal-id" class="icon-id" style="display: inline-block;"></div>
          <div id="modal-cat" style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.35rem;"></div>
        </div>
      </div>

      <label id="modal-code-label-1" style="font-size: 0.75rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase;">Asset Code / Markup</label>
      <div class="modal-code-box" id="modal-svg-code"></div>

      <label id="modal-code-label-2" style="font-size: 0.75rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase;">Implementation Tag</label>
      <div class="modal-code-box" id="modal-usage-code"></div>

      <div class="modal-actions">
        <button class="btn btn-primary" id="modal-copy-svg">Copy Asset</button>
        <button class="btn btn-secondary" id="modal-copy-tag">Copy Tag</button>
        <a class="btn btn-secondary" id="modal-download" download>Download</a>
        <button class="btn btn-secondary" id="modal-download-custom" style="display: none;">Download Custom Color .PNG</button>
      </div>
    </div>
  </div>

  <div class="toast" id="toast">Copied to clipboard!</div>
  <canvas id="export-canvas" width="256" height="256" style="display: none;"></canvas>

  <script>
    const METADATA = __METADATA_JSON__;
    let currentSet = 'png';
    let currentCategory = 'all';
    let currentSearch = '';
    let currentColor = 'default';
    let customHex = '#38bdf8';
    let currentSize = 40;
    let currentStroke = 2.0;
    let currentFill = false; // false = outline (FILL=0), true = filled (FILL=1)
    let currentContainer = 'none'; // 'none' | 'tile' | 'outline' | 'circle'

    const setSelect = document.getElementById('set-select');
    const currentSetLabel = document.getElementById('current-set-label');
    const strokeControlGroup = document.getElementById('stroke-control-group');
    const fillToggleGroup = document.getElementById('fill-toggle-group');
    const fillBtnOutline = document.getElementById('fill-btn-outline');
    const fillBtnFilled = document.getElementById('fill-btn-filled');
    const cbNone = document.getElementById('cb-none');
    const cbTile = document.getElementById('cb-tile');
    const cbOutline = document.getElementById('cb-outline');
    const cbCircle = document.getElementById('cb-circle');
    const containerBtns = [cbNone, cbTile, cbOutline, cbCircle];
    const grid = document.getElementById('icons-grid');
    const searchBox = document.getElementById('search-box');
    const categoryPills = document.getElementById('category-pills');
    const visibleCount = document.getElementById('visible-count');
    const sizeSlider = document.getElementById('size-slider');
    const sizeLabel = document.getElementById('size-label');
    const strokeSlider = document.getElementById('stroke-slider');
    const strokeLabel = document.getElementById('stroke-label');
    const themeToggle = document.getElementById('theme-toggle');
    const toast = document.getElementById('toast');
    const bannerSamples = document.getElementById('banner-samples');

    const hexColorPicker = document.getElementById('hex-color-picker');
    const hexColorInput = document.getElementById('hex-color-input');
    const exportCanvas = document.getElementById('export-canvas');

    // Modal elements
    const modalOverlay = document.getElementById('modal-overlay');
    const modalClose = document.getElementById('modal-close');
    const modalPreview = document.getElementById('modal-preview');
    const modalTitle = document.getElementById('modal-title');
    const modalId = document.getElementById('modal-id');
    const modalCat = document.getElementById('modal-cat');
    const modalCodeLabel1 = document.getElementById('modal-code-label-1');
    const modalCodeLabel2 = document.getElementById('modal-code-label-2');
    const modalSvgCode = document.getElementById('modal-svg-code');
    const modalUsageCode = document.getElementById('modal-usage-code');
    const modalCopySvg = document.getElementById('modal-copy-svg');
    const modalCopyTag = document.getElementById('modal-copy-tag');
    const modalDownload = document.getElementById('modal-download');
    const modalDownloadCustom = document.getElementById('modal-download-custom');

    let selectedIcon = null;

    // Color conversion utilities
    function hexToRgb(hex) {
      hex = hex.replace('#', '');
      if (hex.length === 3) hex = hex.split('').map(function(c) { return c + c; }).join('');
      const num = parseInt(hex, 16);
      if (isNaN(num)) return { r: 56, g: 189, b: 248 };
      return { r: (num >> 16) & 255, g: (num >> 8) & 255, b: num & 255 };
    }

    function adjustBrightness(hex, percent) {
      const rgb = hexToRgb(hex);
      const factor = 1 + percent / 100;
      const r = Math.min(255, Math.max(0, Math.round(rgb.r * factor)));
      const g = Math.min(255, Math.max(0, Math.round(rgb.g * factor)));
      const b = Math.min(255, Math.max(0, Math.round(rgb.b * factor)));
      return 'rgb(' + r + ',' + g + ',' + b + ')';
    }

    function getThemeForHex(hex) {
      const isBlack = (hex.toLowerCase() === '#000000' || hex.toLowerCase() === '#0f172a');
      const light = isBlack ? '#475569' : adjustBrightness(hex, 32);
      const mid = isBlack ? '#1e293b' : hex;
      const dark = isBlack ? '#000000' : adjustBrightness(hex, -38);
      const rgb = hexToRgb(hex);
      const shadow = isBlack ? 'rgba(0,0,0,0.65)' : 'rgba(' + rgb.r + ',' + rgb.g + ',' + rgb.b + ',0.45)';
      return { light: light, mid: mid, dark: dark, shadow: shadow };
    }

        function getIconColor(icon) {
      if (currentColor !== 'default') return currentColor;
      const catColors = {
        'Navigation': '#0284c7',
        'Building': '#059669',
        'Amenities': '#d97706',
        'Transit': '#7c3aed',
        'Services': '#0ea5e9',
        'Healthcare': '#dc2626',
        'Campus': '#6366f1',
        'Safety': '#ea580c',
        'UI': '#64748b',
        'Media': '#ec4899'
      };
      return (icon && catColors[icon.category]) ? catColors[icon.category] : '#38bdf8';
    }

    function wrapWithContainer(contentHtml, icon) {
      if (currentContainer === 'none') return contentHtml;
      const col = getIconColor(icon);
      const rgb = hexToRgb(col);
      const badgeBg = 'rgba(' + rgb.r + ',' + rgb.g + ',' + rgb.b + ',0.15)';
      return '<div class="icon-badge-wrap badge-' + currentContainer + '" style="--badge-color: ' + col + '; --badge-bg: ' + badgeBg + ';">' + contentHtml + '</div>';
    }

    function renderBanner() {
      const isLine = (currentSet === 'line');
      const isSolid = (currentSet === 'solid');
      const isDuotone = (currentSet === 'duotone');
      const isTactical = (currentSet === 'tactical');
      const isGfExample = (currentSet === 'gf-example');
      const isM3 = (currentSet === 'm3');
      const isLucide = (currentSet === 'lucide');
      const isTabler = (currentSet === 'tabler');
      const isPuck = (currentSet === 'png-circle');
      const arrowIcon = METADATA.find(function(i) { return i.id === 'wf-arrow-up'; });
      const liftIcon = METADATA.find(function(i) { return i.id === 'wf-lift'; });
      const exitIcon = METADATA.find(function(i) { return i.id === 'wf-exit'; });

      if (isGfExample) {
        const col1 = (currentColor === 'default') ? '#38bdf8' : currentColor;
        const col2 = (currentColor === 'default') ? '#10b981' : currentColor;
        const col3 = (currentColor === 'default') ? '#ef4444' : currentColor;
        bannerSamples.innerHTML = 
          '<div class="totem-badge">' +
            '<span class="material-symbols-outlined" style="font-size: 22px; color: ' + col1 + '; vertical-align: middle;">' + (arrowIcon ? arrowIcon.gf_symbol : 'arrow_upward') + '</span>' +
            '<span>Main Concourse</span>' +
          '</div>' +
          '<div class="totem-badge" style="color: #10b981; border-color: rgba(16, 185, 129, 0.4); background: rgba(16, 185, 129, 0.15);">' +
            '<span class="material-symbols-outlined" style="font-size: 22px; color: ' + col2 + '; vertical-align: middle;">' + (liftIcon ? liftIcon.gf_symbol : 'elevator') + '</span>' +
            '<span>Passenger Lift L2</span>' +
          '</div>' +
          '<div class="totem-badge" style="color: #ef4444; border-color: rgba(239, 68, 68, 0.4); background: rgba(239, 68, 68, 0.15);">' +
            '<span class="material-symbols-outlined" style="font-size: 22px; color: ' + col3 + '; vertical-align: middle;">' + (exitIcon ? exitIcon.gf_symbol : 'logout') + '</span>' +
            '<span>Building Exit</span>' +
          '</div>';
      } else if (isLine || isSolid || isDuotone || isTactical || isM3 || isLucide || isTabler) {
        function getInner(icon) {
          if (!icon) return '';
          if (isLucide) return icon.paths_lucide;
          if (isTabler) return icon.paths_tabler;
          if (isLucide) return icon.paths_lucide;
          if (isTabler) return icon.paths_tabler;
          if (isM3) return currentFill ? (icon.paths_m3_filled || icon.paths_m3) : icon.paths_m3;
          if (isTactical) return icon.paths_tactical;
          if (isDuotone) return icon.paths_duotone;
          return isSolid ? icon.paths_solid : icon.paths_line;
        }
        function getSvgWrapper(inner, col) {
          const colorToUse = (currentColor === 'default') ? col : currentColor;
          if (isLucide) {
            return '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="' + colorToUse + '" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="wf-icon-lucide">' + inner + '</svg>';
          }
          if (isTabler) {
            return '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="' + colorToUse + '" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="wf-icon-tabler">' + inner + '</svg>';
          }
          if (isLucide) {
            return '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="' + colorToUse + '" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="wf-icon-lucide">' + inner + '</svg>';
          }
          if (isTabler) {
            return '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="' + colorToUse + '" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="wf-icon-tabler">' + inner + '</svg>';
          }
          if (isM3) {
            if (currentFill) {
              return '<svg width="22" height="22" viewBox="0 0 24 24" fill="' + colorToUse + '" class="wf-icon-m3 wf-icon-m3-filled">' + inner + '</svg>';
            }
            return '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="' + colorToUse + '" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="wf-icon-m3">' + inner + '</svg>';
          }
          if (isTactical) {
            const accentCol = (currentColor === 'default') ? '#f59e0b' : currentColor;
            return '<svg width="22" height="22" viewBox="0 0 24 24" class="wf-icon-tactical" style="--wf-accent:' + accentCol + '">' + inner + '</svg>';
          }
          if (isDuotone) {
            return '<svg width="22" height="22" viewBox="0 0 24 24" class="wf-icon-duotone" style="color:' + colorToUse + '">' + inner + '</svg>';
          }
          if (isSolid) {
            return '<svg width="22" height="22" viewBox="0 0 24 24" fill="' + colorToUse + '">' + inner + '</svg>';
          }
          return '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="' + colorToUse + '" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">' + inner + '</svg>';
        }

        bannerSamples.innerHTML = 
          '<div class="totem-badge">' +
            getSvgWrapper(getInner(arrowIcon), '#38bdf8') +
            '<span>Main Concourse</span>' +
          '</div>' +
          '<div class="totem-badge" style="color: #10b981; border-color: rgba(16, 185, 129, 0.4); background: rgba(16, 185, 129, 0.15);">' +
            getSvgWrapper(getInner(liftIcon), '#10b981') +
            '<span>Passenger Lift L2</span>' +
          '</div>' +
          '<div class="totem-badge" style="color: #ef4444; border-color: rgba(239, 68, 68, 0.4); background: rgba(239, 68, 68, 0.15);">' +
            getSvgWrapper(getInner(exitIcon), '#ef4444') +
            '<span>Building Exit</span>' +
          '</div>';
      } else {
        const folder = isPuck ? 'png-circle' : 'png';
        bannerSamples.innerHTML = 
          '<div class="totem-badge">' +
            '<img src="' + folder + '/wf-arrow-up.png" width="24" height="24" style="vertical-align:middle;">' +
            '<span>Main Concourse</span>' +
          '</div>' +
          '<div class="totem-badge" style="color: #10b981; border-color: rgba(16, 185, 129, 0.4); background: rgba(16, 185, 129, 0.15);">' +
            '<img src="' + folder + '/wf-lift.png" width="24" height="24" style="vertical-align:middle;">' +
            '<span>Passenger Lift L2</span>' +
          '</div>' +
          '<div class="totem-badge" style="color: #ef4444; border-color: rgba(239, 68, 68, 0.4); background: rgba(239, 68, 68, 0.15);">' +
            '<img src="' + folder + '/wf-exit.png" width="24" height="24" style="vertical-align:middle;">' +
            '<span>Building Exit</span>' +
          '</div>';
      }
    }

    function renderIcons() {
      grid.innerHTML = '';
      const query = currentSearch.toLowerCase().trim();
      const isLine = (currentSet === 'line');
      const isSolid = (currentSet === 'solid');
      const isDuotone = (currentSet === 'duotone');
      const isTactical = (currentSet === 'tactical');
      const isGfExample = (currentSet === 'gf-example');
      const isM3 = (currentSet === 'm3');
      const isLucide = (currentSet === 'lucide');
      const isTabler = (currentSet === 'tabler');
      const isSquircle = (currentSet === 'png');
      const isPuck = (currentSet === 'png-circle');
      const isDefaultColor = (currentColor === 'default');

      if (isLine) {
        currentSetLabel.textContent = 'Modern Line (SVG)';
        strokeControlGroup.style.opacity = '1';
        strokeControlGroup.style.pointerEvents = 'auto';
      } else if (isSolid) {
        currentSetLabel.textContent = 'Solid Signage (SVG)';
        strokeControlGroup.style.opacity = '0.3';
        strokeControlGroup.style.pointerEvents = 'none';
      } else if (isDuotone) {
        currentSetLabel.textContent = 'Duotone Pictograms (SVG)';
        strokeControlGroup.style.opacity = '0.3';
        strokeControlGroup.style.pointerEvents = 'none';
      } else if (isTactical) {
        currentSetLabel.textContent = isDefaultColor ? 'Tactical Cyber (Chiseled Amber SVG)' : 'Tactical Cyber (' + currentColor + ' SVG)';
        strokeControlGroup.style.opacity = '0.3';
        strokeControlGroup.style.pointerEvents = 'none';
      } else if (isGfExample) {
        currentSetLabel.textContent = isDefaultColor ? 'GF example icons (Google Fonts)' : 'GF example icons (' + currentColor + ')';
        strokeControlGroup.style.opacity = '0.3';
        strokeControlGroup.style.pointerEvents = 'none';
      } else if (isLucide) {
        currentSetLabel.textContent = isDefaultColor ? 'Lucide Icons (Open Source ISC/MIT SVG)' : 'Lucide Icons (' + currentColor + ' SVG)';
        strokeControlGroup.style.opacity = '1';
        strokeControlGroup.style.pointerEvents = 'auto';
      } else if (isTabler) {
        currentSetLabel.textContent = isDefaultColor ? 'Tabler Icons (Open Source MIT SVG)' : 'Tabler Icons (' + currentColor + ' SVG)';
        strokeControlGroup.style.opacity = '1';
        strokeControlGroup.style.pointerEvents = 'auto';
      } else if (isLucide) {
        currentSetLabel.textContent = isDefaultColor ? 'Lucide Icons (Open Source ISC/MIT SVG)' : 'Lucide Icons (' + currentColor + ' SVG)';
        strokeControlGroup.style.opacity = '1';
        strokeControlGroup.style.pointerEvents = 'auto';
      } else if (isTabler) {
        currentSetLabel.textContent = isDefaultColor ? 'Tabler Icons (Open Source MIT SVG)' : 'Tabler Icons (' + currentColor + ' SVG)';
        strokeControlGroup.style.opacity = '1';
        strokeControlGroup.style.pointerEvents = 'auto';
      } else if (isM3) {
        const fillSuffix = currentFill ? ' — Filled' : ' — Outline';
        currentSetLabel.textContent = isDefaultColor ? ('Material 3 (M3 Clean Vector SVG' + fillSuffix + ')') : ('Material 3 (' + currentColor + ' SVG' + fillSuffix + ')');
        // Stroke slider only makes sense for outline mode
        if (currentFill) {
          strokeControlGroup.style.opacity = '0.3';
          strokeControlGroup.style.pointerEvents = 'none';
        } else {
          strokeControlGroup.style.opacity = '1';
          strokeControlGroup.style.pointerEvents = 'auto';
        }
      } else if (isSquircle) {
        currentSetLabel.textContent = isDefaultColor ? '3D Squircle Badges (PNG)' : '3D Squircle Badges (' + currentColor + ')';
        strokeControlGroup.style.opacity = '0.3';
        strokeControlGroup.style.pointerEvents = 'none';
      } else if (isPuck) {
        currentSetLabel.textContent = isDefaultColor ? '3D Circular Pucks (PNG)' : '3D Circular Pucks (' + currentColor + ')';
        strokeControlGroup.style.opacity = '0.3';
        strokeControlGroup.style.pointerEvents = 'none';
      }

      renderBanner();

      const filtered = METADATA.filter(function(icon) {
        const matchesCategory = (currentCategory === 'all' || icon.category === currentCategory);
        const matchesSearch = !query || 
          icon.name.toLowerCase().includes(query) ||
          icon.id.toLowerCase().includes(query) ||
          (icon.keywords && icon.keywords.some(function(k) { return k.toLowerCase().includes(query); }));
        return matchesCategory && matchesSearch;
      });

      visibleCount.textContent = filtered.length;

      const dynamicTheme = isDefaultColor ? null : getThemeForHex(currentColor);

      filtered.forEach(function(icon) {
        const card = document.createElement('div');
        card.className = 'icon-card';

        let previewHtml = '';
        let actionButtonsHtml = '';

        if (isSquircle) {
          if (isDefaultColor) {
            previewHtml = '<div class="icon-preview png-mode">' + wrapWithContainer('<img src="png/' + icon.id + '.png" class="wf-png-thumb" alt="' + icon.name + '" loading="lazy">', icon) + '</div>';
          } else {
            previewHtml = 
              '<div class="icon-preview png-mode">' +
                wrapWithContainer('<div class="dynamic-badge" style="background: linear-gradient(145deg, ' + dynamicTheme.light + ' 0%, ' + dynamicTheme.mid + ' 55%, ' + dynamicTheme.dark + ' 100%); box-shadow: 0 12px 24px -4px ' + dynamicTheme.shadow + ', inset 0 1.5px 1.5px rgba(255,255,255,0.7), inset 0 -2px 3px rgba(0,0,0,0.4);">' +
                  '<div class="gloss"></div>' +
                  '<div class="dynamic-glyph">' +
                    '<svg viewBox="0 0 24 24">' + icon.paths_solid + '</svg>' +
                  '</div>' +
                '</div>', icon) +
              '</div>';
          }
          actionButtonsHtml = 
            '<button class="card-btn copy-asset-btn" data-id="' + icon.id + '">Copy &lt;img&gt;</button>' +
            '<button class="card-btn download-asset-btn" data-id="' + icon.id + '">Download</button>';
        } else if (isPuck) {
          if (isDefaultColor) {
            previewHtml = '<div class="icon-preview png-mode">' + wrapWithContainer('<img src="png-circle/' + icon.id + '.png" class="wf-png-thumb" alt="' + icon.name + '" loading="lazy">', icon) + '</div>';
          } else {
            previewHtml = 
              '<div class="icon-preview png-mode">' +
                wrapWithContainer('<div class="dynamic-puck" style="background: radial-gradient(circle at 35% 25%, ' + dynamicTheme.light + ' 0%, ' + dynamicTheme.mid + ' 45%, ' + dynamicTheme.dark + ' 100%); box-shadow: 0 14px 28px -5px ' + dynamicTheme.shadow + ', inset 0 2px 2px rgba(255,255,255,0.8), inset 0 -2px 4px rgba(0,0,0,0.5);">' +
                  '<div class="gloss-dome"></div>' +
                  '<div class="dynamic-glyph">' +
                    '<svg viewBox="0 0 24 24">' + icon.paths_solid + '</svg>' +
                  '</div>' +
                '</div>', icon) +
              '</div>';
          }
          actionButtonsHtml = 
            '<button class="card-btn copy-asset-btn" data-id="' + icon.id + '">Copy &lt;img&gt;</button>' +
            '<button class="card-btn download-asset-btn" data-id="' + icon.id + '">Download</button>';
        } else if (isGfExample) {
          const colorVal = isDefaultColor ? 'var(--live-color, #38bdf8)' : currentColor;
          const gfSymbol = icon.gf_symbol || 'help';
          previewHtml = 
            '<div class="icon-preview gf-mode" style="color: ' + colorVal + ';">' +
              wrapWithContainer('<span class="material-symbols-outlined" style="font-size: var(--live-size, 40px); color: ' + colorVal + ';">' + gfSymbol + '</span>', icon) +
            '</div>';
          actionButtonsHtml = 
            '<button class="card-btn copy-asset-btn" data-id="' + icon.id + '">Copy &lt;span&gt;</button>' +
            '<button class="card-btn download-asset-btn" data-id="' + icon.id + '">Download</button>';
        } else if (isLucide) {
          const colorVal = isDefaultColor ? 'var(--live-color, #38bdf8)' : currentColor;
          previewHtml = '<div class="icon-preview lucide-mode">' + wrapWithContainer('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="' + colorVal + '" stroke-width="var(--live-stroke, 2px)" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-lucide">' + icon.paths_lucide + '</svg>', icon) + '</div>';
          actionButtonsHtml = 
            '<button class="card-btn copy-asset-btn" data-id="' + icon.id + '">Copy SVG</button>' +
            '<button class="card-btn download-asset-btn" data-id="' + icon.id + '">Download</button>';
        } else if (isTabler) {
          const colorVal = isDefaultColor ? 'var(--live-color, #38bdf8)' : currentColor;
          previewHtml = '<div class="icon-preview tabler-mode">' + wrapWithContainer('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="' + colorVal + '" stroke-width="var(--live-stroke, 2px)" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-tabler">' + icon.paths_tabler + '</svg>', icon) + '</div>';
          actionButtonsHtml = 
            '<button class="card-btn copy-asset-btn" data-id="' + icon.id + '">Copy SVG</button>' +
            '<button class="card-btn download-asset-btn" data-id="' + icon.id + '">Download</button>';
        } else if (isLucide) {
          const colorVal = isDefaultColor ? 'var(--live-color, #38bdf8)' : currentColor;
          previewHtml = '<div class="icon-preview lucide-mode">' + wrapWithContainer('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="' + colorVal + '" stroke-width="var(--live-stroke, 2px)" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-lucide">' + icon.paths_lucide + '</svg>', icon) + '</div>';
          actionButtonsHtml = 
            '<button class="card-btn copy-asset-btn" data-id="' + icon.id + '">Copy SVG</button>' +
            '<button class="card-btn download-asset-btn" data-id="' + icon.id + '">Download</button>';
        } else if (isTabler) {
          const colorVal = isDefaultColor ? 'var(--live-color, #38bdf8)' : currentColor;
          previewHtml = '<div class="icon-preview tabler-mode">' + wrapWithContainer('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="' + colorVal + '" stroke-width="var(--live-stroke, 2px)" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-tabler">' + icon.paths_tabler + '</svg>', icon) + '</div>';
          actionButtonsHtml = 
            '<button class="card-btn copy-asset-btn" data-id="' + icon.id + '">Copy SVG</button>' +
            '<button class="card-btn download-asset-btn" data-id="' + icon.id + '">Download</button>';
        } else if (isM3) {
          const colorVal = isDefaultColor ? 'var(--live-color, #38bdf8)' : currentColor;
          if (currentFill) {
            const paths = icon.paths_m3_filled || icon.paths_m3;
            previewHtml = '<div class="icon-preview m3-filled-mode" style="color: ' + colorVal + '">' + wrapWithContainer('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="wf-icon wf-icon-m3 wf-icon-m3-filled">' + paths + '</svg>', icon) + '</div>';
          } else {
            previewHtml = '<div class="icon-preview m3-mode">' + wrapWithContainer('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="' + colorVal + '" stroke-width="var(--live-stroke, 2px)" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-m3">' + icon.paths_m3 + '</svg>', icon) + '</div>';
          }
          actionButtonsHtml = 
            '<button class="card-btn copy-asset-btn" data-id="' + icon.id + '">Copy SVG</button>' +
            '<button class="card-btn download-asset-btn" data-id="' + icon.id + '">Download</button>';
        } else if (isTactical) {
          const accentCol = isDefaultColor ? '#f59e0b' : currentColor;
          previewHtml = '<div class="icon-preview tactical-mode">' + wrapWithContainer('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="wf-icon wf-icon-tactical" style="--wf-accent: ' + accentCol + ';">' + icon.paths_tactical + '</svg>', icon) + '</div>';
          actionButtonsHtml = 
            '<button class="card-btn copy-asset-btn" data-id="' + icon.id + '">Copy SVG</button>' +
            '<button class="card-btn download-asset-btn" data-id="' + icon.id + '">Download</button>';
        } else if (isDuotone) {
          const colorVal = isDefaultColor ? 'var(--live-color, #38bdf8)' : currentColor;
          previewHtml = '<div class="icon-preview duotone-mode" style="color: ' + colorVal + '">' + wrapWithContainer('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="wf-icon wf-icon-duotone">' + icon.paths_duotone + '</svg>', icon) + '</div>';
          actionButtonsHtml = 
            '<button class="card-btn copy-asset-btn" data-id="' + icon.id + '">Copy SVG</button>' +
            '<button class="card-btn download-asset-btn" data-id="' + icon.id + '">Download</button>';
        } else {
          const paths = isSolid ? icon.paths_solid : icon.paths_line;
          const strokeCol = isDefaultColor ? '#38bdf8' : currentColor;
          const fillCol = isDefaultColor ? '#38bdf8' : currentColor;

          const svgSnippet = isSolid
            ? '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="' + fillCol + '">' + paths + '</svg>'
            : '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="' + strokeCol + '" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' + paths + '</svg>';
          previewHtml = '<div class="icon-preview ' + (isSolid ? 'solid-mode' : 'line-mode') + '">' + wrapWithContainer(svgSnippet, icon) + '</div>';
          actionButtonsHtml = 
            '<button class="card-btn copy-asset-btn" data-id="' + icon.id + '">Copy SVG</button>' +
            '<button class="card-btn download-asset-btn" data-id="' + icon.id + '">Download</button>';
        }

        const idLabel = isGfExample ? (icon.id + ' • GF: ' + icon.gf_symbol) : icon.id;
        card.innerHTML = 
          previewHtml +
          '<div class="icon-name">' + icon.name + '</div>' +
          '<div class="icon-id">' + idLabel + '</div>' +
          '<div class="card-actions">' +
            actionButtonsHtml +
          '</div>';

        card.addEventListener('click', function(e) {
          if (e.target.closest('.card-btn')) return;
          openModal(icon);
        });

        card.querySelector('.copy-asset-btn').addEventListener('click', function(e) {
          e.stopPropagation();
          if (isSquircle || isPuck) {
            copyImgTag(icon);
          } else if (isGfExample) {
            copyGfTag(icon);
          } else {
            copySvgText(icon);
          }
        });

        card.querySelector('.download-asset-btn').addEventListener('click', function(e) {
          e.stopPropagation();
          if (isSquircle || isPuck) {
            downloadPng(icon);
          } else {
            downloadSvg(icon);
          }
        });

        grid.appendChild(card);
      });

      updateStyles();
    }

    function updateStyles() {
      document.documentElement.style.setProperty('--live-size', currentSize + 'px');
      document.documentElement.style.setProperty('--live-stroke', currentStroke + 'px');
      const activeColorCss = (currentColor === 'default') ? '#38bdf8' : currentColor;
      document.documentElement.style.setProperty('--live-color', activeColorCss);
    }

    function showToast(msg) {
      toast.textContent = msg;
      toast.classList.add('show');
      setTimeout(function() { toast.classList.remove('show'); }, 2000);
    }

    function copyGfTag(icon) {
      const tag = '<span class="material-symbols-outlined">' + (icon.gf_symbol || 'help') + '</span>';
      navigator.clipboard.writeText(tag).then(function() {
        showToast('Copied ' + tag);
      });
    }

    function getFullSvg(icon) {
      const isSolid = (currentSet === 'solid');
      const isDuotone = (currentSet === 'duotone');
      const isTactical = (currentSet === 'tactical');
      const isGfExample = (currentSet === 'gf-example');
      const isM3 = (currentSet === 'm3');
      const colorVal = (currentColor === 'default') ? 'currentColor' : currentColor;
      if (isGfExample) {
        return '<svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24" fill="' + colorVal + '" class="wf-icon wf-icon-gf ' + icon.id + '">\\n  ' + icon.paths_gf_example + '\\n</svg>';
      }
      if (isM3) {
        if (currentFill) {
          const filledPaths = icon.paths_m3_filled || icon.paths_m3;
          return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="' + colorVal + '" class="wf-icon wf-icon-m3 wf-icon-m3-filled ' + icon.id + '">\\n  ' + filledPaths + '\\n</svg>';
        }
        return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="' + colorVal + '" stroke-width="' + currentStroke + '" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-m3 ' + icon.id + '">\\n  ' + icon.paths_m3 + '\\n</svg>';
      }
      if (isTactical) {
        const accentCol = (currentColor === 'default') ? '#f59e0b' : currentColor;
        return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="wf-icon wf-icon-tactical ' + icon.id + '" style="--wf-accent: ' + accentCol + ';">\\n  ' + icon.paths_tactical + '\\n</svg>';
      }
      if (isDuotone) {
        const styleAttr = (currentColor === 'default') ? '' : ' style="color: ' + currentColor + '"';
        return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="wf-icon wf-icon-duotone ' + icon.id + '"' + styleAttr + '>\\n  ' + icon.paths_duotone + '\\n</svg>';
      }
      if (isSolid) {
        return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="' + colorVal + '" class="wf-icon wf-icon-solid ' + icon.id + '">\\n  ' + icon.paths_solid + '\\n</svg>';
      }
      return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="' + colorVal + '" stroke-width="' + currentStroke + '" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-line ' + icon.id + '">\\n  ' + icon.paths_line + '\\n</svg>';
    }

    function copySvgText(icon) {
      const svg = getFullSvg(icon);
      navigator.clipboard.writeText(svg).then(function() {
        showToast('Copied ' + icon.id + ' (' + currentSet + ') to clipboard!');
      });
    }

    function copyImgTag(icon) {
      const folder = (currentSet === 'png-circle') ? 'png-circle' : 'png';
      const imgTag = '<img src="' + folder + '/' + icon.id + '.png" alt="' + icon.name + '" width="64" height="64">';
      navigator.clipboard.writeText(imgTag).then(function() {
        showToast('Copied <img> tag for ' + icon.id + '!');
      });
    }

    function downloadSvg(icon) {
      const svg = getFullSvg(icon);
      const blob = new Blob([svg], { type: 'image/svg+xml' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = icon.id + '-' + currentSet + '.svg';
      a.click();
      URL.revokeObjectURL(url);
    }

    function downloadPng(icon) {
      if (currentColor === 'default') {
        const folder = (currentSet === 'png-circle') ? 'png-circle' : 'png';
        const a = document.createElement('a');
        a.href = folder + '/' + icon.id + '.png';
        a.download = icon.id + '-' + folder + '.png';
        a.click();
      } else {
        exportCustomPng(icon, currentSet === 'png-circle');
      }
    }

    // Dynamic 256x256 Canvas PNG Generator
    function exportCustomPng(icon, isPuck) {
      const ctx = exportCanvas.getContext('2d');
      ctx.clearRect(0, 0, 256, 256);
      const theme = getThemeForHex(currentColor);

      if (isPuck) {
        // Draw 3D Circular Puck
        ctx.save();
        ctx.shadowColor = theme.shadow;
        ctx.shadowBlur = 24;
        ctx.shadowOffsetY = 12;
        ctx.beginPath();
        ctx.arc(128, 128, 98, 0, Math.PI * 2);
        ctx.fillStyle = theme.mid;
        ctx.fill();
        ctx.restore();

        ctx.save();
        ctx.beginPath();
        ctx.arc(128, 128, 98, 0, Math.PI * 2);
        ctx.clip();

        const radGrad = ctx.createRadialGradient(95, 80, 5, 128, 128, 110);
        radGrad.addColorStop(0, theme.light);
        radGrad.addColorStop(0.48, theme.mid);
        radGrad.addColorStop(1, theme.dark);
        ctx.fillStyle = radGrad;
        ctx.fillRect(0, 0, 256, 256);

        // Gloss dome
        ctx.save();
        ctx.beginPath();
        ctx.ellipse(128, 65, 82, 45, 0, 0, Math.PI * 2);
        const glossGrad = ctx.createLinearGradient(128, 20, 128, 110);
        glossGrad.addColorStop(0, 'rgba(255,255,255,0.52)');
        glossGrad.addColorStop(0.65, 'rgba(255,255,255,0.08)');
        glossGrad.addColorStop(1, 'rgba(255,255,255,0)');
        ctx.fillStyle = glossGrad;
        ctx.fill();
        ctx.restore();

        ctx.lineWidth = 2.5;
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.45)';
        ctx.stroke();
      } else {
        // Draw 3D Squircle Badge
        ctx.save();
        ctx.shadowColor = theme.shadow;
        ctx.shadowBlur = 24;
        ctx.shadowOffsetY = 12;
        ctx.beginPath();
        ctx.roundRect(26, 26, 204, 204, 48);
        ctx.fillStyle = theme.mid;
        ctx.fill();
        ctx.restore();

        ctx.save();
        ctx.beginPath();
        ctx.roundRect(26, 26, 204, 204, 48);
        ctx.clip();

        const linGrad = ctx.createLinearGradient(26, 26, 230, 230);
        linGrad.addColorStop(0, theme.light);
        linGrad.addColorStop(0.55, theme.mid);
        linGrad.addColorStop(1, theme.dark);
        ctx.fillStyle = linGrad;
        ctx.fillRect(0, 0, 256, 256);

        // Gloss
        ctx.save();
        ctx.beginPath();
        ctx.ellipse(128, 50, 90, 50, 0, 0, Math.PI * 2);
        const glossGrad = ctx.createLinearGradient(128, 26, 128, 120);
        glossGrad.addColorStop(0, 'rgba(255,255,255,0.48)');
        glossGrad.addColorStop(0.7, 'rgba(255,255,255,0.08)');
        glossGrad.addColorStop(1, 'rgba(255,255,255,0)');
        ctx.fillStyle = glossGrad;
        ctx.fill();
        ctx.restore();

        ctx.lineWidth = 2;
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
        ctx.stroke();
      }

      // Draw SVG pictogram via Image
      const svgBlob = new Blob([
        '<svg xmlns="http://www.w3.org/2000/svg" width="104" height="104" viewBox="0 0 24 24" fill="#ffffff">' +
          icon.paths_solid +
        '</svg>'
      ], { type: 'image/svg+xml;charset=utf-8' });
      const url = URL.createObjectURL(svgBlob);
      const img = new Image();
      img.onload = function() {
        ctx.drawImage(img, 76, 76, 104, 104);
        ctx.restore();
        URL.revokeObjectURL(url);

        exportCanvas.toBlob(function(blob) {
          const a = document.createElement('a');
          a.href = URL.createObjectURL(blob);
          const sanitizedColor = currentColor.replace('#', '');
          a.download = icon.id + '-' + (isPuck ? 'puck' : 'badge') + '-' + sanitizedColor + '.png';
          a.click();
          showToast('Downloaded custom ' + currentColor + ' PNG!');
        });
      };
      img.src = url;
    }

    function openModal(icon) {
      selectedIcon = icon;
      const isLine = (currentSet === 'line');
      const isSolid = (currentSet === 'solid');
      const isSquircle = (currentSet === 'png');
      const isPuck = (currentSet === 'png-circle');
      const folder = isPuck ? 'png-circle' : 'png';
      const isDefaultColor = (currentColor === 'default');

      if (isSquircle || isPuck) {
        modalTitle.textContent = icon.name + (isPuck ? ' (3D Circular Puck)' : ' (3D Squircle Badge)');
        modalId.textContent = icon.id + '.png • 256x256 RGBA';
        modalCat.textContent = 'Category: ' + icon.category + ' • Keywords: ' + icon.keywords.join(', ');

        if (isDefaultColor) {
          modalPreview.innerHTML = '<img src="' + folder + '/' + icon.id + '.png" alt="' + icon.name + '">';
          modalDownloadCustom.style.display = 'none';
        } else {
          const dynamicTheme = getThemeForHex(currentColor);
          if (isPuck) {
            modalPreview.innerHTML = 
              '<div class="dynamic-puck" style="width: 72px; height: 72px; background: radial-gradient(circle at 35% 25%, ' + dynamicTheme.light + ' 0%, ' + dynamicTheme.mid + ' 45%, ' + dynamicTheme.dark + ' 100%); box-shadow: 0 14px 28px -5px ' + dynamicTheme.shadow + ', inset 0 2px 2px rgba(255,255,255,0.8);">' +
                '<div class="gloss-dome"></div>' +
                '<div class="dynamic-glyph" style="width:38px;height:38px;"><svg viewBox="0 0 24 24">' + icon.paths_solid + '</svg></div>' +
              '</div>';
          } else {
            modalPreview.innerHTML = 
              '<div class="dynamic-badge" style="width: 72px; height: 72px; background: linear-gradient(145deg, ' + dynamicTheme.light + ' 0%, ' + dynamicTheme.mid + ' 55%, ' + dynamicTheme.dark + ' 100%); box-shadow: 0 12px 24px -4px ' + dynamicTheme.shadow + ', inset 0 1.5px 1.5px rgba(255,255,255,0.7);">' +
                '<div class="gloss"></div>' +
                '<div class="dynamic-glyph" style="width:38px;height:38px;"><svg viewBox="0 0 24 24">' + icon.paths_solid + '</svg></div>' +
              '</div>';
          }
          modalDownloadCustom.style.display = 'inline-flex';
        }

        modalCodeLabel1.textContent = 'HTML Image Tag';
        modalSvgCode.textContent = '<img src="' + folder + '/' + icon.id + '.png" alt="' + icon.name + '" width="64" height="64">';

        modalCodeLabel2.textContent = 'CSS Background & Asset URL';
        modalUsageCode.textContent = '.kiosk-btn {\\n  background-image: url("' + folder + '/' + icon.id + '.png");\\n  background-size: contain;\\n  background-repeat: no-repeat;\\n  width: 64px;\\n  height: 64px;\\n}';

        modalCopySvg.textContent = 'Copy <img> Tag';
        modalCopyTag.textContent = 'Copy Asset Path';
        modalDownload.textContent = 'Download Pre-rendered .PNG';
        modalDownload.href = folder + '/' + icon.id + '.png';
      } else {
        const isDuotone = (currentSet === 'duotone');
        const isTactical = (currentSet === 'tactical');
        const isGfExample = (currentSet === 'gf-example');
        const isM3 = (currentSet === 'm3');
        const isLucide = (currentSet === 'lucide');
        const isTabler = (currentSet === 'tabler');
        let setDisplayName = 'Line';
        if (isSolid) setDisplayName = 'Solid';
        else if (isDuotone) setDisplayName = 'Duotone';
        else if (isTactical) setDisplayName = 'Tactical Cyber';
        else if (isGfExample) setDisplayName = 'GF example icons';
        else if (isM3) setDisplayName = currentFill ? 'Material 3 (Filled)' : 'Material 3';
        else if (isLucide) setDisplayName = 'Lucide Open Source (ISC/MIT)';
        else if (isTabler) setDisplayName = 'Tabler Open Source (MIT)';

        modalTitle.textContent = isGfExample ? (icon.name + ' (Google Fonts: ' + icon.gf_symbol + ')') : (icon.name + ' (' + setDisplayName + ')');
        modalId.textContent = isGfExample ? (icon.id + ' • Google Fonts Material Symbol: ' + icon.gf_symbol) : (icon.id + ' • ' + setDisplayName + ' SVG');
        modalCat.textContent = 'Category: ' + icon.category + ' • Keywords: ' + icon.keywords.join(', ');
        modalDownloadCustom.style.display = 'none';

        const colorVal = (currentColor === 'default') ? '#38bdf8' : currentColor;
        if (isGfExample) {
          modalPreview.innerHTML = wrapWithContainer('<span class="material-symbols-outlined" style="font-size: 64px; color: ' + colorVal + ';">' + icon.gf_symbol + '</span>', icon);
        } else if (isLucide) {
          modalPreview.innerHTML = wrapWithContainer('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="' + colorVal + '" stroke-width="' + currentStroke + '" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-lucide">' + icon.paths_lucide + '</svg>', icon);
        } else if (isTabler) {
          modalPreview.innerHTML = wrapWithContainer('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="' + colorVal + '" stroke-width="' + currentStroke + '" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-tabler">' + icon.paths_tabler + '</svg>', icon);
        } else if (isLucide) {
          modalPreview.innerHTML = wrapWithContainer('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="' + colorVal + '" stroke-width="' + currentStroke + '" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-lucide">' + icon.paths_lucide + '</svg>', icon);
        } else if (isTabler) {
          modalPreview.innerHTML = wrapWithContainer('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="' + colorVal + '" stroke-width="' + currentStroke + '" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-tabler">' + icon.paths_tabler + '</svg>', icon);
        } else if (isM3) {
          if (currentFill) {
            const filledPaths = icon.paths_m3_filled || icon.paths_m3;
            modalPreview.innerHTML = wrapWithContainer('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="' + colorVal + '" class="wf-icon wf-icon-m3 wf-icon-m3-filled">' + filledPaths + '</svg>', icon);
          } else {
            modalPreview.innerHTML = wrapWithContainer('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="' + colorVal + '" stroke-width="' + currentStroke + '" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-m3">' + icon.paths_m3 + '</svg>', icon);
          }
        } else if (isTactical) {
          const accentCol = (currentColor === 'default') ? '#f59e0b' : currentColor;
          modalPreview.innerHTML = wrapWithContainer('<div style="width: 72px; height: 72px;"><svg viewBox="0 0 24 24" class="wf-icon wf-icon-tactical" style="width:100%;height:100%;--wf-accent:' + accentCol + ';">' + icon.paths_tactical + '</svg></div>', icon);
        } else if (isDuotone) {
          modalPreview.innerHTML = wrapWithContainer('<div style="color: ' + colorVal + '; width: 72px; height: 72px;"><svg viewBox="0 0 24 24" style="width:100%;height:100%;">' + icon.paths_duotone + '</svg></div>', icon);
        } else if (isSolid) {
          modalPreview.innerHTML = wrapWithContainer('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="' + colorVal + '">' + icon.paths_solid + '</svg>', icon);
        } else {
          modalPreview.innerHTML = wrapWithContainer('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="' + colorVal + '" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">' + icon.paths_line + '</svg>', icon);
        }
        
        if (isGfExample) {
          modalCodeLabel1.textContent = 'Google Fonts HTML Tag';
          modalSvgCode.textContent = '<span class="material-symbols-outlined">' + icon.gf_symbol + '</span>';

          modalCodeLabel2.textContent = 'Google Fonts Spec & Official Link';
          const gfUrl = 'https://fonts.google.com/icons?selected=Material+Symbols+Outlined:' + icon.gf_symbol + ':FILL@0;wght@400;GRAD@0;opsz@48';
          modalUsageCode.textContent = '<!-- Google Fonts Material Symbol -->\\nSymbol: ' + icon.gf_symbol + '\\nFamily: Material Symbols Outlined\\nURL: ' + gfUrl + '\\n\\n<!-- Sprite / Web Component -->\\n<wf-icon name="' + icon.id + '" set="gf-example" size="32"></wf-icon>\\n<svg class="wf-icon wf-icon-gf"><use href="dist/wayfinding-icons-gf-example.svg#' + icon.id + '"></use></svg>';

          modalCopySvg.textContent = 'Copy <span> Tag';
          modalCopyTag.textContent = 'Copy GF URL';
          modalDownload.textContent = 'Download .SVG';
          modalDownload.href = 'svg/gf-example/' + icon.id + '.svg';
        } else {
          modalCodeLabel1.textContent = 'Raw SVG Code';
          const rawSvg = getFullSvg(icon);
          modalSvgCode.textContent = rawSvg;

          modalCodeLabel2.textContent = 'Web Component / Sprite Tag';
          if (isLucide) {
            usageCode = '<!-- Lucide Open Source Icon (ISC License - 100% Free for Commercial Use) -->\\n<wf-icon name="' + icon.id + '" set="lucide" size="32"></wf-icon>\\n\\n<!-- SVG Sprite Symbol -->\\n<svg class="wf-icon wf-icon-lucide"><use href="dist/wayfinding-icons-lucide.svg#' + icon.id + '"></use></svg>';
          } else if (isTabler) {
            usageCode = '<!-- Tabler Open Source Icon (MIT License - 100% Free for Commercial Use) -->\\n<wf-icon name="' + icon.id + '" set="tabler" size="32"></wf-icon>\\n\\n<!-- SVG Sprite Symbol -->\\n<svg class="wf-icon wf-icon-tabler"><use href="dist/wayfinding-icons-tabler.svg#' + icon.id + '"></use></svg>';
          } else if (isM3) {
            usageCode = '<!-- Web Component (Material 3) -->\\n<wf-icon name="' + icon.id + '" set="m3" size="32"></wf-icon>\\n\\n<!-- SVG Sprite Symbol -->\\n<svg class="wf-icon wf-icon-m3"><use href="dist/wayfinding-icons-m3.svg#' + icon.id + '"></use></svg>';
          } else if (isTactical) {
            usageCode = '<!-- Web Component (Tactical Cyber) -->\\n<wf-icon name="' + icon.id + '" set="tactical" size="32"></wf-icon>\\n\\n<!-- SVG Sprite Symbol -->\\n<svg class="wf-icon wf-icon-tactical"><use href="dist/wayfinding-icons-tactical.svg#' + icon.id + '"></use></svg>';
          } else if (isDuotone) {
            usageCode = '<!-- Web Component (Duotone) -->\\n<wf-icon name="' + icon.id + '" set="duotone" size="32"></wf-icon>\\n\\n<!-- SVG Sprite Symbol -->\\n<svg class="wf-icon wf-icon-duotone"><use href="dist/wayfinding-icons-duotone.svg#' + icon.id + '"></use></svg>';
          } else if (isSolid) {
            usageCode = '<!-- Web Component (Solid) -->\\n<wf-icon name="' + icon.id + '" set="solid" size="32"></wf-icon>\\n\\n<!-- SVG Sprite Symbol -->\\n<svg class="wf-icon"><use href="dist/wayfinding-icons-solid.svg#' + icon.id + '"></use></svg>';
          } else {
            usageCode = '<!-- Web Component (Line) -->\\n<wf-icon name="' + icon.id + '" set="line" size="32"></wf-icon>\\n\\n<!-- SVG Sprite Symbol -->\\n<svg class="wf-icon"><use href="dist/wayfinding-icons-line.svg#' + icon.id + '"></use></svg>';
          }
          modalUsageCode.textContent = usageCode;

          modalCopySvg.textContent = 'Copy Raw SVG';
          modalCopyTag.textContent = 'Copy <wf-icon>';
          modalDownload.textContent = 'Download .SVG';
          modalDownload.href = 'svg/' + currentSet + '/' + icon.id + '.svg';
        }
      }

      modalOverlay.classList.add('active');
    }

    function closeModal() {
      modalOverlay.classList.remove('active');
    }

    // Set dropdown change listener
    setSelect.addEventListener('change', function(e) {
      currentSet = e.target.value;
      // Reset fill to outline when switching sets
      currentFill = false;
      fillBtnOutline.classList.add('active');
      fillBtnFilled.classList.remove('active');
      // Show fill toggle only for M3
      if (currentSet === 'm3') {
        fillToggleGroup.classList.add('m3-active');
      } else {
        fillToggleGroup.classList.remove('m3-active');
      }
      renderIcons();
    });

    // Fill toggle button listeners (M3 only)
    fillBtnOutline.addEventListener('click', function() {
      currentFill = false;
      fillBtnOutline.classList.add('active');
      fillBtnFilled.classList.remove('active');
      renderBanner();
      renderIcons();
    });
    fillBtnFilled.addEventListener('click', function() {
      currentFill = true;
      fillBtnFilled.classList.add('active');
      fillBtnOutline.classList.remove('active');
      renderBanner();
      renderIcons();
    });

        // Container shape listeners (None, Tile, Outline, Circle)
    function setContainerShape(shape) {
      currentContainer = shape;
      containerBtns.forEach(function(b) {
        if (b) b.classList.remove('active');
      });
      if (shape === 'none' && cbNone) cbNone.classList.add('active');
      else if (shape === 'tile' && cbTile) cbTile.classList.add('active');
      else if (shape === 'outline' && cbOutline) cbOutline.classList.add('active');
      else if (shape === 'circle' && cbCircle) cbCircle.classList.add('active');
      renderIcons();
    }

    if (cbNone) cbNone.addEventListener('click', function() { setContainerShape('none'); });
    if (cbTile) cbTile.addEventListener('click', function() { setContainerShape('tile'); });
    if (cbOutline) cbOutline.addEventListener('click', function() { setContainerShape('outline'); });
    if (cbCircle) cbCircle.addEventListener('click', function() { setContainerShape('circle'); });

    // Search and filter listeners
    searchBox.addEventListener('input', function(e) {
      currentSearch = e.target.value;
      renderIcons();
    });

    categoryPills.addEventListener('click', function(e) {
      if (!e.target.classList.contains('pill')) return;
      categoryPills.querySelectorAll('.pill').forEach(function(p) { p.classList.remove('active'); });
      e.target.classList.add('active');
      currentCategory = e.target.dataset.cat;
      renderIcons();
    });

    sizeSlider.addEventListener('input', function(e) {
      currentSize = e.target.value;
      sizeLabel.textContent = currentSize + 'px';
      updateStyles();
    });

    strokeSlider.addEventListener('input', function(e) {
      currentStroke = parseFloat(e.target.value).toFixed(2);
      strokeLabel.textContent = currentStroke + 'px';
      updateStyles();
    });

    // Swatches listener
    document.querySelectorAll('.color-swatch').forEach(function(swatch) {
      swatch.addEventListener('click', function() {
        document.querySelectorAll('.color-swatch').forEach(function(s) { s.classList.remove('active'); });
        swatch.classList.add('active');
        currentColor = swatch.dataset.color;
        if (currentColor !== 'default') {
          hexColorPicker.value = currentColor;
          hexColorInput.value = currentColor.toUpperCase();
        }
        renderIcons();
      });
    });

    // Custom Hex Color Picker listener
    hexColorPicker.addEventListener('input', function(e) {
      document.querySelectorAll('.color-swatch').forEach(function(s) { s.classList.remove('active'); });
      currentColor = e.target.value;
      hexColorInput.value = currentColor.toUpperCase();
      renderIcons();
    });

    // Custom Hex Text Input listener
    hexColorInput.addEventListener('input', function(e) {
      let val = e.target.value.trim();
      if (!val.startsWith('#')) val = '#' + val;
      if (/^#[0-9A-Fa-f]{6}$/.test(val)) {
        document.querySelectorAll('.color-swatch').forEach(function(s) { s.classList.remove('active'); });
        currentColor = val.toLowerCase();
        hexColorPicker.value = currentColor;
        renderIcons();
      }
    });

    modalClose.addEventListener('click', closeModal);
    modalOverlay.addEventListener('click', function(e) {
      if (e.target === modalOverlay) closeModal();
    });

    modalCopySvg.addEventListener('click', function() {
      if (!selectedIcon) return;
      if (currentSet === 'png' || currentSet === 'png-circle') {
        copyImgTag(selectedIcon);
      } else if (currentSet === 'gf-example') {
        copyGfTag(selectedIcon);
      } else {
        copySvgText(selectedIcon);
      }
    });

    modalCopyTag.addEventListener('click', function() {
      if (!selectedIcon) return;
      const isPng = (currentSet === 'png' || currentSet === 'png-circle');
      if (isPng) {
        const folder = (currentSet === 'png-circle') ? 'png-circle' : 'png';
        navigator.clipboard.writeText(folder + '/' + selectedIcon.id + '.png').then(function() {
          showToast('Copied: ' + folder + '/' + selectedIcon.id + '.png');
        });
      } else if (currentSet === 'gf-example') {
        const gfUrl = 'https://fonts.google.com/icons?selected=Material+Symbols+Outlined:' + selectedIcon.gf_symbol + ':FILL@0;wght@400;GRAD@0;opsz@48';
        navigator.clipboard.writeText(gfUrl).then(function() {
          showToast('Copied Google Fonts URL!');
        });
      } else {
        navigator.clipboard.writeText('<wf-icon name="' + selectedIcon.id + '" set="' + currentSet + '" size="32"></wf-icon>').then(function() {
          showToast('Copied <wf-icon> (' + currentSet + ') tag!');
        });
      }
    });

    modalDownloadCustom.addEventListener('click', function() {
      if (selectedIcon) {
        exportCustomPng(selectedIcon, currentSet === 'png-circle');
      }
    });

    themeToggle.addEventListener('click', function() {
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'light' ? 'dark' : 'light';
      document.documentElement.setAttribute('data-theme', next);
    });

    // Initial render
    renderIcons();
  </script>
</body>
</html>
"""

final_html = html_template.replace("__CATEGORY_PILLS__", category_pills_html)
final_html = final_html.replace("__METADATA_JSON__", json.dumps(metadata))

showcase_path = os.path.join(BASE_DIR, "index.html")
with open(showcase_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print("Updated index.html successfully with 8 design sets including Material 3 (M3 Clean Vector SVG), GF example icons, and dynamic hex color recoloring!")
