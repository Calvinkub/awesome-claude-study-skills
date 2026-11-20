# Components and fill tactics

All classes live in `assets/template.html`. Copy the whole `<style>` block; do not invent new CSS unless a component below cannot express the idea.

## Component catalogue

| Need | Component | Snippet |
| --- | --- | --- |
| Everyday analogy | yellow box | `<div class="box y"><div class="t">เปรียบเทียบง่ายๆ</div>…</div>` |
| Core idea / why it matters | blue box | `<div class="box b"><div class="t">ใจความ</div>…</div>` |
| Worked example with numbers | green box | `<div class="box g"><div class="t">ตัวอย่าง: …</div>…</div>` |
| Exam trap / common mistake | red box | `<div class="box r"><div class="t">กับดัก</div>…</div>` |
| Pipeline / process | flow chips | `<div class="flow"><span class="chip">A</span><span class="arr">→</span><span class="chip f">B</span></div>` |
| Ordered procedure | numbered steps | `<ol class="steps"><li>…</li></ol>` |
| A vs B comparison | table or `.vs` | `<div class="vs"><div class="mini">A</div><div class="mid">vs</div><div class="mini">B</div></div>` |
| Ranked list / hits | rank chips | `<div class="rank"><span class="rk hit">D5</span><span class="rk">D1</span></div>` |
| Course map | `.map` + `.mbox` | `<div class="mbox" style="--mc:var(--c3)"><b>Title</b>terms<br><i>"slogan"</i></div>` |
| Small cards side by side | `.two` / `.three` + `.mini` | `<div class="mini"><b class="h">Term</b>definition</div>` |
| Formula / code | `pre` | use `.k` keyword, `.s` string, `.cm` comment, `.bad`, `.ok` spans |
| Self-check list | `.cbx` | `<ul class="cbx"><li>…</li></ul>` |
| Q→A drill | `table.qa` | first column question, second answer |
| Mechanism diagram | inline SVG | `viewBox` sized to column; text ≥ 8px; colours from the page accent |
| Tags on headings | `.tag`, `.tag.calc`, `.id` | `<span class="tag calc">คำนวณมือ</span> <span class="id">lec8-1</span>` |

## Density rules (explain a lot, but scannable)

- Every concept gets at least **two** of: analogy, core idea, worked example, trap.
- Every formula gets a worked example with real numbers, shown step by step.
- Bold the 1–3 words a student must remember in each sentence.
- Use `·` to join short facts on one line instead of long bullet lists.
- Prefer tables for anything with 2+ attributes per item.
- Write in the language of the source material; keep technical terms in English.

## Fill tactics — page is UNDER (gap > ~8 mm)

Add content in this order (most exam value first). Rough heights at 10.2px base font:

| Gap | Add |
| --- | --- |
| 8–20 mm | one more red trap box, or 2–3 rows in an existing table, or a one-line "สรุป 1 บรรทัด" blue box |
| 20–45 mm | a second worked example (green), or a mini Q→A drill table (4–5 rows), or a `.three` row of `.mini` term cards |
| 45–80 mm | a new full-width section: "โจทย์ฝึก + เฉลย" (3 practice questions with answers), or an SVG diagram of the mechanism, or a comparison table with "เก่ง / พลาด / ใช้เมื่อ" rows |
| > 80 mm | pull the next sub-topic onto this page, or add both a diagram and a practice block |

Only add content that comes from the source material or is a correct worked example of it. Never pad with filler text, repeated content, or empty decoration.

A gap under ~6 mm is fine — leave it. Do not use `.stretch` or empty spacing to reach the footer; the hole check flags it.

## Fill tactics — page UNEVEN

A 2-column grid where one column ends early leaves a half-empty band the page-level fill cannot see. Fix before adding new content:

1. Move a box or table from the tall column to the end of the short column.
2. Or add a block sized to `col_mm` to the short column (an analogy box, a trap box, a practice table).
3. When appending a new grid under an existing one, first balance the existing grid — otherwise the hole stays above the new content.

## Fill tactics — page OVERFLOWS

Fix in this order:

1. Shorten wording (cut repeated words, turn sentences into `·`-joined fragments).
2. Move one section to the next page, or to a new page.
3. Turn a bullet list into a 2-column table or `columns:2` list.
4. Lower font for that page only: `<section class="page p3" style="--fs:9.7px">`. Do not go below 9.4px.
