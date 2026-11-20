# Contributing

Thanks for adding a study skill.

## Add a skill

1. Create `skills/<skill-name>/SKILL.md`. The folder name must equal the `name` field.
2. Frontmatter:
   ```yaml
   ---
   name: skill-name
   description: Use when the user asks to <trigger>. <What it does, one line.>
   ---
   ```
   Keep `description` under ~200 characters so it also works as a claude.ai upload.
3. Body: numbered **Steps** and a **Rules** list. Imperative verbs. One routine per skill.
4. Test it in Claude Code on one real topic. Check that Claude waits for answers and does not leak quiz answers.
5. Add a row to the Skills table in `README.md` and bump the skill count badge.

## Rules

- Skills must be useful for learning, not adverts for a product.
- Ground claims about learning science in a citation.
- No copied text from paywalled or copyrighted sources. Rewrite in your own words and link the source.
