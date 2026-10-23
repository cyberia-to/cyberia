#!/usr/bin/env python3
# Migration market funnel: 5.7B adults -> barriers -> nine status currencies
# -> rooting or a jurisdiction portfolio -> the nomad awareness ladder.
# Emitted on an exact character grid so every box edge and connector lands on
# the same column. Paste the output between a ```svgbob fence; optica's
# render_svgbob_blocks converts it to inline currentColor SVG.
# Keep every body line within the box inner width, and avoid ( ) in labels —
# svgbob reads parentheses as arc primitives.

class Grid:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.g = [[' '] * w for _ in range(h)]
    def put(self, x, y, s):
        for i, ch in enumerate(s):
            self.g[y][x + i] = ch
    def putc(self, x, y, ch): self.g[y][x] = ch
    def hline(self, x1, x2, y, ch='-'):
        for x in range(x1, x2 + 1):
            self.g[y][x] = '+' if self.g[y][x] in '|+' else ch
    def vline(self, y1, y2, x, ch='|'):
        for y in range(y1, y2 + 1):
            self.g[y][x] = '+' if self.g[y][x] in '-+' else ch
    def box(self, x, y, w, title=None, body=None):
        body = body or []
        has_title = title is not None
        sep = has_title and len(body) > 0
        h = 2 + (1 if has_title else 0) + (1 if sep else 0) + len(body)
        self.putc(x, y, '+'); self.putc(x+w-1, y, '+')
        self.putc(x, y+h-1, '+'); self.putc(x+w-1, y+h-1, '+')
        self.hline(x+1, x+w-2, y); self.hline(x+1, x+w-2, y+h-1)
        self.vline(y+1, y+h-2, x); self.vline(y+1, y+h-2, x+w-1)
        def place(s, row):
            self.put(x + (w - len(s)) // 2, row, s)
        row = y + 1
        if has_title:
            place(title, row); row += 1
        if sep:
            self.putc(x, row, '+'); self.putc(x+w-1, row, '+')
            self.hline(x+1, x+w-2, row); row += 1
        for line in body:
            place(line, row); row += 1
        return h
    def ctext(self, cx, y, s):
        self.put(cx - len(s) // 2, y, s)
    def a_down(self, x, y1, y2):
        self.vline(y1, y2 - 1, x); self.putc(x, y2, 'v')
    def a_right(self, y, x1, x2):
        self.hline(x1, x2 - 1, y); self.putc(x2, y, '>')
    def text(self):
        return '\n'.join(''.join(r).rstrip() for r in self.g)


G = Grid(80, 108)
FULL_X, FULL_W = 1, 78
CX = FULL_X + FULL_W // 2

# ---- top of the funnel -------------------------------------------------
G.box(FULL_X, 0, FULL_W, title="WORLD ADULTS  .  5.7B",
      body=["the settled 4.5B stay outside the funnel"])
G.a_down(CX, 5, 7)

G.box(FULL_X, 8, FULL_W, title="WANT TO LEAVE  .  ~900M  [16%]",
      body=["gap ~500  .  survival ~170  .  trajectory ~130  .  values ~100"])
G.a_down(CX, 13, 15)

# ---- aspiration x capability split ------------------------------------
G.box(1, 16, 38, title="TRAPPED  .  ~750M",
      body=["barriers: access . money . skills", "removable via corridors  -->"])
G.box(41, 16, 38, title="ABLE  .  ~150M",
      body=["aspiration x capability", "actively preparing ~25M"])
G.a_right(19, 39, 40)          # trapped -> able
G.a_down(41 + 19, 22, 24)      # able -> moving

G.box(20, 25, 40, body=["MOVING  .  ~25-35M PEOPLE / YEAR"])
G.a_down(CX, 28, 32)

# ---- nine status currencies -------------------------------------------
G.ctext(CX, 34, "NINE STATUS CURRENCIES  .  totals include dependents")

COLS = [(1, 19), (20, 19), (39, 19), (58, 20)]
row1 = [
    ("BLOOD ~1.5M", ["birth: parents,", "kids + ancestry", "cannot be bought"]),
    ("MARRIAGE ~1.8M", ["union by choice", "spouses,partners", "hence sham checks"]),
    ("SPONSOR ~0.3M", ["third party pays", "PSR, parole", "crowdfunded"]),
    ("STUDY ~2.6M", ["degree as ticket", "5-10 yr clocks", "$150B to unis"]),
]
row2 = [
    ("LABOR ~11M", ["skill: points,", "permits, shifts", "$860B remittance"]),
    ("SUFFERING ~7M", ["move; ~1M grant", "asylum, upfront", "120M stock queue"]),
    ("MONEY ~0.3M", ["capital: CBI/RBI", "investor visas", "$20-25B / yr"]),
    ("IDEOLOGY 1000s", ["conviction:", "decree 702,visas", "2024+ frontier"]),
]
for (x, w), (t, b) in zip(COLS, row1):
    G.box(x, 36, w, title=t, body=b)
for (x, w), (t, b) in zip(COLS, row2):
    G.box(x, 43, w, title=t, body=b)

G.box(15, 50, 50, title="CLUB CITIZENSHIP  .  ~4-5M / yr",
      body=["free movement: EU/EEA, ECOWAS, Mercosur,",
            "intra-GCC, EAEU  .  inherited key = Blood -1 gen"])
G.a_down(CX, 55, 57)

# ---- product ladder ----------------------------------------------------
LAD = [(1, 16, "VISA", "presence"),
       (21, 16, "RESIDENCY", "living rights"),
       (41, 16, "PR", "resident"),
       (61, 17, "PASSPORT", "rooting")]
for x, w, t, sub in LAD:
    G.box(x, 58, w, title=t, body=[sub])
G.a_right(60, 17, 20)
G.a_right(60, 37, 40)
G.a_right(60, 57, 60)
G.a_down(9, 63, 65)            # ladder -> rooting
G.a_down(69, 63, 65)          # ladder -> portfolio

# ---- rooting vs portfolio ---------------------------------------------
G.box(1, 66, 38, title="ROOTING",
      body=["~10M close a position / yr", "stock ~200M  .  exited the market"])
G.box(41, 66, 38, title="PORTFOLIO  .  the market gap",
      body=["60-80M open positions", "demand maturity: N0 --> N3"])
G.a_down(41 + 19, 72, 74)

G.box(41, 75, 38, title="+ MOBILE RESERVE",
      body=["able, not yet willing . buys options", "shock -> a wave in weeks [2022 case]"])
G.a_down(CX, 81, 83)

# ---- nomad awareness ladder -------------------------------------------
G.ctext(CX, 85, "NOMAD SEGMENT  .  AWARENESS LADDER")
NOM = [(1, 18, "N0 ASLEEP ~28M", ["visa = routine", "status: no Q", "woken by shock"]),
       (21, 18, "N1 HURTING ~8M", ["risk seen now", "banking, taxes", "risk: false exit"]),
       (41, 18, "N2 SEEKING ~2-3M", ["wants multi-jur", "market = junk", "no product/name"]),
       (61, 18, "N3 BUILD ~0.3M", ["no-presence port", "hand-assembled", "owns the method"])]
for x, w, t, b in NOM:
    G.box(x, 87, w, title=t, body=b)
G.a_right(90, 19, 20)
G.a_right(90, 39, 40)
G.a_right(90, 59, 60)
G.ctext(9, 94, "lever: shocks")
G.ctext(29, 94, "lever: content")
G.ctext(49, 94, "lever: method")
G.ctext(69, 94, "source of method")

# ---- money trail footer -----------------------------------------------
G.box(1, 96, 78, title="MONEY TRAIL",
      body=["remittances $860B  .  universities $150-200B  .  CBI/RBI $20-25B",
            "smuggling $10B  .  sponsorship $2-5B crowdfunded",
            "flow: labor 11 . study 2.6 . blood+marriage 3.3 . suffering 7",
            ". club 4.5 . money 0.3 . irregular 2.5 . nomad churn 2.5  =  25-35M"])

print(G.text())
