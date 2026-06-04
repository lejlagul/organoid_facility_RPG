#!/usr/bin/env python3
import sys
from pathlib import Path

try:
    import qrcode
    from PIL import Image, ImageDraw, ImageFont
except Exception as exc:
    print("Missing dependency. Install with: pip install qrcode[pil] pillow")
    raise

URL = sys.argv[1] if len(sys.argv) > 1 else "https://lejlagul.github.io/organoid_facility_RPG/"
ROOT = Path(__file__).resolve().parent
qr_path = ROOT / "organoid_facility_RPG_QR.png"
sign_path = ROOT / "stand_sign_ready.html"

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=18, border=4)
qr.add_data(URL)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

w, h = img.size
canvas_w = w + 190
canvas_h = h + 330
canvas = Image.new("RGB", (canvas_w, canvas_h), "white")
canvas.paste(img, ((canvas_w - w) // 2, 76))
draw = ImageDraw.Draw(canvas)
try:
    title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 56)
    sub_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 40)
    small_font = ImageFont.truetype("DejaVuSans.ttf", 24)
except Exception:
    title_font = sub_font = small_font = ImageFont.load_default()

def center(text, y, font):
    box = draw.textbbox((0, 0), text, font=font)
    draw.text(((canvas_w - (box[2]-box[0]))/2, y), text, fill="black", font=font)

center("Scan to play", 10, title_font)
center("Organoid Quest", h + 105, sub_font)
center(URL, h + 166, small_font)
canvas.save(qr_path)

sign_html = f"""<!doctype html>
<html lang='en'>
<head>
<meta charset='utf-8'>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<title>Organoid Quest Stand Sign</title>
<style>
  @page {{ size: A4; margin: 16mm; }}
  body {{ font-family: Arial, Helvetica, sans-serif; margin: 0; text-align: center; color: #111827; }}
  main {{ min-height: calc(297mm - 32mm); display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 16px; }}
  h1 {{ font-size: 46px; line-height: 1.04; margin: 0; }}
  h2 {{ font-size: 26px; margin: 0; color: #374151; }}
  img {{ width: 68%; max-width: 440px; padding: 16px; border: 1px solid #e5e7eb; border-radius: 18px; }}
  p {{ max-width: 720px; font-size: 22px; line-height: 1.35; margin: 0; }}
  .badge {{ display: inline-block; border: 2px solid #111827; border-radius: 999px; padding: 10px 18px; font-weight: bold; font-size: 18px; }}
  .url {{ font-size: 15px; color: #4b5563; overflow-wrap: anywhere; }}
</style>
</head>
<body>
<main>
  <h1>Can you choose the right gut-on-chip platform?</h1>
  <h2>Play Organoid Quest: Platform RPG</h2>
  <img src='organoid_facility_RPG_QR.png' alt='QR code to play Organoid Quest'>
  <p>Scan the QR code, collect a clinical sample, build an organoid model, and match a client question to the best gut-on-chip system.</p>
  <div class='badge'>Imperial College Organoid Facility</div>
  <p class='url'>{URL}</p>
</main>
</body>
</html>"""
sign_path.write_text(sign_html, encoding="utf-8")
print(f"Created {qr_path}")
print(f"Created {sign_path}")
