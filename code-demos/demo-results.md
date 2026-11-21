# Demo Results - Prashanthi (Member 3) - Issue #7

## Prompt given to the AI agent
"Fix calculate_average in demo.py so it does not crash on an empty list. Keep the normal case working. Show me the diff."

## Test BEFORE agent fix
- test_normal: PASSED
- test_empty_list: FAILED - ZeroDivisionError: division by zero
- test_single_number: PASSED

## What the agent changed
- Added check: if not numbers: return 0
- I inspected the diff before approving.

## Test AFTER agent fix
- test_normal: PASSED
- test_empty_list: PASSED after fix
- test_single_number: PASSED

## What the agent MISSED
- The agent fixed the crash but did not explain why returning 0 is a design choice.
- I had to add the empty-list test myself.
- Human still needed to check the edge case.

## Workflow we used
specify -> agent edits -> run tests -> inspect diff -> human approval
