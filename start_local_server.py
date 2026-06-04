#!/usr/bin/env python3
"""Start a temporary local web server and generate a QR for phones on the same Wi-Fi.

Run from inside the game folder:
  python3 start_local_server.py

Then open qr_local_network.png and scan it from a phone on the same Wi-Fi.
"""
import os
import socket
import sys
from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

PORT = 8000


def get_lan_ip() -> str:
    """Best-effort LAN IP detection."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(("8.8.8.8", 80))
        return sock.getsockname()[0]
    except Exception:
        try:
            return socket.gethostbyname(socket.gethostname())
        except Exception:
            return "127.0.0.1"
    finally:
        sock.close()


def make_qr(url: str, out: Path) -> None:
    try:
        import qrcode
    except ImportError:
        print("QR package is missing. Install it with: pip install qrcode[pil]")
        print(f"You can still open the game at: {url}")
        return
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=12,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#071421", back_color="white").convert("RGB")
    img.save(out)
    print(f"Saved phone QR: {out.resolve()}")


if not Path("index.html").exists():
    raise SystemExit("Please run this script from inside the organoid_quest_qr_game folder, where index.html is located.")

ip = get_lan_ip()
url = f"http://{ip}:{PORT}/index.html"
make_qr(url, Path("qr_local_network.png"))

print("\nTemporary local server is running.")
print(f"Laptop URL: http://localhost:{PORT}/index.html")
print(f"Phone URL:  {url}")
print("\nFor phone scanning, laptop and phone must be on the same Wi-Fi.")
print("Some institutional/guest Wi-Fi networks block this. Public hosting is best for the real stand.")
print("Press Ctrl+C to stop the server.\n")

server = ThreadingHTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
