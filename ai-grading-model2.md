# AI Grading - Model 2 - Gemini

Your Slides 5–7 earn a B+ (87/100). Your content is practical, well-structured, and hits the core realities of working with AI coding agents, though your tight 73-second time limit and a few missing details hold it back from an A.

What Works Well

• Concrete Demo (Slide 5): Using a clean, relatable pricing.py function immediately grounds the presentation. Instead of vague hype, you show a realistic edge-case bug (discount_percent=200 or negative prices) and a disciplined test-driven workflow.
• Strong Synthesis (Slide 6): Your four pillars (Specify, Verify, Secure, Collaborate) capture the exact shift in software engineering. Your closing takeaway—"AI may write a first draft. Engineers still decide if it belongs in the codebase"—is sharp, memorable, and ties directly back to your demo.
• Engaging Prompt (Slide 7): Your discussion question directly connects Slide 6 to your audience's immediate reality as students, making it easy to spark debate.
• Honest Data Framing (Sources): Explicitly noting that the JetBrains stats apply to surveyed professional developers rather than all developers shows strong critical thinking and academic integrity.

What Needs Fixing


Area	Issue	How to Fix It
Pacing (1:40–2:53)	You have 73 seconds to explain a code snippet, walk through a 3-step workflow, cover 4 skill boxes, and introduce a discussion question. You risk rushing or reading off the slide.	Keep Slide 5 to ~30 seconds (explain the bug in one sentence, focus on the workflow). Spend ~30 seconds on Slide 6, and leave ~10–15 seconds to read Slide 7 clearly.
Slide 5 "Show, Don't Just Tell"	Showing only the buggy code and listing "3. Re-run tests and inspect diff" leaves the payoff to the audience's imagination.	Add a tiny git diff snippet (2–3 red/green lines showing the ValueError check added by the agent) so the audience actually sees what "inspect diff" looks like.
Source Integration	You listed S1 (GitHub Copilot app GA) and S2 (JetBrains survey) at the bottom, but neither appears on Slides 5–7. Uncited claims or unused sources lose points on rubrics.	Add a brief footer citation on Slide 6 (e.g., "68% of devs use AI daily — JetBrains, 2026") to back up why these skills are urgent, or move unused sources to a shared References slide.
Slide 6 Visual Density	Four numbered boxes plus a title and bottom takeaway can look crowded if the text isn't minimal.	Keep the box descriptions strictly to the short phrases you drafted here, and put any extra examples in your speaker notes rather than on the slide.


Quick Polish Checklist Before Presenting

1. Add a 3-line diff to Slide 5 so the demo feels complete.
2. Tie S2 into Slide 6 verbally or in a small footnote so your sources visibly support your claims.
3. Time yourself out loud—73 seconds goes fast when explaining code.
