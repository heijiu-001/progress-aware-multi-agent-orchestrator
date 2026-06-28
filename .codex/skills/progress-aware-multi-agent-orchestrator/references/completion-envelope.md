# Agent Completion Envelopes

## Implementation

```yaml
agent:
role: implementation
task_id:
round:
status: completed | partial | blocked | failed
base_commit:
result_commit:
changed_files:
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

## Acceptance

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
unverified_risks:
acceptance_decision:
recommended_next_step:
```
