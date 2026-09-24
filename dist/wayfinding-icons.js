/**
 * Wayfinding Kiosk Icon Library (JavaScript / Web Component)
 * Supports both 'line' and 'solid' sets
 */

export const WAYFINDING_LINE = {
  "wf-arrow-up": "<path d=\"M12 19V5\"/><path d=\"m5 12 7-7 7 7\"/>",
  "wf-arrow-right": "<path d=\"M5 12h14\"/><path d=\"m12 5 7 7-7 7\"/>",
  "wf-arrow-down": "<path d=\"M12 5v14\"/><path d=\"m19 12-7 7-7-7\"/>",
  "wf-arrow-left": "<path d=\"M19 12H5\"/><path d=\"m12 19-7-7 7-7\"/>",
  "wf-arrow-up-right": "<path d=\"M7 17 17 7\"/><path d=\"M8 7h9v9\"/>",
  "wf-arrow-up-left": "<path d=\"m17 17-10-10\"/><path d=\"M16 7H7v9\"/>",
  "wf-u-turn": "<path d=\"M9 10v7\"/><path d=\"m5 13 4 4 4-4\"/><path d=\"M9 10a5 5 0 0 1 10 0v8\"/>",
  "wf-signpost": "<path d=\"M12 3v18\"/><path d=\"M12 5H5a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h7l2-2.5L12 5z\"/><path d=\"M12 12h7a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-7l-2-2.5 2-2.5z\"/>",
  "wf-pin": "<path d=\"M12 21s-6-5.686-6-10a6 6 0 0 1 12 0c0 4.314-6 10-6 10z\"/><circle cx=\"12\" cy=\"11\" r=\"2.5\"/>",
  "wf-facing": "<circle cx=\"12\" cy=\"12\" r=\"9\"/><polygon points=\"12 4 15 12 12 10 9 12 12 4\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"17\" r=\"1\" fill=\"currentColor\"/>",
  "wf-map": "<polygon points=\"3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21\"/><line x1=\"9\" y1=\"3\" x2=\"9\" y2=\"18\"/><line x1=\"15\" y1=\"6\" x2=\"15\" y2=\"21\"/>",
  "wf-touch": "<path d=\"M12 11V6a1.5 1.5 0 0 1 3 0v5\"/><path d=\"M15 9.5a1.5 1.5 0 0 1 3 0V12a1.5 1.5 0 0 1 3 0v3a6 6 0 0 1-6 6h-2a6 6 0 0 1-4.24-1.76L5 15.4a1.5 1.5 0 0 1 2.2-2L9.5 15V6a1.5 1.5 0 0 1 3 0v5\"/><path d=\"M12 3a9 9 0 0 1 9 9\"/><path d=\"M12 6a6 6 0 0 1 6 6\"/>",
  "wf-entrance": "<path d=\"M14 20V4a1 1 0 0 1 1-1h5a1 1 0 0 1 1 1v16\"/><path d=\"m14 4-7 2.5v12l7 1.5\"/><circle cx=\"10\" cy=\"12\" r=\"0.75\" fill=\"currentColor\"/><line x1=\"2\" y1=\"20\" x2=\"22\" y2=\"20\"/><path d=\"M2 11h8\"/><path d=\"m7 7.5 3.5 3.5-3.5 3.5\"/>",
  "wf-exit": "<path d=\"M10 20V4a1 1 0 0 0-1-1H4a1 1 0 0 0-1 1v16\"/><path d=\"m10 4 7 2.5v12l-7 1.5\"/><circle cx=\"14\" cy=\"12\" r=\"0.75\" fill=\"currentColor\"/><line x1=\"2\" y1=\"20\" x2=\"22\" y2=\"20\"/><path d=\"M14 11h8\"/><path d=\"m18.5 7.5 3.5 3.5-3.5 3.5\"/>",
  "wf-lift": "<rect x=\"3\" y=\"3\" width=\"12\" height=\"18\" rx=\"2\"/><circle cx=\"6.5\" cy=\"8\" r=\"1.4\"/><path d=\"M4.5 16.5v-2a1.8 1.8 0 0 1 3.6 0v2\"/><circle cx=\"11.5\" cy=\"8\" r=\"1.4\"/><path d=\"M9.7 16.5v-2a1.8 1.8 0 0 1 3.6 0v2\"/><polygon points=\"18.5 4.5 15.5 8.5 21.5 8.5\" fill=\"currentColor\"/><polygon points=\"18.5 19.5 15.5 15.5 21.5 15.5\" fill=\"currentColor\"/><line x1=\"18.5\" y1=\"11\" x2=\"18.5\" y2=\"13\"/>",
  "wf-stairs": "<path d=\"M4 19h4v-4h4v-4h4V7h4\"/><circle cx=\"7\" cy=\"6\" r=\"2\"/><path d=\"m11 11-2-2.5-3 1.5\"/>",
  "wf-escalator-up": "<path d=\"M3 7h4l7 10h7\"/><path d=\"m5 17 4-4\"/><path d=\"M5 13h4v4\"/><circle cx=\"6\" cy=\"4\" r=\"1.5\"/><path d=\"m8 9-2-2-3 2\"/>",
  "wf-escalator-down": "<path d=\"M3 17h4l7-10h7\"/><path d=\"m19 17-4-4\"/><path d=\"M15 17h4v-4\"/><circle cx=\"18\" cy=\"4\" r=\"1.5\"/><path d=\"m16 9 2-2 3 2\"/>",
  "wf-ramp": "<polygon points=\"3 19 21 19 21 11 3 19\"/><circle cx=\"14\" cy=\"7\" r=\"1.5\"/><path d=\"M12 14a2.5 2.5 0 0 1 3-2.4l1.5-1.6\"/>",
  "wf-accessible": "<circle cx=\"12\" cy=\"4.5\" r=\"2\"/><path d=\"M10 9h3.5l1.5 5h3\"/><path d=\"M13.5 14A4 4 0 1 1 8 11.5\"/><path d=\"M8 12h3\"/>",
  "wf-levels": "<polygon points=\"12 3 21 7.5 12 12 3 7.5 12 3\"/><polyline points=\"3 12 12 16.5 21 12\"/><polyline points=\"3 16.5 12 21 21 16.5\"/>",
  "wf-no-entry": "<circle cx=\"12\" cy=\"12\" r=\"9\"/><line x1=\"6\" y1=\"12\" x2=\"18\" y2=\"12\" stroke-width=\"3\"/>",
  "wf-prohibited": "<circle cx=\"12\" cy=\"12\" r=\"9\"/><line x1=\"5.6\" y1=\"5.6\" x2=\"18.4\" y2=\"18.4\"/>",
  "wf-staff-only": "<rect x=\"5\" y=\"8\" width=\"14\" height=\"13\" rx=\"2\"/><circle cx=\"12\" cy=\"13\" r=\"2.5\"/><path d=\"M9 19c0-1.7 1.3-3 3-3s3 1.3 3 3\"/><path d=\"M9 8V5a3 3 0 0 1 6 0v3\"/>",
  "wf-toilets": "<line x1=\"12\" y1=\"4\" x2=\"12\" y2=\"20\"/><circle cx=\"7\" cy=\"5\" r=\"1.5\"/><path d=\"M5 9h4v6H8v5H6v-5H5V9z\"/><circle cx=\"17\" cy=\"5\" r=\"1.5\"/><path d=\"M15 15l-1-6h6l-1 6h-4z\"/><path d=\"M16 15v5h2v-5\"/>",
  "wf-toilet-male": "<circle cx=\"12\" cy=\"4\" r=\"2\"/><path d=\"M9 8h6a1 1 0 0 1 1 1v6h-2v6h-4v-6H8V9a1 1 0 0 1 1-1z\"/>",
  "wf-toilet-female": "<circle cx=\"12\" cy=\"4\" r=\"2\"/><path d=\"M9.5 8h5l2.5 8h-4v5h-2v-5H7l2.5-8z\"/>",
  "wf-toilet-accessible": "<circle cx=\"10\" cy=\"5\" r=\"1.8\"/><path d=\"M8 9h3l1.5 4h2.5\"/><path d=\"M11 13a3.5 3.5 0 1 1-5-2\"/><path d=\"M17 9h4v11h-4\"/><path d=\"M19 12v3\"/>",
  "wf-baby-change": "<line x1=\"3\" y1=\"18\" x2=\"21\" y2=\"18\"/><circle cx=\"7\" cy=\"9\" r=\"2.5\"/><path d=\"M10 13c1.5 0 3-1 4-2 1.5 1.5 3.5 1.5 5 1\"/><path d=\"M12 4v4\"/><path d=\"m10 6 4 0\"/>",
  "wf-cafe": "<path d=\"M18 8h1a4 4 0 0 1 0 8h-1\"/><path d=\"M2 8h16v7a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z\"/><line x1=\"6\" y1=\"2\" x2=\"6\" y2=\"5\"/><line x1=\"10\" y1=\"2\" x2=\"10\" y2=\"5\"/><line x1=\"14\" y1=\"2\" x2=\"14\" y2=\"5\"/>",
  "wf-food": "<path d=\"M18 2v20\"/><path d=\"M21 2c0 4-3 5-3 8\"/><path d=\"M3 2v6c0 1.7 1.3 3 3 3v11\"/><path d=\"M6 2v6\"/><path d=\"M9 2v6c0 1.7-1.3 3-3 3\"/>",
  "wf-retail": "<path d=\"M6 8V6a6 6 0 0 1 12 0v2\"/><rect x=\"4\" y=\"8\" width=\"16\" height=\"13\" rx=\"2\"/><circle cx=\"9\" cy=\"13\" r=\"1\" fill=\"currentColor\"/><circle cx=\"15\" cy=\"13\" r=\"1\" fill=\"currentColor\"/>",
  "wf-atm": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"16\" rx=\"2\"/><line x1=\"7\" y1=\"9\" x2=\"17\" y2=\"9\"/><line x1=\"7\" y1=\"13\" x2=\"12\" y2=\"13\"/><rect x=\"14\" y=\"12\" width=\"3\" height=\"4\" rx=\"0.5\"/>",
  "wf-payment": "<rect x=\"2\" y=\"5\" width=\"20\" height=\"14\" rx=\"2\"/><line x1=\"2\" y1=\"10\" x2=\"22\" y2=\"10\"/><circle cx=\"7\" cy=\"15\" r=\"1.5\"/><circle cx=\"11\" cy=\"15\" r=\"1.5\"/>",
  "wf-pharmacy": "<path d=\"M12 3v18\"/><path d=\"M3 12h18\"/><circle cx=\"12\" cy=\"12\" r=\"9\"/>",
  "wf-water": "<path d=\"M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z\"/><path d=\"M12 18a4 4 0 0 0 4-4\"/>",
  "wf-wifi": "<path d=\"M5 12.55a11 11 0 0 1 14.08 0\"/><path d=\"M1.42 9a16 16 0 0 1 21.16 0\"/><path d=\"M8.53 16.11a6 6 0 0 1 6.95 0\"/><circle cx=\"12\" cy=\"19.5\" r=\"1.2\" fill=\"currentColor\"/>",
  "wf-seating": "<path d=\"M5 11V6a3 3 0 0 1 6 0v5\"/><path d=\"M13 11V6a3 3 0 0 1 6 0v5\"/><rect x=\"3\" y=\"11\" width=\"18\" height=\"5\" rx=\"1.5\"/><path d=\"M5 16v5\"/><path d=\"M19 16v5\"/>",
  "wf-parking": "<rect x=\"3\" y=\"3\" width=\"18\" height=\"18\" rx=\"3\"/><path d=\"M9 17V7h4.5a3.5 3.5 0 0 1 0 7H9\"/>",
  "wf-car": "<path d=\"M4 17h16\"/><path d=\"M5 17l1.5-6h11l1.5 6\"/><circle cx=\"7.5\" cy=\"17\" r=\"2\"/><circle cx=\"16.5\" cy=\"17\" r=\"2\"/><path d=\"M7 11l1.5-4.5a1.5 1.5 0 0 1 1.4-1h4.2a1.5 1.5 0 0 1 1.4 1L17 11\"/>",
  "wf-bus": "<rect x=\"4\" y=\"3\" width=\"16\" height=\"15\" rx=\"3\"/><line x1=\"4\" y1=\"10\" x2=\"20\" y2=\"10\"/><circle cx=\"8\" cy=\"14\" r=\"1.5\"/><circle cx=\"16\" cy=\"14\" r=\"1.5\"/><path d=\"M6 18v3\"/><path d=\"M18 18v3\"/><line x1=\"9\" y1=\"6\" x2=\"15\" y2=\"6\"/>",
  "wf-ev": "<rect x=\"3\" y=\"4\" width=\"12\" height=\"16\" rx=\"2\"/><path d=\"m8 9 2-3v4h2l-3 4v-3H7l2-2\"/><path d=\"M15 9h3a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2h-1\"/><circle cx=\"17\" cy=\"17\" r=\"1\"/>",
  "wf-info": "<circle cx=\"12\" cy=\"12\" r=\"9\"/><circle cx=\"12\" cy=\"8\" r=\"1.2\" fill=\"currentColor\"/><path d=\"M11 12h2v5h-2z\"/>",
  "wf-help": "<circle cx=\"12\" cy=\"12\" r=\"9\"/><path d=\"M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3\"/><circle cx=\"12\" cy=\"17\" r=\"1\" fill=\"currentColor\"/>",
  "wf-reception": "<path d=\"M4 19h16\"/><path d=\"M4 15h16\"/><path d=\"M12 4v4\"/><path d=\"M8 8a4 4 0 0 1 8 0H8z\"/><path d=\"M10 15v-3h4v3\"/>",
  "wf-security": "<path d=\"M12 3s7 2.5 7 8c0 5.5-5 9.5-7 10-2-.5-7-4.5-7-10 0-5.5 7-8 7-8z\"/><path d=\"m9 12 2 2 4-4\"/>",
  "wf-phone": "<path d=\"M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z\"/>",
  "wf-intercom": "<rect x=\"6\" y=\"3\" width=\"12\" height=\"18\" rx=\"2\"/><circle cx=\"12\" cy=\"8\" r=\"2\"/><line x1=\"9\" y1=\"13\" x2=\"15\" y2=\"13\"/><circle cx=\"12\" cy=\"17\" r=\"1.5\" fill=\"currentColor\"/>",
  "wf-hospital": "<path d=\"M3 21h18\"/><path d=\"M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16\"/><path d=\"M12 7v6\"/><path d=\"M9 10h6\"/><rect x=\"9.5\" y=\"16\" width=\"5\" height=\"5\"/>",
  "wf-first-aid": "<rect x=\"3\" y=\"7\" width=\"18\" height=\"14\" rx=\"2\"/><path d=\"M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2\"/><path d=\"M12 11v6\"/><path d=\"M9 14h6\"/>",
  "wf-consult": "<path d=\"M6 3v5a6 6 0 0 0 12 0V3\"/><circle cx=\"6\" cy=\"3\" r=\"1\" fill=\"currentColor\"/><circle cx=\"18\" cy=\"3\" r=\"1\" fill=\"currentColor\"/><path d=\"M12 14v4a3 3 0 0 0 6 0v-2\"/><circle cx=\"18\" cy=\"16\" r=\"2\"/>",
  "wf-pathology": "<path d=\"M9 3h6\"/><path d=\"M10 3v5l-4.5 9A2 2 0 0 0 7.3 20h9.4a2 2 0 0 0 1.8-3L14 8V3\"/><line x1=\"7.5\" y1=\"15\" x2=\"16.5\" y2=\"15\"/>",
  "wf-aed": "<path d=\"M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z\"/><polygon points=\"12.5 6 9.5 12 13 12 11.5 17 15.5 11 12 11 12.5 6\" fill=\"currentColor\"/>",
  "wf-student": "<polygon points=\"12 3 22 8.5 12 14 2 8.5 12 3\"/><path d=\"M6 10.7v5.3c0 2.2 2.7 4 6 4s6-1.8 6-4v-5.3\"/><path d=\"M22 8.5v6\"/>",
  "wf-library": "<path d=\"M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5z\"/><path d=\"M4 6h16\"/><line x1=\"8\" y1=\"10\" x2=\"16\" y2=\"10\"/><line x1=\"8\" y1=\"14\" x2=\"14\" y2=\"14\"/>",
  "wf-lecture": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"12\" rx=\"2\"/><line x1=\"3\" y1=\"12\" x2=\"21\" y2=\"12\"/><path d=\"M9 16l-2 5\"/><path d=\"M15 16l2 5\"/><circle cx=\"12\" cy=\"8\" r=\"2\"/>",
  "wf-emergency": "<polygon points=\"12 2 21.5 7.5 21.5 16.5 12 22 2.5 16.5 2.5 7.5 12 2\"/><line x1=\"12\" y1=\"8\" x2=\"12\" y2=\"13\"/><circle cx=\"12\" cy=\"16.5\" r=\"1\" fill=\"currentColor\"/>",
  "wf-evacuate": "<path d=\"M19 3v18h-6\"/><circle cx=\"7.5\" cy=\"5.5\" r=\"1.5\"/><path d=\"M5 10l3-2 3 2.5v4\"/><path d=\"m8 10-3 5\"/><path d=\"m8 14 3 6\"/><path d=\"m11 10.5 4-1.5\"/>",
  "wf-assembly": "<circle cx=\"12\" cy=\"12\" r=\"3\"/><path d=\"M4 4l4 4\"/><path d=\"M4 8V4h4\"/><path d=\"M20 4l-4 4\"/><path d=\"M20 8V4h-4\"/><path d=\"M4 20l4-4\"/><path d=\"M4 16v4h4\"/><path d=\"M20 20l-4-4\"/><path d=\"M20 16v4h-4\"/>",
  "wf-fire": "<path d=\"M12 2c1 3 4 5 4 9a6 6 0 0 1-12 0c0-3.5 2.5-6.5 4-8 1 2 2 3 4-1z\"/><path d=\"M12 13a2.5 2.5 0 0 0-2.5 2.5c0 1.38 1.12 2.5 2.5 2.5s2.5-1.12 2.5-2.5c0-1-.8-1.8-1.5-2.2-.3.3-.6.5-1 .2z\"/>",
  "wf-warning": "<path d=\"m10.29 3.86-8.57 14.85A2 2 0 0 0 3.45 22h17.1a2 2 0 0 0 1.73-3.29L13.71 3.86a2 2 0 0 0-3.42 0z\"/><line x1=\"12\" y1=\"9\" x2=\"12\" y2=\"14\"/><circle cx=\"12\" cy=\"18\" r=\"1\" fill=\"currentColor\"/>",
  "wf-construction": "<polygon points=\"12 2 17 19 7 19 12 2\"/><line x1=\"3\" y1=\"21\" x2=\"21\" y2=\"21\"/><line x1=\"8.5\" y1=\"14\" x2=\"15.5\" y2=\"14\"/><line x1=\"10\" y1=\"9\" x2=\"14\" y2=\"9\"/>",
  "wf-home": "<path d=\"m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V9z\"/><polyline points=\"9 22 9 12 15 12 15 22\"/>",
  "wf-search": "<circle cx=\"11\" cy=\"11\" r=\"7\"/><line x1=\"21\" y1=\"21\" x2=\"16.65\" y2=\"16.65\"/>",
  "wf-menu": "<line x1=\"4\" y1=\"6\" x2=\"20\" y2=\"6\"/><line x1=\"4\" y1=\"12\" x2=\"20\" y2=\"12\"/><line x1=\"4\" y1=\"18\" x2=\"20\" y2=\"18\"/>",
  "wf-back": "<polyline points=\"15 18 9 12 15 6\"/>",
  "wf-close": "<line x1=\"18\" y1=\"6\" x2=\"6\" y2=\"18\"/><line x1=\"6\" y1=\"6\" x2=\"18\" y2=\"18\"/>",
  "wf-hours": "<circle cx=\"12\" cy=\"12\" r=\"9\"/><polyline points=\"12 6 12 12 16 14\"/>",
  "wf-timetable": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"17\" rx=\"2\"/><line x1=\"3\" y1=\"9\" x2=\"21\" y2=\"9\"/><line x1=\"8\" y1=\"2\" x2=\"8\" y2=\"6\"/><line x1=\"16\" y1=\"2\" x2=\"16\" y2=\"6\"/><line x1=\"7\" y1=\"13\" x2=\"17\" y2=\"13\"/><line x1=\"7\" y1=\"17\" x2=\"13\" y2=\"17\"/>",
  "wf-events": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"17\" rx=\"2\"/><line x1=\"3\" y1=\"9\" x2=\"21\" y2=\"9\"/><line x1=\"8\" y1=\"2\" x2=\"8\" y2=\"6\"/><line x1=\"16\" y1=\"2\" x2=\"16\" y2=\"6\"/><polygon points=\"12 12 13.2 14.5 16 14.9 14 16.8 14.5 19.5 12 18.2 9.5 19.5 10 16.8 8 14.9 10.8 14.5 12 12\" fill=\"currentColor\"/>",
  "wf-news": "<path d=\"M4 20h14a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2z\"/><line x1=\"6\" y1=\"6\" x2=\"14\" y2=\"6\"/><line x1=\"6\" y1=\"10\" x2=\"18\" y2=\"10\"/><line x1=\"6\" y1=\"14\" x2=\"18\" y2=\"14\"/>",
  "wf-announce": "<path d=\"m3 11 15-5v12L3 13v-2z\"/><path d=\"M11 13.5V19a2 2 0 0 1-2 2H8\"/><path d=\"M19 9a4 4 0 0 1 0 6\"/>",
  "wf-share": "<circle cx=\"18\" cy=\"5\" r=\"3\"/><circle cx=\"6\" cy=\"12\" r=\"3\"/><circle cx=\"18\" cy=\"19\" r=\"3\"/><line x1=\"8.59\" y1=\"13.51\" x2=\"15.42\" y2=\"17.49\"/><line x1=\"15.41\" y1=\"6.51\" x2=\"8.59\" y2=\"10.49\"/>",
  "wf-chat": "<path d=\"M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z\"/>",
  "wf-like": "<path d=\"M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3H14z\"/><path d=\"M7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3\"/>",
  "wf-camera": "<path d=\"M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z\"/><circle cx=\"12\" cy=\"13\" r=\"4\"/>",
  "wf-video": "<polygon points=\"23 7 16 12 23 17 23 7\"/><rect x=\"1\" y=\"5\" width=\"15\" height=\"14\" rx=\"2\"/>",
  "wf-qr": "<rect x=\"3\" y=\"3\" width=\"7\" height=\"7\"/><rect x=\"14\" y=\"3\" width=\"7\" height=\"7\"/><rect x=\"3\" y=\"14\" width=\"7\" height=\"7\"/><rect x=\"15\" y=\"15\" width=\"2\" height=\"2\"/><rect x=\"19\" y=\"15\" width=\"2\" height=\"2\"/><rect x=\"15\" y=\"19\" width=\"6\" height=\"2\"/><path d=\"M6 6h1v1H6z\" fill=\"currentColor\"/><path d=\"M17 6h1v1h-1z\" fill=\"currentColor\"/><path d=\"M6 17h1v1H6z\" fill=\"currentColor\"/>",
  "wf-email": "<rect x=\"2\" y=\"4\" width=\"20\" height=\"16\" rx=\"2\"/><path d=\"m22 7-10 7L2 7\"/>",
  "wf-web": "<circle cx=\"12\" cy=\"12\" r=\"9\"/><line x1=\"3\" y1=\"12\" x2=\"21\" y2=\"12\"/><path d=\"M12 3a15 15 0 0 1 4 9 15 15 0 0 1-4 9 15 15 0 0 1-4-9 15 15 0 0 1 4-9z\"/>"
};
export const WAYFINDING_TACTICAL = {
  "wf-arrow-up": "<polygon points=\"12 2 20 10 15 10 15 21 9 21 9 10 4 10\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"12 2 12 21 9 21 9 10 4 10\" fill=\"var(--wf-accent-light, #fbbf24)\" opacity=\"0.35\"/>\n<polygon points=\"15 10 20 10 15 21\" fill=\"#334155\" opacity=\"0.4\"/>\n<line x1=\"12\" y1=\"2\" x2=\"12\" y2=\"21\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>",
  "wf-arrow-right": "<polygon points=\"22 12 14 4 14 9 3 9 3 15 14 15 14 20\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"22 12 3 12 3 9 14 9 14 4\" fill=\"var(--wf-accent-light, #fbbf24)\" opacity=\"0.4\"/>\n<polygon points=\"14 15 22 12 14 20\" fill=\"#334155\" opacity=\"0.5\"/>\n<line x1=\"3\" y1=\"12\" x2=\"22\" y2=\"12\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>",
  "wf-arrow-down": "<polygon points=\"12 22 4 14 9 14 9 3 15 3 15 14 20 14\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"12 22 12 3 9 3 9 14 4 14\" fill=\"var(--wf-accent-light, #fbbf24)\" opacity=\"0.4\"/>\n<polygon points=\"15 14 12 22 15 3\" fill=\"#334155\" opacity=\"0.5\"/>\n<line x1=\"12\" y1=\"3\" x2=\"12\" y2=\"22\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>",
  "wf-arrow-left": "<path d=\"M18 5A8 8 0 0 0 6 12l-3-3v8h8l-3-3a6 6 0 0 1 10-2z\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"6 12 3 9 3 17 11 17 8 14\" fill=\"var(--wf-accent-light, #fbbf24)\"/>\n<polygon points=\"19 2 20.5 5 23.5 6.5 20.5 8 19 11 17.5 8 14.5 6.5 17.5 5\" fill=\"var(--wf-accent-light, #fbbf24)\" stroke=\"#0f172a\" stroke-width=\"0.8\"/>",
  "wf-arrow-up-right": "<polygon points=\"6 20 15 11 15 17 21 17 21 3 7 3 7 9 13 9 4 18\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"7 3 21 3 15 9 7 9\" fill=\"var(--wf-accent-light, #fbbf24)\" opacity=\"0.45\"/>\n<polygon points=\"15 11 21 17 15 17\" fill=\"#334155\" opacity=\"0.5\"/>\n<line x1=\"6\" y1=\"20\" x2=\"19\" y2=\"5\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>",
  "wf-arrow-up-left": "<polygon points=\"18 20 9 11 9 17 3 17 3 3 17 3 17 9 11 9 20 18\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"17 3 3 3 9 9 17 9\" fill=\"var(--wf-accent-light, #fbbf24)\" opacity=\"0.45\"/>\n<polygon points=\"9 11 3 17 9 17\" fill=\"#334155\" opacity=\"0.5\"/>\n<line x1=\"18\" y1=\"20\" x2=\"5\" y2=\"5\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>",
  "wf-u-turn": "<path d=\"M8 18l-4-4h3A7 7 0 0 1 14 7a7 7 0 0 1 7 7v7h-4v-7a3 3 0 0 0-3-3 3 3 0 0 0-3 3h3z\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<path d=\"M8 18l-4-4h3a7 7 0 0 1 7-7v4a3 3 0 0 0-3 3h3z\" fill=\"var(--wf-accent-light, #fbbf24)\" opacity=\"0.4\"/>\n<rect x=\"17\" y=\"14\" width=\"4\" height=\"7\" fill=\"#334155\"/>",
  "wf-signpost": "<rect x=\"11\" y=\"2\" width=\"2\" height=\"20\" fill=\"#334155\" stroke=\"#0f172a\" stroke-width=\"1.5\"/>\n<polygon points=\"4 5 11 5 13 7.5 11 10 4 10\" fill=\"#475569\" stroke=\"#0f172a\" stroke-width=\"1.5\" stroke-linejoin=\"round\"/>\n<polygon points=\"13 11 20 11 22 13.5 20 16 13 16\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.5\" stroke-linejoin=\"round\"/>\n<polygon points=\"13 11 17 11 18 13.5 16 16 13 16\" fill=\"var(--wf-accent-light, #fbbf24)\" opacity=\"0.4\"/>",
  "wf-pin": "<polygon points=\"12 2 19 6 19 14 12 22 5 14 5 6\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"12 2 19 6 12 10 5 6\" fill=\"#475569\"/>\n<polygon points=\"12 10 19 6 19 14 12 22\" fill=\"#334155\"/>\n<circle cx=\"12\" cy=\"11\" r=\"3.5\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1\"/>\n<text x=\"12\" y=\"12.5\" font-size=\"3.5\" font-weight=\"900\" text-anchor=\"middle\" fill=\"#0f172a\" font-family=\"sans-serif\">YOU</text>",
  "wf-facing": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<circle cx=\"12\" cy=\"12\" r=\"7\" fill=\"#334155\"/>\n<polygon points=\"12 4 15.5 12 12 10 8.5 12\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.2\" stroke-linejoin=\"round\"/>\n<polygon points=\"12 4 12 10 8.5 12\" fill=\"var(--wf-accent-light, #fbbf24)\"/>\n<circle cx=\"12\" cy=\"16.5\" r=\"1.5\" fill=\"var(--wf-accent, #f59e0b)\"/>",
  "wf-map": "<polygon points=\"3 7 9 3 9 17 3 21\" fill=\"#475569\" stroke=\"#0f172a\" stroke-width=\"1.5\" stroke-linejoin=\"round\"/>\n<polygon points=\"9 3 15 7 15 21 9 17\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.5\" stroke-linejoin=\"round\"/>\n<polygon points=\"15 7 21 3 21 17 15 21\" fill=\"#334155\" stroke=\"#0f172a\" stroke-width=\"1.5\" stroke-linejoin=\"round\"/>\n<polygon points=\"9 3 15 7 12 12\" fill=\"var(--wf-accent-light, #fbbf24)\" opacity=\"0.5\"/>\n<polygon points=\"12 12 15 21 9 17\" fill=\"var(--wf-accent-dark, #d97706)\" opacity=\"0.6\"/>\n<polygon points=\"3 7 9 10 3 14\" fill=\"var(--wf-accent, #f59e0b)\" opacity=\"0.85\"/>\n<polygon points=\"15 7 21 10 18 14\" fill=\"var(--wf-accent, #f59e0b)\" opacity=\"0.85\"/>",
  "wf-touch": "<polygon points=\"4 16 12 11 20 16 12 21\" fill=\"#475569\" stroke=\"#0f172a\" stroke-width=\"1.5\" stroke-linejoin=\"round\"/>\n<polygon points=\"4 16 12 11 12 21\" fill=\"var(--wf-accent, #f59e0b)\" opacity=\"0.85\"/>\n<circle cx=\"12\" cy=\"6\" r=\"3.5\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.5\"/>\n<circle cx=\"12\" cy=\"6\" r=\"1.5\" fill=\"#ffffff\"/>\n<path d=\"M12 9v5l2 2\" fill=\"none\" stroke=\"#0f172a\" stroke-width=\"2\" stroke-linecap=\"round\"/>",
  "wf-entrance": "<polygon points=\"8 3 18 3 21 6 21 21 8 21\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<rect x=\"11\" y=\"6\" width=\"7\" height=\"15\" fill=\"#334155\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>\n<polygon points=\"3 13 8 9 8 12 13 12 13 14 8 14 8 17\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.5\" stroke-linejoin=\"round\"/>\n<polygon points=\"3 13 8 9 8 13\" fill=\"var(--wf-accent-light, #fbbf24)\"/>",
  "wf-exit": "<polygon points=\"12 2 19 6 19 18 12 22 5 18 5 6\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"5 6 12 2 12 22 5 18\" fill=\"#334155\"/>\n<polygon points=\"6.5 7.5 11 4 11 20 6.5 16.5\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<polygon points=\"17.5 7.5 13 4 13 20 17.5 16.5\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<polygon points=\"6.5 7.5 11 4 11 12 6.5 12\" fill=\"var(--wf-accent-light, #fbbf24)\"/>\n<polygon points=\"13 4 17.5 7.5 17.5 12 13 12\" fill=\"var(--wf-accent-light, #fbbf24)\"/>",
  "wf-lift": "<rect x=\"3\" y=\"3\" width=\"18\" height=\"18\" rx=\"2\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<rect x=\"5.5\" y=\"5.5\" width=\"13\" height=\"13\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>\n<circle cx=\"9\" cy=\"9.5\" r=\"1.3\" fill=\"#0f172a\"/>\n<path d=\"M7.5 16v-3a1.5 1.5 0 0 1 3 0v3z\" fill=\"#0f172a\"/>\n<circle cx=\"15\" cy=\"9.5\" r=\"1.3\" fill=\"#0f172a\"/>\n<path d=\"M13.5 16v-3a1.5 1.5 0 0 1 3 0v3z\" fill=\"#0f172a\"/>\n<polygon points=\"12 2.5 10 4.5 14 4.5\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"0.8\"/>\n<polygon points=\"12 21.5 10 19.5 14 19.5\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"0.8\"/>",
  "wf-stairs": "<polygon points=\"3 20 8 20 8 16 13 16 13 12 18 12 18 8 22 8 22 20 3 20\" fill=\"#334155\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"8 20 8 16 13 16 13 12 18 12 18 8 22 8 22 20\" fill=\"#1e293b\"/>\n<polyline points=\"3 20 8 20 8 16 13 16 13 12 18 12 18 8 22 8\" fill=\"none\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"3\" stroke-linecap=\"round\" stroke-linejoin=\"round\"/>\n<line x1=\"5\" y1=\"13\" x2=\"19\" y2=\"4\" stroke=\"var(--wf-accent-light, #fbbf24)\" stroke-width=\"2\" stroke-linecap=\"round\"/>",
  "wf-escalator-up": "<path d=\"M3 6h4.5l8 11H21\" fill=\"none\" stroke=\"#1e293b\" stroke-width=\"5\" stroke-linecap=\"round\" stroke-linejoin=\"round\"/>\n<path d=\"M3 6h4.5l8 11H21\" fill=\"none\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"2.5\" stroke-linecap=\"round\" stroke-linejoin=\"round\"/>\n<polygon points=\"14 7 19 7 19 12\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1\"/>\n<circle cx=\"9\" cy=\"4\" r=\"1.5\" fill=\"#0f172a\"/>\n<path d=\"M7 10l3-3 2 1\" fill=\"none\" stroke=\"#0f172a\" stroke-width=\"2\" stroke-linecap=\"round\"/>",
  "wf-escalator-down": "<path d=\"M3 18h4.5l8-11H21\" fill=\"none\" stroke=\"#1e293b\" stroke-width=\"5\" stroke-linecap=\"round\" stroke-linejoin=\"round\"/>\n<path d=\"M3 18h4.5l8-11H21\" fill=\"none\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"2.5\" stroke-linecap=\"round\" stroke-linejoin=\"round\"/>\n<polygon points=\"10 17 5 17 5 12\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1\"/>\n<circle cx=\"15\" cy=\"4\" r=\"1.5\" fill=\"#0f172a\"/>\n<path d=\"M17 10l-3-3-2 1\" fill=\"none\" stroke=\"#0f172a\" stroke-width=\"2\" stroke-linecap=\"round\"/>",
  "wf-ramp": "<polygon points=\"2 20 22 20 22 9 2 20\" fill=\"#334155\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"2 20 22 9 22 20\" fill=\"#1e293b\"/>\n<line x1=\"2\" y1=\"20\" x2=\"22\" y2=\"9\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"3\" stroke-linecap=\"round\"/>\n<circle cx=\"15\" cy=\"6\" r=\"1.6\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<path d=\"M11 14a2.5 2.5 0 0 1 3-2l2-1.5\" fill=\"none\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linecap=\"round\"/>",
  "wf-accessible": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<circle cx=\"12\" cy=\"5\" r=\"1.8\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<path d=\"M10 9h3.5l1.5 5h3\" fill=\"none\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"2.2\" stroke-linecap=\"round\"/>\n<path d=\"M13 14a4 4 0 1 1-5-2.5\" fill=\"none\" stroke=\"#ffffff\" stroke-width=\"2.2\" stroke-linecap=\"round\"/>\n<polyline points=\"8 12 11 12 12 15\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"2\" stroke-linecap=\"round\"/>",
  "wf-levels": "<polygon points=\"12 2 21 6.5 12 11 3 6.5\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.5\" stroke-linejoin=\"round\"/>\n<polygon points=\"12 2 12 11 3 6.5\" fill=\"var(--wf-accent-light, #fbbf24)\" opacity=\"0.4\"/>\n<polygon points=\"12 7.5 21 12 12 16.5 3 12\" fill=\"#334155\" stroke=\"#0f172a\" stroke-width=\"1.5\" stroke-linejoin=\"round\"/>\n<polygon points=\"12 7.5 12 16.5 3 12\" fill=\"#475569\" opacity=\"0.4\"/>\n<polygon points=\"12 13 21 17.5 12 22 3 17.5\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.5\" stroke-linejoin=\"round\"/>",
  "wf-no-entry": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<circle cx=\"12\" cy=\"12\" r=\"7.5\" fill=\"#334155\"/>\n<rect x=\"4.5\" y=\"10\" width=\"15\" height=\"4\" rx=\"1\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>\n<rect x=\"4.5\" y=\"10\" width=\"15\" height=\"2\" fill=\"var(--wf-accent-light, #fbbf24)\"/>",
  "wf-prohibited": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<circle cx=\"12\" cy=\"12\" r=\"7\" fill=\"#334155\"/>\n<line x1=\"5.5\" y1=\"5.5\" x2=\"18.5\" y2=\"18.5\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"3.5\" stroke-linecap=\"round\"/>\n<line x1=\"5.5\" y1=\"5.5\" x2=\"18.5\" y2=\"18.5\" stroke=\"var(--wf-accent-light, #fbbf24)\" stroke-width=\"1.5\" stroke-linecap=\"round\"/>",
  "wf-staff-only": "<polygon points=\"12 2 19 5 17 14 12 20 7 14 5 5\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"12 4 17 7 15 13 12 17 9 13 7 7\" fill=\"#334155\"/>\n<rect x=\"9.5\" y=\"7\" width=\"5\" height=\"2.5\" rx=\"0.5\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<polygon points=\"12 11 14 13 12 16 10 13\" fill=\"var(--wf-accent, #f59e0b)\"/>",
  "wf-toilets": "<rect x=\"2\" y=\"2\" width=\"20\" height=\"20\" rx=\"3\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<line x1=\"12\" y1=\"3\" x2=\"12\" y2=\"21\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"1.5\"/>\n<circle cx=\"7\" cy=\"6\" r=\"1.5\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<path d=\"M5 10h4v6H8v4H6v-4H5z\" fill=\"#ffffff\"/>\n<circle cx=\"17\" cy=\"6\" r=\"1.5\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<polygon points=\"15 10 19 10 20 16 14 16\" fill=\"#ffffff\"/>\n<rect x=\"15\" y=\"16\" width=\"1.5\" height=\"4\" fill=\"#ffffff\"/>\n<rect x=\"17.5\" y=\"16\" width=\"1.5\" height=\"4\" fill=\"#ffffff\"/>",
  "wf-toilet-male": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<circle cx=\"12\" cy=\"5\" r=\"1.8\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<polygon points=\"10 8.5 14 8.5 15 15 13 15 13 20 11 20 11 15 9 15\" fill=\"#ffffff\" stroke=\"#0f172a\" stroke-width=\"1\"/>\n<polygon points=\"11.5 8.5 12.5 8.5 13 12 11 12\" fill=\"var(--wf-accent, #f59e0b)\"/>",
  "wf-toilet-female": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<circle cx=\"12\" cy=\"5\" r=\"1.8\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<polygon points=\"10 8.5 14 8.5 16 16 8 16\" fill=\"#ffffff\" stroke=\"#0f172a\" stroke-width=\"1\"/>\n<rect x=\"9.5\" y=\"16\" width=\"2\" height=\"4\" fill=\"#ffffff\"/>\n<rect x=\"12.5\" y=\"16\" width=\"2\" height=\"4\" fill=\"#ffffff\"/>\n<polygon points=\"12 8.5 14 8.5 15 12 12 12\" fill=\"var(--wf-accent, #f59e0b)\"/>",
  "wf-toilet-accessible": "<polygon points=\"12 2 20 6 20 18 12 22 4 18 4 6\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<circle cx=\"10\" cy=\"6\" r=\"1.6\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<path d=\"M8 10h3l1.5 4h2.5\" fill=\"none\" stroke=\"#ffffff\" stroke-width=\"1.8\" stroke-linecap=\"round\"/>\n<path d=\"M11 14a3.5 3.5 0 1 1-5-2\" fill=\"none\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"2\" stroke-linecap=\"round\"/>\n<rect x=\"16\" y=\"8\" width=\"3\" height=\"9\" rx=\"0.5\" fill=\"#334155\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"1\"/>",
  "wf-baby-change": "<polygon points=\"3 17 21 17 19 20 5 20\" fill=\"#334155\" stroke=\"#0f172a\" stroke-width=\"1.5\" stroke-linejoin=\"round\"/>\n<line x1=\"2\" y1=\"17\" x2=\"22\" y2=\"17\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"2.5\" stroke-linecap=\"round\"/>\n<circle cx=\"7\" cy=\"9\" r=\"2.2\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<path d=\"M10 13c2 0 4-2 6-2s4 2 5 2\" fill=\"none\" stroke=\"#ffffff\" stroke-width=\"2\" stroke-linecap=\"round\"/>\n<circle cx=\"15\" cy=\"9\" r=\"1.5\" fill=\"#ffffff\"/>",
  "wf-cafe": "<path d=\"M5 8c-2 2-2 5 0 7s5 2 7 0l5-5c2-2 2-5 0-7s-5-2-7 0z\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<path d=\"M19 8c2 2 2 5 0 7s-5 2-7 0l-5-5c-2-2-2-5 0-7s5-2 7 0z\" fill=\"#334155\" opacity=\"0.7\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<line x1=\"8\" y1=\"2\" x2=\"8\" y2=\"4\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"1.5\" stroke-linecap=\"round\"/>\n<line x1=\"12\" y1=\"1\" x2=\"12\" y2=\"3\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"1.5\" stroke-linecap=\"round\"/>\n<line x1=\"16\" y1=\"2\" x2=\"16\" y2=\"4\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"1.5\" stroke-linecap=\"round\"/>",
  "wf-food": "<polygon points=\"18 2 20 2 19 14 19 22 17 22 17 14\" fill=\"#ffffff\" stroke=\"#0f172a\" stroke-width=\"1.5\" stroke-linejoin=\"round\"/>\n<path d=\"M21 2c0 4-3 5-3 8\" fill=\"none\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"1.8\" stroke-linecap=\"round\"/>\n<path d=\"M4 2v6c0 2 1.5 3 3.5 3v11h2V11c2 0 3.5-1 3.5-3V2\" fill=\"none\" stroke=\"#ffffff\" stroke-width=\"1.8\" stroke-linecap=\"round\"/>\n<line x1=\"7.5\" y1=\"2\" x2=\"7.5\" y2=\"7\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"1.5\"/>",
  "wf-retail": "<polygon points=\"5 8 19 8 18 21 6 21\" fill=\"#334155\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"5 8 19 8 13 21 6 21\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<polygon points=\"5 8 12 8 8 21 6 21\" fill=\"var(--wf-accent-light, #fbbf24)\"/>\n<path d=\"M9 8V5a3 3 0 0 1 6 0v3\" fill=\"none\" stroke=\"#0f172a\" stroke-width=\"2\" stroke-linecap=\"round\"/>",
  "wf-atm": "<rect x=\"4\" y=\"3\" width=\"16\" height=\"18\" rx=\"2\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<rect x=\"7\" y=\"5.5\" width=\"10\" height=\"6.5\" rx=\"1\" fill=\"#334155\" stroke=\"#0f172a\" stroke-width=\"1\"/>\n<rect x=\"8.5\" y=\"7\" width=\"7\" height=\"3.5\" rx=\"0.5\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<line x1=\"7\" y1=\"15\" x2=\"17\" y2=\"15\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"2\" stroke-linecap=\"round\"/>\n<rect x=\"13.5\" y=\"17\" width=\"4\" height=\"2\" fill=\"#ffffff\"/>",
  "wf-payment": "<polygon points=\"3 14 7 8 17 8 21 14\" fill=\"#334155\" stroke=\"#0f172a\" stroke-width=\"1.5\" stroke-linejoin=\"round\"/>\n<path d=\"M3 14c0 4.5 4 7 9 7s9-2.5 9-7z\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.5\"/>\n<line x1=\"7\" y1=\"6\" x2=\"15\" y2=\"13\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"2.5\" stroke-linecap=\"round\"/>\n<circle cx=\"16\" cy=\"5\" r=\"2.5\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1\"/>",
  "wf-pharmacy": "<path d=\"M4 11c0 5 3.5 8 8 8s8-3 8-8z\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<line x1=\"3\" y1=\"11\" x2=\"21\" y2=\"11\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"2\" stroke-linecap=\"round\"/>\n<line x1=\"16\" y1=\"4\" x2=\"10\" y2=\"13\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"3\" stroke-linecap=\"round\"/>\n<polygon points=\"12 14 13 14 13 15 14 15 14 16 13 16 13 17 12 17 12 16 11 16 11 15 12 15\" fill=\"var(--wf-accent, #f59e0b)\" transform=\"scale(1.2) translate(-2,-2)\"/>",
  "wf-water": "<polygon points=\"12 2 17 8 17 15 12 21 7 15 7 8\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"12 2 17 8 12 15 7 8\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<polygon points=\"12 2 12 15 7 8\" fill=\"var(--wf-accent-light, #fbbf24)\"/>\n<polyline points=\"8 12 11 15 16 9\" stroke=\"#ffffff\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" fill=\"none\"/>",
  "wf-wifi": "<path d=\"M4 8a13 13 0 0 1 16 0\" fill=\"none\" stroke=\"#1e293b\" stroke-width=\"3\" stroke-linecap=\"round\"/>\n<path d=\"M4 8a13 13 0 0 1 16 0\" fill=\"none\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"1.5\" stroke-linecap=\"round\"/>\n<path d=\"M7 12a8 8 0 0 1 10 0\" fill=\"none\" stroke=\"#1e293b\" stroke-width=\"3\" stroke-linecap=\"round\"/>\n<path d=\"M7 12a8 8 0 0 1 10 0\" fill=\"none\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"1.5\" stroke-linecap=\"round\"/>\n<circle cx=\"12\" cy=\"18\" r=\"2.2\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>",
  "wf-seating": "<polygon points=\"5 5 19 5 17 12 7 12\" fill=\"#334155\" stroke=\"#0f172a\" stroke-width=\"1.5\" stroke-linejoin=\"round\"/>\n<rect x=\"4\" y=\"12\" width=\"16\" height=\"4.5\" rx=\"1.5\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.5\"/>\n<line x1=\"6\" y1=\"16.5\" x2=\"4\" y2=\"21\" stroke=\"#1e293b\" stroke-width=\"2\" stroke-linecap=\"round\"/>\n<line x1=\"18\" y1=\"16.5\" x2=\"20\" y2=\"21\" stroke=\"#1e293b\" stroke-width=\"2\" stroke-linecap=\"round\"/>",
  "wf-parking": "<polygon points=\"4 6 20 6 22 13 2 13\" fill=\"#334155\" stroke=\"#0f172a\" stroke-width=\"1.5\" stroke-linejoin=\"round\"/>\n<polygon points=\"2 13 22 13 20 18 4 18\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.5\" stroke-linejoin=\"round\"/>\n<circle cx=\"6.5\" cy=\"18\" r=\"2.2\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>\n<circle cx=\"17.5\" cy=\"18\" r=\"2.2\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>\n<polygon points=\"5 13 7 8 17 8 19 13\" fill=\"var(--wf-accent, #f59e0b)\" opacity=\"0.85\"/>",
  "wf-car": "<polygon points=\"5 11 8 5 16 5 19 11\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.5\" stroke-linejoin=\"round\"/>\n<rect x=\"3\" y=\"11\" width=\"18\" height=\"6\" rx=\"2\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.5\"/>\n<circle cx=\"7\" cy=\"17\" r=\"2\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1\"/>\n<circle cx=\"17\" cy=\"17\" r=\"2\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1\"/>\n<line x1=\"3\" y1=\"13\" x2=\"6\" y2=\"13\" stroke=\"var(--wf-accent-light, #fbbf24)\" stroke-width=\"1.5\"/>\n<line x1=\"18\" y1=\"13\" x2=\"21\" y2=\"13\" stroke=\"var(--wf-accent-light, #fbbf24)\" stroke-width=\"1.5\"/>",
  "wf-bus": "<rect x=\"5\" y=\"3\" width=\"14\" height=\"16\" rx=\"3\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<rect x=\"7\" y=\"5.5\" width=\"10\" height=\"2.5\" rx=\"0.5\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<rect x=\"7\" y=\"9.5\" width=\"10\" height=\"4.5\" rx=\"0.5\" fill=\"#334155\"/>\n<circle cx=\"8\" cy=\"16\" r=\"1.3\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<circle cx=\"16\" cy=\"16\" r=\"1.3\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<line x1=\"7\" y1=\"19\" x2=\"7\" y2=\"21.5\" stroke=\"#0f172a\" stroke-width=\"2\"/>\n<line x1=\"17\" y1=\"19\" x2=\"17\" y2=\"21.5\" stroke=\"#0f172a\" stroke-width=\"2\"/>",
  "wf-ev": "<polygon points=\"12 2 19 6 19 18 12 22 5 18 5 6\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"12 2 19 6 12 11 5 6\" fill=\"#475569\"/>\n<polygon points=\"12 11 19 6 19 18 12 22\" fill=\"#334155\"/>\n<polygon points=\"12 5 8 12 12 12 11 18 16 11 12 11\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"0.8\"/>",
  "wf-info": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<circle cx=\"12\" cy=\"12\" r=\"7\" fill=\"#334155\"/>\n<path d=\"M12 5 A7 7 0 0 1 19 12 L12 12 Z\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<circle cx=\"12\" cy=\"12\" r=\"3.5\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>\n<circle cx=\"12\" cy=\"12\" r=\"1.5\" fill=\"var(--wf-accent, #f59e0b)\"/>",
  "wf-help": "<polygon points=\"12 2 20 6.5 20 17.5 12 22 4 17.5 4 6.5\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"12 4.5 18 8 18 16 12 19.5 6 16 6 8\" fill=\"#334155\"/>\n<path d=\"M10 8.5a2.5 2.5 0 0 1 4 1.5c0 1.5-2 2-2 3.5\" fill=\"none\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"2.5\" stroke-linecap=\"round\"/>\n<circle cx=\"12\" cy=\"16.5\" r=\"1.3\" fill=\"var(--wf-accent, #f59e0b)\"/>",
  "wf-reception": "<polygon points=\"4 14 20 14 18 19 6 19\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.5\" stroke-linejoin=\"round\"/>\n<rect x=\"3\" y=\"14\" width=\"18\" height=\"2.5\" rx=\"0.5\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<circle cx=\"12\" cy=\"6\" r=\"2.5\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>\n<path d=\"M9 14a3 3 0 0 1 6 0\" fill=\"#334155\"/>",
  "wf-security": "<rect x=\"5\" y=\"5\" width=\"14\" height=\"9\" rx=\"1.5\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<rect x=\"7\" y=\"7\" width=\"10\" height=\"5\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<polygon points=\"10 14 14 14 16 20 8 20\" fill=\"#334155\" stroke=\"#0f172a\" stroke-width=\"1.5\" stroke-linejoin=\"round\"/>\n<line x1=\"3\" y1=\"20\" x2=\"21\" y2=\"20\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"2\"/>",
  "wf-phone": "<polygon points=\"12 2 20 6 18 16 12 21 6 16 4 6\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"12 4 18 7.5 16.5 15 12 19 7.5 15 6 7.5\" fill=\"#334155\"/>\n<path d=\"M9 8h2l1 2.5-1.5 1.5a7 7 0 0 0 3 3l1.5-1.5 2.5 1v2a2 2 0 0 1-2 2A10 10 0 0 1 7 9a2 2 0 0 1 2-1\" fill=\"var(--wf-accent, #f59e0b)\"/>",
  "wf-intercom": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<circle cx=\"12\" cy=\"12\" r=\"7.5\" fill=\"#334155\"/>\n<circle cx=\"12\" cy=\"12\" r=\"6\" fill=\"#1e293b\"/>\n<text x=\"12\" y=\"16.5\" font-size=\"12\" font-weight=\"900\" text-anchor=\"middle\" fill=\"var(--wf-accent, #f59e0b)\" font-family=\"sans-serif\">H</text>",
  "wf-hospital": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<circle cx=\"12\" cy=\"12\" r=\"7.5\" fill=\"#1e293b\"/>\n<text x=\"12\" y=\"16.5\" font-size=\"12\" font-weight=\"900\" text-anchor=\"middle\" fill=\"var(--wf-accent, #f59e0b)\" font-family=\"sans-serif\">H</text>",
  "wf-first-aid": "<rect x=\"3\" y=\"6\" width=\"18\" height=\"15\" rx=\"3\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<path d=\"M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2\" fill=\"none\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"2\"/>\n<polygon points=\"10 11 10 9 14 9 14 11 16 11 16 15 14 15 14 17 10 17 10 15 8 15 8 11\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1\"/>",
  "wf-consult": "<rect x=\"3\" y=\"6\" width=\"18\" height=\"15\" rx=\"3\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<polygon points=\"10 11 10 9 14 9 14 11 16 11 16 15 14 15 14 17 10 17 10 15 8 15 8 11\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<line x1=\"8\" y1=\"6\" x2=\"16\" y2=\"6\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"2.5\" stroke-linecap=\"round\"/>",
  "wf-pathology": "<rect x=\"3\" y=\"6\" width=\"18\" height=\"15\" rx=\"3\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<polygon points=\"10 11 10 9 14 9 14 11 16 11 16 15 14 15 14 17 10 17 10 15 8 15 8 11\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<circle cx=\"17.5\" cy=\"8.5\" r=\"1.5\" fill=\"#ffffff\"/>",
  "wf-aed": "<polygon points=\"12 21 3 12 6 5 12 9 18 5 21 12\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"12 19 5 12 7 7 12 10 17 7 19 12\" fill=\"#334155\"/>\n<polygon points=\"12 4 9 11 13 11 11 17 16 10 12 10\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1\"/>",
  "wf-student": "<polygon points=\"12 2 14.5 8 21 9 16 14 18 21 12 17 6 21 8 14 3 9 9.5 8\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"12 2 14.5 8 12 12 9.5 8\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<polygon points=\"21 9 16 14 12 12 14.5 8\" fill=\"#334155\"/>\n<polygon points=\"18 21 12 17 12 12 16 14\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<polygon points=\"6 21 8 14 12 12 12 17\" fill=\"var(--wf-accent-light, #fbbf24)\"/>\n<polygon points=\"3 9 9.5 8 12 12 8 14\" fill=\"var(--wf-accent, #f59e0b)\"/>",
  "wf-library": "<rect x=\"3\" y=\"4\" width=\"4\" height=\"17\" rx=\"0.5\" fill=\"#334155\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>\n<rect x=\"8\" y=\"2\" width=\"5\" height=\"19\" rx=\"0.5\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>\n<rect x=\"14\" y=\"5\" width=\"4\" height=\"16\" rx=\"0.5\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>\n<rect x=\"19\" y=\"8\" width=\"3\" height=\"13\" rx=\"0.5\" fill=\"#475569\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>\n<line x1=\"9.5\" y1=\"6\" x2=\"11.5\" y2=\"6\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"1.5\"/>",
  "wf-lecture": "<rect x=\"3\" y=\"3\" width=\"18\" height=\"13\" rx=\"1.5\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<rect x=\"5\" y=\"5\" width=\"14\" height=\"9\" fill=\"#334155\"/>\n<polygon points=\"6 6 12 6 12 9 6 9\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<line x1=\"6\" y1=\"11\" x2=\"18\" y2=\"11\" stroke=\"#ffffff\" stroke-width=\"1.2\"/>\n<polygon points=\"9 16 15 16 17 21 7 21\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.5\" stroke-linejoin=\"round\"/>",
  "wf-emergency": "<polygon points=\"7 2 17 2 22 7 22 17 17 22 7 22 2 17 2 7\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<circle cx=\"12\" cy=\"12\" r=\"7.5\" fill=\"#334155\"/>\n<line x1=\"12\" y1=\"2\" x2=\"12\" y2=\"5\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"2\"/>\n<line x1=\"12\" y1=\"19\" x2=\"12\" y2=\"22\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"2\"/>\n<line x1=\"2\" y1=\"12\" x2=\"5\" y2=\"12\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"2\"/>\n<line x1=\"19\" y1=\"12\" x2=\"22\" y2=\"12\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"2\"/>\n<polygon points=\"11 7 13 7 13 13 11 13\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<circle cx=\"12\" cy=\"16\" r=\"1.3\" fill=\"var(--wf-accent, #f59e0b)\"/>",
  "wf-evacuate": "<polygon points=\"13 3 21 3 21 21 13 21\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"15 5 19 5 19 19 15 19\" fill=\"var(--wf-accent-light, #fbbf24)\"/>\n<circle cx=\"7\" cy=\"6\" r=\"1.8\" fill=\"#0f172a\"/>\n<path d=\"M5 16l2-3 2 1.5 3-4.5h2\" stroke=\"#0f172a\" stroke-width=\"2\" stroke-linecap=\"round\" fill=\"none\"/>",
  "wf-assembly": "<polygon points=\"12 2 14.5 7 20 5 18 10.5 23 13 18 15.5 20 21 14.5 19 12 24 9.5 19 4 21 6 15.5 1 13 6 10.5 4 5 9.5 7\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"12 2 14.5 7 12 13 9.5 7\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<polygon points=\"20 5 18 10.5 12 13 14.5 7\" fill=\"#334155\"/>\n<polygon points=\"23 13 18 15.5 12 13 18 10.5\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<polygon points=\"20 21 14.5 19 12 13 18 15.5\" fill=\"var(--wf-accent-light, #fbbf24)\"/>\n<polygon points=\"12 24 9.5 19 12 13 14.5 19\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<polygon points=\"4 21 6 15.5 12 13 9.5 19\" fill=\"#334155\"/>\n<polygon points=\"1 13 6 10.5 12 13 6 15.5\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<polygon points=\"4 5 9.5 7 12 13 6 10.5\" fill=\"var(--wf-accent-light, #fbbf24)\"/>",
  "wf-fire": "<polygon points=\"12 2 15 8.5 22 9.5 17 14.5 18.5 21.5 12 18 5.5 21.5 7 14.5 2 9.5 9 8.5\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"12 2 15 8.5 12 14 9 8.5\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<polygon points=\"22 9.5 17 14.5 12 14 15 8.5\" fill=\"var(--wf-accent-light, #fbbf24)\"/>\n<polygon points=\"18.5 21.5 12 18 12 14 17 14.5\" fill=\"var(--wf-accent-dark, #d97706)\"/>\n<polygon points=\"5.5 21.5 7 14.5 12 14 12 18\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<polygon points=\"2 9.5 9 8.5 12 14 7 14.5\" fill=\"var(--wf-accent-light, #fbbf24)\"/>",
  "wf-warning": "<polygon points=\"12 2 23 20 1 20\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"12 5 20.5 18.5 3.5 18.5\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.2\" stroke-linejoin=\"round\"/>\n<polygon points=\"12 5 20.5 18.5 12 18.5\" fill=\"var(--wf-accent-light, #fbbf24)\" opacity=\"0.4\"/>\n<line x1=\"12\" y1=\"9\" x2=\"12\" y2=\"13.5\" stroke=\"#0f172a\" stroke-width=\"2.5\" stroke-linecap=\"round\"/>\n<circle cx=\"12\" cy=\"16.5\" r=\"1.3\" fill=\"#0f172a\"/>",
  "wf-construction": "<polygon points=\"12 2 23 20 1 20\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"12 2 12 20 1 20\" fill=\"var(--wf-accent-light, #fbbf24)\" opacity=\"0.35\"/>\n<line x1=\"6\" y1=\"16\" x2=\"18\" y2=\"16\" stroke=\"#0f172a\" stroke-width=\"2.5\"/>\n<line x1=\"8\" y1=\"12\" x2=\"16\" y2=\"12\" stroke=\"#0f172a\" stroke-width=\"2.5\"/>\n<polygon points=\"12 5 15 10 9 10\" fill=\"#1e293b\"/>",
  "wf-home": "<polygon points=\"12 2 22 10 19 10 19 21 5 21 5 10 2 10\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"12 2 22 10 19 10 12 4.5 5 10 2 10\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.2\" stroke-linejoin=\"round\"/>\n<polygon points=\"12 2 22 10 19 10 12 4.5\" fill=\"var(--wf-accent-light, #fbbf24)\"/>\n<rect x=\"9.5\" y=\"13\" width=\"5\" height=\"8\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>",
  "wf-search": "<circle cx=\"10.5\" cy=\"10.5\" r=\"7.5\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<circle cx=\"10.5\" cy=\"10.5\" r=\"5.5\" fill=\"#334155\"/>\n<path d=\"M7 7 A5 5 0 0 1 14 7\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"2\" stroke-linecap=\"round\" fill=\"none\"/>\n<polygon points=\"15 15 21 21 22 20 16 14\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.5\" stroke-linejoin=\"round\"/>",
  "wf-menu": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"3.5\" rx=\"1.5\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.5\"/>\n<rect x=\"3\" y=\"10.25\" width=\"18\" height=\"3.5\" rx=\"1.5\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.5\"/>\n<rect x=\"3\" y=\"16.5\" width=\"18\" height=\"3.5\" rx=\"1.5\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.5\"/>",
  "wf-back": "<polygon points=\"16 3 6 12 16 21 19 18 11 12 19 6\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"16 3 6 12 11 12 19 6\" fill=\"var(--wf-accent-light, #fbbf24)\"/>",
  "wf-close": "<polygon points=\"6 3 12 9 18 3 21 6 15 12 21 18 18 21 12 15 6 21 3 18 9 12 3 6\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"6 3 12 9 15 12 9 12 3 6\" fill=\"var(--wf-accent-light, #fbbf24)\"/>",
  "wf-hours": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<circle cx=\"12\" cy=\"12\" r=\"7.5\" fill=\"#334155\"/>\n<path d=\"M12 4.5 A7.5 7.5 0 0 1 19.5 12 L12 12 Z\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<line x1=\"12\" y1=\"6\" x2=\"12\" y2=\"12\" stroke=\"#0f172a\" stroke-width=\"2\" stroke-linecap=\"round\"/>\n<line x1=\"12\" y1=\"12\" x2=\"16\" y2=\"12\" stroke=\"#0f172a\" stroke-width=\"2\" stroke-linecap=\"round\"/>",
  "wf-timetable": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"17\" rx=\"2\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<rect x=\"3\" y=\"4\" width=\"18\" height=\"5\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>\n<circle cx=\"8\" cy=\"13\" r=\"1.3\" fill=\"#ffffff\"/>\n<circle cx=\"12\" cy=\"13\" r=\"1.3\" fill=\"#ffffff\"/>\n<circle cx=\"16\" cy=\"13\" r=\"1.3\" fill=\"#ffffff\"/>\n<circle cx=\"8\" cy=\"17\" r=\"1.3\" fill=\"#ffffff\"/>\n<circle cx=\"12\" cy=\"17\" r=\"1.3\" fill=\"var(--wf-accent, #f59e0b)\"/>",
  "wf-events": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"17\" rx=\"2\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<rect x=\"3\" y=\"4\" width=\"18\" height=\"5\" fill=\"#334155\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>\n<polygon points=\"12 10 13.5 13 17 13.5 14.5 16 15 19.5 12 18 9 19.5 9.5 16 7 13.5 10.5 13\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1\"/>",
  "wf-news": "<polygon points=\"3 4 19 4 21 7 21 21 3 21\" fill=\"#334155\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"19 4 21 7 19 7\" fill=\"#475569\"/>\n<rect x=\"5.5\" y=\"6.5\" width=\"6\" height=\"5\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1\"/>\n<line x1=\"13.5\" y1=\"7\" x2=\"18.5\" y2=\"7\" stroke=\"#ffffff\" stroke-width=\"1.5\"/>\n<line x1=\"13.5\" y1=\"10\" x2=\"18.5\" y2=\"10\" stroke=\"#ffffff\" stroke-width=\"1.5\"/>\n<line x1=\"5.5\" y1=\"14\" x2=\"18.5\" y2=\"14\" stroke=\"#ffffff\" stroke-width=\"1.5\"/>\n<line x1=\"5.5\" y1=\"17.5\" x2=\"15.5\" y2=\"17.5\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"1.5\"/>",
  "wf-announce": "<polygon points=\"4 9 13 4 13 20 4 15\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"4 9 13 4 13 12 4 12\" fill=\"#334155\"/>\n<path d=\"M16 8a5 5 0 0 1 0 8\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"2.5\" stroke-linecap=\"round\" fill=\"none\"/>\n<path d=\"M19 5a9 9 0 0 1 0 14\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"2.5\" stroke-linecap=\"round\" fill=\"none\"/>\n<path d=\"M6 15v4a2 2 0 0 0 2 2h2\" fill=\"none\" stroke=\"#0f172a\" stroke-width=\"2\"/>",
  "wf-share": "<polygon points=\"14 3 22 9 14 15 14 11 4 11 4 7 14 7\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"14 3 22 9 14 9\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<circle cx=\"6\" cy=\"18\" r=\"2.5\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>\n<line x1=\"8.5\" y1=\"17\" x2=\"17\" y2=\"13\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"1.8\"/>",
  "wf-chat": "<path d=\"M4 5h14a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2H8l-5 4V7a2 2 0 0 1 2-2z\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<path d=\"M4 5h14a2 2 0 0 1 2 2v3H4z\" fill=\"#334155\"/>\n<circle cx=\"8\" cy=\"11\" r=\"1.3\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<circle cx=\"12\" cy=\"11\" r=\"1.3\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<circle cx=\"16\" cy=\"11\" r=\"1.3\" fill=\"var(--wf-accent, #f59e0b)\"/>",
  "wf-like": "<path d=\"M13 9V4a2 2 0 0 0-2-2l-3 7v12h10a2 2 0 0 0 2-1.7l1.3-8.5a2 2 0 0 0-2-2.3H13z\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<rect x=\"3\" y=\"9\" width=\"5\" height=\"12\" rx=\"1\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<line x1=\"8\" y1=\"9\" x2=\"8\" y2=\"21\" stroke=\"#0f172a\" stroke-width=\"1.5\"/>\n<path d=\"M13 9V4a2 2 0 0 0-2-2l-3 7h5z\" fill=\"var(--wf-accent-light, #fbbf24)\"/>",
  "wf-camera": "<polygon points=\"4 7 7 4 17 4 20 7 21 7 21 20 3 20 3 7\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<circle cx=\"12\" cy=\"13.5\" r=\"4.5\" fill=\"#334155\" stroke=\"#0f172a\" stroke-width=\"1.5\"/>\n<circle cx=\"12\" cy=\"13.5\" r=\"2.5\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<circle cx=\"18\" cy=\"8\" r=\"1.2\" fill=\"var(--wf-accent-light, #fbbf24)\"/>",
  "wf-video": "<rect x=\"2\" y=\"6\" width=\"13\" height=\"12\" rx=\"2\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<polygon points=\"15 10 22 6 22 18 15 14\" fill=\"var(--wf-accent, #f59e0b)\" stroke=\"#0f172a\" stroke-width=\"1.8\" stroke-linejoin=\"round\"/>\n<polygon points=\"15 10 22 6 15 14\" fill=\"var(--wf-accent-light, #fbbf24)\"/>\n<circle cx=\"6\" cy=\"9.5\" r=\"1.5\" fill=\"var(--wf-accent-light, #fbbf24)\"/>",
  "wf-qr": "<rect x=\"2\" y=\"2\" width=\"20\" height=\"20\" rx=\"3\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<rect x=\"4\" y=\"4\" width=\"6.5\" height=\"6.5\" fill=\"#ffffff\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>\n<rect x=\"5.5\" y=\"5.5\" width=\"3.5\" height=\"3.5\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<rect x=\"13.5\" y=\"4\" width=\"6.5\" height=\"6.5\" fill=\"#ffffff\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>\n<rect x=\"15\" y=\"5.5\" width=\"3.5\" height=\"3.5\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<rect x=\"4\" y=\"13.5\" width=\"6.5\" height=\"6.5\" fill=\"#ffffff\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>\n<rect x=\"5.5\" y=\"15\" width=\"3.5\" height=\"3.5\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<rect x=\"13.5\" y=\"13.5\" width=\"3\" height=\"3\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<rect x=\"17\" y=\"17\" width=\"3\" height=\"3\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<rect x=\"13.5\" y=\"17\" width=\"3\" height=\"3\" fill=\"#ffffff\"/>",
  "wf-email": "<rect x=\"2\" y=\"4\" width=\"20\" height=\"16\" rx=\"2\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<polygon points=\"2 5 12 13 22 5\" fill=\"#334155\" stroke=\"#0f172a\" stroke-width=\"1.2\"/>\n<polygon points=\"2 5 12 13 7 13\" fill=\"var(--wf-accent, #f59e0b)\"/>\n<polygon points=\"22 5 12 13 17 13\" fill=\"var(--wf-accent-light, #fbbf24)\"/>",
  "wf-web": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" fill=\"#1e293b\" stroke=\"#0f172a\" stroke-width=\"1.8\"/>\n<ellipse cx=\"12\" cy=\"12\" rx=\"4.5\" ry=\"9.5\" fill=\"#334155\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"1.5\"/>\n<line x1=\"2.5\" y1=\"12\" x2=\"21.5\" y2=\"12\" stroke=\"var(--wf-accent, #f59e0b)\" stroke-width=\"1.8\"/>\n<circle cx=\"12\" cy=\"12\" r=\"2.2\" fill=\"var(--wf-accent, #f59e0b)\"/>"
};

export const WAYFINDING_DUOTONE = {
  "wf-arrow-up": "<circle cx=\"12\" cy=\"12\" r=\"9\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M12 4.5l6 6h-4v9h-4v-9H6z\" fill=\"currentColor\"/>",
  "wf-arrow-right": "<circle cx=\"12\" cy=\"12\" r=\"9\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M19.5 12l-6-6v4H4.5v4h9v4z\" fill=\"currentColor\"/>",
  "wf-arrow-down": "<circle cx=\"12\" cy=\"12\" r=\"9\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M12 19.5l-6-6h4v-9h4v9h4z\" fill=\"currentColor\"/>",
  "wf-arrow-left": "<circle cx=\"12\" cy=\"12\" r=\"9\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M4.5 12l6 6v-4h9v-4h-9V6z\" fill=\"currentColor\"/>",
  "wf-arrow-up-right": "<circle cx=\"12\" cy=\"12\" r=\"9\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M19.07 4.93 7.76 4.93 11.29 8.46 2.81 16.95 7.05 21.19 15.54 12.71 19.07 16.24Z\" fill=\"currentColor\"/>",
  "wf-arrow-up-left": "<circle cx=\"12\" cy=\"12\" r=\"9\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M4.93 4.93 16.24 4.93 12.71 8.46 21.19 16.95 16.95 21.19 8.46 12.71 4.93 16.24Z\" fill=\"currentColor\"/>",
  "wf-u-turn": "<circle cx=\"12\" cy=\"12\" r=\"9\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M9 18l-5-5h3.5A7.5 7.5 0 0 1 15 5.5a7.5 7.5 0 0 1 7.5 7.5v6h-4v-6a3.5 3.5 0 0 0-3.5-3.5A3.5 3.5 0 0 0 11.5 13H15z\" fill=\"currentColor\"/>",
  "wf-signpost": "<path d=\"M12 12H5a1 1 0 0 1-1-1V8a1 1 0 0 1 1-1h7l2 2.5-2 2.5z\" opacity=\"0.25\" fill=\"currentColor\"/><rect x=\"11\" y=\"2\" width=\"2\" height=\"20\" rx=\"1\" fill=\"currentColor\"/><path d=\"M12 5h7a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-7l-2-2.5 2-2.5z\" fill=\"currentColor\"/>",
  "wf-pin": "<ellipse cx=\"12\" cy=\"20.5\" rx=\"5.5\" ry=\"1.75\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M12 2C8.13 2 5 5.13 5 9c0 5.25 7 12 7 12s7-6.75 7-12c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z\" fill=\"currentColor\"/>",
  "wf-facing": "<circle cx=\"12\" cy=\"12\" r=\"9\" opacity=\"0.25\" fill=\"currentColor\"/><polygon points=\"12 4 16 13 12 11 8 13\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"17\" r=\"1.2\" fill=\"currentColor\"/>",
  "wf-map": "<polygon points=\"3 6 9 3 9 18 3 21\" opacity=\"0.25\" fill=\"currentColor\"/><polygon points=\"15 6 21 3 21 18 15 21\" opacity=\"0.25\" fill=\"currentColor\"/><polygon points=\"9 3 15 6 15 21 9 18\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"11\" r=\"2\" fill=\"currentColor\"/>",
  "wf-touch": "<circle cx=\"12\" cy=\"4\" r=\"5\" opacity=\"0.2\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"4\" r=\"2.5\" opacity=\"0.3\" fill=\"currentColor\"/><path d=\"M12 11V6a1.5 1.5 0 0 1 3 0v5\" fill=\"currentColor\"/><path d=\"M15 9.5a1.5 1.5 0 0 1 3 0V12a1.5 1.5 0 0 1 3 0v3a6 6 0 0 1-6 6h-2a6 6 0 0 1-4.24-1.76L5 15.4a1.5 1.5 0 0 1 2.2-2L9.5 15V6a1.5 1.5 0 0 1 3 0v5\" fill=\"currentColor\"/>",
  "wf-entrance": "<path d=\"M10 2h11a1 1 0 0 1 1 1v17a1 1 0 0 1-1 1h-11v-2h9V4h-9V2z\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"m19 4-6 2.5v11l6 2.5V4z\" opacity=\"0.35\" fill=\"currentColor\"/><rect x=\"1\" y=\"21\" width=\"22\" height=\"2\" rx=\"0.5\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M1 10.5h5V7.5l5.5 4.5-5.5 4.5v-3H1z\" fill=\"currentColor\"/>",
  "wf-exit": "<path d=\"M14 2H3a1 1 0 0 0-1 1v17a1 1 0 0 0 1 1h11v-2H5V4h9V2z\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"m5 4 6 2.5v11L5 20V4z\" opacity=\"0.35\" fill=\"currentColor\"/><rect x=\"1\" y=\"21\" width=\"22\" height=\"2\" rx=\"0.5\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M12.5 10.5h5V7.5l5.5 4.5-5.5 4.5v-3h-5z\" fill=\"currentColor\"/>",
  "wf-lift": "<rect x=\"2\" y=\"2\" width=\"13\" height=\"20\" rx=\"3\" opacity=\"0.25\" fill=\"currentColor\"/><circle cx=\"6\" cy=\"7.5\" r=\"1.5\" fill=\"currentColor\"/><path d=\"M4 16v-3a2 2 0 0 1 4 0v3H4z\" fill=\"currentColor\"/><circle cx=\"11\" cy=\"7.5\" r=\"1.5\" fill=\"currentColor\"/><path d=\"M9 16v-3a2 2 0 0 1 4 0v3H9z\" fill=\"currentColor\"/><polygon points=\"19.5 4 16 8.5 23 8.5\" fill=\"currentColor\"/><polygon points=\"19.5 20 16 15.5 23 15.5\" fill=\"currentColor\"/><rect x=\"18.5\" y=\"10.5\" width=\"2\" height=\"3\" rx=\"0.5\" fill=\"currentColor\"/>",
  "wf-stairs": "<path d=\"M4 19h4v-4h4v-4h4V7h4v12H4z\" opacity=\"0.25\" fill=\"currentColor\"/><circle cx=\"7\" cy=\"5.5\" r=\"1.8\" fill=\"currentColor\"/><path d=\"M5 14l3-3 2 1.5 3-4.5h3v2h-2l-2.5 3.5L10 12l-3 4.5H5z\" fill=\"currentColor\"/>",
  "wf-escalator-up": "<path d=\"M2 7h4.5l7 10H22v3H13.5l-7-10H2V7z\" opacity=\"0.25\" fill=\"currentColor\"/><circle cx=\"8\" cy=\"4.5\" r=\"1.8\" fill=\"currentColor\"/><path d=\"M6 13l2.5-3 2 1.5 2.5-3.5h2v1.5h-1.2l-2 2.8-2-1.5-2 3H6z\" fill=\"currentColor\"/><polygon points=\"18 13 18 18 22 15.5\" fill=\"currentColor\"/>",
  "wf-escalator-down": "<path d=\"M2 17h4.5l7-10H22V4H13.5l-7 10H2v3z\" opacity=\"0.25\" fill=\"currentColor\"/><circle cx=\"16\" cy=\"4.5\" r=\"1.8\" fill=\"currentColor\"/><path d=\"M18 13l-2.5-3-2 1.5-2.5-3.5h-2v1.5h1.2l2 2.8 2-1.5 2 3h1.8z\" fill=\"currentColor\"/><polygon points=\"6 13 6 18 2 15.5\" fill=\"currentColor\"/>",
  "wf-ramp": "<polygon points=\"2 19 22 19 22 11 2 19\" opacity=\"0.25\" fill=\"currentColor\"/><circle cx=\"14\" cy=\"6.5\" r=\"1.8\" fill=\"currentColor\"/><path d=\"M10 11.5a3 3 0 0 1 4-1.2l1.5-1.5 1.4 1-1.5 2a3 3 0 1 1-5.4-.3zm2 3.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z\" fill=\"currentColor\"/>",
  "wf-accessible": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" opacity=\"0.22\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"4.5\" r=\"2\" fill=\"currentColor\"/><path d=\"M10 9h3.5l1.5 5h3\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M13.5 14A4 4 0 1 1 8 11.5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M8 12h3\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/>",
  "wf-levels": "<polygon points=\"3 12 12 16.5 21 12 12 16.5\" opacity=\"0.25\" fill=\"currentColor\"/><polygon points=\"3 16.5 12 21 21 16.5 12 21\" opacity=\"0.2\" fill=\"currentColor\"/><polygon points=\"12 3 21 7.5 12 12 3 7.5 12 3\" fill=\"currentColor\"/><polyline points=\"3 12 12 16.5 21 12\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><polyline points=\"3 16.5 12 21 21 16.5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/>",
  "wf-no-entry": "<circle cx=\"12\" cy=\"12\" r=\"9\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z\" fill=\"currentColor\"/><rect x=\"5.5\" y=\"10.25\" width=\"13\" height=\"3.5\" rx=\"1\" fill=\"currentColor\"/>",
  "wf-prohibited": "<circle cx=\"12\" cy=\"12\" r=\"8\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm-8 10a7.9 7.9 0 0 1 1.77-5.06l11.29 11.29A7.9 7.9 0 0 1 4 12zm14.23 5.06L6.94 5.77A7.9 7.9 0 0 1 18.23 12a7.9 7.9 0 0 1-2.23 5.06z\" fill=\"currentColor\"/>",
  "wf-staff-only": "<rect x=\"4\" y=\"7\" width=\"16\" height=\"14\" rx=\"3\" opacity=\"0.25\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"12\" r=\"2.5\" fill=\"currentColor\"/><path d=\"M8 18c0-2.2 1.8-4 4-4s4 1.8 4 4H8z\" fill=\"currentColor\"/><path d=\"M8 7V5a4 4 0 0 1 8 0v2h-2V5a2 2 0 0 0-4 0v2H8z\" fill=\"currentColor\"/>",
  "wf-toilets": "<rect x=\"2\" y=\"2\" width=\"20\" height=\"20\" rx=\"4\" opacity=\"0.2\" fill=\"currentColor\"/><circle cx=\"7\" cy=\"5\" r=\"1.5\" fill=\"currentColor\"/><path d=\"M5 9h4v6H8v5H6v-5H5V9z\" fill=\"currentColor\"/><circle cx=\"17\" cy=\"5\" r=\"1.5\" fill=\"currentColor\"/><path d=\"M15 15l-1-6h6l-1 6h-4z\" fill=\"currentColor\"/><path d=\"M16 15v5h2v-5\" fill=\"currentColor\"/>",
  "wf-toilet-male": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" opacity=\"0.22\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"4\" r=\"2\" fill=\"currentColor\"/><path d=\"M9 8h6a1 1 0 0 1 1 1v6h-2v6h-4v-6H8V9a1 1 0 0 1 1-1z\" fill=\"currentColor\"/>",
  "wf-toilet-female": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" opacity=\"0.22\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"4\" r=\"2\" fill=\"currentColor\"/><path d=\"M9.5 8h5l2.5 8h-4v5h-2v-5H7l2.5-8z\" fill=\"currentColor\"/>",
  "wf-toilet-accessible": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" opacity=\"0.22\" fill=\"currentColor\"/><circle cx=\"10\" cy=\"5\" r=\"1.8\" fill=\"currentColor\"/><path d=\"M8 9h3l1.5 4h2.5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M11 13a3.5 3.5 0 1 1-5-2\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M17 9h4v11h-4\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M19 12v3\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/>",
  "wf-baby-change": "<rect x=\"2\" y=\"17\" width=\"20\" height=\"2.5\" rx=\"1\" opacity=\"0.25\" fill=\"currentColor\"/><circle cx=\"6.5\" cy=\"8.5\" r=\"2.5\" fill=\"currentColor\"/><path d=\"M9.5 12.5c1.5 0 3-1 4-2 1.5 1.5 3.5 1.5 5 1\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M12 4v4\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"m10 6 4 0\" stroke=\"currentColor\" stroke-width=\"2\"/>",
  "wf-cafe": "<path d=\"M2 8h14v6a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M16 8h1a4 4 0 0 1 0 8h-1\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M2 8h14v6a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><line x1=\"6\" y1=\"2\" x2=\"6\" y2=\"5\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"/><line x1=\"10\" y1=\"2\" x2=\"10\" y2=\"5\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"/><line x1=\"14\" y1=\"2\" x2=\"14\" y2=\"5\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"/>",
  "wf-food": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M18 2v20\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M21 2c0 4-3 5-3 8\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M4 2v6c0 1.7 1.3 3 3 3v11\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M7 2v6\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M10 2v6c0 1.7-1.3 3-3 3\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/>",
  "wf-retail": "<rect x=\"4\" y=\"8\" width=\"16\" height=\"13\" rx=\"2.5\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M8 8V6a4 4 0 0 1 8 0v2\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><rect x=\"4\" y=\"8\" width=\"16\" height=\"13\" rx=\"2.5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><circle cx=\"9\" cy=\"13\" r=\"1.2\" fill=\"currentColor\"/><circle cx=\"15\" cy=\"13\" r=\"1.2\" fill=\"currentColor\"/>",
  "wf-atm": "<rect x=\"3\" y=\"3\" width=\"18\" height=\"18\" rx=\"3\" opacity=\"0.25\" fill=\"currentColor\"/><rect x=\"3\" y=\"3\" width=\"18\" height=\"18\" rx=\"3\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><line x1=\"7\" y1=\"8\" x2=\"17\" y2=\"8\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"/><line x1=\"7\" y1=\"12\" x2=\"12\" y2=\"12\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"/><rect x=\"14\" y=\"11\" width=\"3.5\" height=\"4.5\" rx=\"0.5\" fill=\"currentColor\"/>",
  "wf-payment": "<rect x=\"2\" y=\"5\" width=\"20\" height=\"14\" rx=\"3\" opacity=\"0.25\" fill=\"currentColor\"/><rect x=\"2\" y=\"5\" width=\"20\" height=\"14\" rx=\"3\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><rect x=\"2\" y=\"9\" width=\"20\" height=\"3\" fill=\"currentColor\"/><circle cx=\"7\" cy=\"15\" r=\"1.5\" fill=\"currentColor\"/><circle cx=\"11\" cy=\"15\" r=\"1.5\" fill=\"currentColor\"/>",
  "wf-pharmacy": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M10 3h4v6h6v4h-6v6h-4v-6H4V9h6z\" fill=\"currentColor\"/>",
  "wf-water": "<path d=\"M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M12 18a4 4 0 0 0 4-4\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"/>",
  "wf-wifi": "<path d=\"M5 12.55a11 11 0 0 1 14.08 0\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.5\" stroke-linecap=\"round\" opacity=\"0.3\"/><path d=\"M1.42 9a16 16 0 0 1 21.16 0\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.5\" stroke-linecap=\"round\"/><path d=\"M8.53 16.11a6 6 0 0 1 6.95 0\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.5\" stroke-linecap=\"round\"/><circle cx=\"12\" cy=\"19.5\" r=\"1.5\" fill=\"currentColor\"/>",
  "wf-seating": "<rect x=\"3\" y=\"11\" width=\"18\" height=\"5\" rx=\"1.5\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M5 11V6a3 3 0 0 1 6 0v5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M13 11V6a3 3 0 0 1 6 0v5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><rect x=\"3\" y=\"11\" width=\"18\" height=\"5\" rx=\"1.5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M5 16v5\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M19 16v5\" stroke=\"currentColor\" stroke-width=\"2\"/>",
  "wf-parking": "<rect x=\"2\" y=\"2\" width=\"20\" height=\"20\" rx=\"4\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M8 19V5h5a4 4 0 0 1 0 8H8\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"3\" stroke-linecap=\"round\"/>",
  "wf-car": "<path d=\"M4 11l2-4.5A2 2 0 0 1 7.8 5h8.4a2 2 0 0 1 1.8 1.5L20 11v6H4v-6z\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M3 16h18v-4l-2-5H5l-2 5v4z\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><circle cx=\"7\" cy=\"16.5\" r=\"2\" fill=\"currentColor\"/><circle cx=\"17\" cy=\"16.5\" r=\"2\" fill=\"currentColor\"/>",
  "wf-bus": "<rect x=\"4\" y=\"3\" width=\"16\" height=\"15\" rx=\"3\" opacity=\"0.25\" fill=\"currentColor\"/><rect x=\"4\" y=\"3\" width=\"16\" height=\"15\" rx=\"3\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><line x1=\"4\" y1=\"10\" x2=\"20\" y2=\"10\" stroke=\"currentColor\" stroke-width=\"2\"/><circle cx=\"8\" cy=\"14\" r=\"1.5\" fill=\"currentColor\"/><circle cx=\"16\" cy=\"14\" r=\"1.5\" fill=\"currentColor\"/><path d=\"M6 18v3\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M18 18v3\" stroke=\"currentColor\" stroke-width=\"2\"/>",
  "wf-ev": "<rect x=\"3\" y=\"4\" width=\"12\" height=\"16\" rx=\"2.5\" opacity=\"0.25\" fill=\"currentColor\"/><rect x=\"3\" y=\"4\" width=\"12\" height=\"16\" rx=\"2.5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"m8 9 2-3v4h2l-3 4v-3H7l2-2\" fill=\"currentColor\"/><path d=\"M15 9h3a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2h-1\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><circle cx=\"17\" cy=\"17\" r=\"1\" fill=\"currentColor\"/>",
  "wf-info": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" opacity=\"0.25\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"7.5\" r=\"1.5\" fill=\"currentColor\"/><rect x=\"10.5\" y=\"11\" width=\"3\" height=\"6\" rx=\"0.75\" fill=\"currentColor\"/>",
  "wf-help": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M9.5 9a2.5 2.5 0 0 1 5 0c0 1.5-2 2.5-2 3.5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.5\" stroke-linecap=\"round\"/><circle cx=\"12\" cy=\"16.5\" r=\"1.5\" fill=\"currentColor\"/>",
  "wf-reception": "<rect x=\"3\" y=\"14\" width=\"18\" height=\"6\" rx=\"1.5\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M8 8a4 4 0 0 1 8 0H8z\" fill=\"currentColor\"/><line x1=\"12\" y1=\"4\" x2=\"12\" y2=\"8\" stroke=\"currentColor\" stroke-width=\"2\"/><rect x=\"3\" y=\"14\" width=\"18\" height=\"6\" rx=\"1.5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><line x1=\"2\" y1=\"20\" x2=\"22\" y2=\"20\" stroke=\"currentColor\" stroke-width=\"2\"/>",
  "wf-security": "<path d=\"M12 2s7 2.5 7 8c0 5.5-5 9.5-7 11-2-1.5-7-5.5-7-11 0-5.5 7-8 7-8z\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M12 2s7 2.5 7 8c0 5.5-5 9.5-7 11-2-1.5-7-5.5-7-11 0-5.5 7-8 7-8z\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"m9 12 2 2 4-4\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.5\" stroke-linecap=\"round\" stroke-linejoin=\"round\"/>",
  "wf-phone": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" opacity=\"0.22\" fill=\"currentColor\"/><path d=\"M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z\" fill=\"currentColor\"/>",
  "wf-intercom": "<rect x=\"5\" y=\"3\" width=\"14\" height=\"18\" rx=\"3\" opacity=\"0.25\" fill=\"currentColor\"/><rect x=\"5\" y=\"3\" width=\"14\" height=\"18\" rx=\"3\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><circle cx=\"12\" cy=\"8\" r=\"2.5\" fill=\"currentColor\"/><line x1=\"9\" y1=\"13\" x2=\"15\" y2=\"13\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"/><circle cx=\"12\" cy=\"17\" r=\"1.5\" fill=\"currentColor\"/>",
  "wf-hospital": "<rect x=\"4\" y=\"3\" width=\"16\" height=\"18\" rx=\"2\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M4 21V5a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v16H4z\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M10 7h4v3h3v4h-3v3h-4v-3H7v-4h3z\" fill=\"currentColor\"/><rect x=\"10\" y=\"17\" width=\"4\" height=\"4\" fill=\"currentColor\"/>",
  "wf-first-aid": "<rect x=\"3\" y=\"7\" width=\"18\" height=\"14\" rx=\"3\" opacity=\"0.25\" fill=\"currentColor\"/><rect x=\"3\" y=\"7\" width=\"18\" height=\"14\" rx=\"3\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M10.5 10h3v2h2v3h-2v2h-3v-2h-2v-3h2z\" fill=\"currentColor\"/>",
  "wf-consult": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" opacity=\"0.22\" fill=\"currentColor\"/><path d=\"M6 3v5a6 6 0 0 0 12 0V3\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><circle cx=\"6\" cy=\"3\" r=\"1.2\" fill=\"currentColor\"/><circle cx=\"18\" cy=\"3\" r=\"1.2\" fill=\"currentColor\"/><path d=\"M12 14v4a3 3 0 0 0 6 0v-2\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><circle cx=\"18\" cy=\"16\" r=\"2\" fill=\"currentColor\"/>",
  "wf-pathology": "<path d=\"M6.5 19.5h11l-3.5-7.5H10l-3.5 7.5z\" opacity=\"0.3\" fill=\"currentColor\"/><path d=\"M9 3h6\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M10 3v5l-4.5 9A2 2 0 0 0 7.3 20h9.4a2 2 0 0 0 1.8-3L14 8V3\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><line x1=\"7.5\" y1=\"15\" x2=\"16.5\" y2=\"15\" stroke=\"currentColor\" stroke-width=\"2\"/>",
  "wf-aed": "<path d=\"M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z\" opacity=\"0.25\" fill=\"currentColor\"/><polygon points=\"12.5 5 9 12 13 12 11 18 16 11 12 11 12.5 5\" fill=\"currentColor\"/>",
  "wf-student": "<polygon points=\"12 3 22 8.5 12 14 2 8.5\" opacity=\"0.25\" fill=\"currentColor\"/><polygon points=\"12 3 22 8.5 12 14 2 8.5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M6 10.7v5.3c0 2.2 2.7 4 6 4s6-1.8 6-4v-5.3\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M22 8.5v6\" stroke=\"currentColor\" stroke-width=\"2\"/>",
  "wf-library": "<path d=\"M3 6.5A3.5 3.5 0 0 1 6.5 3H12v15H6.5A3.5 3.5 0 0 0 3 21.5V6.5z\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M21 6.5A3.5 3.5 0 0 0 17.5 3H12v15h5.5A3.5 3.5 0 0 1 21 21.5V6.5z\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M3 6.5A3.5 3.5 0 0 1 6.5 3H12v15H6.5A3.5 3.5 0 0 0 3 21.5V6.5z\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M21 6.5A3.5 3.5 0 0 0 17.5 3H12v15h5.5A3.5 3.5 0 0 1 21 21.5V6.5z\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/>",
  "wf-lecture": "<rect x=\"3\" y=\"3\" width=\"18\" height=\"12\" rx=\"1.5\" opacity=\"0.25\" fill=\"currentColor\"/><rect x=\"3\" y=\"3\" width=\"18\" height=\"12\" rx=\"1.5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><circle cx=\"9\" cy=\"8\" r=\"1.5\" fill=\"currentColor\"/><line x1=\"13\" y1=\"6\" x2=\"18\" y2=\"6\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"/><line x1=\"13\" y1=\"9\" x2=\"16\" y2=\"9\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"/><path d=\"M12 15v6m-4 0h8\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"/>",
  "wf-emergency": "<polygon points=\"7.86 2 16.14 2 22 7.86 22 16.14 16.14 22 7.86 22 2 16.14 2 7.86\" opacity=\"0.25\" fill=\"currentColor\"/><polygon points=\"7.86 2 16.14 2 22 7.86 22 16.14 16.14 22 7.86 22 2 16.14 2 7.86\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M12 7v6\" stroke=\"currentColor\" stroke-width=\"3\" stroke-linecap=\"round\"/><circle cx=\"12\" cy=\"17\" r=\"1.5\" fill=\"currentColor\"/>",
  "wf-evacuate": "<rect x=\"13\" y=\"3\" width=\"8\" height=\"18\" rx=\"1.5\" opacity=\"0.25\" fill=\"currentColor\"/><rect x=\"13\" y=\"3\" width=\"8\" height=\"18\" rx=\"1.5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><circle cx=\"8\" cy=\"6\" r=\"1.8\" fill=\"currentColor\"/><path d=\"M6 16l2-3 2 1.5 3-4.5h2v1.5h-1.2l-2.5 3.5-2-1.5-2 4.5H6z\" fill=\"currentColor\"/>",
  "wf-assembly": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" opacity=\"0.22\" fill=\"currentColor\"/><path d=\"M4 12h5m-2.5-2.5L9 12l-2.5 2.5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"/><path d=\"M20 12h-5m2.5-2.5L15 12l2.5 2.5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"/><path d=\"M12 4v5m-2.5-2.5L12 9l2.5-2.5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"/><path d=\"M12 20v-5m-2.5 2.5L12 15l2.5 2.5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"/><circle cx=\"12\" cy=\"12\" r=\"1.5\" fill=\"currentColor\"/>",
  "wf-fire": "<path d=\"M12 2C9 7 5 9 5 15a7 7 0 0 0 14 0c0-6-4-8-7-13z\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M12 2C9 7 5 9 5 15a7 7 0 0 0 14 0c0-6-4-8-7-13z\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M12 18a3 3 0 0 0 3-3c0-2-1.5-3-3-5-1.5 2-3 3-3 5a3 3 0 0 0 3 3z\" fill=\"currentColor\"/>",
  "wf-warning": "<polygon points=\"12 2 22 20 2 20\" opacity=\"0.25\" fill=\"currentColor\"/><polygon points=\"12 2 22 20 2 20\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><line x1=\"12\" y1=\"9\" x2=\"12\" y2=\"13\" stroke=\"currentColor\" stroke-width=\"3\" stroke-linecap=\"round\"/><circle cx=\"12\" cy=\"17\" r=\"1.5\" fill=\"currentColor\"/>",
  "wf-construction": "<polygon points=\"7 19 17 19 14 5 10 5\" opacity=\"0.25\" fill=\"currentColor\"/><polygon points=\"7 19 17 19 14 5 10 5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><line x1=\"4\" y1=\"21\" x2=\"20\" y2=\"21\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"/><line x1=\"8.5\" y1=\"14\" x2=\"15.5\" y2=\"14\" stroke=\"currentColor\" stroke-width=\"2\"/><line x1=\"9.5\" y1=\"9\" x2=\"14.5\" y2=\"9\" stroke=\"currentColor\" stroke-width=\"2\"/>",
  "wf-home": "<path d=\"M4 10v10a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1V10l-8-6-8 6z\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M3 10l9-7 9 7\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"/><rect x=\"9\" y=\"13\" width=\"6\" height=\"8\" rx=\"0.5\" fill=\"currentColor\"/>",
  "wf-search": "<circle cx=\"10.5\" cy=\"10.5\" r=\"7\" opacity=\"0.25\" fill=\"currentColor\"/><circle cx=\"10.5\" cy=\"10.5\" r=\"7\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><line x1=\"15.5\" y1=\"15.5\" x2=\"21\" y2=\"21\" stroke=\"currentColor\" stroke-width=\"3\" stroke-linecap=\"round\"/>",
  "wf-menu": "<rect x=\"3\" y=\"3\" width=\"18\" height=\"18\" rx=\"4\" opacity=\"0.22\" fill=\"currentColor\"/><line x1=\"7\" y1=\"8\" x2=\"17\" y2=\"8\" stroke=\"currentColor\" stroke-width=\"2.5\" stroke-linecap=\"round\"/><line x1=\"7\" y1=\"12\" x2=\"17\" y2=\"12\" stroke=\"currentColor\" stroke-width=\"2.5\" stroke-linecap=\"round\"/><line x1=\"7\" y1=\"16\" x2=\"17\" y2=\"16\" stroke=\"currentColor\" stroke-width=\"2.5\" stroke-linecap=\"round\"/>",
  "wf-back": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" opacity=\"0.22\" fill=\"currentColor\"/><path d=\"M14 7l-5 5 5 5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"3\" stroke-linecap=\"round\" stroke-linejoin=\"round\"/>",
  "wf-close": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" opacity=\"0.22\" fill=\"currentColor\"/><line x1=\"8\" y1=\"8\" x2=\"16\" y2=\"16\" stroke=\"currentColor\" stroke-width=\"2.5\" stroke-linecap=\"round\"/><line x1=\"16\" y1=\"8\" x2=\"8\" y2=\"16\" stroke=\"currentColor\" stroke-width=\"2.5\" stroke-linecap=\"round\"/>",
  "wf-hours": "<circle cx=\"12\" cy=\"12\" r=\"9\" opacity=\"0.25\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"12\" r=\"9\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><polyline points=\"12 7 12 12 15.5 12\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.5\" stroke-linecap=\"round\"/>",
  "wf-timetable": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"17\" rx=\"2.5\" opacity=\"0.25\" fill=\"currentColor\"/><rect x=\"3\" y=\"4\" width=\"18\" height=\"17\" rx=\"2.5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><line x1=\"3\" y1=\"9\" x2=\"21\" y2=\"9\" stroke=\"currentColor\" stroke-width=\"2\"/><line x1=\"8\" y1=\"2\" x2=\"8\" y2=\"5\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"/><line x1=\"16\" y1=\"2\" x2=\"16\" y2=\"5\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"/><circle cx=\"8\" cy=\"13\" r=\"1.2\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"13\" r=\"1.2\" fill=\"currentColor\"/><circle cx=\"16\" cy=\"13\" r=\"1.2\" fill=\"currentColor\"/><circle cx=\"8\" cy=\"17\" r=\"1.2\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"17\" r=\"1.2\" fill=\"currentColor\"/>",
  "wf-events": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"17\" rx=\"2.5\" opacity=\"0.25\" fill=\"currentColor\"/><rect x=\"3\" y=\"4\" width=\"18\" height=\"17\" rx=\"2.5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><line x1=\"3\" y1=\"9\" x2=\"21\" y2=\"9\" stroke=\"currentColor\" stroke-width=\"2\"/><line x1=\"8\" y1=\"2\" x2=\"8\" y2=\"5\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"/><line x1=\"16\" y1=\"2\" x2=\"16\" y2=\"5\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"/><polygon points=\"12 11 13.5 14 16.5 14.5 14.2 16.8 14.8 20 12 18.2 9.2 20 9.8 16.8 7.5 14.5 10.5 14\" fill=\"currentColor\"/>",
  "wf-news": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"16\" rx=\"2\" opacity=\"0.25\" fill=\"currentColor\"/><rect x=\"3\" y=\"4\" width=\"18\" height=\"16\" rx=\"2\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><rect x=\"6\" y=\"7\" width=\"5\" height=\"4\" fill=\"currentColor\"/><line x1=\"13\" y1=\"7\" x2=\"18\" y2=\"7\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\"/><line x1=\"13\" y1=\"10\" x2=\"18\" y2=\"10\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\"/><line x1=\"6\" y1=\"14\" x2=\"18\" y2=\"14\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\"/><line x1=\"6\" y1=\"17\" x2=\"15\" y2=\"17\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\"/>",
  "wf-announce": "<polygon points=\"4 9 12 5 12 17 4 13\" opacity=\"0.25\" fill=\"currentColor\"/><polygon points=\"4 9 12 5 12 17 4 13\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M6 13v4a2 2 0 0 0 2 2h1v-6\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M16 8a4 4 0 0 1 0 8\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"/><path d=\"M19 6a8 8 0 0 1 0 12\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"/>",
  "wf-share": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" opacity=\"0.22\" fill=\"currentColor\"/><line x1=\"8.6\" y1=\"13.5\" x2=\"15.4\" y2=\"17.5\" stroke=\"currentColor\" stroke-width=\"2\"/><line x1=\"15.4\" y1=\"6.5\" x2=\"8.6\" y2=\"10.5\" stroke=\"currentColor\" stroke-width=\"2\"/><circle cx=\"18\" cy=\"5\" r=\"2.5\" fill=\"currentColor\"/><circle cx=\"6\" cy=\"12\" r=\"2.5\" fill=\"currentColor\"/><circle cx=\"18\" cy=\"19\" r=\"2.5\" fill=\"currentColor\"/>",
  "wf-chat": "<path d=\"M17 11h1a3 3 0 0 0 3-3V5a3 3 0 0 0-3-3H9a3 3 0 0 0-3 3v1\" opacity=\"0.25\" fill=\"currentColor\"/><path d=\"M14 16H6l-3 4V7a3 3 0 0 1 3-3h8a3 3 0 0 1 3 3v6a3 3 0 0 1-3 3z\" fill=\"currentColor\"/><circle cx=\"6.5\" cy=\"10\" r=\"1\" fill=\"#fff\"/><circle cx=\"10\" cy=\"10\" r=\"1\" fill=\"#fff\"/><circle cx=\"13.5\" cy=\"10\" r=\"1\" fill=\"#fff\"/>",
  "wf-like": "<circle cx=\"12\" cy=\"12\" r=\"9.5\" opacity=\"0.22\" fill=\"currentColor\"/><path d=\"M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3H14zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3\" fill=\"currentColor\"/>",
  "wf-camera": "<rect x=\"3\" y=\"7\" width=\"18\" height=\"14\" rx=\"3\" opacity=\"0.25\" fill=\"currentColor\"/><rect x=\"3\" y=\"7\" width=\"18\" height=\"14\" rx=\"3\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M8 7l1.5-2.5h5L16 7\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><circle cx=\"12\" cy=\"14\" r=\"3.5\" fill=\"currentColor\"/><circle cx=\"17.5\" cy=\"10\" r=\"0.8\" fill=\"currentColor\"/>",
  "wf-video": "<rect x=\"2\" y=\"6\" width=\"14\" height=\"12\" rx=\"2.5\" opacity=\"0.25\" fill=\"currentColor\"/><rect x=\"2\" y=\"6\" width=\"14\" height=\"12\" rx=\"2.5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><polygon points=\"22 7 16 11 16 13 22 17 22 7\" fill=\"currentColor\"/><polygon points=\"7.5 9.5 11.5 12 7.5 14.5\" fill=\"currentColor\"/>",
  "wf-qr": "<rect x=\"2\" y=\"2\" width=\"20\" height=\"20\" rx=\"3\" opacity=\"0.22\" fill=\"currentColor\"/><rect x=\"4\" y=\"4\" width=\"6\" height=\"6\" rx=\"1\" fill=\"currentColor\"/><rect x=\"14\" y=\"4\" width=\"6\" height=\"6\" rx=\"1\" fill=\"currentColor\"/><rect x=\"4\" y=\"14\" width=\"6\" height=\"6\" rx=\"1\" fill=\"currentColor\"/><rect x=\"5.5\" y=\"5.5\" width=\"3\" height=\"3\" fill=\"#fff\"/><rect x=\"15.5\" y=\"5.5\" width=\"3\" height=\"3\" fill=\"#fff\"/><rect x=\"5.5\" y=\"15.5\" width=\"3\" height=\"3\" fill=\"#fff\"/><rect x=\"14\" y=\"14\" width=\"2.5\" height=\"2.5\" fill=\"currentColor\"/><rect x=\"17.5\" y=\"17.5\" width=\"2.5\" height=\"2.5\" fill=\"currentColor\"/><rect x=\"14\" y=\"17.5\" width=\"2.5\" height=\"2.5\" fill=\"currentColor\"/>",
  "wf-email": "<rect x=\"2\" y=\"4\" width=\"20\" height=\"16\" rx=\"2.5\" opacity=\"0.25\" fill=\"currentColor\"/><rect x=\"2\" y=\"4\" width=\"20\" height=\"16\" rx=\"2.5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><polyline points=\"22,6 12,13 2,6\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/>",
  "wf-web": "<circle cx=\"12\" cy=\"12\" r=\"9\" opacity=\"0.25\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"12\" r=\"9\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><line x1=\"3\" y1=\"12\" x2=\"21\" y2=\"12\" stroke=\"currentColor\" stroke-width=\"2\"/><ellipse cx=\"12\" cy=\"12\" rx=\"4.5\" ry=\"9\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/>"
};

export const WAYFINDING_SOLID = {
  "wf-arrow-up": "<path d=\"M12 2.5l7 7h-4.5v12h-5v-12H5z\" fill=\"currentColor\"/>",
  "wf-arrow-right": "<path d=\"M21.5 12l-7-7v4.5H2.5v5h12v4.5z\" fill=\"currentColor\"/>",
  "wf-arrow-down": "<path d=\"M12 21.5l-7-7h4.5V2.5h5v12H19z\" fill=\"currentColor\"/>",
  "wf-arrow-left": "<path d=\"M2.5 12l7 7v-4.5h12v-5h-12V5z\" fill=\"currentColor\"/>",
  "wf-arrow-up-right": "<path d=\"M7 3.5h13.5V17l-4.2-4.2-9 9-2.8-2.8 9-9z\" fill=\"currentColor\"/>",
  "wf-arrow-up-left": "<path d=\"M17 3.5H3.5V17l4.2-4.2 9 9 2.8-2.8-9-9z\" fill=\"currentColor\"/>",
  "wf-u-turn": "<path d=\"M9 18l-5-5h3.5A7.5 7.5 0 0 1 15 5.5a7.5 7.5 0 0 1 7.5 7.5v6h-4v-6a3.5 3.5 0 0 0-3.5-3.5A3.5 3.5 0 0 0 11.5 13H15z\" fill=\"currentColor\"/>",
  "wf-signpost": "<path d=\"M10.5 2h3v2h5.5l2 2.5-2 2.5H13.5v2H19a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1h-5.5v5h-3v-5H5a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1h5.5V9H5L3 6.5 5 4h5.5z\" fill=\"currentColor\"/>",
  "wf-pin": "<path d=\"M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z\" fill=\"currentColor\"/>",
  "wf-facing": "<circle cx=\"12\" cy=\"12\" r=\"10\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.5\"/><polygon points=\"12 4 16 13 12 11 8 13 12 4\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"17\" r=\"1.5\" fill=\"currentColor\"/>",
  "wf-map": "<path d=\"M3 6.2l5.7-2.3 6.6 2.6L21 4.2v13.6l-5.7 2.3-6.6-2.6L3 19.8V6.2zm7.2.3v10.9l3.6 1.4V7.9l-3.6-1.4z\" fill=\"currentColor\"/>",
  "wf-touch": "<path d=\"M11 1.5a1.5 1.5 0 0 1 3 0V9.2a3 3 0 0 1 3.5 3v3.5a5.5 5.5 0 0 1-5.5 5.5H10a5.5 5.5 0 0 1-3.9-1.6l-3.5-3.5 1.5-1.5 2.9 1.7V1.5z\" fill=\"currentColor\"/><path d=\"M12.5 0a7 7 0 0 1 7 7h-2a5 5 0 0 0-5-5V0z\" fill=\"currentColor\"/>",
  "wf-entrance": "<path d=\"M13 2h8a1 1 0 0 1 1 1v17a1 1 0 0 1-1 1h-8v-2h6V4h-6V2z\" fill=\"currentColor\"/><path d=\"m13 3-8 3v12l8 3V3z\" fill=\"currentColor\"/><circle cx=\"8\" cy=\"12\" r=\"1\" fill=\"#fff\"/><path d=\"M1 11h7v-3l4 4-4 4v-3H1z\" fill=\"currentColor\"/><rect x=\"1\" y=\"21\" width=\"22\" height=\"2\" rx=\"0.5\" fill=\"currentColor\"/>",
  "wf-exit": "<path d=\"M11 2H3a1 1 0 0 0-1 1v17a1 1 0 0 0 1 1h8v-2H5V4h6V2z\" fill=\"currentColor\"/><path d=\"m11 3 8 3v12l-8 3V3z\" fill=\"currentColor\"/><circle cx=\"16\" cy=\"12\" r=\"1\" fill=\"#fff\"/><path d=\"M15 11h4v-3l4 4-4 4v-3h-4z\" fill=\"currentColor\"/><rect x=\"1\" y=\"21\" width=\"22\" height=\"2\" rx=\"0.5\" fill=\"currentColor\"/>",
  "wf-lift": "<rect x=\"2\" y=\"2\" width=\"13\" height=\"20\" rx=\"3\" fill=\"currentColor\"/><circle cx=\"6\" cy=\"7.5\" r=\"1.5\" fill=\"#fff\"/><path d=\"M4 16v-3a2 2 0 0 1 4 0v3H4z\" fill=\"#fff\"/><circle cx=\"11\" cy=\"7.5\" r=\"1.5\" fill=\"#fff\"/><path d=\"M9 16v-3a2 2 0 0 1 4 0v3H9z\" fill=\"#fff\"/><polygon points=\"19.5 4 16 8.5 23 8.5\" fill=\"currentColor\"/><polygon points=\"19.5 20 16 15.5 23 15.5\" fill=\"currentColor\"/><rect x=\"18.5\" y=\"10.5\" width=\"2\" height=\"3\" rx=\"0.5\" fill=\"currentColor\"/>",
  "wf-stairs": "<polygon points=\"4 20 20 20 20 6 16 6 16 10 12 10 12 14 8 14 8 18 4 18 4 20\" fill=\"currentColor\"/><circle cx=\"8\" cy=\"5\" r=\"2\" fill=\"currentColor\"/><path d=\"m11.5 10-2-2.5-2.5 1.5 1 2 2-1z\" fill=\"currentColor\"/>",
  "wf-escalator-up": "<polygon points=\"3 8 8 8 15 18 21 18 21 20 14 20 7 10 3 10\" fill=\"currentColor\"/><polygon points=\"6 14 6 17 9 17 9 14\" fill=\"currentColor\"/><path d=\"M3 17l4-4 1.4 1.4-2.6 2.6H9v2H3z\" fill=\"currentColor\"/><circle cx=\"7\" cy=\"4\" r=\"1.8\" fill=\"currentColor\"/><path d=\"m9 9.5-2-2.5-2 1.5.8 1.8 1.7-.8z\" fill=\"currentColor\"/>",
  "wf-escalator-down": "<polygon points=\"3 18 8 18 15 8 21 8 21 6 14 6 7 16 3 16\" fill=\"currentColor\"/><path d=\"M19 14l-4 4-1.4-1.4 2.6-2.6H13v-2h6z\" fill=\"currentColor\"/><circle cx=\"17\" cy=\"4\" r=\"1.8\" fill=\"currentColor\"/><path d=\"m15 9.5 2-2.5 2 1.5-.8 1.8-1.7-.8z\" fill=\"currentColor\"/>",
  "wf-ramp": "<polygon points=\"2 20 22 20 22 10 2 20\" fill=\"currentColor\"/><circle cx=\"14\" cy=\"5.5\" r=\"1.8\" fill=\"currentColor\"/><path d=\"M11.5 13a2.8 2.8 0 1 1 3.5-3.3l1.8-1.8 1.4 1.4-2.4 2.4-1.5-.5a1.5 1.5 0 0 0-1.8 1.8z\" fill=\"currentColor\"/>",
  "wf-accessible": "<circle cx=\"12\" cy=\"4\" r=\"2\" fill=\"currentColor\"/><path d=\"M10 8h4.5l1.6 5.5h2.9v2h-4.2l-1.3-4.5H11v3.5a4.5 4.5 0 1 1-5-4.4V8h4zm-1.5 6a2.5 2.5 0 1 0 2.5 2.5V14H8.5z\" fill=\"currentColor\"/>",
  "wf-levels": "<polygon points=\"12 2 21 6.5 12 11 3 6.5\" fill=\"currentColor\"/><polygon points=\"12 7.5 21 12 12 16.5 3 12\" fill=\"currentColor\"/><polygon points=\"12 13 21 17.5 12 22 3 17.5\" fill=\"currentColor\"/>",
  "wf-no-entry": "<path d=\"M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm6 11.5H6v-3h12v3z\" fill=\"currentColor\"/>",
  "wf-prohibited": "<path d=\"M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 2a7.95 7.95 0 0 1 5.36 2.06L6.06 17.36A8 8 0 0 1 12 4zm0 16a7.95 7.95 0 0 1-5.36-2.06L17.94 6.64A8 8 0 0 1 12 20z\" fill=\"currentColor\"/>",
  "wf-staff-only": "<rect x=\"4\" y=\"7\" width=\"16\" height=\"15\" rx=\"3\" fill=\"currentColor\"/><path d=\"M9 7V4a3 3 0 0 1 6 0v3h-2V4a1 1 0 0 0-2 0v3H9z\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"12\" r=\"2\" fill=\"#fff\"/><path d=\"M9 19c0-1.7 1.3-3 3-3s3 1.3 3 3H9z\" fill=\"#fff\"/>",
  "wf-toilets": "<circle cx=\"7\" cy=\"4\" r=\"1.8\" fill=\"currentColor\"/><path d=\"M4.5 8h5a1 1 0 0 1 1 1v6h-2v5H6.5v-5h-2V9a1 1 0 0 1 1-1z\" fill=\"currentColor\"/><circle cx=\"17\" cy=\"4\" r=\"1.8\" fill=\"currentColor\"/><path d=\"M14.5 8h5l2.2 7h-3.2v5h-2v-5h-3.2l2.2-7z\" fill=\"currentColor\"/><line x1=\"12\" y1=\"3\" x2=\"12\" y2=\"21\" stroke=\"currentColor\" stroke-width=\"1.5\"/>",
  "wf-toilet-male": "<circle cx=\"12\" cy=\"4\" r=\"2.2\" fill=\"currentColor\"/><path d=\"M8.5 8.5h7a1.5 1.5 0 0 1 1.5 1.5V16h-2.5v5.5h-5V16H7v-6a1.5 1.5 0 0 1 1.5-1.5z\" fill=\"currentColor\"/>",
  "wf-toilet-female": "<circle cx=\"12\" cy=\"4\" r=\"2.2\" fill=\"currentColor\"/><path d=\"M9 8.5h6l3 8.5h-4.5v4.5h-3V17H6l3-8.5z\" fill=\"currentColor\"/>",
  "wf-toilet-accessible": "<circle cx=\"9\" cy=\"4.5\" r=\"1.8\" fill=\"currentColor\"/><path d=\"M7 8h4.5l1.6 5h2.9v1.8h-4.2l-1.3-4H8.5v3a4 4 0 1 1-4.5-3.9V8H7z\" fill=\"currentColor\"/><rect x=\"17\" y=\"5\" width=\"4\" height=\"15\" rx=\"1\" fill=\"currentColor\"/><rect x=\"15\" y=\"14\" width=\"4\" height=\"2\" fill=\"currentColor\"/>",
  "wf-baby-change": "<rect x=\"2\" y=\"17\" width=\"20\" height=\"2.5\" rx=\"1\" fill=\"currentColor\"/><circle cx=\"6.5\" cy=\"8.5\" r=\"2.2\" fill=\"currentColor\"/><path d=\"M9.5 13a4 4 0 0 0 4-2.5 3.5 3.5 0 0 1 5 1.5v3H9.5z\" fill=\"currentColor\"/><path d=\"M12 4v4m-2-2h4\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"/>",
  "wf-cafe": "<path d=\"M18 7h1a4 4 0 0 1 0 8h-1v-8zm2 6a2 2 0 0 0 0-4v4z\" fill=\"currentColor\"/><path d=\"M2 7h15v7a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V7zm0 12h17a1 1 0 0 1 0 2H2a1 1 0 0 1 0-2z\" fill=\"currentColor\"/><path d=\"M5 2v3m4-3v3m4-3v3\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\"/>",
  "wf-food": "<path d=\"M18 2v20h2V2h-2zm-12 0v7a2 2 0 0 1-2 2v11h2V11a2 2 0 0 1-2-2V2h2zm4 0v7a2 2 0 0 1-2 2v11h2V11a2 2 0 0 0 2-2V2h-2z\" fill=\"currentColor\"/>",
  "wf-retail": "<path d=\"M6 7V5a6 6 0 0 1 12 0v2h3a1 1 0 0 1 1 1l-1.5 13A2 2 0 0 1 18.5 22H5.5a2 2 0 0 1-2-1.8L2 8a1 1 0 0 1 1-1h3zm2 0h8V5a4 4 0 0 0-8 0v2z\" fill=\"currentColor\"/>",
  "wf-atm": "<rect x=\"3\" y=\"3\" width=\"18\" height=\"18\" rx=\"3\" fill=\"currentColor\"/><rect x=\"6\" y=\"6\" width=\"12\" height=\"3\" rx=\"0.5\" fill=\"#fff\"/><rect x=\"6\" y=\"11\" width=\"6\" height=\"2\" fill=\"#fff\"/><rect x=\"14\" y=\"11\" width=\"4\" height=\"6\" rx=\"1\" fill=\"#fff\"/>",
  "wf-payment": "<rect x=\"2\" y=\"4\" width=\"20\" height=\"16\" rx=\"3\" fill=\"currentColor\"/><rect x=\"2\" y=\"8\" width=\"20\" height=\"3.5\" fill=\"#fff\"/><circle cx=\"7\" cy=\"15.5\" r=\"1.8\" fill=\"#fff\"/><circle cx=\"11.5\" cy=\"15.5\" r=\"1.8\" fill=\"#fff\"/>",
  "wf-pharmacy": "<rect x=\"2\" y=\"2\" width=\"20\" height=\"20\" rx=\"4\" fill=\"currentColor\"/><path d=\"M10 6h4v4h4v4h-4v4h-4v-4H6v-4h4V6z\" fill=\"#fff\"/>",
  "wf-water": "<path d=\"M12 2.5C12 2.5 5 10.5 5 15.5a7 7 0 0 0 14 0c0-5-7-13-7-13zm0 16a4.5 4.5 0 0 1-4.5-4.5c0-.6.4-1 1-1s1 .4 1 1A2.5 2.5 0 0 0 12 16.5c.6 0 1 .4 1 1s-.4 1-1 1z\" fill=\"currentColor\"/>",
  "wf-wifi": "<path d=\"M12 4a14.8 14.8 0 0 1 9.9 3.9l-2.1 2.1A11.8 11.8 0 0 0 12 7c-3 0-5.8 1.1-7.8 3L2.1 7.9A14.8 14.8 0 0 1 12 4zm0 6a8.8 8.8 0 0 1 5.8 2.2l-2.1 2.1A5.8 5.8 0 0 0 12 13c-1.4 0-2.8.5-3.7 1.3L6.2 12.2A8.8 8.8 0 0 1 12 10zm0 6a3 3 0 0 1 2 1l-2 2-2-2a3 3 0 0 1 2-1z\" fill=\"currentColor\"/>",
  "wf-seating": "<path d=\"M4 5a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v9h-2V5H6v9H4V5zm-2 9h20a1 1 0 0 1 1 1v4a2 2 0 0 1-2 2h-1v-2H4v2H2a2 2 0 0 1-2-2v-4a1 1 0 0 1 1-1z\" fill=\"currentColor\"/>",
  "wf-parking": "<rect x=\"3\" y=\"3\" width=\"18\" height=\"18\" rx=\"4\" fill=\"currentColor\"/><path d=\"M9 17V7h4.5a3.5 3.5 0 0 1 0 7H11v3H9zm2-5h2.5a1.5 1.5 0 0 0 0-3H11v3z\" fill=\"#fff\"/>",
  "wf-car": "<path d=\"M18.9 6.8A2 2 0 0 0 17.3 6H6.7a2 2 0 0 0-1.6.8L3 11v8a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-1h12v1a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-8l-2.1-4.2zM7.5 15a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm9 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zM6 10l1.3-3h9.4l1.3 3H6z\" fill=\"currentColor\"/>",
  "wf-bus": "<rect x=\"4\" y=\"3\" width=\"16\" height=\"16\" rx=\"3\" fill=\"currentColor\"/><rect x=\"6\" y=\"6\" width=\"12\" height=\"4.5\" rx=\"1\" fill=\"#fff\"/><circle cx=\"8\" cy=\"14\" r=\"1.5\" fill=\"#fff\"/><circle cx=\"16\" cy=\"14\" r=\"1.5\" fill=\"#fff\"/><rect x=\"5.5\" y=\"19\" width=\"3\" height=\"3\" rx=\"0.5\" fill=\"currentColor\"/><rect x=\"15.5\" y=\"19\" width=\"3\" height=\"3\" rx=\"0.5\" fill=\"currentColor\"/>",
  "wf-ev": "<rect x=\"2\" y=\"4\" width=\"13\" height=\"17\" rx=\"3\" fill=\"currentColor\"/><path d=\"M8 8l-2 4h3l-1 4 4-5h-3l2-3H8z\" fill=\"#fff\"/><path d=\"M15 9h2a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2h-1v-2h1v-4h-2V9zm4 1v2h2v-2h-2z\" fill=\"currentColor\"/>",
  "wf-info": "<circle cx=\"12\" cy=\"12\" r=\"10\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"7.5\" r=\"1.5\" fill=\"#fff\"/><path d=\"M10.5 11h3v6h-3z\" fill=\"#fff\"/>",
  "wf-help": "<circle cx=\"12\" cy=\"12\" r=\"10\" fill=\"currentColor\"/><path d=\"M9.5 9a2.5 2.5 0 0 1 4.9.8c0 1.5-2.4 2-2.4 3.7h-2c0-2.3 2.5-2.8 2.5-3.7a.7.7 0 0 0-.7-.7.9.9 0 0 0-.9.9H9.5z\" fill=\"#fff\"/><circle cx=\"11\" cy=\"16.5\" r=\"1.2\" fill=\"#fff\"/>",
  "wf-reception": "<rect x=\"2\" y=\"15\" width=\"20\" height=\"6\" rx=\"1.5\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"6\" r=\"2.5\" fill=\"currentColor\"/><path d=\"M7 15v-1a5 5 0 0 1 10 0v1H7z\" fill=\"currentColor\"/>",
  "wf-security": "<path d=\"M12 2s8 3 8 9c0 6.5-6 10.5-8 11-2-.5-8-4.5-8-11 0-6 8-9 8-9zm-1 13l5-5-1.4-1.4-3.6 3.6-1.6-1.6L8 12l3 3z\" fill=\"currentColor\"/>",
  "wf-phone": "<path d=\"M20 15.5c-1.2 0-2.4-.2-3.6-.6-.4-.1-.8 0-1.1.3l-2.2 2.2a15 15 0 0 1-6.6-6.6l2.2-2.2c.3-.3.4-.7.2-1.1-.4-1.1-.6-2.3-.6-3.5 0-.6-.4-1-1-1H4c-.6 0-1 .4-1 1 0 9.4 7.6 17 17 17 .6 0 1-.4 1-1v-3.5c0-.6-.4-1-1-1z\" fill=\"currentColor\"/>",
  "wf-intercom": "<rect x=\"5\" y=\"2\" width=\"14\" height=\"20\" rx=\"3\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"7.5\" r=\"2.5\" fill=\"#fff\"/><rect x=\"8\" y=\"12\" width=\"8\" height=\"1.8\" rx=\"0.5\" fill=\"#fff\"/><circle cx=\"12\" cy=\"17\" r=\"1.8\" fill=\"#fff\"/>",
  "wf-hospital": "<rect x=\"3\" y=\"3\" width=\"18\" height=\"19\" rx=\"3\" fill=\"currentColor\"/><path d=\"M10 7h4v3h3v4h-3v3h-4v-3H7v-4h3V7z\" fill=\"#fff\"/>",
  "wf-first-aid": "<rect x=\"2\" y=\"6\" width=\"20\" height=\"15\" rx=\"3\" fill=\"currentColor\"/><path d=\"M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2h-2V4h-4v2H8zm2 4h4v3h3v4h-3v3h-4v-3H7v-4h3v-3z\" fill=\"#fff\"/>",
  "wf-consult": "<path d=\"M6 3v6a6 6 0 0 0 12 0V3h-2v6a4 4 0 0 1-8 0V3H6zm6 12a3 3 0 0 0-3 3v2a3 3 0 0 0 6 0v-2a3 3 0 0 0-3-3zm6 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4z\" fill=\"currentColor\"/>",
  "wf-pathology": "<path d=\"M9 2h6v2h-1v5.5l5.2 9.4A2 2 0 0 1 17.5 22H6.5a2 2 0 0 1-1.7-3.1L10 9.5V4H9V2zm2 9.5l-4 7.2a.5.5 0 0 0 .4.8h9.2a.5.5 0 0 0 .4-.8l-4-7.2h-2z\" fill=\"currentColor\"/>",
  "wf-aed": "<path d=\"M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z\" fill=\"currentColor\"/><polygon points=\"12.5 6 9.5 12 13 12 11.5 17 15.5 11 12 11 12.5 6\" fill=\"#fff\"/>",
  "wf-student": "<polygon points=\"12 2 22 7.5 12 13 2 7.5\" fill=\"currentColor\"/><path d=\"M6 10.5v5.5c0 2.2 2.7 4 6 4s6-1.8 6-4v-5.5l-6 3.3-6-3.3zm16-3v6h-2v-5l2-1z\" fill=\"currentColor\"/>",
  "wf-library": "<path d=\"M4 3a2 2 0 0 1 2-2h13a1 1 0 0 1 1 1v20a1 1 0 0 1-1 1H6a2 2 0 0 1-2-2V3zm3 0v17h11V3H7zm2 4h7v2H9V7zm0 4h5v2H9v-2z\" fill=\"currentColor\"/>",
  "wf-lecture": "<rect x=\"2\" y=\"3\" width=\"20\" height=\"13\" rx=\"2\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"8\" r=\"2\" fill=\"#fff\"/><polygon points=\"9 16 7 21 9 21 10.5 16\" fill=\"currentColor\"/><polygon points=\"15 16 17 21 15 21 13.5 16\" fill=\"currentColor\"/><rect x=\"8\" y=\"15\" width=\"8\" height=\"2\" rx=\"0.5\" fill=\"currentColor\"/>",
  "wf-emergency": "<polygon points=\"12 2 22 7.8 22 16.2 12 22 2 16.2 2 7.8\" fill=\"currentColor\"/><rect x=\"11\" y=\"7\" width=\"2\" height=\"6\" rx=\"0.5\" fill=\"#fff\"/><circle cx=\"12\" cy=\"16\" r=\"1.2\" fill=\"#fff\"/>",
  "wf-evacuate": "<rect x=\"16\" y=\"2\" width=\"6\" height=\"20\" rx=\"1\" fill=\"currentColor\"/><circle cx=\"8\" cy=\"5.5\" r=\"1.8\" fill=\"currentColor\"/><path d=\"M5 10l3.5-2 3.5 2.5v4h-2v-3l-2-1.5-3 5-1.5-1 2.5-4z\" fill=\"currentColor\"/><path d=\"m8 14 3 6-1.7 1-3.3-6.5L8 14z\" fill=\"currentColor\"/>",
  "wf-assembly": "<circle cx=\"12\" cy=\"12\" r=\"3\" fill=\"currentColor\"/><polygon points=\"3 3 8 3 8 5 5.5 5 9 8.5 7.5 10 4 6.5 4 9 2 9 2 3\" fill=\"currentColor\"/><polygon points=\"21 3 21 9 19 9 19 6.5 15.5 10 14 8.5 17.5 5 15 5 15 3\" fill=\"currentColor\"/><polygon points=\"3 21 3 15 5 15 5 17.5 8.5 14 10 15.5 6.5 19 9 19 9 21\" fill=\"currentColor\"/><polygon points=\"21 21 15 21 15 19 17.5 19 14 15.5 15.5 14 19 17.5 19 15 21 15\" fill=\"currentColor\"/>",
  "wf-fire": "<path d=\"M12 2c1.2 3.5 4.5 5.5 4.5 10a6.5 6.5 0 0 1-13 0c0-4 2.5-7 4.5-9 1 2 2.5 3 4-1z\" fill=\"currentColor\"/><path d=\"M12 13.5c1.2 0 2 1 2 2a2 2 0 0 1-4 0c0-1 .8-2 2-2z\" fill=\"#fff\"/>",
  "wf-warning": "<path d=\"M12 2L1 21h22L12 2zm-1 7h2v6h-2V9zm1 10a1.2 1.2 0 1 1 0-2.4 1.2 1.2 0 0 1 0 2.4z\" fill=\"currentColor\"/>",
  "wf-construction": "<polygon points=\"12 2 18 19 6 19\" fill=\"currentColor\"/><rect x=\"2\" y=\"20\" width=\"20\" height=\"2.5\" rx=\"0.5\" fill=\"currentColor\"/><polygon points=\"10 8 14 8 15 12 9 12\" fill=\"#fff\"/><polygon points=\"8.5 14 15.5 14 16.5 17 7.5 17\" fill=\"#fff\"/>",
  "wf-home": "<polygon points=\"12 2 2 10 4 10 4 21 10 21 10 14 14 14 14 21 20 21 20 10 22 10\" fill=\"currentColor\"/>",
  "wf-search": "<path d=\"M15.5 14h-.8l-.3-.3a6.5 6.5 0 1 0-.7.7l.3.3v.8l5 5 1.5-1.5-5-5zm-6 0C7 14 5 12 5 9.5S7 5 9.5 5 14 7 14 9.5 12 14 9.5 14z\" fill=\"currentColor\"/>",
  "wf-menu": "<rect x=\"3\" y=\"5\" width=\"18\" height=\"3\" rx=\"1.5\" fill=\"currentColor\"/><rect x=\"3\" y=\"11\" width=\"18\" height=\"3\" rx=\"1.5\" fill=\"currentColor\"/><rect x=\"3\" y=\"17\" width=\"18\" height=\"3\" rx=\"1.5\" fill=\"currentColor\"/>",
  "wf-back": "<path d=\"M15.5 19l-7-7 7-7 1.8 1.8L12 12l5.3 5.2z\" fill=\"currentColor\"/>",
  "wf-close": "<path d=\"M19 6.4L17.6 5 12 10.6 6.4 5 5 6.4l5.6 5.6L5 17.6 6.4 19l5.6-5.6 5.6 5.6 1.4-1.4-5.6-5.6z\" fill=\"currentColor\"/>",
  "wf-hours": "<circle cx=\"12\" cy=\"12\" r=\"10\" fill=\"currentColor\"/><path d=\"M11 6h2v5.5l3.5 2-1 1.7-4.5-2.7V6z\" fill=\"#fff\"/>",
  "wf-timetable": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"17\" rx=\"3\" fill=\"currentColor\"/><rect x=\"6\" y=\"2\" width=\"2\" height=\"4\" rx=\"0.5\" fill=\"currentColor\"/><rect x=\"16\" y=\"2\" width=\"2\" height=\"4\" rx=\"0.5\" fill=\"currentColor\"/><rect x=\"5\" y=\"8\" width=\"14\" height=\"2\" fill=\"#fff\"/><rect x=\"6\" y=\"12\" width=\"12\" height=\"1.8\" fill=\"#fff\"/><rect x=\"6\" y=\"16\" width=\"8\" height=\"1.8\" fill=\"#fff\"/>",
  "wf-events": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"17\" rx=\"3\" fill=\"currentColor\"/><rect x=\"6\" y=\"2\" width=\"2\" height=\"4\" rx=\"0.5\" fill=\"currentColor\"/><rect x=\"16\" y=\"2\" width=\"2\" height=\"4\" rx=\"0.5\" fill=\"currentColor\"/><rect x=\"5\" y=\"8\" width=\"14\" height=\"2\" fill=\"#fff\"/><polygon points=\"12 11 13.2 13.5 16 13.9 14 15.8 14.5 18.5 12 17.2 9.5 18.5 10 15.8 8 13.9 10.8 13.5\" fill=\"#fff\"/>",
  "wf-news": "<rect x=\"2\" y=\"3\" width=\"20\" height=\"18\" rx=\"2\" fill=\"currentColor\"/><rect x=\"5\" y=\"6\" width=\"7\" height=\"2\" fill=\"#fff\"/><rect x=\"5\" y=\"10\" width=\"14\" height=\"1.8\" fill=\"#fff\"/><rect x=\"5\" y=\"13.5\" width=\"14\" height=\"1.8\" fill=\"#fff\"/><rect x=\"5\" y=\"17\" width=\"9\" height=\"1.8\" fill=\"#fff\"/>",
  "wf-announce": "<path d=\"M18 4l-9 4H4a1 1 0 0 0-1 1v6a1 1 0 0 0 1 1h5l9 4V4zm-9 15v3a2 2 0 0 1-2 2H5v-2h2a1 1 0 0 0 1-1v-2h1zm11.5-8.5a4 4 0 0 1 0 5v2a6 6 0 0 0 0-9v2z\" fill=\"currentColor\"/>",
  "wf-share": "<path d=\"M18 16a3 3 0 0 0-2.4 1.2L8.9 13.7a3.3 3.3 0 0 0 0-3.4l6.7-3.5A3 3 0 1 0 15 5a3 3 0 0 0 .1.7L8.4 9.2a3 3 0 1 0 0 5.6l6.7 3.5c0 .2-.1.5-.1.7a3 3 0 1 0 3-3z\" fill=\"currentColor\"/>",
  "wf-chat": "<path d=\"M20 2H4a2 2 0 0 0-2 2v18l4-4h14a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2z\" fill=\"currentColor\"/><circle cx=\"7\" cy=\"10\" r=\"1.5\" fill=\"#fff\"/><circle cx=\"12\" cy=\"10\" r=\"1.5\" fill=\"#fff\"/><circle cx=\"17\" cy=\"10\" r=\"1.5\" fill=\"#fff\"/>",
  "wf-like": "<path d=\"M1 21h4V9H1v12zm22-11a2 2 0 0 0-2-2h-6.3l1-4.6v-.3a1.5 1.5 0 0 0-.4-1.1L14.2 1 7.6 7.6A2 2 0 0 0 7 9v10a2 2 0 0 0 2 2h9c.8 0 1.5-.5 1.8-1.2l3-7.1c.1-.2.2-.5.2-.7v-2z\" fill=\"currentColor\"/>",
  "wf-camera": "<path d=\"M20 4h-3.2L15 2H9L7.2 4H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm-8 14a5 5 0 1 1 0-10 5 5 0 0 1 0 10zm0-8a3 3 0 1 0 0 6 3 3 0 0 0 0-6z\" fill=\"currentColor\"/>",
  "wf-video": "<rect x=\"2\" y=\"5\" width=\"14\" height=\"14\" rx=\"3\" fill=\"currentColor\"/><polygon points=\"18 8 23 4 23 20 18 16\" fill=\"currentColor\"/>",
  "wf-qr": "<rect x=\"2\" y=\"2\" width=\"8\" height=\"8\" rx=\"1.5\" fill=\"currentColor\"/><rect x=\"4\" y=\"4\" width=\"4\" height=\"4\" fill=\"#fff\"/><rect x=\"5\" y=\"5\" width=\"2\" height=\"2\" fill=\"currentColor\"/><rect x=\"14\" y=\"2\" width=\"8\" height=\"8\" rx=\"1.5\" fill=\"currentColor\"/><rect x=\"16\" y=\"4\" width=\"4\" height=\"4\" fill=\"#fff\"/><rect x=\"17\" y=\"5\" width=\"2\" height=\"2\" fill=\"currentColor\"/><rect x=\"2\" y=\"14\" width=\"8\" height=\"8\" rx=\"1.5\" fill=\"currentColor\"/><rect x=\"4\" y=\"16\" width=\"4\" height=\"4\" fill=\"#fff\"/><rect x=\"5\" y=\"17\" width=\"2\" height=\"2\" fill=\"currentColor\"/><rect x=\"14\" y=\"14\" width=\"3\" height=\"3\" fill=\"currentColor\"/><rect x=\"19\" y=\"14\" width=\"3\" height=\"3\" fill=\"currentColor\"/><rect x=\"14\" y=\"19\" width=\"8\" height=\"3\" fill=\"currentColor\"/>",
  "wf-email": "<path d=\"M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z\" fill=\"currentColor\"/>",
  "wf-web": "<circle cx=\"12\" cy=\"12\" r=\"10\" fill=\"currentColor\"/><path d=\"M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z\" fill=\"#fff\"/><path d=\"M12 4a14 14 0 0 1 2 8 14 14 0 0 1-2 8 14 14 0 0 1-2-8 14 14 0 0 1 2-8z\" fill=\"currentColor\"/><line x1=\"2\" y1=\"12\" x2=\"22\" y2=\"12\" stroke=\"#fff\" stroke-width=\"1.8\"/>"
};
export const WAYFINDING_METADATA = [
  {
    "id": "wf-arrow-up",
    "name": "Ahead",
    "category": "Navigation",
    "keywords": [
      "ahead",
      "forward",
      "straight",
      "north",
      "up",
      "arrow",
      "direction"
    ],
    "paths_line": "<path d=\"M12 19V5\"/><path d=\"m5 12 7-7 7 7\"/>",
    "paths_solid": "<path d=\"M12 2.5l7 7h-4.5v12h-5v-12H5z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-arrow-right",
    "name": "Right",
    "category": "Navigation",
    "keywords": [
      "right",
      "east",
      "turn right",
      "arrow",
      "direction"
    ],
    "paths_line": "<path d=\"M5 12h14\"/><path d=\"m12 5 7 7-7 7\"/>",
    "paths_solid": "<path d=\"M21.5 12l-7-7v4.5H2.5v5h12v4.5z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-arrow-down",
    "name": "Down / behind",
    "category": "Navigation",
    "keywords": [
      "down",
      "behind",
      "reverse",
      "south",
      "backwards",
      "arrow",
      "direction"
    ],
    "paths_line": "<path d=\"M12 5v14\"/><path d=\"m19 12-7 7-7-7\"/>",
    "paths_solid": "<path d=\"M12 21.5l-7-7h4.5V2.5h5v12H19z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-arrow-left",
    "name": "Left",
    "category": "Navigation",
    "keywords": [
      "left",
      "west",
      "turn left",
      "arrow",
      "direction"
    ],
    "paths_line": "<path d=\"M19 12H5\"/><path d=\"m12 19-7-7 7-7\"/>",
    "paths_solid": "<path d=\"M2.5 12l7 7v-4.5h12v-5h-12V5z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-arrow-up-right",
    "name": "Ahead right",
    "category": "Navigation",
    "keywords": [
      "ahead right",
      "diagonal right",
      "bear right",
      "northeast",
      "arrow"
    ],
    "paths_line": "<path d=\"M7 17 17 7\"/><path d=\"M8 7h9v9\"/>",
    "paths_solid": "<path d=\"M7 3.5h13.5V17l-4.2-4.2-9 9-2.8-2.8 9-9z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-arrow-up-left",
    "name": "Ahead left",
    "category": "Navigation",
    "keywords": [
      "ahead left",
      "diagonal left",
      "bear left",
      "northwest",
      "arrow"
    ],
    "paths_line": "<path d=\"m17 17-10-10\"/><path d=\"M16 7H7v9\"/>",
    "paths_solid": "<path d=\"M17 3.5H3.5V17l4.2-4.2 9 9 2.8-2.8-9-9z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-u-turn",
    "name": "Turn around",
    "category": "Navigation",
    "keywords": [
      "turn around",
      "u-turn",
      "reverse",
      "loop",
      "opposite direction"
    ],
    "paths_line": "<path d=\"M9 10v7\"/><path d=\"m5 13 4 4 4-4\"/><path d=\"M9 10a5 5 0 0 1 10 0v8\"/>",
    "paths_solid": "<path d=\"M9 18l-5-5h3.5A7.5 7.5 0 0 1 15 5.5a7.5 7.5 0 0 1 7.5 7.5v6h-4v-6a3.5 3.5 0 0 0-3.5-3.5A3.5 3.5 0 0 0 11.5 13H15z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-signpost",
    "name": "Directions",
    "category": "Navigation",
    "keywords": [
      "directions",
      "signpost",
      "guide",
      "guidepost",
      "which way",
      "directory"
    ],
    "paths_line": "<path d=\"M12 3v18\"/><path d=\"M12 5H5a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h7l2-2.5L12 5z\"/><path d=\"M12 12h7a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-7l-2-2.5 2-2.5z\"/>",
    "paths_solid": "<path d=\"M10.5 2h3v2h5.5l2 2.5-2 2.5H13.5v2H19a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1h-5.5v5h-3v-5H5a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1h5.5V9H5L3 6.5 5 4h5.5z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-pin",
    "name": "You are here",
    "category": "Navigation",
    "keywords": [
      "you are here",
      "location",
      "marker",
      "pin",
      "current position",
      "destination"
    ],
    "paths_line": "<path d=\"M12 21s-6-5.686-6-10a6 6 0 0 1 12 0c0 4.314-6 10-6 10z\"/><circle cx=\"12\" cy=\"11\" r=\"2.5\"/>",
    "paths_solid": "<path d=\"M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-facing",
    "name": "Facing this way",
    "category": "Navigation",
    "keywords": [
      "facing this way",
      "orientation",
      "bearing",
      "heading",
      "compass",
      "view angle"
    ],
    "paths_line": "<circle cx=\"12\" cy=\"12\" r=\"9\"/><polygon points=\"12 4 15 12 12 10 9 12 12 4\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"17\" r=\"1\" fill=\"currentColor\"/>",
    "paths_solid": "<circle cx=\"12\" cy=\"12\" r=\"10\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.5\"/><polygon points=\"12 4 16 13 12 11 8 13 12 4\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"17\" r=\"1.5\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-map",
    "name": "Map",
    "category": "Navigation",
    "keywords": [
      "map",
      "floor plan",
      "overview",
      "layout",
      "directory",
      "concourse"
    ],
    "paths_line": "<polygon points=\"3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21\"/><line x1=\"9\" y1=\"3\" x2=\"9\" y2=\"18\"/><line x1=\"15\" y1=\"6\" x2=\"15\" y2=\"21\"/>",
    "paths_solid": "<path d=\"M3 6.2l5.7-2.3 6.6 2.6L21 4.2v13.6l-5.7 2.3-6.6-2.6L3 19.8V6.2zm7.2.3v10.9l3.6 1.4V7.9l-3.6-1.4z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-touch",
    "name": "Touch here",
    "category": "Navigation",
    "keywords": [
      "touch here",
      "tap",
      "finger",
      "interact",
      "touchscreen",
      "press",
      "kiosk"
    ],
    "paths_line": "<path d=\"M12 11V6a1.5 1.5 0 0 1 3 0v5\"/><path d=\"M15 9.5a1.5 1.5 0 0 1 3 0V12a1.5 1.5 0 0 1 3 0v3a6 6 0 0 1-6 6h-2a6 6 0 0 1-4.24-1.76L5 15.4a1.5 1.5 0 0 1 2.2-2L9.5 15V6a1.5 1.5 0 0 1 3 0v5\"/><path d=\"M12 3a9 9 0 0 1 9 9\"/><path d=\"M12 6a6 6 0 0 1 6 6\"/>",
    "paths_solid": "<path d=\"M11 1.5a1.5 1.5 0 0 1 3 0V9.2a3 3 0 0 1 3.5 3v3.5a5.5 5.5 0 0 1-5.5 5.5H10a5.5 5.5 0 0 1-3.9-1.6l-3.5-3.5 1.5-1.5 2.9 1.7V1.5z\" fill=\"currentColor\"/><path d=\"M12.5 0a7 7 0 0 1 7 7h-2a5 5 0 0 0-5-5V0z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-entrance",
    "name": "Entrance",
    "category": "Building",
    "keywords": [
      "entrance",
      "enter",
      "entry",
      "door",
      "ingress",
      "main entrance",
      "doorway"
    ],
    "paths_line": "<path d=\"M14 20V4a1 1 0 0 1 1-1h5a1 1 0 0 1 1 1v16\"/><path d=\"m14 4-7 2.5v12l7 1.5\"/><circle cx=\"10\" cy=\"12\" r=\"0.75\" fill=\"currentColor\"/><line x1=\"2\" y1=\"20\" x2=\"22\" y2=\"20\"/><path d=\"M2 11h8\"/><path d=\"m7 7.5 3.5 3.5-3.5 3.5\"/>",
    "paths_solid": "<path d=\"M13 2h8a1 1 0 0 1 1 1v17a1 1 0 0 1-1 1h-8v-2h6V4h-6V2z\" fill=\"currentColor\"/><path d=\"m13 3-8 3v12l8 3V3z\" fill=\"currentColor\"/><circle cx=\"8\" cy=\"12\" r=\"1\" fill=\"#fff\"/><path d=\"M1 11h7v-3l4 4-4 4v-3H1z\" fill=\"currentColor\"/><rect x=\"1\" y=\"21\" width=\"22\" height=\"2\" rx=\"0.5\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-exit",
    "name": "Exit",
    "category": "Building",
    "keywords": [
      "exit",
      "egress",
      "way out",
      "door",
      "leave",
      "outdoor"
    ],
    "paths_line": "<path d=\"M10 20V4a1 1 0 0 0-1-1H4a1 1 0 0 0-1 1v16\"/><path d=\"m10 4 7 2.5v12l-7 1.5\"/><circle cx=\"14\" cy=\"12\" r=\"0.75\" fill=\"currentColor\"/><line x1=\"2\" y1=\"20\" x2=\"22\" y2=\"20\"/><path d=\"M14 11h8\"/><path d=\"m18.5 7.5 3.5 3.5-3.5 3.5\"/>",
    "paths_solid": "<path d=\"M11 2H3a1 1 0 0 0-1 1v17a1 1 0 0 0 1 1h8v-2H5V4h6V2z\" fill=\"currentColor\"/><path d=\"m11 3 8 3v12l-8 3V3z\" fill=\"currentColor\"/><circle cx=\"16\" cy=\"12\" r=\"1\" fill=\"#fff\"/><path d=\"M15 11h4v-3l4 4-4 4v-3h-4z\" fill=\"currentColor\"/><rect x=\"1\" y=\"21\" width=\"22\" height=\"2\" rx=\"0.5\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-lift",
    "name": "Lift",
    "category": "Building",
    "keywords": [
      "lift",
      "elevator",
      "floors",
      "vertical",
      "accessible lift"
    ],
    "paths_line": "<rect x=\"3\" y=\"3\" width=\"12\" height=\"18\" rx=\"2\"/><circle cx=\"6.5\" cy=\"8\" r=\"1.4\"/><path d=\"M4.5 16.5v-2a1.8 1.8 0 0 1 3.6 0v2\"/><circle cx=\"11.5\" cy=\"8\" r=\"1.4\"/><path d=\"M9.7 16.5v-2a1.8 1.8 0 0 1 3.6 0v2\"/><polygon points=\"18.5 4.5 15.5 8.5 21.5 8.5\" fill=\"currentColor\"/><polygon points=\"18.5 19.5 15.5 15.5 21.5 15.5\" fill=\"currentColor\"/><line x1=\"18.5\" y1=\"11\" x2=\"18.5\" y2=\"13\"/>",
    "paths_solid": "<rect x=\"2\" y=\"2\" width=\"13\" height=\"20\" rx=\"3\" fill=\"currentColor\"/><circle cx=\"6\" cy=\"7.5\" r=\"1.5\" fill=\"#fff\"/><path d=\"M4 16v-3a2 2 0 0 1 4 0v3H4z\" fill=\"#fff\"/><circle cx=\"11\" cy=\"7.5\" r=\"1.5\" fill=\"#fff\"/><path d=\"M9 16v-3a2 2 0 0 1 4 0v3H9z\" fill=\"#fff\"/><polygon points=\"19.5 4 16 8.5 23 8.5\" fill=\"currentColor\"/><polygon points=\"19.5 20 16 15.5 23 15.5\" fill=\"currentColor\"/><rect x=\"18.5\" y=\"10.5\" width=\"2\" height=\"3\" rx=\"0.5\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-stairs",
    "name": "Stairs",
    "category": "Building",
    "keywords": [
      "stairs",
      "staircase",
      "steps",
      "walk up",
      "stairwell"
    ],
    "paths_line": "<path d=\"M4 19h4v-4h4v-4h4V7h4\"/><circle cx=\"7\" cy=\"6\" r=\"2\"/><path d=\"m11 11-2-2.5-3 1.5\"/>",
    "paths_solid": "<polygon points=\"4 20 20 20 20 6 16 6 16 10 12 10 12 14 8 14 8 18 4 18 4 20\" fill=\"currentColor\"/><circle cx=\"8\" cy=\"5\" r=\"2\" fill=\"currentColor\"/><path d=\"m11.5 10-2-2.5-2.5 1.5 1 2 2-1z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-escalator-up",
    "name": "Escalator up",
    "category": "Building",
    "keywords": [
      "escalator up",
      "moving stairs",
      "up",
      "level up",
      "transit"
    ],
    "paths_line": "<path d=\"M3 7h4l7 10h7\"/><path d=\"m5 17 4-4\"/><path d=\"M5 13h4v4\"/><circle cx=\"6\" cy=\"4\" r=\"1.5\"/><path d=\"m8 9-2-2-3 2\"/>",
    "paths_solid": "<polygon points=\"3 8 8 8 15 18 21 18 21 20 14 20 7 10 3 10\" fill=\"currentColor\"/><polygon points=\"6 14 6 17 9 17 9 14\" fill=\"currentColor\"/><path d=\"M3 17l4-4 1.4 1.4-2.6 2.6H9v2H3z\" fill=\"currentColor\"/><circle cx=\"7\" cy=\"4\" r=\"1.8\" fill=\"currentColor\"/><path d=\"m9 9.5-2-2.5-2 1.5.8 1.8 1.7-.8z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-escalator-down",
    "name": "Escalator down",
    "category": "Building",
    "keywords": [
      "escalator down",
      "moving stairs",
      "down",
      "level down",
      "transit"
    ],
    "paths_line": "<path d=\"M3 17h4l7-10h7\"/><path d=\"m19 17-4-4\"/><path d=\"M15 17h4v-4\"/><circle cx=\"18\" cy=\"4\" r=\"1.5\"/><path d=\"m16 9 2-2 3 2\"/>",
    "paths_solid": "<polygon points=\"3 18 8 18 15 8 21 8 21 6 14 6 7 16 3 16\" fill=\"currentColor\"/><path d=\"M19 14l-4 4-1.4-1.4 2.6-2.6H13v-2h6z\" fill=\"currentColor\"/><circle cx=\"17\" cy=\"4\" r=\"1.8\" fill=\"currentColor\"/><path d=\"m15 9.5 2-2.5 2 1.5-.8 1.8-1.7-.8z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-ramp",
    "name": "Ramp",
    "category": "Building",
    "keywords": [
      "ramp",
      "incline",
      "slope",
      "accessible route",
      "step free"
    ],
    "paths_line": "<polygon points=\"3 19 21 19 21 11 3 19\"/><circle cx=\"14\" cy=\"7\" r=\"1.5\"/><path d=\"M12 14a2.5 2.5 0 0 1 3-2.4l1.5-1.6\"/>",
    "paths_solid": "<polygon points=\"2 20 22 20 22 10 2 20\" fill=\"currentColor\"/><circle cx=\"14\" cy=\"5.5\" r=\"1.8\" fill=\"currentColor\"/><path d=\"M11.5 13a2.8 2.8 0 1 1 3.5-3.3l1.8-1.8 1.4 1.4-2.4 2.4-1.5-.5a1.5 1.5 0 0 0-1.8 1.8z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-accessible",
    "name": "Accessible",
    "category": "Building",
    "keywords": [
      "accessible",
      "wheelchair",
      "disabled",
      "disability",
      "step free",
      "accessibility"
    ],
    "paths_line": "<circle cx=\"12\" cy=\"4.5\" r=\"2\"/><path d=\"M10 9h3.5l1.5 5h3\"/><path d=\"M13.5 14A4 4 0 1 1 8 11.5\"/><path d=\"M8 12h3\"/>",
    "paths_solid": "<circle cx=\"12\" cy=\"4\" r=\"2\" fill=\"currentColor\"/><path d=\"M10 8h4.5l1.6 5.5h2.9v2h-4.2l-1.3-4.5H11v3.5a4.5 4.5 0 1 1-5-4.4V8h4zm-1.5 6a2.5 2.5 0 1 0 2.5 2.5V14H8.5z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-levels",
    "name": "Levels",
    "category": "Building",
    "keywords": [
      "levels",
      "floors",
      "stories",
      "multi-level",
      "stack",
      "building layout"
    ],
    "paths_line": "<polygon points=\"12 3 21 7.5 12 12 3 7.5 12 3\"/><polyline points=\"3 12 12 16.5 21 12\"/><polyline points=\"3 16.5 12 21 21 16.5\"/>",
    "paths_solid": "<polygon points=\"12 2 21 6.5 12 11 3 6.5\" fill=\"currentColor\"/><polygon points=\"12 7.5 21 12 12 16.5 3 12\" fill=\"currentColor\"/><polygon points=\"12 13 21 17.5 12 22 3 17.5\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-no-entry",
    "name": "No entry",
    "category": "Building",
    "keywords": [
      "no entry",
      "do not enter",
      "restricted",
      "stop",
      "forbidden",
      "closed"
    ],
    "paths_line": "<circle cx=\"12\" cy=\"12\" r=\"9\"/><line x1=\"6\" y1=\"12\" x2=\"18\" y2=\"12\" stroke-width=\"3\"/>",
    "paths_solid": "<path d=\"M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm6 11.5H6v-3h12v3z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-prohibited",
    "name": "Not permitted",
    "category": "Building",
    "keywords": [
      "not permitted",
      "prohibited",
      "banned",
      "forbidden",
      "slash",
      "restriction"
    ],
    "paths_line": "<circle cx=\"12\" cy=\"12\" r=\"9\"/><line x1=\"5.6\" y1=\"5.6\" x2=\"18.4\" y2=\"18.4\"/>",
    "paths_solid": "<path d=\"M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 2a7.95 7.95 0 0 1 5.36 2.06L6.06 17.36A8 8 0 0 1 12 4zm0 16a7.95 7.95 0 0 1-5.36-2.06L17.94 6.64A8 8 0 0 1 12 20z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-staff-only",
    "name": "Staff only",
    "category": "Building",
    "keywords": [
      "staff only",
      "employees",
      "authorized personnel",
      "restricted access",
      "badge",
      "id"
    ],
    "paths_line": "<rect x=\"5\" y=\"8\" width=\"14\" height=\"13\" rx=\"2\"/><circle cx=\"12\" cy=\"13\" r=\"2.5\"/><path d=\"M9 19c0-1.7 1.3-3 3-3s3 1.3 3 3\"/><path d=\"M9 8V5a3 3 0 0 1 6 0v3\"/>",
    "paths_solid": "<rect x=\"4\" y=\"7\" width=\"16\" height=\"15\" rx=\"3\" fill=\"currentColor\"/><path d=\"M9 7V4a3 3 0 0 1 6 0v3h-2V4a1 1 0 0 0-2 0v3H9z\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"12\" r=\"2\" fill=\"#fff\"/><path d=\"M9 19c0-1.7 1.3-3 3-3s3 1.3 3 3H9z\" fill=\"#fff\"/>"
  },
  {
    "id": "wf-toilets",
    "name": "Toilets",
    "category": "Amenities",
    "keywords": [
      "toilets",
      "restroom",
      "wc",
      "washroom",
      "bathroom",
      "amenities"
    ],
    "paths_line": "<line x1=\"12\" y1=\"4\" x2=\"12\" y2=\"20\"/><circle cx=\"7\" cy=\"5\" r=\"1.5\"/><path d=\"M5 9h4v6H8v5H6v-5H5V9z\"/><circle cx=\"17\" cy=\"5\" r=\"1.5\"/><path d=\"M15 15l-1-6h6l-1 6h-4z\"/><path d=\"M16 15v5h2v-5\"/>",
    "paths_solid": "<circle cx=\"7\" cy=\"4\" r=\"1.8\" fill=\"currentColor\"/><path d=\"M4.5 8h5a1 1 0 0 1 1 1v6h-2v5H6.5v-5h-2V9a1 1 0 0 1 1-1z\" fill=\"currentColor\"/><circle cx=\"17\" cy=\"4\" r=\"1.8\" fill=\"currentColor\"/><path d=\"M14.5 8h5l2.2 7h-3.2v5h-2v-5h-3.2l2.2-7z\" fill=\"currentColor\"/><line x1=\"12\" y1=\"3\" x2=\"12\" y2=\"21\" stroke=\"currentColor\" stroke-width=\"1.5\"/>"
  },
  {
    "id": "wf-toilet-male",
    "name": "Male toilet",
    "category": "Amenities",
    "keywords": [
      "male toilet",
      "men",
      "gents",
      "male restroom",
      "man"
    ],
    "paths_line": "<circle cx=\"12\" cy=\"4\" r=\"2\"/><path d=\"M9 8h6a1 1 0 0 1 1 1v6h-2v6h-4v-6H8V9a1 1 0 0 1 1-1z\"/>",
    "paths_solid": "<circle cx=\"12\" cy=\"4\" r=\"2.2\" fill=\"currentColor\"/><path d=\"M8.5 8.5h7a1.5 1.5 0 0 1 1.5 1.5V16h-2.5v5.5h-5V16H7v-6a1.5 1.5 0 0 1 1.5-1.5z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-toilet-female",
    "name": "Female toilet",
    "category": "Amenities",
    "keywords": [
      "female toilet",
      "women",
      "ladies",
      "female restroom",
      "woman"
    ],
    "paths_line": "<circle cx=\"12\" cy=\"4\" r=\"2\"/><path d=\"M9.5 8h5l2.5 8h-4v5h-2v-5H7l2.5-8z\"/>",
    "paths_solid": "<circle cx=\"12\" cy=\"4\" r=\"2.2\" fill=\"currentColor\"/><path d=\"M9 8.5h6l3 8.5h-4.5v4.5h-3V17H6l3-8.5z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-toilet-accessible",
    "name": "Accessible toilet",
    "category": "Amenities",
    "keywords": [
      "accessible toilet",
      "wheelchair toilet",
      "disabled wc",
      "accessible bathroom"
    ],
    "paths_line": "<circle cx=\"10\" cy=\"5\" r=\"1.8\"/><path d=\"M8 9h3l1.5 4h2.5\"/><path d=\"M11 13a3.5 3.5 0 1 1-5-2\"/><path d=\"M17 9h4v11h-4\"/><path d=\"M19 12v3\"/>",
    "paths_solid": "<circle cx=\"9\" cy=\"4.5\" r=\"1.8\" fill=\"currentColor\"/><path d=\"M7 8h4.5l1.6 5h2.9v1.8h-4.2l-1.3-4H8.5v3a4 4 0 1 1-4.5-3.9V8H7z\" fill=\"currentColor\"/><rect x=\"17\" y=\"5\" width=\"4\" height=\"15\" rx=\"1\" fill=\"currentColor\"/><rect x=\"15\" y=\"14\" width=\"4\" height=\"2\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-baby-change",
    "name": "Baby change",
    "category": "Amenities",
    "keywords": [
      "baby change",
      "parents room",
      "nappy change",
      "infant care",
      "baby care"
    ],
    "paths_line": "<line x1=\"3\" y1=\"18\" x2=\"21\" y2=\"18\"/><circle cx=\"7\" cy=\"9\" r=\"2.5\"/><path d=\"M10 13c1.5 0 3-1 4-2 1.5 1.5 3.5 1.5 5 1\"/><path d=\"M12 4v4\"/><path d=\"m10 6 4 0\"/>",
    "paths_solid": "<rect x=\"2\" y=\"17\" width=\"20\" height=\"2.5\" rx=\"1\" fill=\"currentColor\"/><circle cx=\"6.5\" cy=\"8.5\" r=\"2.2\" fill=\"currentColor\"/><path d=\"M9.5 13a4 4 0 0 0 4-2.5 3.5 3.5 0 0 1 5 1.5v3H9.5z\" fill=\"currentColor\"/><path d=\"M12 4v4m-2-2h4\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"/>"
  },
  {
    "id": "wf-cafe",
    "name": "Caf\u00e9",
    "category": "Amenities",
    "keywords": [
      "cafe",
      "coffee",
      "tea",
      "espresso",
      "beverage",
      "drinks",
      "cafeteria"
    ],
    "paths_line": "<path d=\"M18 8h1a4 4 0 0 1 0 8h-1\"/><path d=\"M2 8h16v7a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z\"/><line x1=\"6\" y1=\"2\" x2=\"6\" y2=\"5\"/><line x1=\"10\" y1=\"2\" x2=\"10\" y2=\"5\"/><line x1=\"14\" y1=\"2\" x2=\"14\" y2=\"5\"/>",
    "paths_solid": "<path d=\"M18 7h1a4 4 0 0 1 0 8h-1v-8zm2 6a2 2 0 0 0 0-4v4z\" fill=\"currentColor\"/><path d=\"M2 7h15v7a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V7zm0 12h17a1 1 0 0 1 0 2H2a1 1 0 0 1 0-2z\" fill=\"currentColor\"/><path d=\"M5 2v3m4-3v3m4-3v3\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\"/>"
  },
  {
    "id": "wf-food",
    "name": "Food",
    "category": "Amenities",
    "keywords": [
      "food",
      "dining",
      "restaurant",
      "food court",
      "cutlery",
      "eat",
      "meal"
    ],
    "paths_line": "<path d=\"M18 2v20\"/><path d=\"M21 2c0 4-3 5-3 8\"/><path d=\"M3 2v6c0 1.7 1.3 3 3 3v11\"/><path d=\"M6 2v6\"/><path d=\"M9 2v6c0 1.7-1.3 3-3 3\"/>",
    "paths_solid": "<path d=\"M18 2v20h2V2h-2zm-12 0v7a2 2 0 0 1-2 2v11h2V11a2 2 0 0 1-2-2V2h2zm4 0v7a2 2 0 0 1-2 2v11h2V11a2 2 0 0 0 2-2V2h-2z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-retail",
    "name": "Retail",
    "category": "Amenities",
    "keywords": [
      "retail",
      "shopping",
      "store",
      "shop",
      "boutique",
      "mall",
      "bag"
    ],
    "paths_line": "<path d=\"M6 8V6a6 6 0 0 1 12 0v2\"/><rect x=\"4\" y=\"8\" width=\"16\" height=\"13\" rx=\"2\"/><circle cx=\"9\" cy=\"13\" r=\"1\" fill=\"currentColor\"/><circle cx=\"15\" cy=\"13\" r=\"1\" fill=\"currentColor\"/>",
    "paths_solid": "<path d=\"M6 7V5a6 6 0 0 1 12 0v2h3a1 1 0 0 1 1 1l-1.5 13A2 2 0 0 1 18.5 22H5.5a2 2 0 0 1-2-1.8L2 8a1 1 0 0 1 1-1h3zm2 0h8V5a4 4 0 0 0-8 0v2z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-atm",
    "name": "ATM",
    "category": "Amenities",
    "keywords": [
      "atm",
      "cash machine",
      "cashpoint",
      "money",
      "withdraw",
      "bank"
    ],
    "paths_line": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"16\" rx=\"2\"/><line x1=\"7\" y1=\"9\" x2=\"17\" y2=\"9\"/><line x1=\"7\" y1=\"13\" x2=\"12\" y2=\"13\"/><rect x=\"14\" y=\"12\" width=\"3\" height=\"4\" rx=\"0.5\"/>",
    "paths_solid": "<rect x=\"3\" y=\"3\" width=\"18\" height=\"18\" rx=\"3\" fill=\"currentColor\"/><rect x=\"6\" y=\"6\" width=\"12\" height=\"3\" rx=\"0.5\" fill=\"#fff\"/><rect x=\"6\" y=\"11\" width=\"6\" height=\"2\" fill=\"#fff\"/><rect x=\"14\" y=\"11\" width=\"4\" height=\"6\" rx=\"1\" fill=\"#fff\"/>"
  },
  {
    "id": "wf-payment",
    "name": "Cashier / pay",
    "category": "Amenities",
    "keywords": [
      "cashier",
      "pay",
      "payment",
      "card",
      "checkout",
      "credit card",
      "pos"
    ],
    "paths_line": "<rect x=\"2\" y=\"5\" width=\"20\" height=\"14\" rx=\"2\"/><line x1=\"2\" y1=\"10\" x2=\"22\" y2=\"10\"/><circle cx=\"7\" cy=\"15\" r=\"1.5\"/><circle cx=\"11\" cy=\"15\" r=\"1.5\"/>",
    "paths_solid": "<rect x=\"2\" y=\"4\" width=\"20\" height=\"16\" rx=\"3\" fill=\"currentColor\"/><rect x=\"2\" y=\"8\" width=\"20\" height=\"3.5\" fill=\"#fff\"/><circle cx=\"7\" cy=\"15.5\" r=\"1.8\" fill=\"#fff\"/><circle cx=\"11.5\" cy=\"15.5\" r=\"1.8\" fill=\"#fff\"/>"
  },
  {
    "id": "wf-pharmacy",
    "name": "Pharmacy",
    "category": "Amenities",
    "keywords": [
      "pharmacy",
      "chemist",
      "dispensary",
      "prescription",
      "medicine",
      "drugs"
    ],
    "paths_line": "<path d=\"M12 3v18\"/><path d=\"M3 12h18\"/><circle cx=\"12\" cy=\"12\" r=\"9\"/>",
    "paths_solid": "<rect x=\"2\" y=\"2\" width=\"20\" height=\"20\" rx=\"4\" fill=\"currentColor\"/><path d=\"M10 6h4v4h4v4h-4v4h-4v-4H6v-4h4V6z\" fill=\"#fff\"/>"
  },
  {
    "id": "wf-water",
    "name": "Drinking water",
    "category": "Amenities",
    "keywords": [
      "drinking water",
      "water fountain",
      "refill",
      "hydration",
      "tap",
      "bottle refill"
    ],
    "paths_line": "<path d=\"M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z\"/><path d=\"M12 18a4 4 0 0 0 4-4\"/>",
    "paths_solid": "<path d=\"M12 2.5C12 2.5 5 10.5 5 15.5a7 7 0 0 0 14 0c0-5-7-13-7-13zm0 16a4.5 4.5 0 0 1-4.5-4.5c0-.6.4-1 1-1s1 .4 1 1A2.5 2.5 0 0 0 12 16.5c.6 0 1 .4 1 1s-.4 1-1 1z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-wifi",
    "name": "Free Wi-Fi",
    "category": "Amenities",
    "keywords": [
      "wifi",
      "free wifi",
      "internet",
      "wireless",
      "network",
      "hotspot"
    ],
    "paths_line": "<path d=\"M5 12.55a11 11 0 0 1 14.08 0\"/><path d=\"M1.42 9a16 16 0 0 1 21.16 0\"/><path d=\"M8.53 16.11a6 6 0 0 1 6.95 0\"/><circle cx=\"12\" cy=\"19.5\" r=\"1.2\" fill=\"currentColor\"/>",
    "paths_solid": "<path d=\"M12 4a14.8 14.8 0 0 1 9.9 3.9l-2.1 2.1A11.8 11.8 0 0 0 12 7c-3 0-5.8 1.1-7.8 3L2.1 7.9A14.8 14.8 0 0 1 12 4zm0 6a8.8 8.8 0 0 1 5.8 2.2l-2.1 2.1A5.8 5.8 0 0 0 12 13c-1.4 0-2.8.5-3.7 1.3L6.2 12.2A8.8 8.8 0 0 1 12 10zm0 6a3 3 0 0 1 2 1l-2 2-2-2a3 3 0 0 1 2-1z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-seating",
    "name": "Waiting area",
    "category": "Amenities",
    "keywords": [
      "waiting area",
      "seating",
      "lounge",
      "rest",
      "chairs",
      "waiting room"
    ],
    "paths_line": "<path d=\"M5 11V6a3 3 0 0 1 6 0v5\"/><path d=\"M13 11V6a3 3 0 0 1 6 0v5\"/><rect x=\"3\" y=\"11\" width=\"18\" height=\"5\" rx=\"1.5\"/><path d=\"M5 16v5\"/><path d=\"M19 16v5\"/>",
    "paths_solid": "<path d=\"M4 5a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v9h-2V5H6v9H4V5zm-2 9h20a1 1 0 0 1 1 1v4a2 2 0 0 1-2 2h-1v-2H4v2H2a2 2 0 0 1-2-2v-4a1 1 0 0 1 1-1z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-parking",
    "name": "Car park",
    "category": "Transit",
    "keywords": [
      "car park",
      "parking",
      "garage",
      "p",
      "vehicle parking",
      "bays"
    ],
    "paths_line": "<rect x=\"3\" y=\"3\" width=\"18\" height=\"18\" rx=\"3\"/><path d=\"M9 17V7h4.5a3.5 3.5 0 0 1 0 7H9\"/>",
    "paths_solid": "<rect x=\"3\" y=\"3\" width=\"18\" height=\"18\" rx=\"4\" fill=\"currentColor\"/><path d=\"M9 17V7h4.5a3.5 3.5 0 0 1 0 7H11v3H9zm2-5h2.5a1.5 1.5 0 0 0 0-3H11v3z\" fill=\"#fff\"/>"
  },
  {
    "id": "wf-car",
    "name": "Drop-off",
    "category": "Transit",
    "keywords": [
      "drop-off",
      "pick-up",
      "car",
      "taxi",
      "passenger",
      "vehicle",
      "rideshare"
    ],
    "paths_line": "<path d=\"M4 17h16\"/><path d=\"M5 17l1.5-6h11l1.5 6\"/><circle cx=\"7.5\" cy=\"17\" r=\"2\"/><circle cx=\"16.5\" cy=\"17\" r=\"2\"/><path d=\"M7 11l1.5-4.5a1.5 1.5 0 0 1 1.4-1h4.2a1.5 1.5 0 0 1 1.4 1L17 11\"/>",
    "paths_solid": "<path d=\"M18.9 6.8A2 2 0 0 0 17.3 6H6.7a2 2 0 0 0-1.6.8L3 11v8a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-1h12v1a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-8l-2.1-4.2zM7.5 15a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm9 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zM6 10l1.3-3h9.4l1.3 3H6z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-bus",
    "name": "Bus / shuttle",
    "category": "Transit",
    "keywords": [
      "bus",
      "shuttle",
      "coach",
      "public transport",
      "transit",
      "stop"
    ],
    "paths_line": "<rect x=\"4\" y=\"3\" width=\"16\" height=\"15\" rx=\"3\"/><line x1=\"4\" y1=\"10\" x2=\"20\" y2=\"10\"/><circle cx=\"8\" cy=\"14\" r=\"1.5\"/><circle cx=\"16\" cy=\"14\" r=\"1.5\"/><path d=\"M6 18v3\"/><path d=\"M18 18v3\"/><line x1=\"9\" y1=\"6\" x2=\"15\" y2=\"6\"/>",
    "paths_solid": "<rect x=\"4\" y=\"3\" width=\"16\" height=\"16\" rx=\"3\" fill=\"currentColor\"/><rect x=\"6\" y=\"6\" width=\"12\" height=\"4.5\" rx=\"1\" fill=\"#fff\"/><circle cx=\"8\" cy=\"14\" r=\"1.5\" fill=\"#fff\"/><circle cx=\"16\" cy=\"14\" r=\"1.5\" fill=\"#fff\"/><rect x=\"5.5\" y=\"19\" width=\"3\" height=\"3\" rx=\"0.5\" fill=\"currentColor\"/><rect x=\"15.5\" y=\"19\" width=\"3\" height=\"3\" rx=\"0.5\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-ev",
    "name": "EV charging",
    "category": "Transit",
    "keywords": [
      "ev charging",
      "electric vehicle",
      "charger",
      "plug",
      "clean energy"
    ],
    "paths_line": "<rect x=\"3\" y=\"4\" width=\"12\" height=\"16\" rx=\"2\"/><path d=\"m8 9 2-3v4h2l-3 4v-3H7l2-2\"/><path d=\"M15 9h3a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2h-1\"/><circle cx=\"17\" cy=\"17\" r=\"1\"/>",
    "paths_solid": "<rect x=\"2\" y=\"4\" width=\"13\" height=\"17\" rx=\"3\" fill=\"currentColor\"/><path d=\"M8 8l-2 4h3l-1 4 4-5h-3l2-3H8z\" fill=\"#fff\"/><path d=\"M15 9h2a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2h-1v-2h1v-4h-2V9zm4 1v2h2v-2h-2z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-info",
    "name": "Information",
    "category": "Services",
    "keywords": [
      "information",
      "info",
      "help desk",
      "inquiries",
      "directory",
      "about"
    ],
    "paths_line": "<circle cx=\"12\" cy=\"12\" r=\"9\"/><circle cx=\"12\" cy=\"8\" r=\"1.2\" fill=\"currentColor\"/><path d=\"M11 12h2v5h-2z\"/>",
    "paths_solid": "<circle cx=\"12\" cy=\"12\" r=\"10\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"7.5\" r=\"1.5\" fill=\"#fff\"/><path d=\"M10.5 11h3v6h-3z\" fill=\"#fff\"/>"
  },
  {
    "id": "wf-help",
    "name": "Help",
    "category": "Services",
    "keywords": [
      "help",
      "assistance",
      "support",
      "question",
      "faq"
    ],
    "paths_line": "<circle cx=\"12\" cy=\"12\" r=\"9\"/><path d=\"M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3\"/><circle cx=\"12\" cy=\"17\" r=\"1\" fill=\"currentColor\"/>",
    "paths_solid": "<circle cx=\"12\" cy=\"12\" r=\"10\" fill=\"currentColor\"/><path d=\"M9.5 9a2.5 2.5 0 0 1 4.9.8c0 1.5-2.4 2-2.4 3.7h-2c0-2.3 2.5-2.8 2.5-3.7a.7.7 0 0 0-.7-.7.9.9 0 0 0-.9.9H9.5z\" fill=\"#fff\"/><circle cx=\"11\" cy=\"16.5\" r=\"1.2\" fill=\"#fff\"/>"
  },
  {
    "id": "wf-reception",
    "name": "Reception",
    "category": "Services",
    "keywords": [
      "reception",
      "front desk",
      "concierge",
      "check-in",
      "counter",
      "lobby"
    ],
    "paths_line": "<path d=\"M4 19h16\"/><path d=\"M4 15h16\"/><path d=\"M12 4v4\"/><path d=\"M8 8a4 4 0 0 1 8 0H8z\"/><path d=\"M10 15v-3h4v3\"/>",
    "paths_solid": "<rect x=\"2\" y=\"15\" width=\"20\" height=\"6\" rx=\"1.5\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"6\" r=\"2.5\" fill=\"currentColor\"/><path d=\"M7 15v-1a5 5 0 0 1 10 0v1H7z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-security",
    "name": "Security",
    "category": "Services",
    "keywords": [
      "security",
      "guard",
      "protection",
      "safe",
      "shield",
      "patrol"
    ],
    "paths_line": "<path d=\"M12 3s7 2.5 7 8c0 5.5-5 9.5-7 10-2-.5-7-4.5-7-10 0-5.5 7-8 7-8z\"/><path d=\"m9 12 2 2 4-4\"/>",
    "paths_solid": "<path d=\"M12 2s8 3 8 9c0 6.5-6 10.5-8 11-2-.5-8-4.5-8-11 0-6 8-9 8-9zm-1 13l5-5-1.4-1.4-3.6 3.6-1.6-1.6L8 12l3 3z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-phone",
    "name": "Phone",
    "category": "Services",
    "keywords": [
      "phone",
      "telephone",
      "call",
      "public phone",
      "contact"
    ],
    "paths_line": "<path d=\"M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z\"/>",
    "paths_solid": "<path d=\"M20 15.5c-1.2 0-2.4-.2-3.6-.6-.4-.1-.8 0-1.1.3l-2.2 2.2a15 15 0 0 1-6.6-6.6l2.2-2.2c.3-.3.4-.7.2-1.1-.4-1.1-.6-2.3-.6-3.5 0-.6-.4-1-1-1H4c-.6 0-1 .4-1 1 0 9.4 7.6 17 17 17 .6 0 1-.4 1-1v-3.5c0-.6-.4-1-1-1z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-intercom",
    "name": "Help point",
    "category": "Services",
    "keywords": [
      "help point",
      "intercom",
      "call button",
      "emergency intercom",
      "pillar",
      "speaker"
    ],
    "paths_line": "<rect x=\"6\" y=\"3\" width=\"12\" height=\"18\" rx=\"2\"/><circle cx=\"12\" cy=\"8\" r=\"2\"/><line x1=\"9\" y1=\"13\" x2=\"15\" y2=\"13\"/><circle cx=\"12\" cy=\"17\" r=\"1.5\" fill=\"currentColor\"/>",
    "paths_solid": "<rect x=\"5\" y=\"2\" width=\"14\" height=\"20\" rx=\"3\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"7.5\" r=\"2.5\" fill=\"#fff\"/><rect x=\"8\" y=\"12\" width=\"8\" height=\"1.8\" rx=\"0.5\" fill=\"#fff\"/><circle cx=\"12\" cy=\"17\" r=\"1.8\" fill=\"#fff\"/>"
  },
  {
    "id": "wf-hospital",
    "name": "Hospital",
    "category": "Healthcare",
    "keywords": [
      "hospital",
      "clinic",
      "medical center",
      "infirmary",
      "health",
      "ward"
    ],
    "paths_line": "<path d=\"M3 21h18\"/><path d=\"M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16\"/><path d=\"M12 7v6\"/><path d=\"M9 10h6\"/><rect x=\"9.5\" y=\"16\" width=\"5\" height=\"5\"/>",
    "paths_solid": "<rect x=\"3\" y=\"3\" width=\"18\" height=\"19\" rx=\"3\" fill=\"currentColor\"/><path d=\"M10 7h4v3h3v4h-3v3h-4v-3H7v-4h3V7z\" fill=\"#fff\"/>"
  },
  {
    "id": "wf-first-aid",
    "name": "First aid",
    "category": "Healthcare",
    "keywords": [
      "first aid",
      "emergency care",
      "medical kit",
      "cross",
      "treatment"
    ],
    "paths_line": "<rect x=\"3\" y=\"7\" width=\"18\" height=\"14\" rx=\"2\"/><path d=\"M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2\"/><path d=\"M12 11v6\"/><path d=\"M9 14h6\"/>",
    "paths_solid": "<rect x=\"2\" y=\"6\" width=\"20\" height=\"15\" rx=\"3\" fill=\"currentColor\"/><path d=\"M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2h-2V4h-4v2H8zm2 4h4v3h3v4h-3v3h-4v-3H7v-4h3v-3z\" fill=\"#fff\"/>"
  },
  {
    "id": "wf-consult",
    "name": "Consulting / GP",
    "category": "Healthcare",
    "keywords": [
      "consulting",
      "gp",
      "doctor",
      "physician",
      "clinic",
      "stethoscope",
      "appointment"
    ],
    "paths_line": "<path d=\"M6 3v5a6 6 0 0 0 12 0V3\"/><circle cx=\"6\" cy=\"3\" r=\"1\" fill=\"currentColor\"/><circle cx=\"18\" cy=\"3\" r=\"1\" fill=\"currentColor\"/><path d=\"M12 14v4a3 3 0 0 0 6 0v-2\"/><circle cx=\"18\" cy=\"16\" r=\"2\"/>",
    "paths_solid": "<path d=\"M6 3v6a6 6 0 0 0 12 0V3h-2v6a4 4 0 0 1-8 0V3H6zm6 12a3 3 0 0 0-3 3v2a3 3 0 0 0 6 0v-2a3 3 0 0 0-3-3zm6 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-pathology",
    "name": "Pathology",
    "category": "Healthcare",
    "keywords": [
      "pathology",
      "lab",
      "laboratory",
      "blood test",
      "specimen",
      "microscope"
    ],
    "paths_line": "<path d=\"M9 3h6\"/><path d=\"M10 3v5l-4.5 9A2 2 0 0 0 7.3 20h9.4a2 2 0 0 0 1.8-3L14 8V3\"/><line x1=\"7.5\" y1=\"15\" x2=\"16.5\" y2=\"15\"/>",
    "paths_solid": "<path d=\"M9 2h6v2h-1v5.5l5.2 9.4A2 2 0 0 1 17.5 22H6.5a2 2 0 0 1-1.7-3.1L10 9.5V4H9V2zm2 9.5l-4 7.2a.5.5 0 0 0 .4.8h9.2a.5.5 0 0 0 .4-.8l-4-7.2h-2z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-aed",
    "name": "Defibrillator",
    "category": "Healthcare",
    "keywords": [
      "defibrillator",
      "aed",
      "cardiac",
      "resuscitation",
      "heart",
      "shock",
      "emergency"
    ],
    "paths_line": "<path d=\"M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z\"/><polygon points=\"12.5 6 9.5 12 13 12 11.5 17 15.5 11 12 11 12.5 6\" fill=\"currentColor\"/>",
    "paths_solid": "<path d=\"M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z\" fill=\"currentColor\"/><polygon points=\"12.5 6 9.5 12 13 12 11.5 17 15.5 11 12 11 12.5 6\" fill=\"#fff\"/>"
  },
  {
    "id": "wf-student",
    "name": "Student hub",
    "category": "Campus",
    "keywords": [
      "student hub",
      "student services",
      "campus center",
      "union",
      "graduation cap",
      "alumni"
    ],
    "paths_line": "<polygon points=\"12 3 22 8.5 12 14 2 8.5 12 3\"/><path d=\"M6 10.7v5.3c0 2.2 2.7 4 6 4s6-1.8 6-4v-5.3\"/><path d=\"M22 8.5v6\"/>",
    "paths_solid": "<polygon points=\"12 2 22 7.5 12 13 2 7.5\" fill=\"currentColor\"/><path d=\"M6 10.5v5.5c0 2.2 2.7 4 6 4s6-1.8 6-4v-5.5l-6 3.3-6-3.3zm16-3v6h-2v-5l2-1z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-library",
    "name": "Library",
    "category": "Campus",
    "keywords": [
      "library",
      "books",
      "study",
      "reading",
      "learning",
      "quiet zone"
    ],
    "paths_line": "<path d=\"M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5z\"/><path d=\"M4 6h16\"/><line x1=\"8\" y1=\"10\" x2=\"16\" y2=\"10\"/><line x1=\"8\" y1=\"14\" x2=\"14\" y2=\"14\"/>",
    "paths_solid": "<path d=\"M4 3a2 2 0 0 1 2-2h13a1 1 0 0 1 1 1v20a1 1 0 0 1-1 1H6a2 2 0 0 1-2-2V3zm3 0v17h11V3H7zm2 4h7v2H9V7zm0 4h5v2H9v-2z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-lecture",
    "name": "Lecture room",
    "category": "Campus",
    "keywords": [
      "lecture room",
      "theatre",
      "auditorium",
      "classroom",
      "presentation",
      "seminar"
    ],
    "paths_line": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"12\" rx=\"2\"/><line x1=\"3\" y1=\"12\" x2=\"21\" y2=\"12\"/><path d=\"M9 16l-2 5\"/><path d=\"M15 16l2 5\"/><circle cx=\"12\" cy=\"8\" r=\"2\"/>",
    "paths_solid": "<rect x=\"2\" y=\"3\" width=\"20\" height=\"13\" rx=\"2\" fill=\"currentColor\"/><circle cx=\"12\" cy=\"8\" r=\"2\" fill=\"#fff\"/><polygon points=\"9 16 7 21 9 21 10.5 16\" fill=\"currentColor\"/><polygon points=\"15 16 17 21 15 21 13.5 16\" fill=\"currentColor\"/><rect x=\"8\" y=\"15\" width=\"8\" height=\"2\" rx=\"0.5\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-emergency",
    "name": "Emergency",
    "category": "Safety",
    "keywords": [
      "emergency",
      "alarm",
      "alert",
      "danger",
      "urgent",
      "critical"
    ],
    "paths_line": "<polygon points=\"12 2 21.5 7.5 21.5 16.5 12 22 2.5 16.5 2.5 7.5 12 2\"/><line x1=\"12\" y1=\"8\" x2=\"12\" y2=\"13\"/><circle cx=\"12\" cy=\"16.5\" r=\"1\" fill=\"currentColor\"/>",
    "paths_solid": "<polygon points=\"12 2 22 7.8 22 16.2 12 22 2 16.2 2 7.8\" fill=\"currentColor\"/><rect x=\"11\" y=\"7\" width=\"2\" height=\"6\" rx=\"0.5\" fill=\"#fff\"/><circle cx=\"12\" cy=\"16\" r=\"1.2\" fill=\"#fff\"/>"
  },
  {
    "id": "wf-evacuate",
    "name": "Emergency exit",
    "category": "Safety",
    "keywords": [
      "emergency exit",
      "evacuate",
      "escape",
      "running man",
      "fire exit",
      "safety"
    ],
    "paths_line": "<path d=\"M19 3v18h-6\"/><circle cx=\"7.5\" cy=\"5.5\" r=\"1.5\"/><path d=\"M5 10l3-2 3 2.5v4\"/><path d=\"m8 10-3 5\"/><path d=\"m8 14 3 6\"/><path d=\"m11 10.5 4-1.5\"/>",
    "paths_solid": "<rect x=\"16\" y=\"2\" width=\"6\" height=\"20\" rx=\"1\" fill=\"currentColor\"/><circle cx=\"8\" cy=\"5.5\" r=\"1.8\" fill=\"currentColor\"/><path d=\"M5 10l3.5-2 3.5 2.5v4h-2v-3l-2-1.5-3 5-1.5-1 2.5-4z\" fill=\"currentColor\"/><path d=\"m8 14 3 6-1.7 1-3.3-6.5L8 14z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-assembly",
    "name": "Assembly point",
    "category": "Safety",
    "keywords": [
      "assembly point",
      "muster point",
      "meeting point",
      "evacuation assembly",
      "safe area"
    ],
    "paths_line": "<circle cx=\"12\" cy=\"12\" r=\"3\"/><path d=\"M4 4l4 4\"/><path d=\"M4 8V4h4\"/><path d=\"M20 4l-4 4\"/><path d=\"M20 8V4h-4\"/><path d=\"M4 20l4-4\"/><path d=\"M4 16v4h4\"/><path d=\"M20 20l-4-4\"/><path d=\"M20 16v4h-4\"/>",
    "paths_solid": "<circle cx=\"12\" cy=\"12\" r=\"3\" fill=\"currentColor\"/><polygon points=\"3 3 8 3 8 5 5.5 5 9 8.5 7.5 10 4 6.5 4 9 2 9 2 3\" fill=\"currentColor\"/><polygon points=\"21 3 21 9 19 9 19 6.5 15.5 10 14 8.5 17.5 5 15 5 15 3\" fill=\"currentColor\"/><polygon points=\"3 21 3 15 5 15 5 17.5 8.5 14 10 15.5 6.5 19 9 19 9 21\" fill=\"currentColor\"/><polygon points=\"21 21 15 21 15 19 17.5 19 14 15.5 15.5 14 19 17.5 19 15 21 15\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-fire",
    "name": "Fire",
    "category": "Safety",
    "keywords": [
      "fire",
      "flame",
      "hose",
      "hydrant",
      "extinguisher",
      "fire safety"
    ],
    "paths_line": "<path d=\"M12 2c1 3 4 5 4 9a6 6 0 0 1-12 0c0-3.5 2.5-6.5 4-8 1 2 2 3 4-1z\"/><path d=\"M12 13a2.5 2.5 0 0 0-2.5 2.5c0 1.38 1.12 2.5 2.5 2.5s2.5-1.12 2.5-2.5c0-1-.8-1.8-1.5-2.2-.3.3-.6.5-1 .2z\"/>",
    "paths_solid": "<path d=\"M12 2c1.2 3.5 4.5 5.5 4.5 10a6.5 6.5 0 0 1-13 0c0-4 2.5-7 4.5-9 1 2 2.5 3 4-1z\" fill=\"currentColor\"/><path d=\"M12 13.5c1.2 0 2 1 2 2a2 2 0 0 1-4 0c0-1 .8-2 2-2z\" fill=\"#fff\"/>"
  },
  {
    "id": "wf-warning",
    "name": "Caution",
    "category": "Safety",
    "keywords": [
      "caution",
      "warning",
      "hazard",
      "attention",
      "careful",
      "notice"
    ],
    "paths_line": "<path d=\"m10.29 3.86-8.57 14.85A2 2 0 0 0 3.45 22h17.1a2 2 0 0 0 1.73-3.29L13.71 3.86a2 2 0 0 0-3.42 0z\"/><line x1=\"12\" y1=\"9\" x2=\"12\" y2=\"14\"/><circle cx=\"12\" cy=\"18\" r=\"1\" fill=\"currentColor\"/>",
    "paths_solid": "<path d=\"M12 2L1 21h22L12 2zm-1 7h2v6h-2V9zm1 10a1.2 1.2 0 1 1 0-2.4 1.2 1.2 0 0 1 0 2.4z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-construction",
    "name": "Under construction",
    "category": "Safety",
    "keywords": [
      "under construction",
      "work in progress",
      "maintenance",
      "cone",
      "barrier",
      "renovation"
    ],
    "paths_line": "<polygon points=\"12 2 17 19 7 19 12 2\"/><line x1=\"3\" y1=\"21\" x2=\"21\" y2=\"21\"/><line x1=\"8.5\" y1=\"14\" x2=\"15.5\" y2=\"14\"/><line x1=\"10\" y1=\"9\" x2=\"14\" y2=\"9\"/>",
    "paths_solid": "<polygon points=\"12 2 18 19 6 19\" fill=\"currentColor\"/><rect x=\"2\" y=\"20\" width=\"20\" height=\"2.5\" rx=\"0.5\" fill=\"currentColor\"/><polygon points=\"10 8 14 8 15 12 9 12\" fill=\"#fff\"/><polygon points=\"8.5 14 15.5 14 16.5 17 7.5 17\" fill=\"#fff\"/>"
  },
  {
    "id": "wf-home",
    "name": "Home",
    "category": "UI",
    "keywords": [
      "home",
      "main screen",
      "start",
      "homepage",
      "welcome"
    ],
    "paths_line": "<path d=\"m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V9z\"/><polyline points=\"9 22 9 12 15 12 15 22\"/>",
    "paths_solid": "<polygon points=\"12 2 2 10 4 10 4 21 10 21 10 14 14 14 14 21 20 21 20 10 22 10\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-search",
    "name": "Search",
    "category": "UI",
    "keywords": [
      "search",
      "find",
      "lookup",
      "explore",
      "magnifier",
      "query"
    ],
    "paths_line": "<circle cx=\"11\" cy=\"11\" r=\"7\"/><line x1=\"21\" y1=\"21\" x2=\"16.65\" y2=\"16.65\"/>",
    "paths_solid": "<path d=\"M15.5 14h-.8l-.3-.3a6.5 6.5 0 1 0-.7.7l.3.3v.8l5 5 1.5-1.5-5-5zm-6 0C7 14 5 12 5 9.5S7 5 9.5 5 14 7 14 9.5 12 14 9.5 14z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-menu",
    "name": "Menu",
    "category": "UI",
    "keywords": [
      "menu",
      "hamburger",
      "navigation",
      "options",
      "list"
    ],
    "paths_line": "<line x1=\"4\" y1=\"6\" x2=\"20\" y2=\"6\"/><line x1=\"4\" y1=\"12\" x2=\"20\" y2=\"12\"/><line x1=\"4\" y1=\"18\" x2=\"20\" y2=\"18\"/>",
    "paths_solid": "<rect x=\"3\" y=\"5\" width=\"18\" height=\"3\" rx=\"1.5\" fill=\"currentColor\"/><rect x=\"3\" y=\"11\" width=\"18\" height=\"3\" rx=\"1.5\" fill=\"currentColor\"/><rect x=\"3\" y=\"17\" width=\"18\" height=\"3\" rx=\"1.5\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-back",
    "name": "Back",
    "category": "UI",
    "keywords": [
      "back",
      "previous",
      "return",
      "left arrow",
      "undo"
    ],
    "paths_line": "<polyline points=\"15 18 9 12 15 6\"/>",
    "paths_solid": "<path d=\"M15.5 19l-7-7 7-7 1.8 1.8L12 12l5.3 5.2z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-close",
    "name": "Close",
    "category": "UI",
    "keywords": [
      "close",
      "dismiss",
      "exit modal",
      "cancel",
      "x"
    ],
    "paths_line": "<line x1=\"18\" y1=\"6\" x2=\"6\" y2=\"18\"/><line x1=\"6\" y1=\"6\" x2=\"18\" y2=\"18\"/>",
    "paths_solid": "<path d=\"M19 6.4L17.6 5 12 10.6 6.4 5 5 6.4l5.6 5.6L5 17.6 6.4 19l5.6-5.6 5.6 5.6 1.4-1.4-5.6-5.6z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-hours",
    "name": "Opening hours",
    "category": "UI",
    "keywords": [
      "opening hours",
      "trading hours",
      "times",
      "clock",
      "schedule",
      "open"
    ],
    "paths_line": "<circle cx=\"12\" cy=\"12\" r=\"9\"/><polyline points=\"12 6 12 12 16 14\"/>",
    "paths_solid": "<circle cx=\"12\" cy=\"12\" r=\"10\" fill=\"currentColor\"/><path d=\"M11 6h2v5.5l3.5 2-1 1.7-4.5-2.7V6z\" fill=\"#fff\"/>"
  },
  {
    "id": "wf-timetable",
    "name": "Timetable",
    "category": "UI",
    "keywords": [
      "timetable",
      "schedule",
      "departures",
      "timesheet",
      "planner",
      "calendar"
    ],
    "paths_line": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"17\" rx=\"2\"/><line x1=\"3\" y1=\"9\" x2=\"21\" y2=\"9\"/><line x1=\"8\" y1=\"2\" x2=\"8\" y2=\"6\"/><line x1=\"16\" y1=\"2\" x2=\"16\" y2=\"6\"/><line x1=\"7\" y1=\"13\" x2=\"17\" y2=\"13\"/><line x1=\"7\" y1=\"17\" x2=\"13\" y2=\"17\"/>",
    "paths_solid": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"17\" rx=\"3\" fill=\"currentColor\"/><rect x=\"6\" y=\"2\" width=\"2\" height=\"4\" rx=\"0.5\" fill=\"currentColor\"/><rect x=\"16\" y=\"2\" width=\"2\" height=\"4\" rx=\"0.5\" fill=\"currentColor\"/><rect x=\"5\" y=\"8\" width=\"14\" height=\"2\" fill=\"#fff\"/><rect x=\"6\" y=\"12\" width=\"12\" height=\"1.8\" fill=\"#fff\"/><rect x=\"6\" y=\"16\" width=\"8\" height=\"1.8\" fill=\"#fff\"/>"
  },
  {
    "id": "wf-events",
    "name": "Events",
    "category": "UI",
    "keywords": [
      "events",
      "what's on",
      "calendar",
      "activities",
      "happenings",
      "starred"
    ],
    "paths_line": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"17\" rx=\"2\"/><line x1=\"3\" y1=\"9\" x2=\"21\" y2=\"9\"/><line x1=\"8\" y1=\"2\" x2=\"8\" y2=\"6\"/><line x1=\"16\" y1=\"2\" x2=\"16\" y2=\"6\"/><polygon points=\"12 12 13.2 14.5 16 14.9 14 16.8 14.5 19.5 12 18.2 9.5 19.5 10 16.8 8 14.9 10.8 14.5 12 12\" fill=\"currentColor\"/>",
    "paths_solid": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"17\" rx=\"3\" fill=\"currentColor\"/><rect x=\"6\" y=\"2\" width=\"2\" height=\"4\" rx=\"0.5\" fill=\"currentColor\"/><rect x=\"16\" y=\"2\" width=\"2\" height=\"4\" rx=\"0.5\" fill=\"currentColor\"/><rect x=\"5\" y=\"8\" width=\"14\" height=\"2\" fill=\"#fff\"/><polygon points=\"12 11 13.2 13.5 16 13.9 14 15.8 14.5 18.5 12 17.2 9.5 18.5 10 15.8 8 13.9 10.8 13.5\" fill=\"#fff\"/>"
  },
  {
    "id": "wf-news",
    "name": "News",
    "category": "UI",
    "keywords": [
      "news",
      "updates",
      "newspaper",
      "bulletin",
      "articles",
      "press"
    ],
    "paths_line": "<path d=\"M4 20h14a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2z\"/><line x1=\"6\" y1=\"6\" x2=\"14\" y2=\"6\"/><line x1=\"6\" y1=\"10\" x2=\"18\" y2=\"10\"/><line x1=\"6\" y1=\"14\" x2=\"18\" y2=\"14\"/>",
    "paths_solid": "<rect x=\"2\" y=\"3\" width=\"20\" height=\"18\" rx=\"2\" fill=\"currentColor\"/><rect x=\"5\" y=\"6\" width=\"7\" height=\"2\" fill=\"#fff\"/><rect x=\"5\" y=\"10\" width=\"14\" height=\"1.8\" fill=\"#fff\"/><rect x=\"5\" y=\"13.5\" width=\"14\" height=\"1.8\" fill=\"#fff\"/><rect x=\"5\" y=\"17\" width=\"9\" height=\"1.8\" fill=\"#fff\"/>"
  },
  {
    "id": "wf-announce",
    "name": "Announcements",
    "category": "UI",
    "keywords": [
      "announcements",
      "broadcast",
      "megaphone",
      "bullhorn",
      "notices",
      "alerts"
    ],
    "paths_line": "<path d=\"m3 11 15-5v12L3 13v-2z\"/><path d=\"M11 13.5V19a2 2 0 0 1-2 2H8\"/><path d=\"M19 9a4 4 0 0 1 0 6\"/>",
    "paths_solid": "<path d=\"M18 4l-9 4H4a1 1 0 0 0-1 1v6a1 1 0 0 0 1 1h5l9 4V4zm-9 15v3a2 2 0 0 1-2 2H5v-2h2a1 1 0 0 0 1-1v-2h1zm11.5-8.5a4 4 0 0 1 0 5v2a6 6 0 0 0 0-9v2z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-share",
    "name": "Share / social",
    "category": "Media",
    "keywords": [
      "share",
      "social",
      "send",
      "connect",
      "forward",
      "nodes"
    ],
    "paths_line": "<circle cx=\"18\" cy=\"5\" r=\"3\"/><circle cx=\"6\" cy=\"12\" r=\"3\"/><circle cx=\"18\" cy=\"19\" r=\"3\"/><line x1=\"8.59\" y1=\"13.51\" x2=\"15.42\" y2=\"17.49\"/><line x1=\"15.41\" y1=\"6.51\" x2=\"8.59\" y2=\"10.49\"/>",
    "paths_solid": "<path d=\"M18 16a3 3 0 0 0-2.4 1.2L8.9 13.7a3.3 3.3 0 0 0 0-3.4l6.7-3.5A3 3 0 1 0 15 5a3 3 0 0 0 .1.7L8.4 9.2a3 3 0 1 0 0 5.6l6.7 3.5c0 .2-.1.5-.1.7a3 3 0 1 0 3-3z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-chat",
    "name": "Chat",
    "category": "Media",
    "keywords": [
      "chat",
      "message",
      "conversation",
      "talk",
      "feedback",
      "bubble"
    ],
    "paths_line": "<path d=\"M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z\"/>",
    "paths_solid": "<path d=\"M20 2H4a2 2 0 0 0-2 2v18l4-4h14a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2z\" fill=\"currentColor\"/><circle cx=\"7\" cy=\"10\" r=\"1.5\" fill=\"#fff\"/><circle cx=\"12\" cy=\"10\" r=\"1.5\" fill=\"#fff\"/><circle cx=\"17\" cy=\"10\" r=\"1.5\" fill=\"#fff\"/>"
  },
  {
    "id": "wf-like",
    "name": "Like / feedback",
    "category": "Media",
    "keywords": [
      "like",
      "feedback",
      "thumbs up",
      "satisfaction",
      "survey",
      "rate",
      "positive"
    ],
    "paths_line": "<path d=\"M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3H14z\"/><path d=\"M7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3\"/>",
    "paths_solid": "<path d=\"M1 21h4V9H1v12zm22-11a2 2 0 0 0-2-2h-6.3l1-4.6v-.3a1.5 1.5 0 0 0-.4-1.1L14.2 1 7.6 7.6A2 2 0 0 0 7 9v10a2 2 0 0 0 2 2h9c.8 0 1.5-.5 1.8-1.2l3-7.1c.1-.2.2-.5.2-.7v-2z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-camera",
    "name": "Photos",
    "category": "Media",
    "keywords": [
      "photos",
      "camera",
      "pictures",
      "images",
      "snapshots",
      "photography"
    ],
    "paths_line": "<path d=\"M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z\"/><circle cx=\"12\" cy=\"13\" r=\"4\"/>",
    "paths_solid": "<path d=\"M20 4h-3.2L15 2H9L7.2 4H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm-8 14a5 5 0 1 1 0-10 5 5 0 0 1 0 10zm0-8a3 3 0 1 0 0 6 3 3 0 0 0 0-6z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-video",
    "name": "Video",
    "category": "Media",
    "keywords": [
      "video",
      "camcorder",
      "record",
      "clip",
      "stream",
      "film"
    ],
    "paths_line": "<polygon points=\"23 7 16 12 23 17 23 7\"/><rect x=\"1\" y=\"5\" width=\"15\" height=\"14\" rx=\"2\"/>",
    "paths_solid": "<rect x=\"2\" y=\"5\" width=\"14\" height=\"14\" rx=\"3\" fill=\"currentColor\"/><polygon points=\"18 8 23 4 23 20 18 16\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-qr",
    "name": "Scan QR",
    "category": "Media",
    "keywords": [
      "scan qr",
      "qr code",
      "mobile scan",
      "barcode",
      "transfer to phone"
    ],
    "paths_line": "<rect x=\"3\" y=\"3\" width=\"7\" height=\"7\"/><rect x=\"14\" y=\"3\" width=\"7\" height=\"7\"/><rect x=\"3\" y=\"14\" width=\"7\" height=\"7\"/><rect x=\"15\" y=\"15\" width=\"2\" height=\"2\"/><rect x=\"19\" y=\"15\" width=\"2\" height=\"2\"/><rect x=\"15\" y=\"19\" width=\"6\" height=\"2\"/><path d=\"M6 6h1v1H6z\" fill=\"currentColor\"/><path d=\"M17 6h1v1h-1z\" fill=\"currentColor\"/><path d=\"M6 17h1v1H6z\" fill=\"currentColor\"/>",
    "paths_solid": "<rect x=\"2\" y=\"2\" width=\"8\" height=\"8\" rx=\"1.5\" fill=\"currentColor\"/><rect x=\"4\" y=\"4\" width=\"4\" height=\"4\" fill=\"#fff\"/><rect x=\"5\" y=\"5\" width=\"2\" height=\"2\" fill=\"currentColor\"/><rect x=\"14\" y=\"2\" width=\"8\" height=\"8\" rx=\"1.5\" fill=\"currentColor\"/><rect x=\"16\" y=\"4\" width=\"4\" height=\"4\" fill=\"#fff\"/><rect x=\"17\" y=\"5\" width=\"2\" height=\"2\" fill=\"currentColor\"/><rect x=\"2\" y=\"14\" width=\"8\" height=\"8\" rx=\"1.5\" fill=\"currentColor\"/><rect x=\"4\" y=\"16\" width=\"4\" height=\"4\" fill=\"#fff\"/><rect x=\"5\" y=\"17\" width=\"2\" height=\"2\" fill=\"currentColor\"/><rect x=\"14\" y=\"14\" width=\"3\" height=\"3\" fill=\"currentColor\"/><rect x=\"19\" y=\"14\" width=\"3\" height=\"3\" fill=\"currentColor\"/><rect x=\"14\" y=\"19\" width=\"8\" height=\"3\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-email",
    "name": "Email",
    "category": "Media",
    "keywords": [
      "email",
      "mail",
      "envelope",
      "contact",
      "send to email",
      "newsletter"
    ],
    "paths_line": "<rect x=\"2\" y=\"4\" width=\"20\" height=\"16\" rx=\"2\"/><path d=\"m22 7-10 7L2 7\"/>",
    "paths_solid": "<path d=\"M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z\" fill=\"currentColor\"/>"
  },
  {
    "id": "wf-web",
    "name": "Website",
    "category": "Media",
    "keywords": [
      "website",
      "web",
      "internet",
      "browser",
      "url",
      "online",
      "portal"
    ],
    "paths_line": "<circle cx=\"12\" cy=\"12\" r=\"9\"/><line x1=\"3\" y1=\"12\" x2=\"21\" y2=\"12\"/><path d=\"M12 3a15 15 0 0 1 4 9 15 15 0 0 1-4 9 15 15 0 0 1-4-9 15 15 0 0 1 4-9z\"/>",
    "paths_solid": "<circle cx=\"12\" cy=\"12\" r=\"10\" fill=\"currentColor\"/><path d=\"M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z\" fill=\"#fff\"/><path d=\"M12 4a14 14 0 0 1 2 8 14 14 0 0 1-2 8 14 14 0 0 1-2-8 14 14 0 0 1 2-8z\" fill=\"currentColor\"/><line x1=\"2\" y1=\"12\" x2=\"22\" y2=\"12\" stroke=\"#fff\" stroke-width=\"1.8\"/>"
  }
];

/**
 * Returns raw SVG string for an icon ID
 */
export function getWayfindingSvg(iconId, { set = 'line', size = 24, strokeWidth = 2, className = '' } = {}) {
  const isSolid = set === 'solid';
  const dict = isSolid ? WAYFINDING_SOLID : WAYFINDING_LINE;
  const paths = dict[iconId];
  if (!paths) {
    console.warn(`Wayfinding icon "${iconId}" not found in ${set} set`);
    return '';
  }
  if (isSolid) {
    return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" fill="currentColor" class="wf-icon wf-icon-solid ${iconId} ${className}">${paths}</svg>`;
  }
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${strokeWidth}" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-line ${iconId} ${className}">${paths}</svg>`;
}

/**
 * Custom Web Component <wf-icon name="wf-pin" set="solid" size="32"></wf-icon>
 */
class WayfindingIconElement extends HTMLElement {
  static get observedAttributes() {
    return ['name', 'set', 'size', 'stroke-width', 'color'];
  }

  connectedCallback() {
    this.render();
  }

  attributeChangedCallback() {
    this.render();
  }

  render() {
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
    } else if (set === 'm3') {
    const paths = WAYFINDING_M3[iconId] || '';
    return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-m3 ${iconId} ${className}">${paths}</svg>`;
  }
  if (set === 'gf-example') {
    const paths = WAYFINDING_GF_EXAMPLE[iconId] || '';
    return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 -960 960 960" fill="currentColor" class="wf-icon wf-icon-gf ${iconId} ${className}">${paths}</svg>`;
  }
  if (set === 'tactical') {
      const paths = WAYFINDING_TACTICAL[name] || '';
      this.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" class="wf-icon wf-icon-tactical ${name}">${paths}</svg>`;
    } else {
      const paths = WAYFINDING_LINE[name] || '';
      this.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${strokeWidth}" stroke-linecap="round" stroke-linejoin="round" class="wf-icon wf-icon-line ${name}">${paths}</svg>`;
    }
  }
}

if (typeof window !== 'undefined' && !customElements.get('wf-icon')) {
  customElements.define('wf-icon', WayfindingIconElement);
}

export const GOOGLE_FONTS_SYMBOL_MAPPING = {
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
};

export const WAYFINDING_GF_EXAMPLE = {
  "wf-arrow-up": "<path d=\"M440-160v-487L216-423l-56-57 320-320 320 320-56 57-224-224v487h-80Z\"/>",
  "wf-arrow-right": "<path d=\"M647-440H160v-80h487L423-744l57-56 320 320-320 320-57-56 224-224Z\"/>",
  "wf-arrow-down": "<path d=\"M440-800v487L216-537l-56 57 320 320 320-320-56-57-224 224v-487h-80Z\"/>",
  "wf-arrow-left": "<path d=\"m313-440 224 224-57 56-320-320 320-320 57 56-224 224h487v80H313Z\"/>",
  "wf-arrow-up-right": "<path d=\"m216-160-56-56 464-464H360v-80h400v400h-80v-264L216-160Z\"/>",
  "wf-arrow-up-left": "<path d=\"M744-160 280-624v264h-80v-400h400v80H336l464 464-56 56Z\"/>",
  "wf-u-turn": "<path d=\"M640-120v-480q0-66-47-113t-113-47q-66 0-113 47t-47 113v168l64-64 56 56-160 160-160-160 56-56 64 64v-168q0-100 70-170t170-70q100 0 170 70t70 170v480h-80Z\"/>",
  "wf-signpost": "<path d=\"M440-80v-160H240L120-360l120-120h200v-80H160v-240h280v-80h80v80h200l120 120-120 120H520v80h280v240H520v160h-80ZM240-640h447l40-40-40-40H240v80Zm33 320h447v-80H273l-40 40 40 40Zm-33-320v-80 80Zm480 320v-80 80Z\"/>",
  "wf-pin": "<path d=\"M480-480q33 0 56.5-23.5T560-560q0-33-23.5-56.5T480-640q-33 0-56.5 23.5T400-560q0 33 23.5 56.5T480-480Zm0 294q122-112 181-203.5T720-552q0-109-69.5-178.5T480-800q-101 0-170.5 69.5T240-552q0 71 59 162.5T480-186Zm0 106Q319-217 239.5-334.5T160-552q0-150 96.5-239T480-880q127 0 223.5 89T800-552q0 100-79.5 217.5T480-80Zm0-480Z\"/>",
  "wf-facing": "<path d=\"m260-260 300-140 140-300-300 140-140 300Zm220-180q-17 0-28.5-11.5T440-480q0-17 11.5-28.5T480-520q17 0 28.5 11.5T520-480q0 17-11.5 28.5T480-440Zm0 360q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z\"/>",
  "wf-map": "<path d=\"m600-120-240-84-186 72q-20 8-37-4.5T120-170v-560q0-13 7.5-23t20.5-15l212-72 240 84 186-72q20-8 37 4.5t17 33.5v560q0 13-7.5 23T812-192l-212 72Zm-40-98v-468l-160-56v468l160 56Zm80 0 120-40v-474l-120 46v468Zm-440-10 120-46v-468l-120 40v474Zm440-458v468-468Zm-320-56v468-468Z\"/>",
  "wf-touch": "<path d=\"M419-80q-28 0-52.5-12T325-126L107-403l19-20q20-21 48-25t52 11l74 45v-328q0-17 11.5-28.5T340-760q17 0 29 11.5t12 28.5v472l-97-60 104 133q6 7 14 11t17 4h221q33 0 56.5-23.5T720-240v-160q0-17-11.5-28.5T680-440H461v-80h219q50 0 85 35t35 85v160q0 66-47 113T640-80H419ZM167-620q-13-22-20-47.5t-7-52.5q0-83 58.5-141.5T340-920q83 0 141.5 58.5T540-720q0 27-7 52.5T513-620l-69-40q8-14 12-28.5t4-31.5q0-50-35-85t-85-35q-50 0-85 35t-35 85q0 17 4 31.5t12 28.5l-69 40Zm335 280Z\"/>",
  "wf-entrance": "<path d=\"M480-120v-80h280v-560H480v-80h280q33 0 56.5 23.5T840-760v560q0 33-23.5 56.5T760-120H480Zm-80-160-55-58 102-102H120v-80h327L345-622l55-58 200 200-200 200Z\"/>",
  "wf-exit": "<path d=\"M200-120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h280v80H200v560h280v80H200Zm440-160-55-58 102-102H360v-80h327L585-622l55-58 200 200-200 200Z\"/>",
  "wf-lift": "<path d=\"M280-240h120v-160h40v-100q0-33-23.5-56.5T360-580h-40q-33 0-56.5 23.5T240-500v100h40v160Zm60-380q21 0 35.5-14.5T390-670q0-21-14.5-35.5T340-720q-21 0-35.5 14.5T290-670q0 21 14.5 35.5T340-620Zm180 100h200L620-680 520-520Zm100 240 100-160H520l100 160ZM200-120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h560q33 0 56.5 23.5T840-760v560q0 33-23.5 56.5T760-120H200Zm0-80h560v-560H200v560Zm0 0v-560 560Z\"/>",
  "wf-stairs": "<path d=\"M240-240h177v-133h103v-133h103v-134h97v-80H543v133H440v133H337v134h-97v80Zm-40 120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h560q33 0 56.5 23.5T840-760v560q0 33-23.5 56.5T760-120H200Zm0-80h560v-560H200v560Zm0-560v560-560Z\"/>",
  "wf-escalator-up": "<path d=\"M280-240h132l200-360h68q25 0 42.5-17.5T740-660q0-25-17.5-42.5T680-720H548L348-360h-68q-25 0-42.5 17.5T220-300q0 25 17.5 42.5T280-240Zm-80 120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h560q33 0 56.5 23.5T840-760v560q0 33-23.5 56.5T760-120H200Zm0-80h560v-560H200v560Zm0-560v560-560Z\"/>",
  "wf-escalator-down": "<path d=\"M260-720q-33 0-56.5-23.5T180-800q0-33 23.5-56.5T260-880q33 0 56.5 23.5T340-800q0 33-23.5 56.5T260-720Zm420 200q-25 0-42.5-17.5T620-580q0-25 17.5-42.5T680-640q25 0 42.5 17.5T740-580q0 25-17.5 42.5T680-520ZM180-80v-280h-60v-240q0-33 23.5-56.5T200-680h120q22 0 40 10.5t29 29.5l143 247 41-61q8-12 21.5-19t28.5-7h117q25 0 42.5 17.5T800-420v140h-40v200H600v-284l-31 44h-88L380-496v416H180Z\"/>",
  "wf-ramp": "<path d=\"M440-120v-252q-33 45-79 85.5T258-211l-58-58q30-17 71-47t78.5-71.5q37.5-41.5 64-95T440-600v-87l-64 63-56-56 160-160 160 160-56 56-64-63v567h-80Z\"/>",
  "wf-accessible": "<path d=\"M480-720q-33 0-56.5-23.5T400-800q0-33 23.5-56.5T480-880q33 0 56.5 23.5T560-800q0 33-23.5 56.5T480-720ZM680-80v-200H480q-33 0-56.5-23.5T400-360v-240q0-33 23.5-56.5T480-680q24 0 41.5 10.5T559-636q55 66 99.5 90.5T760-520v80q-53 0-107-23t-93-55v138h120q33 0 56.5 23.5T760-300v220h-80Zm-280 0q-83 0-141.5-58.5T200-280q0-72 45.5-127T360-476v82q-35 14-57.5 44.5T280-280q0 50 35 85t85 35q39 0 69.5-22.5T514-240h82q-14 69-69 114.5T400-80Z\"/>",
  "wf-levels": "<path d=\"M480-118 120-398l66-50 294 228 294-228 66 50-360 280Zm0-202L120-600l360-280 360 280-360 280Zm0-280Zm0 178 230-178-230-178-230 178 230 178Z\"/>",
  "wf-no-entry": "<path d=\"M280-440h400v-80H280v80ZM480-80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z\"/>",
  "wf-prohibited": "<path d=\"m336-280 144-144 144 144 56-56-144-144 144-144-56-56-144 144-144-144-56 56 144 144-144 144 56 56ZM480-80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z\"/>",
  "wf-staff-only": "<path d=\"M160-80q-33 0-56.5-23.5T80-160v-440q0-33 23.5-56.5T160-680h200v-120q0-33 23.5-56.5T440-880h80q33 0 56.5 23.5T600-800v120h200q33 0 56.5 23.5T880-600v440q0 33-23.5 56.5T800-80H160Zm0-80h640v-440H600q0 33-23.5 56.5T520-520h-80q-33 0-56.5-23.5T360-600H160v440Zm80-80h240v-18q0-17-9.5-31.5T444-312q-20-9-40.5-13.5T360-330q-23 0-43.5 4.5T276-312q-17 8-26.5 22.5T240-258v18Zm320-60h160v-60H560v60Zm-200-60q25 0 42.5-17.5T420-420q0-25-17.5-42.5T360-480q-25 0-42.5 17.5T300-420q0 25 17.5 42.5T360-360Zm200-60h160v-60H560v60ZM440-600h80v-200h-80v200Zm40 220Z\"/>",
  "wf-toilets": "<path d=\"M220-80v-300h-60v-220q0-33 23.5-56.5T240-680h120q33 0 56.5 23.5T440-600v220h-60v300H220Zm80-640q-33 0-56.5-23.5T220-800q0-33 23.5-56.5T300-880q33 0 56.5 23.5T380-800q0 33-23.5 56.5T300-720ZM600-80v-240H480l102-306q8-26 29.5-40t48.5-14q27 0 48.5 14t29.5 40l102 306H720v240H600Zm60-640q-33 0-56.5-23.5T580-800q0-33 23.5-56.5T660-880q33 0 56.5 23.5T740-800q0 33-23.5 56.5T660-720Z\"/>",
  "wf-toilet-male": "<path d=\"M400-80v-280h-80v-240q0-33 23.5-56.5T400-680h160q33 0 56.5 23.5T640-600v240h-80v280H400Zm80-640q-33 0-56.5-23.5T400-800q0-33 23.5-56.5T480-880q33 0 56.5 23.5T560-800q0 33-23.5 56.5T480-720Z\"/>",
  "wf-toilet-female": "<path d=\"M400-80v-240H280l122-308q10-24 31-38t47-14q26 0 47 14t31 38l122 308H560v240H400Zm80-640q-33 0-56.5-23.5T400-800q0-33 23.5-56.5T480-880q33 0 56.5 23.5T560-800q0 33-23.5 56.5T480-720Z\"/>",
  "wf-toilet-accessible": "<path d=\"M320-80q-83 0-141.5-58.5T120-280q0-83 58.5-141.5T320-480v80q-50 0-85 35t-35 85q0 50 35 85t85 35q50 0 85-35t35-85h80q0 83-58.5 141.5T320-80Zm360-40v-200H440q-44 0-68-37.5t-6-78.5l74-164h-91l-24 62-77-22 28-72q9-23 29.5-35.5T350-680h208q45 0 68.5 36.5T632-566l-66 146h114q33 0 56.5 23.5T760-340v220h-80Zm-40-580q-33 0-56.5-23.5T560-780q0-33 23.5-56.5T640-860q33 0 56.5 23.5T720-780q0 33-23.5 56.5T640-700Z\"/>",
  "wf-baby-change": "<path d=\"M120-80v-400l63-185q8-26 30-40.5t47-14.5q8 0 16 1.5t16 5.5l166 73h102v80H440l-108-47-52 157v370H120Zm240-120v-80h480v80H360Zm420-120q-25 0-42.5-17.5T720-380q0-25 17.5-42.5T780-440q25 0 42.5 17.5T840-380q0 25-17.5 42.5T780-320Zm-260 0q-33 0-56.5-23.5T440-400v-40h-80v-80h120q17 0 28.5 11.5T520-480v40h80v-80h80v120q0 33-23.5 56.5T600-320h-80ZM320-760q-33 0-56.5-23.5T240-840q0-33 23.5-56.5T320-920q33 0 56.5 23.5T400-840q0 33-23.5 56.5T320-760Z\"/>",
  "wf-cafe": "<path d=\"M160-120v-80h640v80H160Zm160-160q-66 0-113-47t-47-113v-400h640q33 0 56.5 23.5T880-760v120q0 33-23.5 56.5T800-560h-80v120q0 66-47 113t-113 47H320Zm0-80h240q33 0 56.5-23.5T640-440v-320H240v320q0 33 23.5 56.5T320-360Zm400-280h80v-120h-80v120ZM320-360h-80 400-320Z\"/>",
  "wf-food": "<path d=\"M280-80v-366q-51-14-85.5-56T160-600v-280h80v280h40v-280h80v280h40v-280h80v280q0 56-34.5 98T360-446v366h-80Zm400 0v-320H560v-280q0-83 58.5-141.5T760-880v800h-80Z\"/>",
  "wf-retail": "<path d=\"M240-80q-33 0-56.5-23.5T160-160v-480q0-33 23.5-56.5T240-720h80q0-66 47-113t113-47q66 0 113 47t47 113h80q33 0 56.5 23.5T800-640v480q0 33-23.5 56.5T720-80H240Zm0-80h480v-480h-80v80q0 17-11.5 28.5T600-520q-17 0-28.5-11.5T560-560v-80H400v80q0 17-11.5 28.5T360-520q-17 0-28.5-11.5T320-560v-80h-80v480Zm160-560h160q0-33-23.5-56.5T480-800q-33 0-56.5 23.5T400-720ZM240-160v-480 480Z\"/>",
  "wf-atm": "<path d=\"M415-360v-180h-90v-60h240v60h-90v180h-60Zm-335 0v-200q0-17 11.5-28.5T120-600h120q17 0 28.5 11.5T280-560v200h-60v-60h-80v60H80Zm60-120h80v-60h-80v60Zm480 120v-200q0-17 11.5-28.5T660-600h180q17 0 28.5 11.5T880-560v200h-60v-180h-40v140h-60v-140h-40v180h-60Z\"/>",
  "wf-payment": "<path d=\"M560-440q-50 0-85-35t-35-85q0-50 35-85t85-35q50 0 85 35t35 85q0 50-35 85t-85 35ZM280-320q-33 0-56.5-23.5T200-400v-320q0-33 23.5-56.5T280-800h560q33 0 56.5 23.5T920-720v320q0 33-23.5 56.5T840-320H280Zm80-80h400q0-33 23.5-56.5T840-480v-160q-33 0-56.5-23.5T760-720H360q0 33-23.5 56.5T280-640v160q33 0 56.5 23.5T360-400Zm440 240H120q-33 0-56.5-23.5T40-240v-440h80v440h680v80ZM280-400v-320 320Z\"/>",
  "wf-pharmacy": "<path d=\"M120-120v-80l80-240-80-240v-80h508l58-160 94 34-46 126h106v80l-80 240 80 240v80H120Zm320-160h80v-120h120v-80H520v-120h-80v120H320v80h120v120Zm-236 80h552l-80-240 80-240H204l80 240-80 240Zm276-240Z\"/>",
  "wf-water": "<path d=\"M491-200q12-1 20.5-9.5T520-230q0-14-9-22.5t-23-7.5q-41 3-87-22.5T343-375q-2-11-10.5-18t-19.5-7q-14 0-23 10.5t-6 24.5q17 91 80 130t127 35ZM480-80q-137 0-228.5-94T160-408q0-100 79.5-217.5T480-880q161 137 240.5 254.5T800-408q0 140-91.5 234T480-80Zm0-80q104 0 172-70.5T720-408q0-73-60.5-165T480-774Q361-665 300.5-573T240-408q0 107 68 177.5T480-160Zm0-320Z\"/>",
  "wf-wifi": "<path d=\"M480-120q-42 0-71-29t-29-71q0-42 29-71t71-29q42 0 71 29t29 71q0 42-29 71t-71 29ZM254-346l-84-86q59-59 138.5-93.5T480-560q92 0 171.5 35T790-430l-84 84q-44-44-102-69t-124-25q-66 0-124 25t-102 69ZM84-516 0-600q92-94 215-147t265-53q142 0 265 53t215 147l-84 84q-77-77-178.5-120.5T480-680q-116 0-217.5 43.5T84-516Z\"/>",
  "wf-seating": "<path d=\"M200-120q-17 0-28.5-11.5T160-160v-40q-50 0-85-35t-35-85v-200q0-50 35-85t85-35v-80q0-50 35-85t85-35h400q50 0 85 35t35 85v80q50 0 85 35t35 85v200q0 50-35 85t-85 35v40q0 17-11.5 28.5T760-120q-17 0-28.5-11.5T720-160v-40H240v40q0 17-11.5 28.5T200-120Zm-40-160h640q17 0 28.5-11.5T840-320v-200q0-17-11.5-28.5T800-560q-17 0-28.5 11.5T760-520v160H200v-160q0-17-11.5-28.5T160-560q-17 0-28.5 11.5T120-520v200q0 17 11.5 28.5T160-280Zm120-160h400v-80q0-27 11-49t29-39v-112q0-17-11.5-28.5T680-760H280q-17 0-28.5 11.5T240-720v112q18 17 29 39t11 49v80Zm200 0Zm0 160Zm0-80Z\"/>",
  "wf-parking": "<path d=\"M240-120v-720h280q100 0 170 70t70 170q0 100-70 170t-170 70H400v240H240Zm160-400h128q33 0 56.5-23.5T608-600q0-33-23.5-56.5T528-680H400v160Z\"/>",
  "wf-car": "<path d=\"M240-200v40q0 17-11.5 28.5T200-120h-40q-17 0-28.5-11.5T120-160v-320l84-240q6-18 21.5-29t34.5-11h440q19 0 34.5 11t21.5 29l84 240v320q0 17-11.5 28.5T800-120h-40q-17 0-28.5-11.5T720-160v-40H240Zm-8-360h496l-42-120H274l-42 120Zm-32 80v200-200Zm100 160q25 0 42.5-17.5T360-380q0-25-17.5-42.5T300-440q-25 0-42.5 17.5T240-380q0 25 17.5 42.5T300-320Zm360 0q25 0 42.5-17.5T720-380q0-25-17.5-42.5T660-440q-25 0-42.5 17.5T600-380q0 25 17.5 42.5T660-320Zm-460 40h560v-200H200v200Z\"/>",
  "wf-bus": "<path d=\"M240-120q-17 0-28.5-11.5T200-160v-82q-18-20-29-44.5T160-340v-380q0-83 77-121.5T480-880q172 0 246 37t74 123v380q0 29-11 53.5T760-242v82q0 17-11.5 28.5T720-120h-40q-17 0-28.5-11.5T640-160v-40H320v40q0 17-11.5 28.5T280-120h-40Zm242-640h224-448 224Zm158 280H240h480-80Zm-400-80h480v-120H240v120Zm100 240q25 0 42.5-17.5T400-380q0-25-17.5-42.5T340-440q-25 0-42.5 17.5T280-380q0 25 17.5 42.5T340-320Zm280 0q25 0 42.5-17.5T680-380q0-25-17.5-42.5T620-440q-25 0-42.5 17.5T560-380q0 25 17.5 42.5T620-320ZM258-760h448q-15-17-64.5-28.5T482-800q-107 0-156.5 12.5T258-760Zm62 480h320q33 0 56.5-23.5T720-360v-120H240v120q0 33 23.5 56.5T320-280Z\"/>",
  "wf-ev": "<path d=\"m340-200 100-160h-60v-120L280-320h60v120ZM240-560h240v-200H240v200Zm0 360h240v-280H240v280Zm-80 80v-640q0-33 23.5-56.5T240-840h240q33 0 56.5 23.5T560-760v280h50q29 0 49.5 20.5T680-410v185q0 17 14 31t31 14q18 0 31.5-14t13.5-31v-375h-10q-17 0-28.5-11.5T720-640v-80h20v-60h40v60h40v-60h40v60h20v80q0 17-11.5 28.5T840-600h-10v375q0 42-30.5 73.5T725-120q-43 0-74-31.5T620-225v-185q0-5-2.5-7.5T610-420h-50v300H160Zm320-80H240h240Z\"/>",
  "wf-info": "<path d=\"M440-280h80v-240h-80v240Zm40-320q17 0 28.5-11.5T520-640q0-17-11.5-28.5T480-680q-17 0-28.5 11.5T440-640q0 17 11.5 28.5T480-600Zm0 520q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z\"/>",
  "wf-help": "<path d=\"M478-240q21 0 35.5-14.5T528-290q0-21-14.5-35.5T478-340q-21 0-35.5 14.5T428-290q0 21 14.5 35.5T478-240Zm-36-154h74q0-33 7.5-52t42.5-52q26-26 41-49.5t15-56.5q0-56-41-86t-97-30q-57 0-92.5 30T342-618l66 26q5-18 22.5-39t53.5-21q32 0 48 17.5t16 38.5q0 20-12 37.5T506-526q-44 39-54 59t-10 73Zm38 314q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z\"/>",
  "wf-reception": "<path d=\"M80-240v-480h800v480h-80v-80H640v80h-80v-400H160v400H80Zm560-320h160v-80H640v80Zm0 160h160v-80H640v80Z\"/>",
  "wf-security": "<path d=\"M480-80q-139-35-229.5-159.5T160-516v-244l320-120 320 120v244q0 152-90.5 276.5T480-80Zm0-84q104-33 172-132t68-220v-189l-240-90-240 90v189q0 121 68 220t172 132Zm0-316Z\"/>",
  "wf-phone": "<path d=\"M798-120q-125 0-247-54.5T329-329Q229-429 174.5-551T120-798q0-18 12-30t30-12h162q14 0 25 9.5t13 22.5l26 140q2 16-1 27t-11 19l-97 98q20 37 47.5 71.5T387-386q31 31 65 57.5t72 48.5l94-94q9-9 23.5-13.5T670-390l138 28q14 4 23 14.5t9 23.5v162q0 18-12 30t-30 12ZM241-600l66-66-17-94h-89q5 41 14 81t26 79Zm358 358q39 17 79.5 27t81.5 13v-88l-94-19-67 67ZM241-600Zm358 358Z\"/>",
  "wf-intercom": "<path d=\"M690-480h60v-68l59 34 30-52-59-34 59-34-30-52-59 34v-68h-60v68l-59-34-30 52 59 34-59 34 30 52 59-34v68ZM80-120q-33 0-56.5-23.5T0-200v-560q0-33 23.5-56.5T80-840h800q33 0 56.5 23.5T960-760v560q0 33-23.5 56.5T880-120H80Zm556-80h244v-560H80v560h4q42-75 116-117.5T360-360q86 0 160 42.5T636-200ZM360-400q50 0 85-35t35-85q0-50-35-85t-85-35q-50 0-85 35t-35 85q0 50 35 85t85 35ZM182-200h356q-34-38-80.5-59T360-280q-51 0-97 21t-81 59Zm178-280q-17 0-28.5-11.5T320-520q0-17 11.5-28.5T360-560q17 0 28.5 11.5T400-520q0 17-11.5 28.5T360-480Zm120 0Z\"/>",
  "wf-hospital": "<path d=\"M420-280h120v-140h140v-120H540v-140H420v140H280v120h140v140ZM200-120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h560q33 0 56.5 23.5T840-760v560q0 33-23.5 56.5T760-120H200Zm0-80h560v-560H200v560Zm0-560v560-560Z\"/>",
  "wf-first-aid": "<path d=\"M160-80q-33 0-56.5-23.5T80-160v-480q0-33 23.5-56.5T160-720h160v-80q0-33 23.5-56.5T400-880h160q33 0 56.5 23.5T640-800v80h160q33 0 56.5 23.5T880-640v480q0 33-23.5 56.5T800-80H160Zm0-80h640v-480H160v480Zm240-560h160v-80H400v80ZM160-160v-480 480Zm280-200v120h80v-120h120v-80H520v-120h-80v120H320v80h120Z\"/>",
  "wf-consult": "<path d=\"M540-80q-108 0-184-76t-76-184v-23q-86-14-143-80.5T80-600v-240h120v-40h80v160h-80v-40h-40v160q0 66 47 113t113 47q66 0 113-47t47-113v-160h-40v40h-80v-160h80v40h120v240q0 90-57 156.5T360-363v23q0 75 52.5 127.5T540-160q75 0 127.5-52.5T720-340v-67q-35-12-57.5-43T640-520q0-50 35-85t85-35q50 0 85 35t35 85q0 39-22.5 70T800-407v67q0 108-76 184T540-80Zm220-400q17 0 28.5-11.5T800-520q0-17-11.5-28.5T760-560q-17 0-28.5 11.5T720-520q0 17 11.5 28.5T760-480Zm0-40Z\"/>",
  "wf-pathology": "<path d=\"M200-120v-80h200v-80q-83 0-141.5-58.5T200-480q0-61 33.5-111t90.5-73q8-34 35.5-55t62.5-21l-22-62 38-14-14-36 76-28 12 38 38-14 110 300-38 14 14 38-76 28-12-38-38 14-24-66q-15 14-34.5 21t-39.5 5q-22-2-41-13.5T338-582q-27 16-42.5 43T280-480q0 50 35 85t85 35h320v80H520v80h240v80H200Zm346-458 36-14-68-188-38 14 70 188Zm-126-22q17 0 28.5-11.5T460-640q0-17-11.5-28.5T420-680q-17 0-28.5 11.5T380-640q0 17 11.5 28.5T420-600Zm126 22Zm-126-62Zm0 0Z\"/>",
  "wf-aed": "<path d=\"M300-840q52 0 99 22t81 62q34-40 81-62t99-22q94 0 157 63t63 157q0 5-.5 10t-.5 10h-80q1-5 1-10v-10q0-60-40-100t-100-40q-47 0-87 26.5T518-666h-76q-15-41-55-67.5T300-760q-60 0-100 40t-40 100v10q0 5 1 10H81q0-5-.5-10t-.5-10q0-94 63-157t157-63Zm-88 480h112q32 31 70 67t86 79q48-43 86-79t70-67h113q-38 42-90 91T538-158l-58 52-58-52q-69-62-120.5-111T212-360Zm230 40q13 0 22.5-7.5T478-347l54-163 35 52q5 8 14 13t19 5h320v-80H623l-69-102q-6-9-15.5-13.5T518-640q-13 0-22.5 7.5T482-613l-54 162-34-51q-5-8-14-13t-19-5H40v80h297l69 102q6 9 15.5 13.5T442-320Zm38-167Z\"/>",
  "wf-student": "<path d=\"M480-120 200-272v-240L40-600l440-240 440 240v320h-80v-276l-80 44v240L480-120Zm0-332 274-148-274-148-274 148 274 148Zm0 241 200-108v-151L480-360 280-470v151l200 108Zm0-241Zm0 90Zm0 0Z\"/>",
  "wf-library": "<path d=\"M480-60q-72-68-165-104t-195-36v-440q101 0 194 36.5T480-498q73-69 166-105.5T840-640v440q-103 0-195.5 36T480-60Zm0-104q63-47 134-75t146-37v-276q-73 13-143.5 52.5T480-394q-66-66-136.5-105.5T200-552v276q75 9 146 37t134 75Zm0-436q-66 0-113-47t-47-113q0-66 47-113t113-47q66 0 113 47t47 113q0 66-47 113t-113 47Zm0-80q33 0 56.5-23.5T560-760q0-33-23.5-56.5T480-840q-33 0-56.5 23.5T400-760q0 33 23.5 56.5T480-680Zm0-80Zm0 366Z\"/>",
  "wf-lecture": "<path d=\"M840-120v-640H120v320H40v-320q0-33 23.5-56.5T120-840h720q33 0 56.5 23.5T920-760v560q0 33-23.5 56.5T840-120ZM360-400q-66 0-113-47t-47-113q0-66 47-113t113-47q66 0 113 47t47 113q0 66-47 113t-113 47Zm0-80q33 0 56.5-23.5T440-560q0-33-23.5-56.5T360-640q-33 0-56.5 23.5T280-560q0 33 23.5 56.5T360-480ZM40-80v-112q0-34 17.5-62.5T104-298q62-31 126-46.5T360-360q66 0 130 15.5T616-298q29 15 46.5 43.5T680-192v112H40Zm80-80h480v-32q0-11-5.5-20T580-226q-54-27-109-40.5T360-280q-56 0-111 13.5T140-226q-9 5-14.5 14t-5.5 20v32Zm240-400Zm0 400Z\"/>",
  "wf-emergency": "<path d=\"M410-120v-238L204-239l-70-121 206-120-206-119 70-121 206 119v-239h140v239l206-119 70 121-206 119 206 120-70 121-206-119v238H410Z\"/>",
  "wf-evacuate": "<path d=\"M520-40v-240l-84-80-40 176-276-56 16-80 192 40 64-324-72 28v136h-80v-188l158-68q35-15 51.5-19.5T480-720q21 0 39 11t29 29l40 64q26 42 70.5 69T760-520v80q-66 0-123.5-27.5T540-540l-24 120 84 80v300h-80Zm20-700q-33 0-56.5-23.5T460-820q0-33 23.5-56.5T540-900q33 0 56.5 23.5T620-820q0 33-23.5 56.5T540-740Z\"/>",
  "wf-assembly": "<path d=\"M0-240v-63q0-43 44-70t116-27q13 0 25 .5t23 2.5q-14 21-21 44t-7 48v65H0Zm240 0v-65q0-32 17.5-58.5T307-410q32-20 76.5-30t96.5-10q53 0 97.5 10t76.5 30q32 20 49 46.5t17 58.5v65H240Zm540 0v-65q0-26-6.5-49T754-397q11-2 22.5-2.5t23.5-.5q72 0 116 26.5t44 70.5v63H780Zm-455-80h311q-10-20-55.5-35T480-370q-55 0-100.5 15T325-320ZM160-440q-33 0-56.5-23.5T80-520q0-34 23.5-57t56.5-23q34 0 57 23t23 57q0 33-23 56.5T160-440Zm640 0q-33 0-56.5-23.5T720-520q0-34 23.5-57t56.5-23q34 0 57 23t23 57q0 33-23 56.5T800-440Zm-320-40q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T600-600q0 50-34.5 85T480-480Zm0-80q17 0 28.5-11.5T520-600q0-17-11.5-28.5T480-640q-17 0-28.5 11.5T440-600q0 17 11.5 28.5T480-560Zm1 240Zm-1-280Z\"/>",
  "wf-fire": "<path d=\"M240-400q0 52 21 98.5t60 81.5q-1-5-1-9v-9q0-32 12-60t35-51l113-111 113 111q23 23 35 51t12 60v9q0 4-1 9 39-35 60-81.5t21-98.5q0-50-18.5-94.5T648-574q-20 13-42 19.5t-45 6.5q-62 0-107.5-41T401-690q-39 33-69 68.5t-50.5 72Q261-513 250.5-475T240-400Zm240 52-57 56q-11 11-17 25t-6 29q0 32 23.5 55t56.5 23q33 0 56.5-23t23.5-55q0-16-6-29.5T537-292l-57-56Zm0-492v132q0 34 23.5 57t57.5 23q18 0 33.5-7.5T622-658l18-22q74 42 117 117t43 163q0 134-93 227T480-80q-134 0-227-93t-93-227q0-129 86.5-245T480-840Z\"/>",
  "wf-warning": "<path d=\"m40-120 440-760 440 760H40Zm138-80h604L480-720 178-200Zm302-40q17 0 28.5-11.5T520-280q0-17-11.5-28.5T480-320q-17 0-28.5 11.5T440-280q0 17 11.5 28.5T480-240Zm-40-120h80v-200h-80v200Zm40-100Z\"/>",
  "wf-construction": "<path d=\"M756-120 537-339l84-84 219 219-84 84Zm-552 0-84-84 276-276-68-68-28 28-51-51v82l-28 28-121-121 28-28h82l-50-50 142-142q20-20 43-29t47-9q24 0 47 9t43 29l-92 92 50 50-28 28 68 68 90-90q-4-11-6.5-23t-2.5-24q0-59 40.5-99.5T701-841q15 0 28.5 3t27.5 9l-99 99 72 72 99-99q7 14 9.5 27.5T841-701q0 59-40.5 99.5T701-561q-12 0-24-2t-23-7L204-120Z\"/>",
  "wf-home": "<path d=\"M240-200h120v-240h240v240h120v-360L480-740 240-560v360Zm-80 80v-480l320-240 320 240v480H520v-240h-80v240H160Zm320-350Z\"/>",
  "wf-search": "<path d=\"M784-120 532-372q-30 24-69 38t-83 14q-109 0-184.5-75.5T120-580q0-109 75.5-184.5T380-840q109 0 184.5 75.5T640-580q0 44-14 83t-38 69l252 252-56 56ZM380-400q75 0 127.5-52.5T560-580q0-75-52.5-127.5T380-760q-75 0-127.5 52.5T200-580q0 75 52.5 127.5T380-400Z\"/>",
  "wf-menu": "<path d=\"M120-240v-80h720v80H120Zm0-200v-80h720v80H120Zm0-200v-80h720v80H120Z\"/>",
  "wf-back": "<path d=\"m313-440 224 224-57 56-320-320 320-320 57 56-224 224h487v80H313Z\"/>",
  "wf-close": "<path d=\"m256-200-56-56 224-224-224-224 56-56 224 224 224-224 56 56-224 224 224 224-56 56-224-224-224 224Z\"/>",
  "wf-hours": "<path d=\"m612-292 56-56-148-148v-184h-80v216l172 172ZM480-80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-400Zm0 320q133 0 226.5-93.5T800-480q0-133-93.5-226.5T480-800q-133 0-226.5 93.5T160-480q0 133 93.5 226.5T480-160Z\"/>",
  "wf-timetable": "<path d=\"M200-80q-33 0-56.5-23.5T120-160v-560q0-33 23.5-56.5T200-800h40v-80h80v80h320v-80h80v80h40q33 0 56.5 23.5T840-720v560q0 33-23.5 56.5T760-80H200Zm0-80h560v-400H200v400Zm0-480h560v-80H200v80Zm0 0v-80 80Zm280 240q-17 0-28.5-11.5T440-440q0-17 11.5-28.5T480-480q17 0 28.5 11.5T520-440q0 17-11.5 28.5T480-400Zm-160 0q-17 0-28.5-11.5T280-440q0-17 11.5-28.5T320-480q17 0 28.5 11.5T360-440q0 17-11.5 28.5T320-400Zm320 0q-17 0-28.5-11.5T600-440q0-17 11.5-28.5T640-480q17 0 28.5 11.5T680-440q0 17-11.5 28.5T640-400ZM480-240q-17 0-28.5-11.5T440-280q0-17 11.5-28.5T480-320q17 0 28.5 11.5T520-280q0 17-11.5 28.5T480-240Zm-160 0q-17 0-28.5-11.5T280-280q0-17 11.5-28.5T320-320q17 0 28.5 11.5T360-280q0 17-11.5 28.5T320-240Zm320 0q-17 0-28.5-11.5T600-280q0-17 11.5-28.5T640-320q17 0 28.5 11.5T680-280q0 17-11.5 28.5T640-240Z\"/>",
  "wf-events": "<path d=\"M580-240q-42 0-71-29t-29-71q0-42 29-71t71-29q42 0 71 29t29 71q0 42-29 71t-71 29ZM200-80q-33 0-56.5-23.5T120-160v-560q0-33 23.5-56.5T200-800h40v-80h80v80h320v-80h80v80h40q33 0 56.5 23.5T840-720v560q0 33-23.5 56.5T760-80H200Zm0-80h560v-400H200v400Zm0-480h560v-80H200v80Zm0 0v-80 80Z\"/>",
  "wf-news": "<path d=\"M160-120q-33 0-56.5-23.5T80-200v-640l67 67 66-67 67 67 67-67 66 67 67-67 67 67 66-67 67 67 67-67 66 67 67-67v640q0 33-23.5 56.5T800-120H160Zm0-80h280v-240H160v240Zm360 0h280v-80H520v80Zm0-160h280v-80H520v80ZM160-520h640v-120H160v120Z\"/>",
  "wf-announce": "<path d=\"M720-440v-80h160v80H720Zm48 280-128-96 48-64 128 96-48 64Zm-80-480-48-64 128-96 48 64-128 96ZM200-200v-160h-40q-33 0-56.5-23.5T80-440v-80q0-33 23.5-56.5T160-600h160l200-120v480L320-360h-40v160h-80Zm240-182v-196l-98 58H160v80h182l98 58Zm120 36v-268q27 24 43.5 58.5T620-480q0 41-16.5 75.5T560-346ZM300-480Z\"/>",
  "wf-share": "<path d=\"M720-80q-50 0-85-35t-35-85q0-7 1-14.5t3-13.5L322-392q-17 15-38 23.5t-44 8.5q-50 0-85-35t-35-85q0-50 35-85t85-35q23 0 44 8.5t38 23.5l282-164q-2-6-3-13.5t-1-14.5q0-50 35-85t85-35q50 0 85 35t35 85q0 50-35 85t-85 35q-23 0-44-8.5T638-672L356-508q2 6 3 13.5t1 14.5q0 7-1 14.5t-3 13.5l282 164q17-15 38-23.5t44-8.5q50 0 85 35t35 85q0 50-35 85t-85 35Zm0-640q17 0 28.5-11.5T760-760q0-17-11.5-28.5T720-800q-17 0-28.5 11.5T680-760q0 17 11.5 28.5T720-720ZM240-440q17 0 28.5-11.5T280-480q0-17-11.5-28.5T240-520q-17 0-28.5 11.5T200-480q0 17 11.5 28.5T240-440Zm480 280q17 0 28.5-11.5T760-200q0-17-11.5-28.5T720-240q-17 0-28.5 11.5T680-200q0 17 11.5 28.5T720-160Zm0-600ZM240-480Zm480 280Z\"/>",
  "wf-chat": "<path d=\"M240-400h320v-80H240v80Zm0-120h480v-80H240v80Zm0-120h480v-80H240v80ZM80-80v-720q0-33 23.5-56.5T160-880h640q33 0 56.5 23.5T880-800v480q0 33-23.5 56.5T800-240H240L80-80Zm126-240h594v-480H160v525l46-45Zm-46 0v-480 480Z\"/>",
  "wf-like": "<path d=\"M720-120H280v-520l280-280 50 50q7 7 11.5 19t4.5 23v14l-44 174h258q32 0 56 24t24 56v80q0 7-2 15t-4 15L794-168q-9 20-30 34t-44 14Zm-360-80h360l120-280v-80H480l54-220-174 174v406Zm0-406v406-406Zm-80-34v80H160v360h120v80H80v-520h200Z\"/>",
  "wf-camera": "<path d=\"M480-260q75 0 127.5-52.5T660-440q0-75-52.5-127.5T480-620q-75 0-127.5 52.5T300-440q0 75 52.5 127.5T480-260Zm0-80q-42 0-71-29t-29-71q0-42 29-71t71-29q42 0 71 29t29 71q0 42-29 71t-71 29ZM160-120q-33 0-56.5-23.5T80-200v-480q0-33 23.5-56.5T160-760h126l74-80h240l74 80h126q33 0 56.5 23.5T880-680v480q0 33-23.5 56.5T800-120H160Zm0-80h640v-480H638l-73-80H395l-73 80H160v480Zm320-240Z\"/>",
  "wf-video": "<path d=\"M160-160q-33 0-56.5-23.5T80-240v-480q0-33 23.5-56.5T160-800h480q33 0 56.5 23.5T720-720v180l160-160v440L720-420v180q0 33-23.5 56.5T640-160H160Zm0-80h480v-480H160v480Zm0 0v-480 480Z\"/>",
  "wf-qr": "<path d=\"M80-680v-200h200v80H160v120H80Zm0 600v-200h80v120h120v80H80Zm600 0v-80h120v-120h80v200H680Zm120-600v-120H680v-80h200v200h-80ZM700-260h60v60h-60v-60Zm0-120h60v60h-60v-60Zm-60 60h60v60h-60v-60Zm-60 60h60v60h-60v-60Zm-60-60h60v60h-60v-60Zm120-120h60v60h-60v-60Zm-60 60h60v60h-60v-60Zm-60-60h60v60h-60v-60Zm240-320v240H520v-240h240ZM440-440v240H200v-240h240Zm0-320v240H200v-240h240Zm-60 500v-120H260v120h120Zm0-320v-120H260v120h120Zm320 0v-120H580v120h120Z\"/>",
  "wf-email": "<path d=\"M160-160q-33 0-56.5-23.5T80-240v-480q0-33 23.5-56.5T160-800h640q33 0 56.5 23.5T880-720v480q0 33-23.5 56.5T800-160H160Zm320-280L160-640v400h640v-400L480-440Zm0-80 320-200H160l320 200ZM160-640v-80 480-400Z\"/>",
  "wf-web": "<path d=\"M480-80q-82 0-155-31.5t-127.5-86Q143-252 111.5-325T80-480q0-83 31.5-155.5t86-127Q252-817 325-848.5T480-880q83 0 155.5 31.5t127 86q54.5 54.5 86 127T880-480q0 82-31.5 155t-86 127.5q-54.5 54.5-127 86T480-80Zm0-82q26-36 45-75t31-83H404q12 44 31 83t45 75Zm-104-16q-18-33-31.5-68.5T322-320H204q29 50 72.5 87t99.5 55Zm208 0q56-18 99.5-55t72.5-87H638q-9 38-22.5 73.5T584-178ZM170-400h136q-3-20-4.5-39.5T300-480q0-21 1.5-40.5T306-560H170q-5 20-7.5 39.5T160-480q0 21 2.5 40.5T170-400Zm216 0h188q3-20 4.5-39.5T580-480q0-21-1.5-40.5T574-560H386q-3 20-4.5 39.5T380-480q0 21 1.5 40.5T386-400Zm268 0h136q5-20 7.5-39.5T800-480q0-21-2.5-40.5T790-560H654q3 20 4.5 39.5T660-480q0 21-1.5 40.5T654-400Zm-16-240h118q-29-50-72.5-87T584-782q18 33 31.5 68.5T638-640Zm-234 0h152q-12-44-31-83t-45-75q-26 36-45 75t-31 83Zm-200 0h118q9-38 22.5-73.5T376-782q-56 18-99.5 55T204-640Z\"/>"
};

export const WAYFINDING_M3 = {
  "wf-arrow-up": "<line x1=\"12\" y1=\"20\" x2=\"12\" y2=\"4\"/><polyline points=\"5 11 12 4 19 11\"/>",
  "wf-arrow-right": "<line x1=\"4\" y1=\"12\" x2=\"20\" y2=\"12\"/><polyline points=\"13 5 20 12 13 19\"/>",
  "wf-arrow-down": "<line x1=\"12\" y1=\"4\" x2=\"12\" y2=\"20\"/><polyline points=\"5 13 12 20 19 13\"/>",
  "wf-arrow-left": "<line x1=\"20\" y1=\"12\" x2=\"4\" y2=\"12\"/><polyline points=\"11 5 4 12 11 19\"/>",
  "wf-arrow-up-right": "<line x1=\"6\" y1=\"18\" x2=\"18\" y2=\"6\"/><polyline points=\"9 6 18 6 18 15\"/>",
  "wf-arrow-up-left": "<line x1=\"18\" y1=\"18\" x2=\"6\" y2=\"6\"/><polyline points=\"15 6 6 6 6 15\"/>",
  "wf-u-turn": "<path d=\"M7 18V11a5 5 0 0 1 10 0v9\"/><polyline points=\"3.5 14.5 7 18 10.5 14.5\"/>",
  "wf-signpost": "<line x1=\"12\" y1=\"3\" x2=\"12\" y2=\"21\"/><path d=\"M6 5h9l3 2.5-3 2.5H6z\"/><path d=\"M18 13H9l-3 2.5 3 2.5h9z\"/>",
  "wf-pin": "<path d=\"M12 21.5c-4.2-4.5-7-8.8-7-12a7 7 0 1 1 14 0c0 3.2-2.8 7.5-7 12z\"/><circle cx=\"12\" cy=\"9.5\" r=\"2.5\"/>",
  "wf-facing": "<circle cx=\"12\" cy=\"12\" r=\"9.5\"/><polygon points=\"12 4 15 12 12 10.5 9 12\" fill=\"currentColor\" stroke=\"none\"/><circle cx=\"12\" cy=\"16.5\" r=\"1.2\" fill=\"currentColor\" stroke=\"none\"/>",
  "wf-map": "<polygon points=\"3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21\"/><line x1=\"9\" y1=\"3\" x2=\"9\" y2=\"18\"/><line x1=\"15\" y1=\"6\" x2=\"15\" y2=\"21\"/>",
  "wf-touch": "<path d=\"M12 3a9 9 0 0 1 9 9\"/><path d=\"M12 7a5 5 0 0 1 5 5\"/><path d=\"M9 14.5V8a1.5 1.5 0 0 1 3 0v6.5\"/><path d=\"M12 11.5a1.5 1.5 0 0 1 3 0V14\"/><path d=\"M15 12.5a1.5 1.5 0 0 1 3 0V15a6 6 0 0 1-6 6h-2a6 6 0 0 1-4.2-1.8L5 15.4a1.5 1.5 0 0 1 2.2-2l1.8 1.6\"/>",
  "wf-entrance": "<rect x=\"9\" y=\"3\" width=\"12\" height=\"18\" rx=\"2\"/><polyline points=\"15 3 9 5.5 9 18.5 15 21\"/><path d=\"M2 12h8\"/><polyline points=\"6.5 8.5 10 12 6.5 15.5\"/>",
  "wf-exit": "<rect x=\"3\" y=\"3\" width=\"12\" height=\"18\" rx=\"2\"/><polyline points=\"9 3 15 5.5 15 18.5 9 21\"/><path d=\"M12 12h10\"/><polyline points=\"18.5 8.5 22 12 18.5 15.5\"/>",
  "wf-lift": "<rect x=\"4\" y=\"3\" width=\"16\" height=\"18\" rx=\"2\"/><line x1=\"12\" y1=\"3\" x2=\"12\" y2=\"21\"/><polygon points=\"8 10 6 13 10 13\" fill=\"currentColor\" stroke=\"none\"/><polygon points=\"16 14 14 11 18 11\" fill=\"currentColor\" stroke=\"none\"/>",
  "wf-stairs": "<path d=\"M3 19h5v-4h5v-4h5V7h3\"/><path d=\"M5 6l4-2\"/><circle cx=\"12\" cy=\"4\" r=\"1.5\" fill=\"currentColor\" stroke=\"none\"/><path d=\"M10 8l3 3-2 4\"/>",
  "wf-escalator-up": "<rect x=\"3\" y=\"3\" width=\"18\" height=\"18\" rx=\"2\"/><path d=\"M6 17h3l6-8h3\"/><polyline points=\"13 6 18 6 18 11\"/><circle cx=\"9.5\" cy=\"7.5\" r=\"1.5\" fill=\"currentColor\" stroke=\"none\"/>",
  "wf-escalator-down": "<rect x=\"3\" y=\"3\" width=\"18\" height=\"18\" rx=\"2\"/><path d=\"M6 7h3l6 8h3\"/><polyline points=\"13 18 18 18 18 13\"/><circle cx=\"9.5\" cy=\"16.5\" r=\"1.5\" fill=\"currentColor\" stroke=\"none\"/>",
  "wf-ramp": "<path d=\"M3 19h18L3 11z\"/><circle cx=\"10\" cy=\"8\" r=\"1.5\" fill=\"currentColor\" stroke=\"none\"/><path d=\"M9 11l2 2 3-3\"/>",
  "wf-accessible": "<circle cx=\"12\" cy=\"4\" r=\"2\" fill=\"currentColor\" stroke=\"none\"/><path d=\"M9 20a5 5 0 1 0 0-10 5 5 0 0 0-1.5.2\"/><path d=\"M9 10h4l2.5 5H19\"/><path d=\"M12 14v4l3 2\"/>",
  "wf-levels": "<path d=\"M12 3L3 7.5 12 12l9-4.5L12 3z\"/><path d=\"M3 12l9 4.5 9-4.5\"/><path d=\"M3 16.5l9 4.5 9-4.5\"/>",
  "wf-no-entry": "<circle cx=\"12\" cy=\"12\" r=\"9.5\"/><line x1=\"6.5\" y1=\"12\" x2=\"17.5\" y2=\"12\" stroke-width=\"2.8\"/>",
  "wf-prohibited": "<circle cx=\"12\" cy=\"12\" r=\"9.5\"/><line x1=\"5.3\" y1=\"5.3\" x2=\"18.7\" y2=\"18.7\" stroke-width=\"2.5\"/>",
  "wf-staff-only": "<rect x=\"5\" y=\"4\" width=\"14\" height=\"17\" rx=\"2\"/><circle cx=\"12\" cy=\"10\" r=\"2.5\"/><path d=\"M8 17a4 4 0 0 1 8 0\"/><line x1=\"10\" y1=\"2\" x2=\"14\" y2=\"2\"/>",
  "wf-toilets": "<circle cx=\"7.5\" cy=\"5\" r=\"1.5\" fill=\"currentColor\" stroke=\"none\"/><path d=\"M5.5 9h4v6h-1v4h-2v-4h-1z\"/><circle cx=\"16.5\" cy=\"5\" r=\"1.5\" fill=\"currentColor\" stroke=\"none\"/><path d=\"M14 9h5l1.5 5h-2l-1 5h-2l-1-5h-2z\"/><line x1=\"12\" y1=\"3\" x2=\"12\" y2=\"21\" stroke-dasharray=\"2 2\"/>",
  "wf-toilet-male": "<circle cx=\"12\" cy=\"4.5\" r=\"2\" fill=\"currentColor\" stroke=\"none\"/><path d=\"M9 9.5h6a1 1 0 0 1 1 1v5h-2v5.5a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5V15.5H8v-5a1 1 0 0 1 1-1z\"/>",
  "wf-toilet-female": "<circle cx=\"12\" cy=\"4.5\" r=\"2\" fill=\"currentColor\" stroke=\"none\"/><path d=\"M9.5 9.5h5l2.5 6.5h-3v4.5a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5V16h-3z\"/>",
  "wf-toilet-accessible": "<circle cx=\"13\" cy=\"4.5\" r=\"2\" fill=\"currentColor\" stroke=\"none\"/><path d=\"M9.5 19.5a5 5 0 1 0 0-10 5 5 0 0 0-1.5.2\"/><path d=\"M9.5 9.5h4.5l2.5 5H20\"/><path d=\"M13 14v4l3 2\"/>",
  "wf-baby-change": "<circle cx=\"7\" cy=\"8\" r=\"1.5\" fill=\"currentColor\" stroke=\"none\"/><path d=\"M5.5 12h3l2 3h4\"/><line x1=\"3\" y1=\"19\" x2=\"21\" y2=\"19\"/><path d=\"M17 11a2.5 2.5 0 0 0-2.5-2.5H13\"/>",
  "wf-cafe": "<path d=\"M4 8h12v7a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4V8z\"/><path d=\"M16 10h2.5a2.5 2.5 0 0 1 0 5H16\"/><line x1=\"2\" y1=\"21\" x2=\"18\" y2=\"21\"/><path d=\"M7 3c0 1.5 1 2 1 3\"/><path d=\"M11 3c0 1.5 1 2 1 3\"/>",
  "wf-food": "<path d=\"M6 3v6a3 3 0 0 0 3 3v9\"/><line x1=\"6\" y1=\"3\" x2=\"6\" y2=\"9\"/><line x1=\"9\" y1=\"3\" x2=\"9\" y2=\"6\"/><path d=\"M18 3c0 4-3 5-3 9v9\"/><path d=\"M15 3h3\"/>",
  "wf-retail": "<path d=\"M6 7V5a3 3 0 0 1 3-3h6a3 3 0 0 1 3 3v2\"/><rect x=\"4\" y=\"7\" width=\"16\" height=\"14\" rx=\"2\"/><circle cx=\"12\" cy=\"13\" r=\"2\"/>",
  "wf-atm": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"16\" rx=\"2\"/><line x1=\"3\" y1=\"9\" x2=\"21\" y2=\"9\"/><line x1=\"7\" y1=\"14\" x2=\"12\" y2=\"14\"/><rect x=\"15\" y=\"13\" width=\"3\" height=\"3\" rx=\"0.5\"/>",
  "wf-payment": "<rect x=\"3\" y=\"5\" width=\"18\" height=\"14\" rx=\"2\"/><line x1=\"3\" y1=\"10\" x2=\"21\" y2=\"10\"/><circle cx=\"7.5\" cy=\"15\" r=\"1.5\" fill=\"currentColor\" stroke=\"none\"/><circle cx=\"11.5\" cy=\"15\" r=\"1.5\" fill=\"currentColor\" stroke=\"none\"/>",
  "wf-pharmacy": "<rect x=\"3\" y=\"5\" width=\"18\" height=\"15\" rx=\"3\"/><line x1=\"12\" y1=\"9\" x2=\"12\" y2=\"16\"/><line x1=\"8.5\" y1=\"12.5\" x2=\"15.5\" y2=\"12.5\"/>",
  "wf-water": "<path d=\"M5 20h14\"/><path d=\"M6 16h8a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2H9\"/><path d=\"M9 6V4\"/><path d=\"M12 12c0 1.7-1.3 3-1.3 3s-1.3-1.3-1.3-3a1.3 1.3 0 0 1 2.6 0z\" fill=\"currentColor\"/>",
  "wf-wifi": "<path d=\"M3 8a13 13 0 0 1 18 0\"/><path d=\"M6.5 12a8.5 8.5 0 0 1 11 0\"/><path d=\"M10 16a3.5 3.5 0 0 1 4 0\"/><circle cx=\"12\" cy=\"19\" r=\"1\" fill=\"currentColor\" stroke=\"none\"/>",
  "wf-seating": "<path d=\"M5 5v10a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2\"/><line x1=\"5\" y1=\"17\" x2=\"5\" y2=\"21\"/><line x1=\"19\" y1=\"17\" x2=\"19\" y2=\"21\"/><line x1=\"5\" y1=\"13\" x2=\"19\" y2=\"13\"/>",
  "wf-parking": "<rect x=\"4\" y=\"3\" width=\"16\" height=\"18\" rx=\"2\"/><path d=\"M9 17V7h4.5a3.5 3.5 0 0 1 0 7H9\"/>",
  "wf-car": "<path d=\"M5 11l2-5h10l2 5\"/><rect x=\"3\" y=\"11\" width=\"18\" height=\"7\" rx=\"2\"/><circle cx=\"7\" cy=\"16\" r=\"1.5\" fill=\"currentColor\" stroke=\"none\"/><circle cx=\"17\" cy=\"16\" r=\"1.5\" fill=\"currentColor\" stroke=\"none\"/><line x1=\"5\" y1=\"18\" x2=\"5\" y2=\"20\"/><line x1=\"19\" y1=\"18\" x2=\"19\" y2=\"20\"/>",
  "wf-bus": "<rect x=\"4\" y=\"3\" width=\"16\" height=\"15\" rx=\"3\"/><line x1=\"4\" y1=\"9\" x2=\"20\" y2=\"9\"/><circle cx=\"8\" cy=\"14.5\" r=\"1.5\" fill=\"currentColor\" stroke=\"none\"/><circle cx=\"16\" cy=\"14.5\" r=\"1.5\" fill=\"currentColor\" stroke=\"none\"/><line x1=\"6\" y1=\"18\" x2=\"6\" y2=\"21\"/><line x1=\"18\" y1=\"18\" x2=\"18\" y2=\"21\"/>",
  "wf-ev": "<rect x=\"3\" y=\"4\" width=\"12\" height=\"16\" rx=\"2\"/><polyline points=\"15 8 18 8 18 16 21 16\"/><line x1=\"19.5\" y1=\"16\" x2=\"19.5\" y2=\"18.5\"/><polygon points=\"9 8 7 12 10 12 8 16\" fill=\"currentColor\" stroke=\"none\"/>",
  "wf-info": "<circle cx=\"12\" cy=\"12\" r=\"9.5\"/><circle cx=\"12\" cy=\"7.5\" r=\"1.2\" fill=\"currentColor\" stroke=\"none\"/><line x1=\"12\" y1=\"11\" x2=\"12\" y2=\"16.5\"/><line x1=\"10.5\" y1=\"11\" x2=\"12\" y2=\"11\"/>",
  "wf-help": "<circle cx=\"12\" cy=\"12\" r=\"9.5\"/><path d=\"M9.5 9a2.5 2.5 0 0 1 5 0c0 1.5-1.5 2-2.5 2.8v1\"/><circle cx=\"12\" cy=\"16.5\" r=\"1.2\" fill=\"currentColor\" stroke=\"none\"/>",
  "wf-reception": "<circle cx=\"12\" cy=\"6\" r=\"2\" fill=\"currentColor\" stroke=\"none\"/><path d=\"M9 12a3 3 0 0 1 6 0\"/><line x1=\"3\" y1=\"15\" x2=\"21\" y2=\"15\"/><line x1=\"4\" y1=\"15\" x2=\"4\" y2=\"20\"/><line x1=\"20\" y1=\"15\" x2=\"20\" y2=\"20\"/>",
  "wf-security": "<path d=\"M12 3l8 3v6c0 5-3.5 9.5-8 10.5C7.5 21.5 4 17 4 12V6l8-3z\"/><polyline points=\"9 12 11.5 14.5 15.5 10\"/>",
  "wf-phone": "<path d=\"M5 4h3.5l1.5 3.5L8 9.5a13 13 0 0 0 6.5 6.5l2-2 3.5 1.5V19a2 2 0 0 1-2 2A17 17 0 0 1 3 6a2 2 0 0 1 2-2z\"/>",
  "wf-intercom": "<rect x=\"6\" y=\"3\" width=\"12\" height=\"18\" rx=\"2.5\"/><circle cx=\"12\" cy=\"8\" r=\"2.5\"/><line x1=\"12\" y1=\"14\" x2=\"12\" y2=\"17\"/><path d=\"M2 9a14 14 0 0 1 0 6\"/><path d=\"M22 9a14 14 0 0 0 0 6\"/>",
  "wf-hospital": "<rect x=\"4\" y=\"3\" width=\"16\" height=\"18\" rx=\"2\"/><line x1=\"12\" y1=\"7\" x2=\"12\" y2=\"13\"/><line x1=\"9\" y1=\"10\" x2=\"15\" y2=\"10\"/><rect x=\"10\" y=\"17\" width=\"4\" height=\"4\"/>",
  "wf-first-aid": "<rect x=\"3\" y=\"6\" width=\"18\" height=\"15\" rx=\"2.5\"/><path d=\"M9 6V4a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2\"/><line x1=\"12\" y1=\"10.5\" x2=\"12\" y2=\"16.5\"/><line x1=\"9\" y1=\"13.5\" x2=\"15\" y2=\"13.5\"/>",
  "wf-consult": "<circle cx=\"12\" cy=\"5\" r=\"2\" fill=\"currentColor\" stroke=\"none\"/><path d=\"M8 12a4 4 0 0 1 8 0v2H8z\"/><path d=\"M6 14v2a6 6 0 0 0 12 0v-2\"/><circle cx=\"18\" cy=\"14\" r=\"1.5\" fill=\"currentColor\" stroke=\"none\"/>",
  "wf-pathology": "<path d=\"M9 3h6\"/><line x1=\"12\" y1=\"3\" x2=\"12\" y2=\"7\"/><path d=\"M10 7L4.5 18A2 2 0 0 0 6.2 21h11.6a2 2 0 0 0 1.7-3L14 7H10z\"/><line x1=\"7.5\" y1=\"15\" x2=\"16.5\" y2=\"15\"/><circle cx=\"10\" cy=\"18\" r=\"1\" fill=\"currentColor\" stroke=\"none\"/><circle cx=\"14\" cy=\"17.5\" r=\"1\" fill=\"currentColor\" stroke=\"none\"/>",
  "wf-aed": "<path d=\"M12 21.5L4 13.5a5.5 5.5 0 0 1 0-7.8 5.5 5.5 0 0 1 7.8 0L12 6l.2-.3a5.5 5.5 0 0 1 7.8 7.8L12 21.5z\"/><polygon points=\"12.5 7 10 12 12.5 12 11.5 16 14.5 11 12 11\" fill=\"currentColor\" stroke=\"none\"/>",
  "wf-student": "<polygon points=\"12 3 2 8 12 13 22 8\"/><path d=\"M6 10.5v5c0 2.5 3 4.5 6 4.5s6-2 6-4.5v-5\"/><line x1=\"22\" y1=\"8\" x2=\"22\" y2=\"15\"/>",
  "wf-library": "<rect x=\"4\" y=\"4\" width=\"4\" height=\"16\" rx=\"1\"/><rect x=\"9.5\" y=\"4\" width=\"4\" height=\"16\" rx=\"1\"/><path d=\"M16 4.5l3.8 14.5a1 1 0 0 1-.7 1.2l-.3.1-3.8-1a1 1 0 0 1-.7-1.2L16 4.5z\"/><line x1=\"2\" y1=\"21\" x2=\"22\" y2=\"21\"/>",
  "wf-lecture": "<rect x=\"4\" y=\"3\" width=\"16\" height=\"10\" rx=\"1.5\"/><circle cx=\"12\" cy=\"17\" r=\"1.5\" fill=\"currentColor\" stroke=\"none\"/><path d=\"M9 22l3-3 3 3\"/><line x1=\"12\" y1=\"13\" x2=\"12\" y2=\"15.5\"/>",
  "wf-emergency": "<rect x=\"5\" y=\"11\" width=\"14\" height=\"9\" rx=\"2\"/><path d=\"M8 11V7a4 4 0 0 1 8 0v4\"/><line x1=\"12\" y1=\"2\" x2=\"12\" y2=\"4\"/><line x1=\"4.5\" y1=\"4.5\" x2=\"6\" y2=\"6\"/><line x1=\"19.5\" y1=\"4.5\" x2=\"18\" y2=\"6\"/>",
  "wf-evacuate": "<rect x=\"3\" y=\"3\" width=\"9\" height=\"18\" rx=\"1.5\"/><circle cx=\"17.5\" cy=\"5\" r=\"1.8\" fill=\"currentColor\" stroke=\"none\"/><path d=\"M14 9l3 2-2 4 4 3\"/><path d=\"M15 11l-3 3-3-1\"/>",
  "wf-assembly": "<polyline points=\"7 4 3 4 3 8\"/><line x1=\"3\" y1=\"4\" x2=\"8\" y2=\"9\"/><polyline points=\"17 4 21 4 21 8\"/><line x1=\"21\" y1=\"4\" x2=\"16\" y2=\"9\"/><polyline points=\"7 20 3 20 3 16\"/><line x1=\"3\" y1=\"20\" x2=\"8\" y2=\"15\"/><polyline points=\"17 20 21 20 21 16\"/><line x1=\"21\" y1=\"20\" x2=\"16\" y2=\"15\"/><circle cx=\"12\" cy=\"12\" r=\"2\" fill=\"currentColor\" stroke=\"none\"/>",
  "wf-fire": "<path d=\"M12 2c0 3.5-3 5.5-3 9a6 6 0 0 0 12 0c0-4-3-6-4-8-.5 2-1.5 3-2.5 3.5C14.5 5.5 13 3.5 12 2z\"/><path d=\"M12 13a2.5 2.5 0 0 0 2.5 2.5c0 1.5-1 2.5-2.5 2.5s-2.5-1-2.5-2.5A2.5 2.5 0 0 1 12 13z\" fill=\"currentColor\"/>",
  "wf-warning": "<path d=\"M12 3.2L2.5 19.8A1.5 1.5 0 0 0 3.8 22h16.4a1.5 1.5 0 0 0 1.3-2.2L12 3.2z\"/><line x1=\"12\" y1=\"9\" x2=\"12\" y2=\"14.5\"/><circle cx=\"12\" cy=\"18\" r=\"1.2\" fill=\"currentColor\" stroke=\"none\"/>",
  "wf-construction": "<polygon points=\"12 3 5 19 19 19\"/><line x1=\"2\" y1=\"21\" x2=\"22\" y2=\"21\"/><line x1=\"8.5\" y1=\"14\" x2=\"15.5\" y2=\"14\"/><line x1=\"10\" y1=\"10\" x2=\"14\" y2=\"10\"/>",
  "wf-home": "<path d=\"M3 10.5L12 3l9 7.5V20a1.5 1.5 0 0 1-1.5 1.5H4.5A1.5 1.5 0 0 1 3 20V10.5z\"/><path d=\"M9 21.5v-7a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v7\"/>",
  "wf-search": "<circle cx=\"11\" cy=\"11\" r=\"7\"/><line x1=\"16.5\" y1=\"16.5\" x2=\"21.5\" y2=\"21.5\"/>",
  "wf-menu": "<line x1=\"4\" y1=\"6\" x2=\"20\" y2=\"6\"/><line x1=\"4\" y1=\"12\" x2=\"20\" y2=\"12\"/><line x1=\"4\" y1=\"18\" x2=\"20\" y2=\"18\"/>",
  "wf-back": "<polyline points=\"15 19 8 12 15 5\"/>",
  "wf-close": "<line x1=\"5\" y1=\"5\" x2=\"19\" y2=\"19\"/><line x1=\"19\" y1=\"5\" x2=\"5\" y2=\"19\"/>",
  "wf-hours": "<circle cx=\"12\" cy=\"12\" r=\"9.5\"/><polyline points=\"12 7 12 12 16 14\"/>",
  "wf-timetable": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"17\" rx=\"2\"/><line x1=\"3\" y1=\"9\" x2=\"21\" y2=\"9\"/><line x1=\"8\" y1=\"2\" x2=\"8\" y2=\"5\"/><line x1=\"16\" y1=\"2\" x2=\"16\" y2=\"5\"/><line x1=\"7.5\" y1=\"14\" x2=\"10.5\" y2=\"14\"/><line x1=\"13.5\" y1=\"14\" x2=\"16.5\" y2=\"14\"/>",
  "wf-events": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"17\" rx=\"2\"/><line x1=\"3\" y1=\"9\" x2=\"21\" y2=\"9\"/><line x1=\"8\" y1=\"2\" x2=\"8\" y2=\"5\"/><line x1=\"16\" y1=\"2\" x2=\"16\" y2=\"5\"/><polygon points=\"12 11.5 13 13.8 15.5 14 13.5 15.6 14.2 18 12 16.7 9.8 18 10.5 15.6 8.5 14 11 13.8\" fill=\"currentColor\" stroke=\"none\"/>",
  "wf-news": "<rect x=\"3\" y=\"4\" width=\"18\" height=\"16\" rx=\"2\"/><line x1=\"7\" y1=\"8\" x2=\"17\" y2=\"8\"/><rect x=\"7\" y=\"11\" width=\"4\" height=\"4\" rx=\"0.5\"/><line x1=\"13\" y1=\"12\" x2=\"17\" y2=\"12\"/><line x1=\"13\" y1=\"15\" x2=\"17\" y2=\"15\"/>",
  "wf-announce": "<path d=\"M3 11v2a2 2 0 0 0 2 2h2l5 4V5L7 9H5a2 2 0 0 0-2 2z\"/><path d=\"M16 8.5a5 5 0 0 1 0 7\"/><path d=\"M19 6a9 9 0 0 1 0 12\"/>",
  "wf-share": "<circle cx=\"18\" cy=\"5\" r=\"2.5\"/><circle cx=\"6\" cy=\"12\" r=\"2.5\"/><circle cx=\"18\" cy=\"19\" r=\"2.5\"/><line x1=\"8.3\" y1=\"10.9\" x2=\"15.7\" y2=\"6.1\"/><line x1=\"8.3\" y1=\"13.1\" x2=\"15.7\" y2=\"17.9\"/>",
  "wf-chat": "<path d=\"M20 15a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h3v4l5-4h8z\"/><circle cx=\"8\" cy=\"9\" r=\"1\" fill=\"currentColor\" stroke=\"none\"/><circle cx=\"12\" cy=\"9\" r=\"1\" fill=\"currentColor\" stroke=\"none\"/><circle cx=\"16\" cy=\"9\" r=\"1\" fill=\"currentColor\" stroke=\"none\"/>",
  "wf-like": "<path d=\"M7 10v10H4a1 1 0 0 1-1-1v-8a1 1 0 0 1 1-1h3zm3 10h7a2 2 0 0 0 2-1.5l1.5-6A2 2 0 0 0 18.5 10H14V5a2 2 0 0 0-2-2l-2 7v10z\"/>",
  "wf-camera": "<path d=\"M9 4.5l1.5-2h3l1.5 2H19a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-11a2 2 0 0 1 2-2h4z\"/><circle cx=\"12\" cy=\"13\" r=\"3.5\"/><circle cx=\"18\" cy=\"8.5\" r=\"0.8\" fill=\"currentColor\" stroke=\"none\"/>",
  "wf-video": "<rect x=\"3\" y=\"5\" width=\"13\" height=\"14\" rx=\"2\"/><polygon points=\"16 10 21 6.5 21 17.5 16 14\"/>",
  "wf-qr": "<rect x=\"3\" y=\"3\" width=\"7\" height=\"7\" rx=\"1.5\"/><rect x=\"14\" y=\"3\" width=\"7\" height=\"7\" rx=\"1.5\"/><rect x=\"3\" y=\"14\" width=\"7\" height=\"7\" rx=\"1.5\"/><rect x=\"5.5\" y=\"5.5\" width=\"2\" height=\"2\" fill=\"currentColor\" stroke=\"none\"/><rect x=\"16.5\" y=\"5.5\" width=\"2\" height=\"2\" fill=\"currentColor\" stroke=\"none\"/><rect x=\"5.5\" y=\"16.5\" width=\"2\" height=\"2\" fill=\"currentColor\" stroke=\"none\"/><path d=\"M14 14h3v3h-3z\" fill=\"currentColor\" stroke=\"none\"/><path d=\"M18 18h3v3h-3z\" fill=\"currentColor\" stroke=\"none\"/><path d=\"M18 14h3v1h-3z\" fill=\"currentColor\" stroke=\"none\"/>",
  "wf-email": "<rect x=\"3\" y=\"5\" width=\"18\" height=\"14\" rx=\"2\"/><polyline points=\"3 7 12 13 21 7\"/>",
  "wf-web": "<circle cx=\"12\" cy=\"12\" r=\"9.5\"/><line x1=\"2.5\" y1=\"12\" x2=\"21.5\" y2=\"12\"/><ellipse cx=\"12\" cy=\"12\" rx=\"4.5\" ry=\"9.5\"/>"
};
