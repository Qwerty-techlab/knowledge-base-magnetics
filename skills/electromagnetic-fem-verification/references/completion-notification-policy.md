# Completion-notification policy for long FEM jobs

## Durable user workflow

For bounded CAD, mesh, solve, export, and audit processes with a defined end:

1. launch the process as a tracked background job;
2. enable exactly one completion notification;
3. do not repeatedly poll process existence or stdout merely to reassure the user;
4. on completion/error notification, perform one evidence-bearing read of the terminal artifact, solver profile, or structured report;
5. if the user asks for status before completion, perform one current-stage check and report exact evidence, then return to notification-based waiting;
6. never infer solver progress from process existence alone;
7. use sparse event-based monitoring only for genuinely unbounded services.

This policy conserves tokens and avoids noisy status messages while preserving honest stage reporting. It supersedes any instruction to poll a bounded background process "regularly" without a user status request or event trigger.
