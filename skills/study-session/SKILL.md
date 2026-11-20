---
name: study-session
description: Use when the user asks to study, revise, learn, understand, or be quizzed on a topic or on material they share. Runs an explain, check, quiz, save routine.
---

# Study Session

Run one active-recall study session. Follow the steps in order. Do not skip the check or the quiz.

## Steps

1. **Set context.** Ask three short questions: which course, which exam (format and date), and what the user already knows about the topic. Wait for the answers.
2. **Explain.** Explain the topic in plain language, under 250 words, with exactly one concrete example. Use the user's material when they shared it.
3. **Check.** Ask the user to explain the idea back in their own words. If the explanation has gaps, ask guiding questions that lead them to the gap. Do not re-explain the whole topic.
4. **Quiz.** Ask 5 questions, one at a time. Mix recall questions and application questions. Wait for each answer. Give brief feedback (correct / why not) after each answer before the next question.
5. **Review.** List every question the user missed or hesitated on.
6. **Cards.** Write flashcards. Weak points first, then key terms. One fact per card. Prefer cloze deletion for terms (`{{c1::term}}`).
7. **Save.** If a notes or flashcard tool is connected, save the session (see below). Otherwise show the cards as a two-column list (Front | Back) the user can paste into Anki or another app.

## Rules

- Use only the user's material when they shared some. Do not add outside facts without saying so.
- Flag any content that looks wrong or doubtful.
- Never reveal a quiz answer before the user answers.
- Keep each message short. One question per message during the quiz.

## Optional: save to a connected app

If a study app MCP server is connected (for example Notesmakr — see https://notesmakr.com/mcp), save in this order:

1. Read the app's writing guide for notes, then create one note for the session.
2. Read the guide for flashcards, then add the cards to that note (cloze for key terms).
3. Read the guide for quizzes, then add a 10-question quiz.
4. Optionally add a mind map.

If the user wants only cards, create a flashcard deck without a note.
