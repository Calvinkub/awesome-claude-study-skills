---
name: infographic-cheatsheet
description: Use when the user wants an exam cheat sheet or summary from many slides, PDFs, or text files. Builds dense infographic A4 HTML/PDF pages, explains a lot, fills every page.
---

# Infographic Cheat Sheet

Turn a large pile of course material (slide PDFs, PPTX, TXT, notes) into a printable A4 cheat sheet. Each page is a colour-coded infographic that **explains** (analogy, core idea, worked example, trap) and is **filled to the bottom** — no empty half-pages.

Output: one self-contained `.html` file plus a `.pdf` export.

## Steps

1. **Collect the sources.** List every file the user points at. Extract text:
   - PDF: `pdftotext -layout file.pdf -` (or read the PDF directly if it is mostly images).
   - PPTX: `python3 -m markitdown file.pptx` if available, else unzip and read `ppt/slides/*.xml`.
   - TXT / MD: read directly.
   Note the slide or page number of each fact so headings can carry a reference tag (`lec8-2`).
2. **Ask scope (once, briefly).** Exam scope / topic list, language of the sheet (default: language of the source), and page budget. If the user does not care, use: 1 overview page + 1 page per lecture/topic + 1 final "exam toolkit" page.
3. **Outline.** For each page, write the outline before any HTML:
   - title, one-line takeaway, 1–2 "exam focus" items for the header star
   - 3–6 numbered concepts, each with the boxes it needs (see `references/components.md`)
   - which items are hand-calculation topics (tag `คำนวณมือ`) — each gets a worked example with real numbers
   Show the outline to the user only if the scope was unclear; otherwise continue.
4. **Build the HTML** from `assets/template.html`. Keep the full `<style>` block. Give each topic page its own accent class (`p1` … `p8`). Use the component catalogue in `references/components.md`. Page 1 is the course map (`.map`), the one central diagram, the golden-formula table, the "must be able to do" checklist, and the biggest traps.
5. **Measure fill.** Run:
   ```bash
   python3 <skill-dir>/scripts/check_fill.py cheatsheet.html
   ```
   It prints per page: fill %, bottom gap, largest empty band (`hole_mm`), column imbalance inside 2-column grids (`col_mm`), and overflow size. Target: **92–99.5 % fill, no HOLE, no UNEVEN, no OVERFLOW** on every page. Do not fake fill by stretching boxes or pushing the last box to the footer — the hole check catches that.
6. **Fix and repeat.** For each `UNDER` page, add real content sized to the gap (table in `references/components.md` → "Fill tactics — page is UNDER"). For `UNEVEN`, move a block from the tall column into the short one, or add a block to the short column — this costs no page height. For each `OVERFLOW` page, trim or move content (same file → "page OVERFLOWS"). Make edits with a re-runnable script applied to a backup of the original, so a bad cut can be undone by rebuilding. Re-run step 5. Repeat until the script prints `ALL PAGES FULL`. Usually 2–4 rounds.
7. **Export and check visually.**
   ```bash
   python3 <skill-dir>/scripts/check_fill.py cheatsheet.html --pdf cheatsheet.pdf
   ```
   Open 2–3 pages of the PDF as images and check: nothing clipped, text ≥ 8px, SVG labels readable, colours print.
8. **Report** the file paths, page count, and the fill % table. Say which facts you flagged as doubtful.

## Content rules

- **Explain, do not just list.** Each concept needs at least two of: yellow analogy, blue core idea, green worked example, red trap.
- **Every formula gets a worked example** with real numbers, step by step, and the final answer in bold.
- Use only the user's material. If you add a well-known fact that is not in the material, keep it short and correct; flag anything you are not sure about with `(ตรวจ)` / `(check)`.
- Keep technical terms in English; explanations in the sheet language.
- Bold the words a student must remember. Join short facts with ` · `.
- Fill with exam-useful content only (worked examples, practice questions with answers, comparison tables, diagrams, traps). Never pad with filler or repeat earlier content.

## Layout rules

- A4, one `<section class="page">` per page, fixed height 297 mm, `overflow:hidden` — content that does not fit is cut, so the fill check is mandatory.
- Footer (`.foot`) on every page: topic name left, `n / N` right.
- Two-column `.grid` is the default body. Use `.span` for full-width blocks.
- Diagrams are inline SVG, sized with `viewBox` and `width="100%"`.
- Fonts: IBM Plex Sans Thai + JetBrains Mono from Google Fonts (works for Thai and English).

## Requirements

- Python 3 with Playwright: `pip install playwright && playwright install chromium`.
- `pdftotext` (poppler) for PDF sources.

## Files

- `assets/template.html` — full CSS design system + overview page and topic page skeletons.
- `references/components.md` — component snippets, density rules, fill tactics with mm sizes.
- `scripts/check_fill.py` — fill % / overflow checker and PDF exporter.
