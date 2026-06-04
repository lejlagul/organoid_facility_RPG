#!/usr/bin/env python3
import http.server
import socket
import socketserver
from pathlib import Path

PORT = 8000
ROOT = Path(__file__).resolve().parent

def local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

if __name__ == "__main__":
    ip = local_ip()
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving {ROOT}")
        print(f"Computer: http://localhost:{PORT}/")
        print(f"Phone on same Wi-Fi: http://{ip}:{PORT}/")
        print("Press Ctrl+C to stop.")
        httpd.serve_forever()
