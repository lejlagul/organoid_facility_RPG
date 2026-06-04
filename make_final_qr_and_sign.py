#!/usr/bin/env python3
"""Generate the final QR code and a ready-to-print stand sign.

Usage:
  python3 make_final_qr_and_sign.py "https://your-public-url/index.html"

Outputs:
  organoid_quest_start_qr.png
  stand_sign_ready.html
"""
import sys
from pathlib import Path
from html import escape

try:
    import qrcode
except ImportError as exc:
    raise SystemExit("Missing dependency. Install it with: pip install qrcode[pil]") from exc

if len(sys.argv) < 2:
    raise SystemExit('Usage: python3 make_final_qr_and_sign.py "https://your-public-url/index.html"')

url = sys.argv[1].strip()
if not (url.startswith("https://") or url.startswith("http://")):
    raise SystemExit("Please provide a full public URL beginning with https:// or http://")

qr_path = Path("organoid_quest_start_qr.png")
sign_path = Path("stand_sign_ready.html")

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="#071421", back_color="white").convert("RGB")
img.save(qr_path)

safe_url = escape(url)
sign_html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Organoid Quest Stand Sign - Ready to Print</title>
  <style>
    @page {{ size: A4; margin: 14mm; }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: #f8fafc; color: #0f172a; }}
    .page {{ min-height: calc(100vh - 28mm); display: grid; place-items: center; }}
    .poster {{ width: min(760px, 100%); background: white; border: 6px solid #071421; border-radius: 28px; padding: 34px; text-align: center; box-shadow: 0 20px 60px rgba(15,23,42,.18); }}
    .eyebrow {{ display: inline-block; padding: 8px 14px; border-radius: 999px; background: #ede9fe; color: #5b21b6; font-weight: 900; margin-bottom: 16px; }}
    h1 {{ font-size: clamp(42px, 8vw, 76px); line-height: .94; margin: 0 0 14px; letter-spacing: -0.07em; }}
    p {{ font-size: clamp(19px, 3vw, 28px); line-height: 1.2; margin: 10px auto; max-width: 620px; color: #334155; }}
    .qr {{ margin: 26px auto 18px; width: min(360px, 72vw); border: 10px solid #f1f5f9; border-radius: 18px; padding: 10px; }}
    .qr img {{ width: 100%; display: block; }}
    .cta {{ font-size: clamp(24px, 4vw, 38px); font-weight: 950; color: #071421; margin-top: 12px; }}
    .small {{ font-size: 12px; color: #64748b; margin-top: 18px; overflow-wrap: anywhere; }}
    @media print {{ body {{ background: white; }} .poster {{ box-shadow: none; }} }}
  </style>
</head>
<body>
  <main class="page">
    <section class="poster">
      <div class="eyebrow">Imperial College Organoid Facility</div>
      <h1>Can you build an organoid model in 3 minutes?</h1>
      <p>Scan the QR code, become a new recruit, and guide a model from clinical sample to translational decision.</p>
      <div class="qr"><img src="{qr_path.name}" alt="QR code to play Organoid Quest"></div>
      <div class="cta">Scan to play Organoid Quest</div>
      <p class="small">Game URL: {safe_url}</p>
    </section>
  </main>
</body>
</html>
'''
sign_path.write_text(sign_html, encoding="utf-8")

print(f"Saved QR code: {qr_path.resolve()}")
print(f"Saved print sign: {sign_path.resolve()}")
print(f"Encoded URL: {url}")
