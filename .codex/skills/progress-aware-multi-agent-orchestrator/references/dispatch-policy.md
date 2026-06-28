# Dispatch Policy

## Default software delivery sequence

1. Planner issues a structured development task sheet.
2. Implementation agent executes it.
3. Planner verifies implementation evidence is sufficient.
4. Planner issues a structured acceptance sheet.
5. Acceptance agent independently validates.
6. Planner classifies findings.
7. Planner issues a focused correction task sheet.
8. Reassess the repository state before any next dispatch.
9. Repeat until acceptance.

## Required dispatch summary

Before showing multiple agent prompts, state:

- current stage;
- agents that start now;
- agents that wait;
- the trigger for each waiting agent;
- the handoff package for each agent;
- the conflict-prevention method;
- the final integration owner.

## Exceptions

Parallelize only when workstreams are independent and ownership is isolated.

Do not start acceptance before:

- the target commit or artifact is known;
- the implementation report is available;
- the acceptance baseline is stable.

Do not start repair before:

- findings are classified;
- the correct owner is identified;
- stale or invalid requirements are resolved.
