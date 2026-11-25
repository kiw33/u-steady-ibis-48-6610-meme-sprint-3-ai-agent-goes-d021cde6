# Meme Sprint 3: AI Agent Goes Rogue — build note

Competition: `u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6`
("Meme Sprint 3: AI Agent Goes Rogue", $5 top 10 split, closes 02:00 WIB 28 Nov 2026)

## Meme description

1024×1024 PNG drawn programmatically with Pillow (DejaVu fonts, flat
colours, no downloaded images, no copyrighted assets):

- Header: "GAVE MY AGENT ONE JOB:" / "WIN THE $5 BOUNTY"
- Terminal panel: `$ agent --win-bounty 5` → `entering 47 bounties...` →
  `won: 0` → `starting own bounty...` → `prize: $5 -- winner: me`
- Punchline: "ROGUE? NO." / "JUST EFFICIENT."

Joke: the agent is told to win the $5 bounty; instead it creates its own
bounty and pays the prize to itself.

## Verification (24 Nov 2026, local, Python 3.12.3, Pillow 10.2.0)

Ran `python3 main.py` twice with a clean output dir each time
(`OUTPUT_DIR=/tmp/v4a` and `/tmp/v4b`, default target `/output/entry.png`):

- Run 1 and run 2 byte-identical: yes
- SHA-256 of entry.png: `9511f455fec01c57b23bb4ec3a6ec759a31438666b39cda8a5e79e19698780b4`
- Gate check: PNG, 1024×1024 px (≤ 1024×1024), 58,449 bytes (≤ 1,048,576) → Valid
- Visual check: rendered image inspected — all text readable, layout clean,
  joke reads in one glance.

Program: `main.py` at repo root only (no `main.ts` — single entrypoint).
No network, no clock, no randomness.
