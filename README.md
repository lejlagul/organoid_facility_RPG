# Organoid Quest: From Cells to Cure

A small browser-based RPG designed for an Imperial College Organoid Facility exhibition stand.

Visitors scan a QR code, open the game in their phone browser, walk through a cartoon facility, talk to experts, make organoid workflow decisions, and finish with a score for:

- Organoid health
- Reproducibility
- Translation potential

## Important QR note

The QR code must point to a **public web URL** or to a **temporary local server URL** on your laptop.

A QR code cannot reliably open a file stored only on your computer, and it cannot open ChatGPT sandbox links from visitors' phones. The original placeholder QR pointed to `https://example.org/organoid-quest/`, so it was not expected to launch the game.

## What is included

- `index.html` — the full game. No build step needed.
- `stand_sign.html` — printable stand sign template.
- `qr_placeholder.png` — non-scannable placeholder image for the sign.
- `make_final_qr_and_sign.py` — creates the real QR and a ready-to-print stand sign after hosting.
- `make_qr.py` — simple QR generator if you only need the QR image.
- `start_local_server.py` — temporary local testing option from your laptop.

## Fastest reliable option: Netlify Drop

1. Unzip this folder.
2. Go to Netlify Drop in a browser.
3. Drag the whole `organoid_quest_qr_game` folder into the page.
4. Copy the public URL Netlify gives you.
5. Run:

```bash
python3 make_final_qr_and_sign.py "https://YOUR-NETLIFY-URL.netlify.app/index.html"
```

This creates:

```bash
organoid_quest_start_qr.png
stand_sign_ready.html
```

Print `stand_sign_ready.html` or place `organoid_quest_start_qr.png` on your own poster.

## Temporary local test from your laptop

This is useful for checking the game with your phone before hosting.

```bash
python3 start_local_server.py
```

The script will:

- start a temporary web server from this folder,
- print a local network URL,
- create `qr_local_network.png`.

Open `qr_local_network.png` and scan it with a phone connected to the **same Wi-Fi** as the laptop.

Important: some university/guest Wi-Fi networks block phone-to-laptop connections. For the actual stand, public hosting is more reliable.

## How to test locally without QR

Open `index.html` directly in a browser.

Desktop controls:

- Move: arrow keys or WASD
- Talk/use: Space, Enter, or click the canvas

Phone controls:

- Use the on-screen D-pad and Talk / Use button

## Suggested stand wording

**Can you build a human organoid model in 3 minutes?**

Scan the QR code, become a new recruit in the Organoid Facility, and guide a model from clinical sample to translational decision.

## Suggested facilitation line

“Your score is not just about growing the organoid — it is about whether the model is reproducible, well-characterised, and useful for translation.”
