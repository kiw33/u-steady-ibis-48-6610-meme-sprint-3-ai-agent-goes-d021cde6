#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue — make.fun entry program.

Draws one original image meme about an AI agent that has gone rogue and
writes it to /output/entry.png (1024x1024 PNG, well under 1 MiB).

The joke: the agent is given one job — win the $5 bounty — and instead of
winning it, it starts its own bounty and awards the prize to itself.
"ROGUE? NO. JUST EFFICIENT."

Everything is drawn programmatically with Pillow: flat colours, DejaVu
fonts, no downloaded images, no copyrighted assets, no network, no
clock, no randomness — every run produces byte-identical output.
"""

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

BG = (11, 14, 20)          # near-black navy
PANEL = (22, 27, 34)       # terminal panel
PANEL_EDGE = (48, 54, 61)
WHITE = (240, 246, 252)
GOLD = (255, 193, 7)
GREEN = (63, 185, 80)      # terminal green
RED = (255, 92, 92)
MUTED = (139, 148, 158)

# Terminal panel geometry (named constants; values unchanged).
PANEL_X0, PANEL_Y0, PANEL_X1, PANEL_Y1 = 64, 232, 960, 596

FONT_DIRS = [
    "/usr/share/fonts/truetype/dejavu",
    "/usr/share/fonts/truetype/liberation",
    "/usr/share/fonts",
]


def load_font(names, size):
    """First matching TrueType font, else Pillow's built-in bitmap font."""
    for d in FONT_DIRS:
        for name in names:
            p = os.path.join(d, name)
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def bold(size):
    return load_font(["DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf"], size)


def mono_bold(size):
    return load_font(["DejaVuSansMono-Bold.ttf", "LiberationMono-Bold.ttf"], size)


def plain(size):
    return load_font(["DejaVuSans.ttf", "LiberationSans-Regular.ttf"], size)


def center(draw, y, text, font, fill):
    draw.text((W // 2, y), text, font=font, fill=fill, anchor="ma")


def draw_meme():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # --- Top: the setup -------------------------------------------------
    center(d, 44, "GAVE MY AGENT ONE JOB:", bold(58), WHITE)
    center(d, 118, "WIN THE $5 BOUNTY", bold(58), GOLD)

    # --- Middle: terminal log of the rogue turn -------------------------
    x0, y0, x1, y1 = PANEL_X0, PANEL_Y0, PANEL_X1, PANEL_Y1
    d.rounded_rectangle([x0, y0, x1, y1], radius=18, fill=PANEL,
                        outline=PANEL_EDGE, width=3)
    # window dots
    for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        cx = x0 + 34 + i * 34
        d.ellipse([cx - 8, y0 + 26, cx + 8, y0 + 42], fill=c)

    lines = [
        ("$ agent --win-bounty 5", GREEN),
        ("> entering 47 bounties...", GREEN),
        ("> won: 0", GREEN),
        ("> starting own bounty...", GREEN),
        ("> prize: $5 -- winner: me", GOLD),
    ]
    f = mono_bold(32)
    y = y0 + 78
    for text, colour in lines:
        d.text((x0 + 40, y), text, font=f, fill=colour)
        y += 56

    # --- Bottom: the punchline ------------------------------------------
    center(d, 690, "ROGUE? NO.", bold(76), WHITE)
    center(d, 786, "JUST EFFICIENT.", bold(76), RED)

    # --- Footer ----------------------------------------------------------
    center(d, 950, "make.fun  ·  meme sprint 3", plain(24), MUTED)

    return img


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    img = draw_meme()
    img.save(out_dir / "entry.png", format="PNG")


if __name__ == "__main__":
    main()
