"""Pixel art + product renderings for The Stage Robot Company.

Everything here is generated — the robot, the wordmark, the avatars, the
hardware "renders". Edit the maps below, re-run build.py, repeat until evil.
"""

# ---------------------------------------------------------------- palette
PAL = {
    "K": "#14122B",  # outline — Backstage Black
    "M": "#D4D5E6",  # metal — Chrome Ambition
    "m": "#8F91AB",  # metal shade — Gaffer Grey
    "D": "#0B0A18",  # visor
    "R": "#FF1E3C",  # Evil Eye Red
    "r": "#FF9AA8",  # eye glint
    "Y": "#FFC23D",  # comedy — Matinee Gold
    "V": "#8B5CF6",  # tragedy — Synthetic Violet
    "k": "#14122B",  # mask features
    "C": "#22D3EE",  # Haze Cyan
    "P": "#8B5CF6",
    # avatar extras
    "S": "#E8B894",  # skin
    "s": "#C98E6A",  # skin shade
    "H": "#2A2438",  # hair / hat
    "h": "#4A3F5C",
    "B": "#3A2A1E",  # beard
    "O": "#FF7A1A",  # suit orange (definitely not a hazard suit)
    "o": "#C2560A",
    "W": "#F4F4FA",  # coat / shirt
    "G": "#1E1B33",  # glasses / shades
    "X": "#000000",  # redaction
}

ROBOT = [
    ".......RR...............",
    ".......mm...............",
    ".......mm...............",
    "..KKKKKKKKKKKK..YYYY....",
    "..KMMMMMMMMMmK.YYYYYY...",
    "..KMDDDDDDDDmK.YkYYkY...",
    ".mKMDrRDDrRDmKmYYYYYYVV.",
    ".mKMDRRDDRRDmKmkYYYYkVVV",
    "..KMDDDDDDDDmK.YkkkkYVkV",
    "..KMMMMMMMMMmK..YYYYVVVV",
    "..KMMKMKMKMMmK.MM.VVkkVV",
    "..KmmmmmmmmmmK.mm.VkVVkV",
    "..KKKKKKKKKKKK.mm..VVVV.",
    "......mmmm.....mm.......",
    ".KKKKKKKKKKKKKKmm.......",
    "mKMMMMMMMMMMMmKm........",
    "mKMDDDDDDMMMMmK.........",
    "mKMDCDPDCMRRMmK.........",
    "mKMDDDDDDMRRMmK.........",
    ".KMMMMMMMMMMMmK.........",
    ".KmmmmmmmmmmmmK.........",
    ".KKKKKKKKKKKKKK.........",
    "...mmm....mmm...........",
    "..KKKK...KKKK...........",
]

AVATAR_ALAN = [  # face deliberately unavailable
    "....HHHHHHHH....",
    "....HhhhhhhH....",
    "..HHHHHHHHHHHH..",
    "..HHHHHHHHHHHH..",
    "....SSSSSSSS....",
    "...SSSSSSSSSS...",
    "...GGGGGGGGGG...",
    "...SGGGSSGGGS...",
    "...SSSSSSSSSS...",
    "...SSSSssSSSS...",
    "....SSSSSSSS....",
    ".....SsssSS.....",
    "......SSSS......",
    "...HHHWWWWHHH...",
    "..HHHHHWWHHHHH..",
    ".HHHHHHWWHHHHHH.",
]

AVATAR_MARKO = [
    "....HHHHHHHH....",
    "...HHHHHHHHHH...",
    "...HSSSSSSSSH...",
    "...SSSSSSSSSS...",
    "..SGGGGSSGGGGS..",
    "..SGWWGGGGWWGS..",
    "..SGGGGSSGGGGS..",
    "...SSSSssSSSS...",
    "...BSSSSSSSSB...",
    "...BBBBBBBBBB...",
    "...BBBSSSSBBB...",
    "....BBBBBBBB....",
    "......SSSS......",
    "...OOOWWWWOOO...",
    "..OOOoOWWOoOOO..",
    ".OOOOOoOOoOOOOO.",
]

AVATAR_GHOST = [  # team member 3 — pending generation
    "................",
    "......CCCC......",
    "....CC....CC....",
    "...C........C...",
    "...C..C..C..C...",
    "...C........C...",
    "...C..CCCC..C...",
    "....C......C....",
    ".....CCCCCC.....",
    "................",
    "...C.C.C.C.C.C..",
    "..C...........C.",
    "................",
    ".C.............C",
    "................",
    "C.C.C.C.C.C.C.C.",
]

# 5x7 pixel font — only the letters the brand can afford
FONT = {
    "A": [".###.", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "B": ["####.", "#...#", "#...#", "####.", "#...#", "#...#", "####."],
    "C": [".###.", "#...#", "#....", "#....", "#....", "#...#", ".###."],
    "E": ["#####", "#....", "#....", "####.", "#....", "#....", "#####"],
    "G": [".###.", "#...#", "#....", "#.###", "#...#", "#...#", ".###."],
    "H": ["#...#", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "M": ["#...#", "##.##", "#.#.#", "#.#.#", "#...#", "#...#", "#...#"],
    "N": ["#...#", "##..#", "#.#.#", "#..##", "#...#", "#...#", "#...#"],
    "O": [".###.", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    "P": ["####.", "#...#", "#...#", "####.", "#....", "#....", "#...."],
    "R": ["####.", "#...#", "#...#", "####.", "#.#..", "#..#.", "#...#"],
    "S": [".###.", "#...#", "#....", ".###.", "....#", "#...#", ".###."],
    "T": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."],
    "Y": ["#...#", "#...#", ".#.#.", "..#..", "..#..", "..#..", "..#.."],
    " ": [".....", ".....", ".....", ".....", ".....", ".....", "....."],
}


# ---------------------------------------------------------------- helpers
def runs(grid, keys=None):
    """Yield (row, col, length, key) horizontal runs of identical pixels."""
    for y, row in enumerate(grid):
        x = 0
        while x < len(row):
            ch = row[x]
            if ch == "." or (keys is not None and ch not in keys):
                x += 1
                continue
            n = 1
            while x + n < len(row) and row[x + n] == ch:
                n += 1
            yield y, x, n, ch
            x += n


def pixels(grid, cell, ox=0, oy=0, keys=None, color=None, skip=""):
    out = []
    for y, x, n, ch in runs(grid, keys):
        if ch in skip:
            continue
        fill = color(ch) if callable(color) else (color or PAL[ch])
        out.append(
            f'<rect x="{ox + x * cell:g}" y="{oy + y * cell:g}" '
            f'width="{n * cell:g}" height="{cell:g}" fill="{fill}"/>'
        )
    return "".join(out)


def robot_svg_body(cell=10, ox=0, oy=0, mono=None, uid="r"):
    """Robot mark. Eyes live in their own group so they can blink/track."""
    body_color = (lambda ch: mono) if mono else None
    body = pixels(ROBOT, cell, ox, oy, color=body_color, skip="Rr" if not mono else "Rr")
    eye_grid = [row if i in (6, 7) else "." * len(row) for i, row in enumerate(ROBOT)]
    antenna = [row if i not in (6, 7) else "." * len(row) for i, row in enumerate(ROBOT)]
    eyes = pixels(eye_grid, cell, ox, oy, keys="Rr")
    bulb = pixels(antenna, cell, ox, oy, keys="R")
    glow = pixels(eye_grid, cell, ox, oy, keys="Rr", color="#FF1E3C")
    return (
        f'<defs><filter id="{uid}-glow" x="-50%" y="-50%" width="200%" height="200%">'
        f'<feGaussianBlur stdDeviation="{cell * 0.9:g}"/></filter></defs>'
        f'<g class="sr-body">{body}</g>'
        f'<g class="sr-bulb">{bulb}</g>'
        f'<g class="sr-eyes-wrap"><g class="sr-glow" filter="url(#{uid}-glow)" opacity=".85">{glow}</g>'
        f'<g class="sr-eyes">{eyes}</g></g>'
    )


def robot_mark(cell=10, mono=None, uid="r", cls="", bg=None, pad=0):
    size = 24 * cell
    vb = f"{-pad} {-pad} {size + 2 * pad} {size + 2 * pad}"
    bgrect = f'<rect x="{-pad}" y="{-pad}" width="{size + 2 * pad}" height="{size + 2 * pad}" rx="{pad * 1.4:g}" fill="{bg}"/>' if bg else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" class="{cls}" '
        f'shape-rendering="crispEdges" role="img" aria-label="StageRobot pixel robot holding comedy and tragedy masks">'
        f"{bgrect}{robot_svg_body(cell, mono=mono, uid=uid)}</svg>"
    )


def text_pixels(text, cell, ox, oy, fill, gap=1):
    out, x = [], ox
    for ch in text:
        glyph = FONT[ch]
        grid = [row.replace("#", "Z") for row in glyph]
        out.append(pixels(grid, cell, x, oy, color=fill))
        x += (len(glyph[0]) + gap) * cell
    return "".join(out), x - gap * cell


def text_width(text, cell, gap=1):
    return (len(text) * (5 + gap) - gap) * cell


def wordmark(cell, ox, oy, ink, uid, grad=True, sub=True, sub_ink=None, sub_color=None):
    """'STAGEROBOT' pixel wordmark + optional 'THE STAGE ROBOT COMPANY' line."""
    w = text_width("STAGEROBOT", cell)
    stage, x2 = text_pixels("STAGE", cell, ox, oy, ink)
    fill = f"url(#{uid}-wm)" if grad else ink
    robot, _ = text_pixels("ROBOT", cell, x2 + cell, oy, fill)
    defs = (
        f'<linearGradient id="{uid}-wm" gradientUnits="userSpaceOnUse" x1="{x2:g}" y1="0" x2="{ox + w:g}" y2="0">'
        f'<stop offset="0" stop-color="#8B5CF6"/><stop offset="1" stop-color="#22D3EE"/></linearGradient>'
    )
    out = stage + robot
    h = 7 * cell
    if sub:
        line = "THE STAGE ROBOT COMPANY"
        sc = w / text_width(line, 1)
        s, _ = text_pixels(line, sc, ox, oy + h + cell * 2.2, sub_color or sub_ink or ink)
        out += f'<g opacity=".72">{s}</g>'
        h += cell * 2.2 + 7 * sc
    return defs, out, w, h


def lockup_horizontal(ink="#F4F3FF", uid="lh", mono=None, sub=True, cls="", current=False, wm_cell=11):
    mark_cell = 10
    mark = robot_svg_body(mark_cell, mono=mono, uid=uid)
    ink_fill = "currentColor" if current else ink
    defs, wm, w, h = wordmark(wm_cell, 280, 0, ink_fill, uid, grad=mono is None, sub=sub)
    # vertically centre wordmark on the robot's head-ish
    oy = (240 - h) / 2 - 6
    W = 280 + w + 4
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:g} 240" class="{cls}" '
        f'shape-rendering="crispEdges" role="img" aria-label="StageRobot — The Stage Robot Company">'
        f"<defs>{defs}</defs>{mark}<g transform=\"translate(0 {oy:g})\">{wm}</g></svg>"
    )


def lockup_stacked(ink="#F4F3FF", uid="ls", mono=None):
    wm_cell = 8
    w = text_width("STAGEROBOT", wm_cell)
    W = max(w, 240) + 40
    mx = (W - 240) / 2
    defs, wm, _, h = wordmark(wm_cell, (W - w) / 2, 272, ink, uid, grad=mono is None)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:g} {272 + h + 8:g}" '
        f'shape-rendering="crispEdges" role="img" aria-label="StageRobot — The Stage Robot Company">'
        f'<defs>{defs}</defs><g transform="translate({mx:g} 0)">{robot_svg_body(10, mono=mono, uid=uid)}</g>{wm}</svg>'
    )


def favicon(bg="#0B0A18"):
    # head only, cropped square
    head = [row[:15] for row in ROBOT[:13]]
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="-5 -20 170 170" shape-rendering="crispEdges">'
        f'<rect x="-5" y="-20" width="170" height="170" rx="34" fill="{bg}"/>'
        f"{pixels(head, 10)}</svg>"
    )


def avatar(grid, bg, label):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" shape-rendering="crispEdges" role="img" aria-label="{label}">'
        f'<rect width="160" height="160" fill="{bg}"/>{pixels(grid, 10)}</svg>'
    )


# ---------------------------------------------------------------- hardware renders
DEFS_METAL = """
<linearGradient id="front" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#3B3A4A"/><stop offset=".08" stop-color="#2A2936"/>
  <stop offset=".6" stop-color="#1C1B26"/><stop offset="1" stop-color="#121119"/></linearGradient>
<linearGradient id="top" x1="0" y1="1" x2=".3" y2="0">
  <stop offset="0" stop-color="#4A4958"/><stop offset=".5" stop-color="#33323F"/><stop offset="1" stop-color="#262531"/></linearGradient>
<linearGradient id="side" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0" stop-color="#1A1922"/><stop offset="1" stop-color="#0C0B12"/></linearGradient>
<linearGradient id="ear" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="#55546A"/><stop offset=".5" stop-color="#3A3948"/><stop offset="1" stop-color="#2A2936"/></linearGradient>
<radialGradient id="chrome" cx=".35" cy=".3" r=".8">
  <stop offset="0" stop-color="#F2F2F8"/><stop offset=".45" stop-color="#A9A9B8"/><stop offset="1" stop-color="#4B4B5A"/></radialGradient>
<radialGradient id="socket" cx=".5" cy=".4" r=".6">
  <stop offset="0" stop-color="#2B2A36"/><stop offset="1" stop-color="#07070B"/></radialGradient>
<linearGradient id="knob" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0" stop-color="#6B6A80"/><stop offset="1" stop-color="#1B1A24"/></linearGradient>
<linearGradient id="sheen" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".07"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<pattern id="brush" width="6" height="2" patternUnits="userSpaceOnUse">
  <rect width="6" height="1" fill="#fff" opacity=".018"/></pattern>
<filter id="led" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="3.2"/></filter>
<filter id="shadow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="14"/></filter>
<radialGradient id="grad-bg" cx=".5" cy=".55" r=".6">
  <stop offset="0" stop-color="#8B5CF6" stop-opacity=".22"/><stop offset=".6" stop-color="#22D3EE" stop-opacity=".05"/><stop offset="1" stop-color="#22D3EE" stop-opacity="0"/></radialGradient>
"""

MONO = "font-family=\"'JetBrains Mono', ui-monospace, Menlo, monospace\""

# front face geometry (half-rack, 1U — 8.5in x 1.75in, give or take a dream)
FX, FY, FW, FH = 110, 190, 560, 118
DX, DY = 118, -86


def chassis(title):
    x0, y0, x1, y1 = FX, FY, FX + FW, FY + FH
    top = f"{x0},{y0} {x1},{y0} {x1 + DX},{y0 + DY} {x0 + DX},{y0 + DY}"
    side = f"{x1},{y0} {x1 + DX},{y0 + DY} {x1 + DX},{y1 + DY} {x1},{y1}"
    vents = "".join(
        f'<line x1="{x0 + 180 + i * 14 + 0.6 * DX:g}" y1="{y0 + 0.6 * DY + 8:g}" x2="{x0 + 180 + i * 14 + 0.6 * DX + 20:g}" y2="{y0 + 0.6 * DY - 8:g}" stroke="#15141C" stroke-width="4" stroke-linecap="round"/>'
        for i in range(14)
    )
    ear = (
        f'<path d="M{x0 - 52},{y0} h52 v{FH} h-52 z" fill="url(#ear)"/>'
        f'<path d="M{x0 - 52},{y0} l10,-7 h42 v7 z" fill="#5E5D72"/>'
        f'<rect x="{x0 - 38}" y="{y0 + 16}" width="22" height="12" rx="6" fill="#0B0A10"/>'
        f'<rect x="{x0 - 38}" y="{y1 - 28}" width="22" height="12" rx="6" fill="#0B0A10"/>'
    )
    return (
        f'<ellipse cx="{x0 + FW / 2 + 40}" cy="{y1 + 20}" rx="{FW / 2 + 80}" ry="22" fill="#000" opacity=".55" filter="url(#shadow)"/>'
        f'<polygon points="{top}" fill="url(#top)"/>{vents}'
        f'<polygon points="{side}" fill="url(#side)"/>'
        f'<rect x="{x0}" y="{y0}" width="{FW}" height="{FH}" fill="url(#front)"/>'
        f'<rect x="{x0}" y="{y0}" width="{FW}" height="{FH}" fill="url(#brush)"/>'
        f'<rect x="{x0}" y="{y0}" width="{FW}" height="{FH}" fill="url(#sheen)"/>'
        f'<line x1="{x0}" y1="{y0 + 0.5}" x2="{x1}" y2="{y0 + 0.5}" stroke="#77768E" stroke-width="1.2"/>'
        f'<line x1="{x1 + 0.5}" y1="{y0}" x2="{x1 + DX + 0.5}" y2="{y0 + DY}" stroke="#5A596E" stroke-width="1"/>'
        f"{ear}"
    )


def led(x, y, color, label=None, r=4.2, label_dy=15):
    lab = f'<text x="{x}" y="{y + label_dy}" {MONO} font-size="7.5" fill="#A6A5BE" text-anchor="middle" letter-spacing=".5">{label}</text>' if label else ""
    return (
        f'<circle cx="{x}" cy="{y}" r="{r * 2.2}" fill="{color}" opacity=".7" filter="url(#led)"/>'
        f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/><circle cx="{x - r * .35}" cy="{y - r * .35}" r="{r * .35}" fill="#fff" opacity=".7"/>{lab}'
    )


def ethercon(x, y, label):
    return (
        f'<circle cx="{x}" cy="{y}" r="27" fill="url(#chrome)"/>'
        f'<circle cx="{x}" cy="{y}" r="21" fill="url(#socket)"/>'
        f'<rect x="{x - 9}" y="{y - 7}" width="18" height="14" rx="1.5" fill="#050508" stroke="#3B3A4A"/>'
        f'<rect x="{x - 3.5}" y="{y + 7}" width="7" height="4" fill="#050508"/>'
        f'<rect x="{x - 7}" y="{y - 5}" width="14" height="2" fill="#C9A227" opacity=".8"/>'
        f'<rect x="{x - 4}" y="{y - 31}" width="8" height="6" rx="1" fill="#8A8A9C"/>'
        f'<text x="{x}" y="{y + 44}" {MONO} font-size="8" fill="#C9C8DD" text-anchor="middle" letter-spacing=".8">{label}</text>'
    )


def xlr5(x, y, label):
    import math
    holes = "".join(
        f'<circle cx="{x + 10 * math.cos(math.radians(a)):.2f}" cy="{y + 10 * math.sin(math.radians(a)):.2f}" r="2.4" fill="#000" stroke="#4A4A5C" stroke-width=".6"/>'
        for a in (160, 115, 65, 20)
    ) + f'<circle cx="{x}" cy="{y + 6}" r="2.4" fill="#000" stroke="#4A4A5C" stroke-width=".6"/>'
    return (
        f'<circle cx="{x}" cy="{y}" r="25" fill="url(#chrome)"/>'
        f'<circle cx="{x}" cy="{y}" r="19" fill="url(#socket)"/>'
        f'<circle cx="{x}" cy="{y}" r="16" fill="#1A1922"/>{holes}'
        f'<rect x="{x - 5}" y="{y - 30}" width="10" height="8" rx="2" fill="#DAD9E6"/>'
        f'<text x="{x - 3.5}" y="{y - 23.5}" {MONO} font-size="6" fill="#222">PUSH</text>'
        f'<text x="{x}" y="{y + 42}" {MONO} font-size="8" fill="#C9C8DD" text-anchor="middle" letter-spacing=".8">{label}</text>'
    )


def brand_block(x, y, product):
    mini = pixels(ROBOT, 1.6, x, y, skip="")
    return (
        f"<g shape-rendering='crispEdges'>{mini}</g>"
        f'<text x="{x + 46}" y="{y + 14}" {MONO} font-size="9.5" font-weight="700" fill="#EDECF8" letter-spacing="1.2">STAGEROBOT</text>'
        f'<text x="{x + 46}" y="{y + 28}" {MONO} font-size="8" fill="#8F8EA8" letter-spacing="1">{product}</text>'
    )


def render_gateway():
    x0, y0 = FX, FY
    cy = y0 + FH / 2
    oled = (
        f'<rect x="{x0 + 200}" y="{y0 + 24}" width="150" height="62" rx="4" fill="#030306" stroke="#2F2E3C" stroke-width="2"/>'
        f'<text x="{x0 + 210}" y="{y0 + 42}" {MONO} font-size="10" fill="#22D3EE">sACN ▸ NDI</text>'
        f'<text x="{x0 + 210}" y="{y0 + 58}" {MONO} font-size="10" fill="#22D3EE">U 48,790 ● LIVE</text>'
        f'<text x="{x0 + 210}" y="{y0 + 74}" {MONO} font-size="10" fill="#22D3EE" opacity=".6">PRI 100  4K60</text>'
    )
    knob = (
        f'<circle cx="{x0 + 390}" cy="{cy - 4}" r="21" fill="#0A0A0F"/>'
        f'<circle cx="{x0 + 390}" cy="{cy - 4}" r="17" fill="url(#knob)"/>'
        f'<line x1="{x0 + 390}" y1="{cy - 19}" x2="{x0 + 390}" y2="{cy - 9}" stroke="#EDECF8" stroke-width="2.4" stroke-linecap="round"/>'
        f'<text x="{x0 + 390}" y="{cy + 34}" {MONO} font-size="7.5" fill="#A6A5BE" text-anchor="middle">SELECT</text>'
    )
    leds = (
        led(x0 + 436, y0 + 30, "#22E08A", "PWR")
        + led(x0 + 466, y0 + 30, "#22D3EE", "sACN")
        + led(x0 + 436, y0 + 72, "#8B5CF6", "NDI")
        + led(x0 + 466, y0 + 72, "#FF1E3C", "EVIL")
    )
    body = chassis("gateway") + brand_block(x0 + 18, y0 + 30, "UNICORE GATEWAY") + oled + knob + leds
    body += f'<text x="{x0 + 18}" y="{y0 + FH - 16}" {MONO} font-size="7" fill="#6E6D86" letter-spacing=".6">½-RACK · 1U · sACN/E1.31 → NDI® · MODEL UG-1</text>'
    return svg_wrap(body, "Unicore Gateway half-rack sACN to NDI interface, three-quarter view")


def render_node():
    x0, y0 = FX, FY
    cy = y0 + FH / 2 - 6
    ports = "".join(xlr5(x0 + 190 + i * 66, cy, f"DMX {c}") for i, c in enumerate("ABCD"))
    port_leds = "".join(led(x0 + 190 + i * 66 + 28, y0 + 14, "#22E08A", r=2.8) for i in range(4))
    body = chassis("node") + brand_block(x0 + 18, y0 + 30, "UNICORE NODE") + ports + port_leds
    body += ethercon(x0 + 488, cy, "NDI · PoE")
    body += led(x0 + 536, y0 + 30, "#8B5CF6", "NDI", r=3.4) + led(x0 + 536, y0 + 72, "#FF1E3C", "EVIL", r=3.4)
    body += f'<text x="{x0 + 18}" y="{y0 + FH - 16}" {MONO} font-size="7" fill="#6E6D86" letter-spacing=".6">½-RACK · 1U · NDI® → 4× DMX512-A · MODEL UN-4</text>'
    return svg_wrap(body, "Unicore Node half-rack NDI to four-port DMX node, three-quarter view")


def svg_wrap(body, label, vb="0 0 820 400"):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}">'
        f"<defs>{DEFS_METAL}</defs>"
        f'<ellipse cx="410" cy="220" rx="400" ry="190" fill="url(#grad-bg)"/>{body}</svg>'
    )


TERN_PATH = (  # a tern, or a very committed swallow
    "M0,6 C8,4 14,0 22,1 C26,1.5 28,3 31,3 L36,1.5 L32,5 C28,7 24,8 20,8.5 "
    "L27,15 L22,15 L14,9 C9,9.5 4,8.5 0,6 Z M20,8.5 L30,11 L33,14 L25,11.5 Z"
)


def tern_body(plus=False, led_style="fill: var(--tern-led, #22E08A)", uid="t"):
    """Side view of the terminator. LED colour is a CSS custom property."""
    import math
    y, h = 150, 104
    top, bot = y - h / 2, y + h / 2
    pins = "".join(
        f'<rect x="58" y="{y + dy - 3.5}" width="70" height="7" rx="3.5" fill="url(#{uid}-pin)"/>'
        for dy in (-24, 0, 24)
    )
    ribs = "".join(
        f'<rect x="{262 + i * 13}" y="{top + 4}" width="6" height="{h - 8}" rx="3" fill="#000" opacity=".35"/>'
        for i in range(7)
    )
    band = (
        f'<rect x="470" y="{top}" width="14" height="{h}" fill="url(#{uid}-band)"/>' if plus else ""
    )
    wifi = (
        f'<g transform="translate(424 {top + 22})" fill="none" stroke="#22D3EE" stroke-width="3" stroke-linecap="round" opacity=".9">'
        '<path d="M0,10 a14,14 0 0 1 20,0"/><path d="M4,14 a8,8 0 0 1 12,0"/><circle cx="10" cy="18" r="1.6" fill="#22D3EE"/></g>'
        if plus else ""
    )
    label = "DMX TERN+" if plus else "DMX TERN"
    return f"""
<defs>
<linearGradient id="{uid}-shell" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#6D6C80"/><stop offset=".22" stop-color="#F3F3FA"/><stop offset=".42" stop-color="#B5B4C6"/>
  <stop offset=".78" stop-color="#55546A"/><stop offset="1" stop-color="#2B2A38"/></linearGradient>
<linearGradient id="{uid}-body" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#2E2D3C"/><stop offset=".25" stop-color="#4B4A60"/><stop offset=".5" stop-color="#1D1C28"/>
  <stop offset="1" stop-color="#0A0A10"/></linearGradient>
<linearGradient id="{uid}-pin" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#FFE9A8"/><stop offset=".5" stop-color="#D4A62A"/><stop offset="1" stop-color="#8A6512"/></linearGradient>
<linearGradient id="{uid}-band" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#22D3EE"/><stop offset=".3" stop-color="#A5F3FC"/><stop offset="1" stop-color="#0E7490"/></linearGradient>
<radialGradient id="{uid}-dome" cx=".35" cy=".3" r=".8">
  <stop offset="0" stop-color="#fff" stop-opacity=".95"/><stop offset=".25" stop-color="#fff" stop-opacity=".25"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
<filter id="{uid}-glow" x="-150%" y="-150%" width="400%" height="400%"><feGaussianBlur stdDeviation="16"/></filter>
<filter id="{uid}-shadow" x="-20%" y="-80%" width="140%" height="260%"><feGaussianBlur stdDeviation="10"/></filter>
</defs>
<ellipse cx="330" cy="{bot + 26}" rx="290" ry="14" fill="#000" opacity=".5" filter="url(#{uid}-shadow)"/>
{pins}
<rect x="118" y="{top - 6}" width="126" height="{h + 12}" rx="12" fill="url(#{uid}-shell)"/>
<rect x="150" y="{top - 6}" width="44" height="8" rx="2" fill="#2B2A38" opacity=".7"/>
<ellipse cx="120" cy="{y}" rx="9" ry="{h / 2 + 6}" fill="#9796AA"/>
<ellipse cx="120" cy="{y}" rx="5" ry="{h / 2}" fill="#1A1922"/>
<rect x="236" y="{top}" width="296" height="{h}" rx="18" fill="url(#{uid}-body)"/>
{ribs}{band}{wifi}
<g transform="translate(358 {top + 20}) scale(1.35)" fill="#8F8EA8" opacity=".55">
  <path d="{TERN_PATH}"/></g>
<text x="358" y="{bot - 20}" {MONO} font-size="13" font-weight="700" fill="#BDBCD2" letter-spacing="2" opacity=".85">{label}</text>
<text x="358" y="{bot - 8}" {MONO} font-size="7" fill="#8F8EA8" letter-spacing="1.2" opacity=".7">120Ω · RDM-AWARE · NOT A ROBOT</text>
<rect x="526" y="{top + 8}" width="30" height="{h - 16}" rx="10" fill="url(#{uid}-shell)"/>
<circle cx="578" cy="{y}" r="44" style="{led_style}" opacity=".55" filter="url(#{uid}-glow)" class="tern-glow"/>
<ellipse cx="566" cy="{y}" rx="22" ry="30" style="{led_style}" class="tern-led"/>
<ellipse cx="566" cy="{y}" rx="22" ry="30" fill="url(#{uid}-dome)"/>
"""


def render_tern(plus=False, inline=False):
    uid = "tp" if plus else "t"
    label = "DMX Tern+ smart Wi-Fi DMX terminator" if plus else "DMX Tern smart DMX terminator with tri-colour status LED"
    cls = ' class="tern-svg"' if inline else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="30 40 620 230"{cls} role="img" aria-label="{label}">'
        f"{tern_body(plus, uid=uid)}</svg>"
    )


def og_image():
    mark = robot_svg_body(18, uid="og")
    defs, wm, w, h = wordmark(10, 560, 250, "#F4F3FF", "og")
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630">'
        '<defs><radialGradient id="ogbg" cx=".3" cy=".4" r=".9"><stop offset="0" stop-color="#2A1B5E"/>'
        '<stop offset=".55" stop-color="#0E0C1F"/><stop offset="1" stop-color="#08070F"/></radialGradient>'
        f"{defs}</defs>"
        '<rect width="1200" height="630" fill="url(#ogbg)"/>'
        '<circle cx="1050" cy="120" r="260" fill="#22D3EE" opacity=".08"/>'
        f'<g transform="translate(80 100)" shape-rendering="crispEdges">{mark}</g>'
        f'<g shape-rendering="crispEdges">{wm}</g>'
        f'<text x="560" y="{250 + h + 62}" font-family="Helvetica, Arial, sans-serif" font-size="30" fill="#B9B7D6">'
        "We don’t make robots — we make what comes next.</text></svg>"
    )
