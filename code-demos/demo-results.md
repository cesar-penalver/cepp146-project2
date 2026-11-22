# Demo Results - Prashanthi (Member 3)

## Prompt
"Fix calculate_average so it does not crash on empty list. Do not return a misleading value."

## First AI fix - WRONG
AI returned 0 for empty list.
Test PASSED but fix was WRONG - 0 hides "no data" as real average.

## Corrected fix
Changed to: raise ValueError("Cannot average an empty list")

## Test AFTER correction
- test_normal: PASSED
- test_empty_list: PASSED - correctly raises ValueError
- test_single_number: PASSED

## What I learned
Passing tests does not mean correct. I had to check the diff for meaning, not just syntax.

## Workflow we used
specify -> agent edits -> run tests -> inspect diff -> human approval
