# Research brief: coding agents as a 2026 current event

## Focus

**Topic:** How AI coding agents are changing the software development workflow in 2026.  
**Audience:** Computer Programming and Analysis students who understand basic programs, tests, Git and pull requests.  
**Position:** Neither 'AI will replace all programmers' nor 'AI changes nothing'. Ask what work is delegated and what must still be checked.

## What is an AI coding agent?

An AI coding agent is a tool that can take a task description and carry out a multi-step software-development workflow using codebase context. Depending on the product and permissions, this may include inspecting files, editing code, executing tests, writing summaries and proposing a pull request. This is more active than a basic chat response that only suggests a code snippet.

## Timeline and evidence

**June 17:** GitHub made its agent-centric Copilot desktop app generally available, providing a concrete 2026 product milestone (S1).  
**May–July data, reported August:** JetBrains survey reported weekly adoption of 90% and daily adoption of 68% among respondents, giving a sense of uptake (S2).  
**September revision:** NBER examined whether more code became more software releases, reporting much larger growth in commits than releases (S3).

## The key tension

Coding agents can handle some implementation work, but writing code is not identical to shipping reliable software. Developers must decide what to build, test behavior against requirements, understand unexpected failures, inspect edits, and own the result. These responsibilities are a reason to emphasize programming fundamentals alongside AI-tool literacy.

## A concrete 20-second example

- The team gave an agent a simple Python discount function plus unit tests.
- Existing implementation passed ordinary inputs but mishandled empty lists, negative prices and invalid discounts.
- The agent was asked to update the function, run `python3 -m unittest discover -s tests -v`, and show the diff.
- The team reviewed the output rather than merely accepting the agent's assertion that the task is fixed.

## Implications beyond technology

**Benefits:** Faster first drafts and repetitive edits; potentially lower entry barriers for prototyping.  
**Risks and tradeoffs:** Incorrect behavior, overlooked edge cases, insecure changes, unreviewed dependencies, overreliance and lack of understanding.  
**For CPA students:** Learn programming logic, data structures, testing, debugging, Git workflows and requirement analysis. Learn to interrogate AI-generated solutions rather than treating them as authoritative.

## Evidence caution

- Vendor release notes describe features, not independently measured outcomes.
- Self-reported survey adoption does not equal quality, speed or job displacement.
- The NBER working paper measures development activity and output, not the number of jobs created or destroyed.
- The project demo is **one small illustration**, not scientific evidence of average AI coding-agent performance.

## Final discussion prompt

If AI agents can generate, debug and test software, which programming skills should colleges prioritize to prepare the next generation of developers?
