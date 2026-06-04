#!/usr/bin/env python3
"""Generate a QR code for Organoid Quest.

Use this only after the game is hosted at a public URL.

Usage:
  python3 make_qr.py "https://your-public-url/index.html"
  python3 make_qr.py "https://your-public-url/index.html" final_qr.png
"""
import sys
from pathlib import Path

try:
    import qrcode
except ImportError as exc:
    raise SystemExit("Missing dependency. Install it with: pip install qrcode[pil]") from exc

if len(sys.argv) < 2:
    raise SystemExit('Usage: python3 make_qr.py "https://your-public-url/index.html" [output.png]')

url = sys.argv[1].strip()
if not (url.startswith("https://") or url.startswith("http://")):
    raise SystemExit("Please provide a full URL beginning with https:// or http://")

out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("organoid_quest_start_qr.png")

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="#071421", back_color="white").convert("RGB")
img.save(out)
print(f"Saved QR code to {out.resolve()}")
print(f"Encoded URL: {url}")
