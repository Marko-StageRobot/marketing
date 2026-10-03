# StageRobot.com

Static, single-page parody site for The Stage Robot Company. No build step is needed to deploy — this folder *is* the site.

## Deploy to Cloudflare Pages

- **Dashboard:** Workers & Pages → Create → Pages → *Upload assets* → drag this folder in.
- **CLI:** `npx wrangler pages deploy . --project-name stagerobot`

Cloudflare picks up `_headers` and `404.html` automatically.

## What's here

| Path | What |
|---|---|
| `index.html` | the site |
| `brand.html` | brand book / logo package presentation |
| `404.html` | "This page has been virtualized by PVA" |
| `assets/img/logo/` | full logo package — SVG + PNG |
| `assets/img/products/` | Unicore Gateway, Unicore Node, DMX Tern, DMXTern+ renders — SVG + PNG |
| `assets/img/team/` | pixel portraits |
| `assets/img/og-image.png` | social share card |

## Editing

Everything is generated from `~/Desktop/stagerobot-src/` — edit there, then run `python3 build.py`.
The pixel art (robot, avatars, wordmark font) lives as ASCII maps in `art.py`.
The social share tags in `index.html` point at `https://stagerobot.com/` — update them if the domain changes.
