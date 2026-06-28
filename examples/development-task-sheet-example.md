# Development Task Sheet Example

## Dispatch context

```text
Dispatch mode: PARALLEL_BY_WORKSTREAM
Current stage: Stage 1 - Structured development task sheet
Send now:
- Claude Code implementation task DEV-004
Wait:
- Codex acceptance task ACC-004
Trigger for each waiting agent:
- Send ACC-004 only after DEV-004 returns a completion envelope with a tested commit
Required handoff package:
- DEV-004 task sheet
- base commit
- changed-file scope
- validation commands
Conflict-prevention method:
- Claude Code may edit src/audio/** and tests/audio/**
- Codex remains read-only until acceptance dispatch
Final integration owner:
- Planner / Orchestrator
```

## Structured sheet

```text
Document type: Structured Development Task Sheet
Task ID: DEV-004
Round: 2
Target agent: Claude Code
Dispatch status: START_NOW

1. Core objective
Repair alarm audio selection without changing the public scheduling API.

2. Current verified project state
- VERIFIED: alarm creation works on the current main branch.
- VERIFIED: existing scheduling tests pass.
- CLAIMED: custom audio path persistence is implemented.
- CONTRADICTED: manual inspection shows invalid paths are not handled safely.
- UNKNOWN: behavior for deleted audio files after restart.

3. Prerequisites and dependencies
- Use the current main branch head as the base commit.
- Preserve the existing alarm schema.
- Reuse current audio validation helpers where possible.

4. Technical constraints
- No new runtime dependency.
- Keep current naming conventions.
- Do not change the public scheduler interface.

5. Input definitions
- User-selected local audio path.
- Existing persisted alarm records.

6. Output definitions
- Validated stored audio reference.
- Safe fallback behavior for invalid or missing files.
- Updated automated tests for required edge cases.

7. Functional scope
- Validate selected path on save and load.
- Persist valid selection.
- Use default sound when the saved reference becomes invalid.

8. Explicit non-goals
- No audio player redesign.
- No settings UI refactor.
- No unrelated scheduling cleanup.

9. Editable files or directories
- src/audio/**
- tests/audio/**

10. Read-only files or directories
- src/scheduling/public_api.py
- docs/api/**

11. Architecture and interface constraints
- Do not change the scheduler interface.
- Do not change the alarm persistence contract.

12. Implementation steps
- Inspect the current audio selection and load path.
- Add validation for missing, unreadable, and deleted files.
- Preserve valid existing records.
- Add focused regression tests for fallback behavior.

13. Validation requirements
- Run project-standard test commands for audio and scheduling.
- Run any syntax or type checks already used by the repository.

14. Completion criteria
- Valid paths persist correctly.
- Invalid or deleted paths fall back safely.
- Existing alarm scheduling behavior remains unchanged.

15. Stop and ambiguity rules
- Report any schema conflict before changing it.
- Stop and escalate if a fix requires API or data-contract changes.

16. Required delivery format
- Return the implementation completion envelope.

17. Handoff destination
- Planner / Orchestrator for acceptance preparation.
```
