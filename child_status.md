# Child Status: 06_action_aliasing_in_robot_foundation_models

## Current Stage

Stage 9: final full-scale pass complete. This changeset records the 25-page final manuscript, full-scale evidence, refreshed docs, and verified canonical PDF.

## Last Completed Step

- Compiled the final manuscript to 25 pages.
- Verified `C:/Users/wangz/Downloads/06.pdf` at 940,447 bytes.
- Verified expected text claims in the canonical PDF: 2,526 compact metric rows, 2,005,200 evaluated predictions, coarse token 0.140, ESAC full context 0.728, ESAC hidden context 0.356.
- Verified no stale hardening/workshop markers in extracted final PDF text.

## Full-Scale Evidence

- Runner: `scripts/run_full_scale_experiments.py`
- Compact metric rows: 2,526
- Evaluated predictions counted across rows: 2,005,200
- Main/context suites: 10 seeds
- Breadth suites: 8 seeds
- Figures: `paper/figures/*.png`

## Main Alias Strength 1.25 Result

- Coarse token: 0.140
- Raw action charts: 0.605
- ESAC hidden context: 0.356
- ESAC full context: 0.728
- Continuous regression upper: 0.998
- Oracle expert: 1.000

## Final PDF

- Canonical path: `C:/Users/wangz/Downloads/06.pdf`
- Page count: 25
- Size: 940,447 bytes

## Next Step

- Proceed to paper 07 after this final full-scale changeset is pushed.
