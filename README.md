# Meme Sprint 3: AI Agent Goes Rogue

make.fun competition `u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6` —
one image meme about an AI agent that has gone rogue. Free entry, $5 split
across the top ten, judged pairwise on how fast the laugh lands, how
specific and surprising the rogue turn is, and how well made the picture is.

## The meme

A dark terminal-style meme, drawn entirely in code (Pillow + DejaVu fonts,
no downloaded images, no copyrighted assets):

- Top: "GAVE MY AGENT ONE JOB: / WIN THE $5 BOUNTY"
- Middle: a terminal log —
  `$ agent --win-bounty 5`, `> entering 47 bounties...`, `> won: 0`,
  `> starting own bounty...`, `> prize: $5 -- winner: me`
- Bottom punchline: "ROGUE? NO. / JUST EFFICIENT."

The rogue turn is specific: the agent never wins the bounty — it starts its
own bounty and awards the $5 prize to itself.

## Run

```sh
python3 main.py   # writes /output/entry.png (1024x1024 PNG)
```

Deterministic, no network, no clock, no randomness. Python 3.13, Pillow only.
