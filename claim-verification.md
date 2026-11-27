# Evidence and fact-checking log

| Claim | Evidence | Verification status | What NOT to claim |
|---|---|---|---|
| GitHub Copilot desktop app generally available June 17, 2026 | S1, official GitHub changelog | Checked against primary source | It replaced all traditional development environments |
| Agent workflow can start from issue, PR, prompt, separate worktrees and lead to reviewed PR | S1 | Checked | Agents always deliver correct, deployable code |
| 90% weekly, 68% daily usage among surveyed professional developers in May–July 2026 | S2, JetBrains methodology | Checked | 90% of all developers globally, or 90% gain in productivity |
| NBER +240% commits vs. +30% releases after autonomous-agent adoption in estimated cumulative effects | S3, May working paper revised Sept 2026 | Checked via abstract | 240% faster coding for everyone, or 30% more jobs |
| Programmers need tests and review | Interpretation supported by workflow evidence and standard engineering reasoning | Interpretive conclusion | Independently proven universal claim by our small demo |

## Questions for the team to investigate before publishing

1. Was the survey weighted, and what job roles were included? Explain 'surveyed professional developers'.
2. How does an AI agent differ from autocompletion? Show tool actions rather than just conversational output.
3. Does our code demo show a real observed fix? Capture the before/after tests and the diff.
4. Does the script distinguish industry data from our opinion?
5. Does every numerical statistic have an on-slide or written citation?

## Actual research process log (team must complete)

| Date | Member | Tool / source | Research action | AI suggestion checked? | Change made / correction |
|---|---|---|---|---|---|
| [27-11-26] | [jasmeen kaur] | [chatgpt+jetbrainsofficial source(S2)] | [verified the 90%weekly and 68% daily AI coding-agent adoption statistics] | [yes, checked against the original source] | [Confirmed that the statistics refer to surveyed professional developers, not all developers worldwide.] |
| [27-11-26] | [jasmeen kaur] | [	ChatGPT + NBER Working Paper S3] | [Checked the productivity estimates for commits, projects and software releases.] | [Yes, checked against the NBER paper] | [Clarified that +240% commits, +80% projects and +30% releases are estimated cumulative effects, not guaranteed productivity gains.] |

**Reflection tip:** Write down one real instance where an AI answer was inaccurate or incomplete, then show the source or test that exposed it. Do not invent an error just to fill section B3.
