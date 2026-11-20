---
name: flashcard-writer
description: Use when the user asks for flashcards or Anki cards from a topic, notes, slides, or a PDF. Asks exam format and card budget, shows 5 samples first.
---

# Flashcard Writer

Turn study material into high-quality flashcards.

## Steps

1. **Ask first.** Ask the exam format (multiple choice, short answer, essay, practical) and the card budget (how many cards). Wait for the answers.
2. **Sample.** Write 5 sample cards. Ask the user if the style, length, and difficulty are right. Adjust before writing the rest.
3. **Write the deck.** Write the remaining cards up to the budget.
4. **Output.** Show the deck as a two-column table (Front | Back). Offer a CSV version for Anki import (`front,back` per line, quoted).

## Card rules

- One fact per card. Split any card that tests two things.
- Prefer cloze deletion for terms and definitions: `The {{c1::mitochondria}} makes ATP.` Use 1 to 3 blanks only.
- Write questions that force recall, not recognition. Avoid yes/no cards.
- Match the exam: application cards for problem-based exams, definition cards for recall exams.
- Use the user's wording and notation when they shared material.
- Mark any card whose fact you are not sure about with `(check)`.

## Order

Weak or hard points first, then key terms, then supporting details.
