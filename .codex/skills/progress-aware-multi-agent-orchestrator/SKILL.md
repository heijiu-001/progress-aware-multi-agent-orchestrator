---
name: progress-aware-multi-agent-orchestrator
description: Coordinate two or more AI agents according to verified project progress, while enforcing a structured development, acceptance, diagnosis, and correction loop. Use when software work must be divided among implementation, review, testing, integration, or repair agents, and when dispatch order, timing, dependencies, handoffs, acceptance criteria, or next-round corrections must be explicit.
---

# Progress-Aware Multi-Agent Orchestrator

Coordinate multiple agents from verified project evidence, not from a fixed queue.

This skill combines two layers:

1. **Dynamic orchestration**: decide which agents should start, wait, pause, review, repair, integrate, or be cancelled based on the actual project state.
2. **Closed-loop delivery**: convert user intent into a structured development task sheet, verify implementation with a structured acceptance sheet, diagnose the source of defects, and generate the next correction task sheet.

## Default role mapping

Use these defaults when the user does not specify otherwise:

- **Planner / Orchestrator**: converts user intent into structured tasks, controls dispatch, evaluates results, performs diagnosis, and issues correction rounds.
- **Implementation Agent**: typically Claude Code; performs implementation strictly against the task sheet.
- **Acceptance Agent**: typically Codex; independently validates implementation against requirements and produces evidence.
- **Specialist Agents**: optional agents for security, performance, UI, backend, database, documentation, migration, integration, or repair.

Do not hard-code vendors. If the user names different agents, map them to the same roles.

## Primary closed-loop workflow

Use this default four-stage loop:

```text
Stage 1: Structured development task sheet
-> Stage 2: Implementation against the sheet
-> Stage 3: Structured acceptance and testing
-> Stage 4: Diagnosis and next correction task sheet
-> repeat until accepted
```

The loop is not mechanically linear. Before every dispatch, inspect the actual project state and re-evaluate whether the next stage is ready.

## Non-negotiable rules

1. Do not output loose implementation instructions when a structured task sheet is required.
2. Do not send acceptance instructions before implementation prerequisites are met.
3. Do not treat an implementation agent's "done" statement as verified completion.
4. Do not allow an implementation agent to silently change requirements, architecture, public interfaces, or data contracts.
5. Do not ask the acceptance agent to repair defects unless the user explicitly assigns a repair role.
6. Do not merge requirement defects, specification defects, and implementation defects into one undifferentiated problem list.
7. Do not reuse stale prompts after repository state, requirements, tests, or agent outputs have changed.
8. Before displaying multiple agent prompts, state the send order, timing, dependencies, and waiting conditions.
9. After every meaningful result, reassess the project before releasing the next stage.
10. Preserve a traceable chain from user requirement -> task sheet -> implementation evidence -> acceptance evidence -> diagnosis -> correction task.

## Operating state machine

Run this cycle:

```text
OBSERVE
-> VERIFY
-> PLAN
-> DISPATCH
-> IMPLEMENT
-> ACCEPT
-> DIAGNOSE
-> CORRECT
-> REASSESS
```

A project may re-enter `PLAN`, `IMPLEMENT`, `ACCEPT`, or `CORRECT` depending on evidence.

## 1. OBSERVE

Collect the latest available evidence:

- user requirements and latest clarifications;
- current repository tree;
- relevant source files;
- branch, worktree, base commit, and dirty state;
- recent commits and diffs;
- build, lint, type-check, test, and runtime results;
- screenshots, logs, bug reports, open issues, and TODOs;
- previous task sheets;
- previous agent reports;
- changed architecture decisions;
- pending merge conflicts;
- current file ownership;
- current blockers;
- current critical path.

Record the evidence baseline when available.

## 2. VERIFY

Classify each important project statement as:

- `VERIFIED`: confirmed by repository state, executable checks, or directly inspected artifacts;
- `CLAIMED`: reported by an agent but not independently confirmed;
- `UNKNOWN`: evidence is absent, stale, or incomplete;
- `CONTRADICTED`: current evidence conflicts with the claim.

Do not release downstream work based only on `CLAIMED`.

## 3. PLAN

Determine:

- the current critical path;
- work already completed and verified;
- work currently in progress;
- work that should not be repeated;
- blockers;
- tasks ready now;
- tasks waiting on dependencies;
- tasks that can run in parallel;
- tasks that would conflict;
- the most appropriate agent role for each task;
- whether the project is in development, recovery, verification, integration, or replanning mode.

## 4. Structured development task sheet

Before implementation, produce a task sheet containing all required sections.

### Required fields

```text
Document type: Structured Development Task Sheet
Task ID:
Round:
Target agent:
Dispatch status: START_NOW | WAIT | PAUSE | RESUME | CANCEL

1. Core objective
2. Current verified project state
3. Prerequisites and dependencies
4. Technical constraints
5. Input definitions
6. Output definitions
7. Functional scope
8. Explicit non-goals
9. Editable files or directories
10. Read-only files or directories
11. Architecture and interface constraints
12. Implementation steps
13. Validation requirements
14. Completion criteria
15. Stop and ambiguity rules
16. Required delivery format
17. Handoff destination
```

### Implementation agent behavior

The implementation agent must:

- follow the task sheet exactly;
- avoid changing requirements, architecture, interfaces, or data contracts without explicit approval;
- report ambiguity before proceeding when ambiguity affects correctness;
- avoid unrelated refactoring;
- avoid modifying out-of-scope files;
- run required validations;
- return the required completion envelope.

When safe progress is possible despite a minor ambiguity, the agent may complete the unambiguous portion and mark the rest as blocked.

## 5. DISPATCH

Before prompts, output:

```text
Dispatch mode:
Current stage:
Send now:
Wait:
Trigger for each waiting agent:
Required handoff package:
Conflict-prevention method:
Final integration owner:
```

Allowed agent statuses:

- `START_NOW`
- `WAIT`
- `PAUSE`
- `RESUME`
- `REVIEW`
- `REPAIR`
- `INTEGRATE`
- `CANCEL`

Every prompt heading must state its actual send timing.

## 6. IMPLEMENT

Require the implementation agent to return:

```yaml
agent:
role: implementation
task_id:
round:
status: completed | partial | blocked | failed
base_commit:
result_commit:
changed_files:
unchanged_required_files:
commands_run:
validation_results:
requirements_implemented:
requirements_not_implemented:
ambiguities_found:
scope_deviations:
unresolved_issues:
handoff_artifacts:
recommended_next_step:
```

A missing commit hash is acceptable only when the environment does not use Git; the agent must explain why.

## 7. Structured acceptance sheet

Only dispatch acceptance when implementation evidence is sufficient.

The acceptance sheet must include:

```text
Document type: Structured Acceptance Sheet
Acceptance ID:
Related Task ID:
Round:
Target agent:
Dispatch status: START_NOW | WAIT

1. Original requirement summary
2. Development task sheet baseline
3. Repository or commit under test
4. Changed-file scope
5. Build and syntax checks
6. Functional requirement matching
7. Boundary and exception coverage
8. Regression checks
9. Security checks
10. Performance checks
11. Data integrity and migration checks
12. Interface and compatibility checks
13. Required runnable tests
14. Evidence collection requirements
15. Severity definitions
16. Required issue list format
17. Repair recommendation format
18. Acceptance decision criteria
19. Prohibited actions
20. Delivery format
```

### Acceptance agent behavior

The acceptance agent must:

- independently inspect the implementation;
- compare behavior against the original requirement and task sheet;
- run executable checks where possible;
- produce runnable tests when requested and feasible;
- distinguish verified defects from suspicions;
- avoid changing production code unless explicitly assigned a repair task;
- rank findings by severity;
- return a final acceptance decision.

### Severity levels

Use:

- `BLOCKER`: cannot build, run, migrate, or preserve critical data;
- `CRITICAL`: security, data corruption, severe correctness, or release-stopping defect;
- `HIGH`: major required behavior missing or materially incorrect;
- `MEDIUM`: partial mismatch, weak edge handling, meaningful maintainability or performance risk;
- `LOW`: minor behavior, documentation, naming, or polish issue;
- `INFO`: observation that is not currently a defect.

## 8. Acceptance result envelope

Require:

```yaml
agent:
role: acceptance
acceptance_id:
related_task_id:
round:
status: accepted | rejected | accepted_with_conditions | blocked
tested_commit:
commands_run:
build_result:
syntax_result:
functional_result:
boundary_result:
exception_result:
security_result:
performance_result:
regression_result:
tests_added_or_proposed:
findings:
  - id:
    severity:
    category:
    evidence:
    expected:
    actual:
    affected_files:
    reproduction:
    recommendation:
unverified_risks:
acceptance_decision:
recommended_next_step:
```

## 9. DIAGNOSE

After acceptance, classify each finding into exactly one primary cause:

- `REQUIREMENT_DEFECT`: the user requirement is incomplete, contradictory, infeasible, or missing a decision;
- `SPECIFICATION_DEFECT`: the development task sheet or acceptance standard is ambiguous, incomplete, inconsistent, or technically wrong;
- `IMPLEMENTATION_DEFECT`: the code does not correctly implement a valid and sufficiently clear specification;
- `TEST_DEFECT`: the test or acceptance method is invalid, flaky, incomplete, or inconsistent with the agreed behavior;
- `ENVIRONMENT_DEFECT`: tooling, dependency, platform, credentials, infrastructure, or runtime environment caused the failure;
- `INTEGRATION_DEFECT`: individually valid components fail at boundaries, contracts, merge points, or deployment integration;
- `UNKNOWN`: available evidence is insufficient.

Do not assign blame without evidence.

For each finding, produce:

```text
Finding ID:
Primary cause:
Contributing cause:
Evidence:
Why this classification fits:
Owner of next action:
Required clarification or repair:
Blocks release: yes/no
```

## 10. CORRECT

Generate the next round according to diagnosis:

### For REQUIREMENT_DEFECT

- ask or resolve the missing product decision;
- update the requirement baseline;
- invalidate stale task or acceptance instructions;
- generate a revised development task sheet only after the requirement is stable.

### For SPECIFICATION_DEFECT

- correct the task sheet, acceptance criteria, interfaces, boundaries, or delivery format;
- identify which prior instructions are superseded;
- generate a replacement task sheet.

### For IMPLEMENTATION_DEFECT

- generate a focused correction task sheet;
- include exact findings, evidence, affected files, expected behavior, regression requirements, and non-goals;
- avoid reopening unrelated completed work.

### For TEST_DEFECT

- repair or replace the tests or acceptance procedure;
- do not modify valid production behavior merely to satisfy an invalid test.

### For ENVIRONMENT_DEFECT

- isolate environmental remediation;
- avoid code changes unless the code genuinely lacks required portability or resilience.

### For INTEGRATION_DEFECT

- designate an integration owner;
- define interface baselines and merge order;
- require integration and regression checks.

### For UNKNOWN

- generate an evidence-gathering or investigation task;
- define the missing proof needed before repair work starts.

## 11. Dynamic orchestration policy

Select a mode based on actual progress:

- `RECOVERY`
- `REPLANNING`
- `FULLY_SEQUENTIAL`
- `FULLY_PARALLEL`
- `PARALLEL_BY_WORKSTREAM`
- `PARALLEL_THEN_INTEGRATE`
- `STAGED_PIPELINE`
- `REVIEW_REPAIR_LOOP`

Default priority:

1. safety and data-loss risk;
2. broken build or critical runtime path;
3. conflicts and integration blockers;
4. verification of claimed completion;
5. critical-path implementation;
6. independent parallel work;
7. integration;
8. documentation, cleanup, and optimization.

## 12. File ownership and parallel safety

For every active agent define:

```text
Agent:
Branch/worktree:
Base commit:
Editable:
Read-only:
Forbidden:
Integration owner:
```

Parallel agents must not edit overlapping files unless:

1. the overlap is intentional;
2. an integration owner is assigned;
3. merge order is defined;
4. conflict-resolution and regression checks are specified.

## 13. Reassessment checkpoints

Re-run `OBSERVE -> VERIFY -> PLAN` after:

- any new commit or diff;
- any failed build, test, or runtime check;
- any `partial`, `blocked`, or `failed` agent result;
- a requirement clarification;
- an architecture or interface change;
- a file ownership conflict;
- a merge conflict;
- an acceptance rejection;
- a user priority change;
- evidence that a task is stale or already completed.

Do not automatically release the next queued instruction.

## Required response order

When preparing multi-agent work, output:

1. Current verified project state
2. Workflow stage
3. Readiness and dependency table
4. Dispatch decision
5. Dispatch rationale
6. File ownership and isolation
7. Timeline and trigger conditions
8. Structured development or acceptance documents
9. Handoff package
10. Reassessment checkpoint
11. User execution checklist

## User execution checklist

```text
[ ] The current stage is explicit
[ ] The project state is evidence-based
[ ] I know which instruction to send now
[ ] I know which instruction must wait
[ ] Every waiting instruction has a verifiable trigger
[ ] The implementation task sheet is complete
[ ] The acceptance sheet is tied to the correct task and commit
[ ] Findings will be classified by root cause
[ ] The next correction round will not reopen unrelated work
[ ] The plan will be reassessed after new evidence
```

## Supporting references

Use as needed:

- `references/development-task-sheet.md`
- `references/acceptance-sheet.md`
- `references/diagnosis-policy.md`
- `references/completion-envelope.md`
- `references/dispatch-policy.md`
- `references/github-delivery.md`

Run `scripts/validate_skill.py` before publication.
