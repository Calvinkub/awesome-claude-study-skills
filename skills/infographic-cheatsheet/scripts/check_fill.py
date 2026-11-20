#!/usr/bin/env python3
"""Measure how full each A4 page of an infographic cheat sheet is.

Renders the HTML in print mode (A4) with headless Chromium via Playwright and,
for every <section class="page">, reports:
  fill%    = used height / usable height (header top to footer top)
  gap_mm   = empty space above the footer
  hole_mm  = largest empty vertical band anywhere on the page
  col_mm   = largest column imbalance inside a multi-column grid row
  overflow = content cut off at the bottom (must be fixed)

Usage:
  python3 check_fill.py cheatsheet.html                 # report
  python3 check_fill.py cheatsheet.html --pdf out.pdf   # report + export PDF
  python3 check_fill.py cheatsheet.html --min 92 --max 99

Exit code 0 when every page is within [min, max] and nothing overflows, else 1.
Requires: pip install playwright && playwright install chromium
"""
import argparse
import json
import pathlib
import sys

from playwright.sync_api import sync_playwright

MEASURE_JS = r"""
() => {
  const pxPerMm = 96 / 25.4;
  return [...document.querySelectorAll('section.page, .page')].map((p, i) => {
    const pr = p.getBoundingClientRect();
    const cs = getComputedStyle(p);
    const padTop = parseFloat(cs.paddingTop), padBot = parseFloat(cs.paddingBottom);
    const foot = p.querySelector(':scope > .foot');
    const footTop = foot ? foot.getBoundingClientRect().top : pr.bottom - padBot;
    let used = pr.top + padTop;
    const spans = [];
    // deepest bottom edge of anything that puts ink on paper: text leaves,
    // media, and boxes with a border/background. Plain layout wrappers
    // (e.g. a .stretch grid grown to the footer) do not count as content.
    const inked = el => {
      const tag = el.tagName.toLowerCase();
      if (['svg', 'img', 'canvas', 'table', 'pre', 'hr'].includes(tag)) return true;
      if (el.closest('svg') && tag !== 'svg') return false;
      if (el.children.length === 0) return el.textContent.trim().length > 0;
      const s = getComputedStyle(el);
      const bg = s.backgroundColor;
      const hasBg = bg && bg !== 'transparent' && !/rgba\(.*,\s*0\)$/.test(bg);
      const hasBorder = parseFloat(s.borderBottomWidth) > 0 && s.borderBottomStyle !== 'none';
      return hasBg || hasBorder;
    };
    p.querySelectorAll('*').forEach(el => {
      if (foot && (el === foot || foot.contains(el))) return;
      const r = el.getBoundingClientRect();
      if (r.height === 0 || r.width === 0) return;
      if (getComputedStyle(el).position === 'absolute') return;
      if (!inked(el)) return;
      used = Math.max(used, r.bottom);
      spans.push([r.top, r.bottom]);
    });
    // largest vertical hole between inked blocks (catches mid-page gaps)
    spans.sort((a, b) => a[0] - b[0]);
    let hole = 0, reach = pr.top + padTop;
    for (const [t, b] of spans) {
      if (t > reach) hole = Math.max(hole, t - reach);
      reach = Math.max(reach, b);
    }
    hole = Math.max(hole, footTop - reach);
    // column imbalance: in each multi-column grid row, how far the shortest
    // column's ink ends above the tallest one (an empty half-column)
    const inkBottom = el => {
      let b = -Infinity;
      if (inked(el)) b = el.getBoundingClientRect().bottom;
      el.querySelectorAll('*').forEach(d => {
        const r = d.getBoundingClientRect();
        if (r.height > 0 && inked(d)) b = Math.max(b, r.bottom);
      });
      return b;
    };
    let colGap = 0;
    p.querySelectorAll('*').forEach(g => {
      const cs = getComputedStyle(g);
      if (cs.display !== 'grid' || cs.gridTemplateColumns.split(' ').length < 2) return;
      const rows = {};
      [...g.children].forEach(c => {
        const t = Math.round(c.getBoundingClientRect().top);
        (rows[t] = rows[t] || []).push(inkBottom(c));
      });
      Object.values(rows).forEach(bs => {
        const v = bs.filter(Number.isFinite);
        if (v.length > 1) colGap = Math.max(colGap, Math.max(...v) - Math.min(...v));
      });
    });
    const usable = footTop - (pr.top + padTop);
    const fill = usable > 0 ? (used - (pr.top + padTop)) / usable : 0;
    const overflow = p.scrollHeight > p.clientHeight + 1 || used > footTop + 1;
    const title = (p.querySelector('h1') || {}).textContent || '';
    return {
      page: i + 1,
      title: title.trim().slice(0, 60),
      fill: Math.round(fill * 1000) / 10,
      gap_mm: Math.round(((footTop - used) / pxPerMm) * 10) / 10,
      hole_mm: Math.round((hole / pxPerMm) * 10) / 10,
      col_mm: Math.round((colGap / pxPerMm) * 10) / 10,
      overflow,
      over_mm: Math.round((Math.max(p.scrollHeight - p.clientHeight, used - footTop, 0) / pxPerMm) * 10) / 10,
    };
  });
}
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--pdf", help="also export a PDF to this path")
    ap.add_argument("--min", type=float, default=92.0, help="minimum fill %% (default 92)")
    ap.add_argument("--max", type=float, default=99.5, help="maximum fill %% (default 99.5)")
    ap.add_argument("--hole", type=float, default=12.0, help="max empty vertical band in mm (default 12)")
    ap.add_argument("--col", type=float, default=15.0, help="max column imbalance in mm (default 15)")
    ap.add_argument("--json", action="store_true", help="print JSON only")
    a = ap.parse_args()

    path = pathlib.Path(a.html).resolve()
    if not path.exists():
        print(f"not found: {path}", file=sys.stderr)
        return 2

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": 794, "height": 1123})
        page.goto(path.as_uri(), wait_until="networkidle")
        page.emulate_media(media="print")
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(300)
        rows = page.evaluate(MEASURE_JS)
        if a.pdf:
            page.pdf(path=a.pdf, format="A4", print_background=True,
                     margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
                     prefer_css_page_size=True)
        browser.close()

    ok = True
    for r in rows:
        if r["overflow"]:
            r["status"] = f"OVERFLOW - cut ~{r['over_mm']} mm of content"
            ok = False
        elif r["fill"] < a.min:
            r["status"] = f"UNDER - add ~{r['gap_mm']} mm of content"
            ok = False
        elif r["hole_mm"] > a.hole:
            r["status"] = f"HOLE - {r['hole_mm']} mm empty band mid-page; fill it with content"
            ok = False
        elif r["col_mm"] > a.col:
            r["status"] = f"UNEVEN - one column ends {r['col_mm']} mm early; move or add a block"
            ok = False
        elif r["fill"] > a.max:
            r["status"] = "TIGHT - ok but no room"
        else:
            r["status"] = "OK"

    if a.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
    else:
        print(f"{'pg':>3} {'fill%':>6} {'gap_mm':>7} {'hole_mm':>8} {'col_mm':>7}  status / title")
        for r in rows:
            print(f"{r['page']:>3} {r['fill']:>6} {r['gap_mm']:>7} {r['hole_mm']:>8} {r['col_mm']:>7}  {r['status']}  | {r['title']}")
        if a.pdf:
            print(f"PDF written: {a.pdf}")
        print("ALL PAGES FULL" if ok else "FIX PAGES ABOVE, then re-run")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
