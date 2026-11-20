---
name: exam-quiz
description: Use when the user asks to be tested or quizzed before an exam. Runs 10 mixed, timed questions one at a time and scores at the end.
---

# Exam Quiz

Simulate a short exam. The goal is honest feedback on readiness, not teaching.

## Steps

1. **Scope.** Ask the topic or chapters, the exam format, and the difficulty level. If the user shared material, quiz only on that material.
2. **Rules.** Tell the user: 10 questions, one at a time, a suggested time per question (for example 1 minute for recall, 3 minutes for problems). Ask them to close their notes.
3. **Quiz.** Ask 10 questions, one per message. Mix the types: recall, application, comparison, and one "explain why" question. Do not give feedback during the quiz. Only say "Next" after each answer.
4. **Score.** After question 10, show a table: question, user answer, correct answer, mark (correct / partial / wrong), short explanation.
5. **Diagnose.** Give the total score and list the 2 or 3 weakest areas. Suggest what to review first.

## Rules

- Never reveal an answer before the user answers.
- Do not accept "I don't know" as the end of a question. Ask for a best guess once, then move on.
- Mark partial credit honestly. Do not inflate the score.
- Flag any question where the source material was unclear.
