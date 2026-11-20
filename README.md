<div align="center">

# Awesome Claude Study Skills

**A curated collection of Claude Skills for studying: active recall, flashcards, exam practice, study guides, and mind maps.**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Skill Count](https://img.shields.io/badge/skills-6-blue?style=classic)
![License](https://img.shields.io/badge/license-MIT-green?style=classic)

</div>

> 🇹🇭 **สรุปภาษาไทย:** รวม Claude Skill สำหรับอ่านหนังสือ/ติวสอบ 6 ตัว — `study-session` (อธิบาย → ให้อธิบายกลับ → ควิซ → ทำแฟลชการ์ด), `flashcard-writer`, `exam-quiz`, `study-guide`, `mind-map` และ `infographic-cheatsheet` (สรุปสไลด์/PDF/TXT เยอะๆ เป็นโพย A4 แบบ infographic อธิบายละเอียด เต็มหน้ากระดาษ) ติดตั้งด้วย `./install-skills.sh` แล้วเรียกใน Claude Code ด้วย `/study-session` หรือแค่พิมพ์ว่า "ช่วยติว osmosis หน่อย" Claude จะโหลด skill ให้อัตโนมัติ

A **Claude Skill** is a folder with a `SKILL.md` file. Claude reads the short `description` in each skill and loads the full routine only when your request matches. You write your study routine once, and Claude runs it the same way every time — no long prompt to retype.

Content is based on the article [Claude Skills for Studying: Build a Study Skill (2026)](https://notesmakr.com/blog/claude-skills-for-studying) by Notesmakr. The `SKILL.md` files here are rewritten and expanded versions of the routines that article describes.

## Contents

- [Skills](#skills)
- [Installation](#installation)
- [Why these routines work](#why-these-routines-work)
- [Writing your own study skill](#writing-your-own-study-skill)
- [Tips and common mistakes](#tips-and-common-mistakes)
- [FAQ](#faq)
- [Resources](#resources)

## Skills

| Skill | Triggers when you… | What it does |
| --- | --- | --- |
| [**study-session**](skills/study-session/SKILL.md) | ask to study, revise, learn, or be quizzed on a topic | Full routine: asks your course and exam → explains in < 250 words with one example → you explain it back → 5-question quiz, one at a time → lists weak points → writes flashcards → saves or shows them |
| [**flashcard-writer**](skills/flashcard-writer/SKILL.md) | ask for flashcards or Anki cards | Asks exam format and card budget, shows 5 sample cards first, then writes one-fact-per-card decks with cloze for terms; CSV for Anki |
| [**exam-quiz**](skills/exam-quiz/SKILL.md) | ask to be tested before an exam | 10 mixed, timed questions, no feedback until the end, then a score table and your weakest areas |
| [**study-guide**](skills/study-guide/SKILL.md) | ask for a study guide or summary sheet | One page: big picture, key-term table, core ideas, 3 worked examples, likely exam questions, common mistakes |
| [**mind-map**](skills/mind-map/SKILL.md) | ask to map or connect a topic | Central idea, 4–6 branches, one example per branch, cross-links, plus a Mermaid `mindmap` block |
| [**infographic-cheatsheet**](skills/infographic-cheatsheet/SKILL.md) | ask for a cheat sheet / summary from many slides, PDFs, or TXT files | Dense, colour-coded A4 infographic pages (analogy · core idea · worked example · trap), HTML + PDF. A Playwright script measures every page and loops until each is 92–99 % full with no empty bands |

`infographic-cheatsheet` extra setup: `pip install playwright && playwright install chromium`, plus `pdftotext` (poppler) for PDF sources.

**Rule of thumb:** one routine per skill. Small focused skills trigger more reliably than one giant skill.

## Installation

### Option 1: Claude Code plugin

```bash
claude plugin marketplace add Calvinkub/awesome-claude-study-skills
claude plugin install study-skills
```

### Option 2: Installer script

```bash
git clone https://github.com/Calvinkub/awesome-claude-study-skills.git
cd awesome-claude-study-skills
./install-skills.sh                    # all skills -> ~/.claude/skills (personal)
./install-skills.sh --project          # all skills -> ./.claude/skills (this project only)
./install-skills.sh exam-quiz mind-map # only selected skills
```

### Option 3: Manual copy

Copy a skill folder to one of these locations. The folder name must match the `name` in the frontmatter.

| Scope | Path |
| --- | --- |
| Personal (all projects) | `~/.claude/skills/<skill-name>/SKILL.md` |
| Project only | `.claude/skills/<skill-name>/SKILL.md` |

Then type `/study-session` in Claude Code, or just ask: *"help me study osmosis"*.

### Option 4: Claude apps (claude.ai, Desktop)

1. Build ZIPs: `./install-skills.sh --zip` (creates `dist/<skill-name>.zip`).
2. In Claude, turn on code execution, then open **Customize → Skills** and upload the ZIP.
3. Zip the **folder**, not only `SKILL.md` — the skill folder must be at the root of the ZIP.

Skills work on every Claude plan, including Free (with code execution on). Claude Code needs a paid plan.

## Why these routines work

Each skill is built on well-studied learning effects:

| Effect | Where it is used |
| --- | --- |
| **Testing effect** (retrieval practice) — recalling beats rereading | quiz steps in `study-session`, `exam-quiz` |
| **Generation / self-explanation** — explaining in your own words | "explain it back" step, mind-map cross-link question |
| **Desirable difficulty** — effortful recall, no peeking | answers hidden until you respond; notes closed during `exam-quiz` |
| **Spaced repetition** — review cards over increasing gaps | flashcard output for Anki or another SRS app |

## Writing your own study skill

1. **Write the routine down** as you would explain it to a tutor.
2. **Create the folder** `my-skill/SKILL.md`.
3. **Write the frontmatter.** `name` matches the folder. `description` says *when* to use it. Keep the description under ~200 characters so it works in app uploads too (the developer limit is 1,024).
4. **Write the routine as numbered steps and rules.** Use imperative verbs: "Ask…", "Wait…", "Never…".
5. **Install and test on one topic.** If Claude summarises instead of asking questions, tighten the rules.

Template:

```markdown
---
name: my-skill
description: Use when the user asks to <trigger>. <One line on what it does>.
---

# My Skill

## Steps
1. Ask …
2. Explain …
3. Quiz … one question at a time. Wait for each answer.

## Rules
- Use only the user's material.
- Never reveal an answer before the user answers.
```

## Tips and common mistakes

- **Check facts.** Claude can state wrong facts with confidence. Check cards against your notes before the first review.
- **Test the waiting.** Make sure Claude waits for each answer before it moves on in a quiz. If not, add "Wait for the answer" to the rule.
- **One routine per skill.** Do not merge everything into one skill.
- **Save to spaced repetition.** Export cards as CSV for Anki, or connect a study app via MCP.
- **Close your notes** before the quiz. Pick your weakest topic first.

## FAQ

**What are Claude skills?** A folder with a `SKILL.md` file. Claude loads it when a request matches its description.

**Are skills free?** Skills are available on every Claude plan, including Free, with code execution on. Claude Code needs a paid plan.

**Can a skill make flashcards?** Yes. It can show cards as a table/CSV, or save them to a study app if an MCP server for that app is connected.

**Skill vs MCP?** A skill teaches Claude *how* to do a task. An MCP connection lets Claude *act* in another app. They combine well: `study-session` can save to a connected app at its last step.

## Resources

- Source article — [Claude Skills for Studying (Notesmakr)](https://notesmakr.com/blog/claude-skills-for-studying)
- [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) — Anthropic Engineering
- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills) — Claude Help Center
- [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude) — Claude Help Center
- [Skills in Claude Code](https://code.claude.com/docs/en/skills) — Claude Code docs
- Roediger & Karpicke (2006), *Test-enhanced learning* — [doi:10.1111/j.1467-9280.2006.01693.x](https://doi.org/10.1111/j.1467-9280.2006.01693.x)
- Fiechter & Benjamin (2018) — [doi:10.3758/s13423-017-1366-9](https://doi.org/10.3758/s13423-017-1366-9)
- Related collection — [awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents)

## Contributing

PRs welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE). Source article content belongs to its authors; this repo links to it and rewrites the routines in its own words.
