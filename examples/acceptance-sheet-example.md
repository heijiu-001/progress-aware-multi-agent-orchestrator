# Acceptance Sheet Example

## Dispatch context

```text
Dispatch mode: REVIEW_REPAIR_LOOP
Current stage: Stage 3 - Structured acceptance and testing
Send now:
- Codex acceptance task ACC-004
Wait:
- Any repair task generated from accepted findings
Trigger for each waiting agent:
- Release repair only after findings are classified by root cause
Required handoff package:
- Original requirement summary
- DEV-004 task sheet
- implementation completion envelope
- tested commit
- changed-file list
- commands already run by implementation
Conflict-prevention method:
- Codex operates read-only for production files during acceptance
- Repair work, if needed, is assigned in a later round
Final integration owner:
- Planner / Orchestrator
```

## Structured sheet

```text
Document type: Structured Acceptance Sheet
Acceptance ID: ACC-004
Related Task ID: DEV-004
Round: 2
Target agent: Codex
Dispatch status: START_NOW

1. Original requirement summary
Custom alarm audio must persist and fall back safely when the selected file is invalid, missing, inaccessible, or deleted later.

2. Development task sheet baseline
DEV-004.

3. Repository or commit under test
<implementation commit from DEV-004 completion envelope>

4. Changed-file scope
src/audio/** and tests/audio/**

5. Build and syntax checks
Run project-standard checks and report exact commands.

6. Functional requirement matching
Verify valid, missing, inaccessible, and deleted audio paths.

7. Boundary and exception coverage
Test empty paths, unsupported files, permission errors, and restart behavior.

8. Regression checks
Confirm standard alarm sounds still work and alarm scheduling remains unchanged.

9. Security checks
Check path handling, unsafe file access, and trust boundaries around persisted file paths.

10. Performance checks
Check that validation does not block alarm scheduling or introduce repeated expensive filesystem work.

11. Data integrity and migration checks
Verify persisted references survive restart and do not corrupt existing alarm records.

12. Interface and compatibility checks
Confirm the scheduler public API and persistence contract are unchanged.

13. Required runnable tests
Add or provide executable tests for uncovered cases when feasible.

14. Evidence collection requirements
Include commands, outputs, inspected files, and reproduction steps for each finding.

15. Severity definitions
Use BLOCKER, CRITICAL, HIGH, MEDIUM, LOW, or INFO.

16. Required issue list format
Use structured findings with evidence, expected behavior, actual behavior, affected files, and recommendation.

17. Repair recommendation format
Give minimal targeted fixes and keep unrelated work closed.

18. Acceptance decision criteria
Accept only if required behavior and regressions pass with sufficient evidence.

19. Prohibited actions
Do not modify production code unless explicitly reassigned as a repair agent.

20. Delivery format
Return the acceptance envelope.
```
