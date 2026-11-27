# Video script, production draft

**Title:** AI Coding Agents in 2026: How AI Is Transforming Software Development  
**Target:** 2 minutes 45 seconds to 2 minutes 55 seconds, at a natural speaking pace plus a brief demo pause.  
**Team:** Three speakers shown here; redistribute lines if the actual group is 2 or 4.  
**Rule:** Every group member must appear and speak. Use your own recorded voices; no AI-generated narration.  
**Footnote key:** S1 = GitHub; S2 = JetBrains; S3 = NBER, all in `SOURCES.md`.

## 0:00–0:23 | Slide 1 | Speaker 1: Hook

'Imagine getting a programming task and asking an AI agent to inspect the project, change the code, and run tests. That is no longer just a futuristic idea. In 2026, coding agents are becoming part of everyday software development. But does generating code faster mean shipping better software?'

**Visual:** Title, a flowing path from issue to tested pull request.

## 0:23–0:49 | Slide 2 | Speaker 1: What changed in 2026?

'Unlike a chatbot that only suggests code, a coding agent can work through multiple steps. On June seventeenth, GitHub announced that its Copilot desktop app was generally available. Developers can start tasks from an issue, pull request or prompt, then review changes and validate the results. The workflow is moving from suggestions toward supervised execution.'

**Visual:** ISSUE → AGENT → CODE + TESTS → HUMAN REVIEW. Citation: GitHub, June 2026 [S1].

## 0:49–1:12 | Slide 3 | Speaker 2: Adoption

'How widespread is this? In a 2026 JetBrains survey, ninety percent of surveyed professional developers reported using AI coding agents at work at least weekly, and sixty-eight percent used them daily. These numbers measure usage, not how often the generated code is correct.'

**Visual:** Large 90% / 68% figures with survey qualifier. Citation: JetBrains, 2026 [S2].

## 1:12–1:40 | Slide 4 | Speaker 2: Activity is not delivery

'A study from the National Bureau of Economic Research, revised in September 2026, examined more than five hundred thousand GitHub developers. Its estimates showed much bigger gains in commits than in actual software releases after adoption of autonomous coding agents. In other words, more code activity does not automatically become more finished products. Testing, integration and review can still be bottlenecks.'

**Visual:** +240% commits, +80% projects, +30% releases; mark as study estimates. Citation: NBER, 2026 [S3].

## 1:40–2:12 | Slide 5 | Speaker 3: Demo

'Here is a small Python discount function. The original version works for ordinary prices, but its tests reveal problems with an empty list, a negative price and invalid discounts. A coding agent can attempt a fix, run those tests and show us the changes. However, passing tests only proves the cases we checked. A programmer still needs to review the requirements and the code.'

**Visual:** Record your actual screen: baseline failing tests → agent change or clearly marked workflow simulation → review. Reserve approximately 10 seconds to show the real terminal result. **Do not claim the agent fixed it unless the actual recording confirms that.**

## 2:12–2:37 | Slide 6 | Speaker 3: What changes for students?

'So the important shift is not simply typing less code. Developers need to define problems, write useful tests, inspect generated changes, protect sensitive information and understand what gets deployed. For programming students, core skills like algorithms, debugging, testing and Git remain essential, alongside learning how to work critically with AI agents.'

**Visual:** Four skills: specify, verify, secure, collaborate.

## 2:37–2:53 | Slide 7 | Speaker 3 (or split across all): Final discussion question

'AI coding agents are changing how software is created, but developers are still responsible for the result. Our question is: If AI agents can generate, debug and test software, which programming skills should colleges prioritize to prepare the next generation of developers?'

**Visual:** Discussion question, held until video ends. No further narration after the question.

---

## Rehearsal and verification

- Approximate speaking duration depends on each student's pace and screen-demo hold. **Rehearse and trim until final video is 2:30–3:00**.
- End on exactly the same question shown in `README.md`.
- Use sources on-screen for the 2026 numbers; do not read full URLs aloud.
- Make sure all students appear and speak. Avoid AI-generated voices.
- For slide 5, record a **real run** or label it an illustration. See `code-demos/README.md`.
- Do not read square-bracket production instructions aloud.
