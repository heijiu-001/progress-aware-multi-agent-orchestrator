# Diagnosis Policy

Classify each finding into one primary cause:

- `REQUIREMENT_DEFECT`
- `SPECIFICATION_DEFECT`
- `IMPLEMENTATION_DEFECT`
- `TEST_DEFECT`
- `ENVIRONMENT_DEFECT`
- `INTEGRATION_DEFECT`
- `UNKNOWN`

## Decision guidance

### REQUIREMENT_DEFECT

Use when the requested behavior itself is missing, contradictory, infeasible, or undecided.

### SPECIFICATION_DEFECT

Use when the task sheet, acceptance sheet, boundary, interface, or delivery standard is deficient.

### IMPLEMENTATION_DEFECT

Use when a clear and valid requirement was implemented incorrectly or incompletely.

### TEST_DEFECT

Use when the acceptance method or test is invalid, flaky, incomplete, or inconsistent.

### ENVIRONMENT_DEFECT

Use when infrastructure, permissions, platform, dependency, or tooling is the primary cause.

### INTEGRATION_DEFECT

Use when components are individually acceptable but fail at contracts, merge points, or deployment boundaries.

### UNKNOWN

Use when evidence is insufficient. Assign an evidence-gathering task before repair.

## Required finding record

For each finding, provide:

- `Finding ID`
- `Primary cause`
- `Contributing cause`
- `Evidence`
- `Classification reason`
- `Next owner`
- `Required clarification or repair`
- `Blocks release`
