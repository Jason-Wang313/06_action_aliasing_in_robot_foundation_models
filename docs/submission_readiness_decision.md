# Submission Readiness Decision

## Decision

Workshop-only.

## Rationale

The v2 paper is more defensible because it directly stress-tests the clean-context assumption behind ESAC. The result is honest: ESAC is useful when alias-resolving observations are reliable, but it degrades substantially under context corruption and nearly collapses when that context is hidden.

The paper is not ready for a main conference because all evidence is synthetic and no real RFM or VLA action-token interface is audited.

## Required Before Main-Conference Submission

- Audit action-token fibers in an existing RFM/VLA policy or tokenizer.
- Add real robot or high-fidelity simulator transitions with measured effect metrics.
- Report uncertainty over multiple random seeds.
- Compare against stronger token refinement and continuous-action alternatives.
