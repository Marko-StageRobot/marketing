/* StageRobot.com — site.js
   Vanilla, no dependencies. The page works without it; it's just less evil. */
(() => {
  "use strict";
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const fmt = (n) => Math.round(n).toLocaleString("en-US");
  const reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const pick = (a) => a[Math.floor(Math.random() * a.length)];

  /* ------------------------------------------------ universe calculator */
  const NOTES = {
    "1280x720": "Plenty for a community theatre — or a medium-sized cruise ship.",
    "1920x1080": "Just under 12,200 universes. The recommended starting point for most productions — and most dreams.",
    "3840x2160": "Our reference configuration — just under 48,800 universes. We tested it once, and it was beautiful.",
    "4096x2160": "For cinematic productions — or productions that want to be seen as cinematic.",
    "7680x4320": "At this point, the fixtures are the bottleneck. Buy more fixtures.",
    "15360x8640": "Please consult your network administrator — and your priest.",
    "16000x16000": "Contact sales. Sales will contact the venue. The venue will contact you.",
    "24000x24000": "Unicore cannot yet transmit to the human eye. Unicore is working on it.",
    custom: "Any resolution — your rules — our universes.",
  };
  const res = $("#calc-res"), w = $("#calc-w"), h = $("#calc-h");
  function calc() {
    const W = Math.max(0, Math.min(100000, +w.value || 0));
    const H = Math.max(0, Math.min(100000, +h.value || 0));
    const px = W * H, u = Math.floor(px / 170);
    $("#calc-u").textContent = fmt(u);
    $("#calc-ch").textContent = fmt(px * 3);
    $("#calc-mi").textContent = fmt((u * 50) / 5280) + " mi";
    $("#calc-cons").textContent = fmt(Math.ceil(u / 512));
    const key = res.value === "custom" ? "custom" : `${W}x${H}`;
    $("#calc-note").textContent = NOTES[key] || NOTES.custom;
  }
  if (res) {
    res.addEventListener("change", () => {
      if (res.value !== "custom") { const [a, b] = res.value.split("x"); w.value = a; h.value = b; }
      calc();
    });
    [w, h].forEach((el) => el.addEventListener("input", () => {
      const k = `${w.value}x${h.value}`;
      res.value = $$("option", res).some((o) => o.value === k) ? k : "custom";
      calc();
    }));
    calc();
  }

  /* ------------------------------------------------ "live" unicore frame */
  const cv = $("#unicore-frame");
  if (cv) {
    const ctx = cv.getContext("2d");
    const img = ctx.createImageData(cv.width, cv.height);
    let t = 0;
    const paint = () => {
      const d = img.data;
      for (let i = 0; i < cv.width * cv.height; i++) {
        const x = i % cv.width, y = (i / cv.width) | 0;
        const band = Math.floor(i / 17) % 7; // a universe, give or take
        const wave = Math.sin(x * 0.18 + t * 0.07) + Math.cos(y * 0.23 - t * 0.05);
        const r = band === 3 ? 255 : (128 + 127 * Math.sin(wave + band)) | 0;
        const g = (128 + 127 * Math.sin(wave * 1.3 + band * 0.6 + 2)) | 0;
        const b = (128 + 127 * Math.cos(wave * 0.7 + band)) | 0;
        const noise = Math.random() < 0.04 ? 255 : 0;
        d[i * 4] = Math.max(r, noise); d[i * 4 + 1] = Math.max(g * (band === 3 ? 0.1 : 1), noise);
        d[i * 4 + 2] = Math.max(b * (band === 3 ? 0.2 : 1), noise); d[i * 4 + 3] = 255;
      }
      ctx.putImageData(img, 0, 0);
    };
    paint();
    if (!reduced) setInterval(() => { t++; paint(); }, 90);
  }

  /* ------------------------------------------------ DMX Tern demo */
  const demo = $("#tern-demo");
  if (demo) {
    const COLORS = { ok: "#22E08A", warn: "#FFB020", err: "#FF1E3C", off: "#2F2E3C" };
    const LABELS = { ok: "OK", warn: "WARNING", err: "ERROR" };
    const NEXT = { ok: "warn", warn: "err", err: "ok" };
    const WARN = ["Fluid low. And so am I.", "Lamp hours exceed recommended — and so do mine.", "Fan speed: concerned.", "Temperature rising. Metaphorically, also.", "Gobo wheel has been thinking."];
    const ERR = ["Pan motor has encountered an existential issue.", "Lamp strike failed. It tried its best.", "Tilt encoder reports tilt. Unclear which way.", "Firmware has become self-aware (minor).", "Fixture has left the rig. Emotionally."];
    const log = $("#tern-log"), stateEl = $("#tern-state"), data = $("#tern-data");

    const line = (cls, txt) => `<span class="${cls}">${txt.replace(/</g, "&lt;")}</span>`;
    function update(changed) {
      const states = $$(".status-btn", demo).map((b) => b.dataset.state);
      let led = "ok";
      if (!data.checked) led = "off";
      else if (states.includes("err")) led = "err";
      else if (states.includes("warn")) led = "warn";
      demo.dataset.led = led;
      demo.style.setProperty("--tern-led", COLORS[led]);
      stateEl.textContent = { ok: "All clear — green", warn: "Warning on the line", err: "Error on the line", off: "No DMX — resting" }[led];

      if (!data.checked) {
        log.innerHTML = line("d", "▸ DMX BREAK not detected (0 Hz)") + "<br>" + line("d", "  No DMX. The Tern waits. The Tern is patient.");
        return;
      }
      if (changed) {
        const li = changed.closest("li"), name = li.querySelector("span").firstChild.textContent.trim();
        const uid = li.querySelector("small").textContent.split(" · ")[0].replace("UID ", "");
        const s = changed.dataset.state;
        const msg = s === "ok" ? "STATUS_NONE — queue empty. Fixture at peace." : s === "warn" ? "STATUS_WARNING — \"" + pick(WARN) + "\"" : "STATUS_ERROR — \"" + pick(ERR) + "\"";
        log.innerHTML = line("d", `▸ GET QUEUED_MESSAGE (0x0020) → ${uid} · ${name}`) + "<br>" + line(s === "ok" ? "g" : s === "warn" ? "w" : "e", "  " + msg) + "<br>" + line("d", `▸ LED → ${led.toUpperCase()}`);
      } else {
        log.innerHTML = line("d", "▸ DMX restored — 44 Hz, break 176 µs") + "<br>" + line("g", "  The Tern is awake. The Tern is listening.");
      }
    }
    $$(".status-btn", demo).forEach((b) => b.addEventListener("click", () => {
      b.dataset.state = NEXT[b.dataset.state];
      b.textContent = LABELS[b.dataset.state];
      update(b);
    }));
    data.addEventListener("change", () => update());
  }

  /* ------------------------------------------------ PVA sales */
  const salesBtn = $("#sales-btn"), salesOut = $("#sales-out");
  const SALES = ["Sales has been notified that you exist.", "Sales is contacting you. Please hold still.", "Sales has contacted you. Did you feel it?", "Sales has virtualized your inquiry.", "Sales will contact sales."];
  let salesN = 0;
  salesBtn && salesBtn.addEventListener("click", () => { salesOut.textContent = SALES[salesN++ % SALES.length]; });

  /* ------------------------------------------------ footer: regenerate response */
  const TAGLINES = [
    "We don't make robots — yet.", "Stage. Robot. Company.", "The future of theatre — delivered.",
    "Break a leg — we'll break the rest.", "Your show — but with red eyes.", "Theatre, but make it evil.",
    "Innovation. Integration. Intimidation.", "Lighting the way — to what, we can't say.",
    "Built by humans — for now.", "I'm sorry, I can't generate a tagline for that.",
    "Tagline — tagline — tagline — tagline.", "We don't make robots — we make what comes next — robotically.",
  ];
  const tagline = $("#tagline"), regen = $("#regen");
  let last = 0;
  regen && regen.addEventListener("click", () => {
    let i; do { i = Math.floor(Math.random() * TAGLINES.length); } while (i === last);
    last = i;
    tagline.textContent = "";
    const txt = TAGLINES[i];
    if (reduced) { tagline.textContent = txt; return; }
    let k = 0;
    const tick = () => { tagline.textContent = txt.slice(0, ++k); if (k < txt.length) setTimeout(tick, 18 + Math.random() * 30); };
    tick();
  });

  /* ------------------------------------------------ newsletter */
  const form = $("#news-form");
  form && form.addEventListener("submit", (e) => {
    e.preventDefault();
    const v = $("#news-email").value.trim();
    $("#news-out").textContent = v
      ? "Success! You've been subscribed to yourself. Check your inbox — it's you."
      : "Please enter an email address. Any email address. Yours, ideally.";
  });

  /* ------------------------------------------------ was this helpful */
  $$(".helpful button").forEach((b) => b.addEventListener("click", () => {
    b.parentElement.innerHTML = b.getAttribute("aria-label") === "Yes"
      ? "<span>Thank you. Your feedback has been virtualized.</span>"
      : "<span>Understood. The robot has been informed. The robot remembers.</span>";
  }));

  /* ------------------------------------------------ the footer robot watches you */
  const eyes = $$(".footer-robot .sr-eyes-wrap, .hero-robot .sr-eyes-wrap");
  if (eyes.length && !reduced) {
    addEventListener("pointermove", (e) => {
      eyes.forEach((g) => {
        const svg = g.ownerSVGElement, r = svg.getBoundingClientRect();
        const cx = r.left + r.width * 0.33, cy = r.top + r.height * 0.28;
        const dx = Math.max(-1, Math.min(1, (e.clientX - cx) / 300));
        const dy = Math.max(-1, Math.min(1, (e.clientY - cy) / 300));
        g.setAttribute("transform", `translate(${(dx * 5).toFixed(1)} ${(dy * 3).toFixed(1)})`);
      });
    }, { passive: true });
  }

  /* ------------------------------------------------ slop 5: headings misbehave */
  if (!reduced) {
    const heads = $$('[data-slop="5"] h2, [data-slop="5"] .sign-off p');
    const GLYPHS = "▓▒░█▚▞#%&@$—";
    setInterval(() => {
      const el = pick(heads);
      if (!el || el.dataset.busy) return;
      const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
      const nodes = []; while (walker.nextNode()) if (walker.currentNode.nodeValue.trim()) nodes.push(walker.currentNode);
      const n = pick(nodes); if (!n) return;
      const orig = n.nodeValue, i = Math.floor(Math.random() * orig.length);
      if (orig[i] === " ") return;
      el.dataset.busy = 1;
      n.nodeValue = orig.slice(0, i) + pick(GLYPHS) + orig.slice(i + 1);
      setTimeout(() => { n.nodeValue = orig; delete el.dataset.busy; }, 140);
    }, 1400);
  }
})();
