#!/usr/bin/env python3
"""Square stickers (Powered by Unicore, This Terns Me On, We Don't Make Robots) — 2in × 2in, rounded die-cut, 1/16in bleed.

    python3 sticker.py   → ~/Desktop/stagerobot-merch/
All text is drawn as pixel rects, so there are no fonts to embed or outline.
"""
import shutil
import subprocess
from pathlib import Path

import art

OUT = Path.home() / "Desktop" / "stagerobot-merch"

# glyphs the brand font didn't need until now
art.FONT.update({
    "D": ["####.", "#...#", "#...#", "#...#", "#...#", "#...#", "####."],
    "U": ["#...#", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    "W": ["#...#", "#...#", "#...#", "#.#.#", "#.#.#", "##.##", "#...#"],
    "I": ["###", ".#.", ".#.", ".#.", ".#.", ".#.", "###"],
    ".": [".", ".", ".", ".", ".", ".", "#"],
    "X": ["#...#", "#...#", ".#.#.", "..#..", ".#.#.", "#...#", "#...#"],
    "K": ["#...#", "#..#.", "#.#..", "##...", "#.#..", "#..#.", "#...#"],
    "'": ["#", "#", ".", ".", ".", ".", "."],
})

S = 1000            # trim size in units (1000 = 2 in)
BLEED = 32          # ≈ 1/16 in
RADIUS = 90         # die-cut corner radius
INK = "#0B0A18"


def width(text, cell, gap=1):
    return (sum(len(art.FONT[c][0]) + gap for c in text) - gap) * cell


def centred(text, cell, y, fill):
    rects, _ = art.text_pixels(text, cell, (S - width(text, cell)) / 2, y, fill)
    return rects


def frame(middle, dieline=False):
    """Shared chrome: background, inner outline, bottom URL band, optional dieline."""
    b = BLEED
    body = f"""
<defs>
  <linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#8B5CF6"/><stop offset="1" stop-color="#22D3EE"/></linearGradient>
  <radialGradient id="bg" cx=".5" cy=".28" r=".75">
    <stop offset="0" stop-color="#2A1B5E"/><stop offset=".6" stop-color="#110E24"/><stop offset="1" stop-color="{INK}"/></radialGradient>
</defs>
<rect x="{-b}" y="{-b}" width="{S + 2 * b}" height="{S + 2 * b}" fill="url(#bg)"/>
<rect x="36" y="36" width="{S - 72}" height="{S - 72}" rx="{RADIUS - 36}" fill="none" stroke="#22D3EE" stroke-opacity=".35" stroke-width="8"/>
{middle}
<rect x="{-b}" y="772" width="{S + 2 * b}" height="{S - 772 + b}" fill="url(#g)"/>
<g shape-rendering="crispEdges">{centred("STAGEROBOT.COM", 10, 851, INK)}</g>
"""
    cut = ""
    if dieline:
        cut = (f'<rect x="0" y="0" width="{S}" height="{S}" rx="{RADIUS}" fill="none" stroke="#FF00FF" stroke-width="4" stroke-dasharray="14 8"/>'
               f'<rect x="60" y="60" width="{S - 120}" height="{S - 120}" rx="{RADIUS - 40}" fill="none" stroke="#00C2FF" stroke-width="3" stroke-dasharray="6 6"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-b} {-b} {S + 2 * b} {S + 2 * b}" '
            f'width="{(S + 2 * b) / 500:g}in" height="{(S + 2 * b) / 500:g}in">{body}{cut}</svg>')


def grad_text(text, cell, y, gid, c0, c1):
    x0 = (S - width(text, cell)) / 2
    return (f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="{x0:g}" y1="0" x2="{x0 + width(text, cell):g}" y2="0">'
            f'<stop offset="0" stop-color="{c0}"/><stop offset="1" stop-color="{c1}"/></linearGradient>'
            f'<g shape-rendering="crispEdges">{centred(text, cell, y, f"url(#{gid})")}</g>')


def unicore():
    return (f'<g transform="translate({(S - 288) / 2} 64)">{art.robot_svg_body(12, uid="stk")}</g>'
            f'<g shape-rendering="crispEdges">{centred("POWERED BY", 9, 396, "#C9C7E0")}</g>'
            + grad_text("UNICORE", 22, 482, "gu", "#A78BFA", "#22D3EE"))


def tern():
    render = art.render_tern().replace("<svg ", '<svg x="110" y="92" width="780" height="289" ', 1)
    return (render
            + f'<g shape-rendering="crispEdges">{centred("THIS TERNS", 14, 420, "#EEEDF8")}</g>'
            + grad_text("ME ON", 14, 548, "gt", "#22E08A", "#22D3EE"))


def glowy_robot(cell, uid):
    """Robot mark with a wider halo behind the eyes than the site version has."""
    eyes = [row if i in (6, 7) else "." * len(row) for i, row in enumerate(art.ROBOT)]
    lit = art.pixels(eyes, cell, keys="Rr", color=art.PAL["R"])
    halo = (f'<defs><filter id="{uid}-halo" filterUnits="userSpaceOnUse" x="0" y="0" width="{24 * cell}" height="{16 * cell}">'
            f'<feGaussianBlur stdDeviation="{cell * 1.7:g}"/></filter>'
            f'<filter id="{uid}-bloom" filterUnits="userSpaceOnUse" x="0" y="0" width="{24 * cell}" height="{16 * cell}">'
            f'<feGaussianBlur stdDeviation="{cell * 0.6:g}"/></filter></defs>'
            f'<g filter="url(#{uid}-halo)" opacity=".7">{lit}</g>'
            f'<g filter="url(#{uid}-bloom)">{lit}</g>')
    wrap = '<g class="sr-eyes-wrap">'
    return art.robot_svg_body(cell, uid=uid).replace(wrap, halo + wrap, 1)


def no_robots():
    return (f'<g transform="translate({(S - 288) / 2} 64)">{glowy_robot(12, "stk")}</g>'
            f'<g shape-rendering="crispEdges">{centred("WE DON\'T MAKE", 11, 400, "#C9C7E0")}</g>'
            + grad_text("ROBOTS.", 22, 505, "gr", "#A78BFA", "#22D3EE"))


DESIGNS = {"powered-by-unicore": unicore, "this-terns-me-on": tern, "we-dont-make-robots": no_robots}


def sticker(design="powered-by-unicore", dieline=False):
    return frame(DESIGNS[design](), dieline)


def preview(design):
    """What it looks like after cutting — rounded corners, no bleed."""
    full = sticker(design)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {S} {S}">'
            f'<defs><clipPath id="cut"><rect width="{S}" height="{S}" rx="{RADIUS}"/></clipPath></defs>'
            f'<g clip-path="url(#cut)">{full[full.index(">") + 1:-6]}</g></svg>')


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for d in DESIGNS:
        (OUT / f"{d}-print.svg").write_text(sticker(d), encoding="utf-8")
        (OUT / f"{d}-dieline.svg").write_text(sticker(d, dieline=True), encoding="utf-8")
        (OUT / f"{d}-preview.svg").write_text(preview(d), encoding="utf-8")
        if shutil.which("rsvg-convert"):
            run = lambda *a: subprocess.run(["rsvg-convert", *a], check=True)
            # 2.064in with bleed @ 600dpi
            run("-w", "1238", "-o", str(OUT / f"{d}-print-600dpi.png"), str(OUT / f"{d}-print.svg"))
            run("-f", "pdf", "-o", str(OUT / f"{d}-print.pdf"), str(OUT / f"{d}-print.svg"))
            run("-w", "1000", "-o", str(OUT / f"{d}-preview.png"), str(OUT / f"{d}-preview.svg"))
    print("built →", OUT)
