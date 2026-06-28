# Progress-Aware Multi-Agent Orchestrator

A Codex Skill for evidence-based multi-agent software delivery.

This repository packages a reusable orchestration skill that:

1. evaluates real project progress before dispatching agents;
2. separates verified facts from unverified claims;
3. generates structured development and acceptance documents;
4. classifies findings by root cause instead of blaming one agent by default;
5. creates focused correction rounds after reassessing the repository state.

## Default closed loop

```text
Structured Development Task Sheet
-> Implementation Agent execution
-> Structured Acceptance Sheet
-> Acceptance Agent review
-> Root-cause diagnosis
-> Next correction task sheet
```

Default role mapping:

```text
Planner / Orchestrator
- requirement synthesis
- verified project-state assessment
- agent dispatch decisions
- development task sheet generation
- acceptance sheet generation
- finding diagnosis
- next-round correction planning

Implementation Agent
- default example: Claude Code

Acceptance Agent
- default example: Codex
```

The mapping is illustrative, not hard-coded. Any agent can fill these roles.

## Repository layout

```text
.codex/
  skills/
    progress-aware-multi-agent-orchestrator/
      SKILL.md
      references/
        acceptance-sheet.md
        completion-envelope.md
        development-task-sheet.md
        diagnosis-policy.md
        dispatch-policy.md
        github-delivery.md
      scripts/
        validate_skill.py
examples/
  acceptance-sheet-example.md
  development-task-sheet-example.md
README.md
LICENSE
.gitignore
```

## What the skill enforces

- Dynamic readiness checks before every dispatch.
- Explicit agent states: `START_NOW`, `WAIT`, `PAUSE`, `RESUME`, `REVIEW`, `REPAIR`, `INTEGRATE`, `CANCEL`.
- Evidence categories: `VERIFIED`, `CLAIMED`, `UNKNOWN`, `CONTRADICTED`.
- Safe parallelism with file ownership, branch/worktree isolation, and an integration owner.
- A traceable chain from requirement to task sheet, implementation evidence, acceptance evidence, diagnosis, and correction.

## Validate

```bash
python .codex/skills/progress-aware-multi-agent-orchestrator/scripts/validate_skill.py
```

If your environment uses `python3` instead of `python`, run:

```bash
python3 .codex/skills/progress-aware-multi-agent-orchestrator/scripts/validate_skill.py
```

## Invoke

```text
Use $progress-aware-multi-agent-orchestrator to inspect the current repository,
state what is VERIFIED vs CLAIMED, decide which agent should start or wait, and
prepare the next structured development or acceptance document.
```

## Examples

- [Development task sheet example](examples/development-task-sheet-example.md)
- [Acceptance sheet example](examples/acceptance-sheet-example.md)

## License

MIT
