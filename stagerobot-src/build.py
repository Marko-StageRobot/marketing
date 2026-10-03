#!/usr/bin/env python3
"""Build StageRobot.com into ~/Desktop/stagerobot-site.

    python3 build.py            # site + logo package
    python3 build.py --artifact # also write the claude.ai preview variant
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

import art

SRC = Path(__file__).resolve().parent
SITE = Path.home() / "Desktop" / "stagerobot-site"
IMG = SITE / "assets" / "img"
LOGO = IMG / "logo"


def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def png(svg: Path, width: int, out: Path = None, bg: str = None):
    if not shutil.which("rsvg-convert"):
        return
    out = out or svg.with_suffix(".png")
    cmd = ["rsvg-convert", "-w", str(width), "-o", str(out)]
    if bg:
        cmd += ["-b", bg]
    subprocess.run(cmd + [str(svg)], check=True)


def build_assets():
    # --- logo package
    logos = {
        "logo-mark.svg": art.robot_mark(uid="lm"),
        "logo-mark-mono-white.svg": art.robot_mark(uid="lmw", mono="#F4F3FF"),
        "logo-mark-mono-black.svg": art.robot_mark(uid="lmb", mono="#14122B"),
        "logo-horizontal-on-dark.svg": art.lockup_horizontal(ink="#F4F3FF", uid="lhd"),
        "logo-horizontal-on-light.svg": art.lockup_horizontal(ink="#14122B", uid="lhl"),
        "logo-horizontal-mono-white.svg": art.lockup_horizontal(ink="#F4F3FF", uid="lhw", mono="#F4F3FF"),
        "logo-horizontal-mono-black.svg": art.lockup_horizontal(ink="#14122B", uid="lhb", mono="#14122B"),
        "logo-stacked-on-dark.svg": art.lockup_stacked(ink="#F4F3FF", uid="lsd"),
        "logo-stacked-on-light.svg": art.lockup_stacked(ink="#14122B", uid="lsl"),
        "app-icon.svg": art.robot_mark(uid="ai", bg="#0B0A18", pad=36),
    }
    for name, svg in logos.items():
        write(LOGO / name, svg)
        png(LOGO / name, 1600 if "horizontal" in name else 1024)

    write(SITE / "favicon.svg", art.favicon())
    png(SITE / "favicon.svg", 180, SITE / "apple-touch-icon.png")
    png(SITE / "favicon.svg", 32, SITE / "favicon-32.png")

    # --- products
    prod = IMG / "products"
    write(prod / "unicore-gateway.svg", art.render_gateway())
    write(prod / "unicore-node.svg", art.render_node())
    write(prod / "dmx-tern.svg", art.render_tern())
    write(prod / "dmx-tern-plus.svg", art.render_tern(plus=True))
    for f in prod.glob("*.svg"):
        png(f, 1640)

    # --- team
    team = IMG / "team"
    write(team / "alan-smithee.svg", art.avatar(art.AVATAR_ALAN, "#1E1B33", "Alan Smithee, approximately"))
    write(team / "marko-dragic.svg", art.avatar(art.AVATAR_MARKO, "#1E1B33", "Marko Dragic"))
    write(team / "team-member-3.svg", art.avatar(art.AVATAR_GHOST, "#101826", "[TEAM MEMBER 3 — IMAGE PENDING]"))

    # --- social
    write(IMG / "og-image.svg", art.og_image())
    png(IMG / "og-image.svg", 1200, IMG / "og-image.png")


SNIPPETS = {
    "{{NAV_LOGO}}": lambda: art.lockup_horizontal(uid="nav", cls="nav-logo", current=True, sub=False, wm_cell=17),
    "{{HERO_ROBOT}}": lambda: art.robot_mark(uid="hero", cls="hero-robot"),
    "{{FOOTER_ROBOT}}": lambda: art.robot_mark(uid="foot", cls="footer-robot"),
    "{{TERN_INLINE}}": lambda: art.render_tern(inline=True),
    "{{BRAND_MARK}}": lambda: art.robot_mark(uid="brand", cls="brand-hero-mark"),
}


def render_template(name: str):
    text = (SRC / name).read_text(encoding="utf-8")
    for key, fn in SNIPPETS.items():
        if key in text:
            text = text.replace(key, fn())
    # {{MARK:uid}} → a standalone inline robot with its own filter ids
    return re.sub(r"\{\{MARK:([a-z0-9-]+)\}\}", lambda m: art.robot_mark(uid=m.group(1), cls=f"mark mark-{m.group(1)}"), text)


def build_pages():
    for name in ("index.html", "brand.html", "404.html"):
        if (SRC / name).exists():
            write(SITE / name, render_template(name))
    for rel in ("assets/css/site.css", "assets/js/site.js", "robots.txt", "_headers", "README.md", "humans.txt"):
        if (SRC / rel).exists():
            dst = SITE / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(SRC / rel, dst)


def build_artifact(out: Path):
    """claude.ai wraps pages in its own doctype/head/body — strip ours."""
    out.mkdir(parents=True, exist_ok=True)
    for name in ("index.html", "brand.html"):
        html = (SITE / name).read_text(encoding="utf-8")
        html = re.sub(r"<!doctype html>\s*", "", html, flags=re.I)
        html = re.sub(r"</?(html|head|body)\b[^>]*>\s*", "", html, flags=re.I)
        html = re.sub(r'<meta (charset|name="viewport")[^>]*>\s*', "", html, flags=re.I)
        # the page title must come first (only the first 8KB is scanned)
        m = re.search(r"<title>.*?</title>\s*", html, flags=re.S)
        if m:
            html = m.group(0) + html.replace(m.group(0), "", 1)
        write(out / name, html)


if __name__ == "__main__":
    build_assets()
    build_pages()
    if "--artifact" in sys.argv:
        i = sys.argv.index("--artifact")
        build_artifact(Path(sys.argv[i + 1]) if len(sys.argv) > i + 1 else SRC / "_artifact")
    print("built →", SITE)
