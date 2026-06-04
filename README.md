# Organoid Quest: Platform RPG

A QR-ready, mobile-friendly browser RPG for the Imperial College Organoid Facility stand.

## What is new in this version

- Building-based RPG layout: the player walks into the Hospital, Platform Hall, Culture Lab, Incubator Suite, Imaging/QC, Data Room and Translation Hub.
- Hospital colonoscopy sample-collection mini-game.
- Gut-on-chip platform choice system with scoring for Emulate, CN-BIO, BiomimX, MEPSGEN, HuMiX, Dynamic42 and Mimetas.
- Quick stand demo mode and optional Extended RPG mode with five client platform scenarios and less obvious trade-offs.
- Mobile-first controls: tap-to-walk, D-pad, large Talk / Use button and touch-safe canvas.
- No external game libraries or build step; the game runs as a single static `index.html` file.

## How to publish on GitHub Pages

1. Replace the files in your GitHub repository with the contents of this folder.
2. Make sure `index.html` is in the repository root.
3. Commit the changes.
4. GitHub Pages should update the existing public URL:

   `https://lejlagul.github.io/organoid_facility_RPG/`

5. The QR code remains valid as long as the URL stays the same.

## Generate or regenerate the QR code

```bash
python3 make_final_qr_and_sign.py "https://lejlagul.github.io/organoid_facility_RPG/"
```

This creates:

- `organoid_facility_RPG_QR.png`
- `stand_sign_ready.html`

## Local testing

```bash
python3 start_local_server.py
```

Then open the local URL shown in the terminal. For testing on a phone, the phone and computer need to be on the same Wi-Fi.

## Scientific note

The platform scoring is intentionally simplified for an educational stand game. It is based on public feature summaries and should not be treated as procurement advice, an experimental protocol, or a formal platform recommendation. Real platform selection should also consider access, cost, cell source, biological validation, staff training, sample constraints, timeline, IP/data requirements and the exact assay endpoint.
