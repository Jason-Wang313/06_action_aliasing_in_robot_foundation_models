# Action Aliasing in Robot Foundation Models

This repository contains the final full-scale paper package for assigned paper `06_action_aliasing_in_robot_foundation_models`.

## Thesis

Robot foundation models that emit language-like or discretized action tokens can be physically non-identifiable: a single token may contain an action fiber whose members cause different next-state effects under local robot dynamics. The proposed repair is Effect-Separating Action Charts (ESAC), which audits each token by effect diameter and splits aliased token fibers by observed transition signatures.

## Final Artifact

- Canonical PDF: `C:/Users/wangz/Downloads/06.pdf`
- Verified page count: 25 pages
- Verified PDF size: 940,447 bytes
- Full-scale compact metric rows: 2,526
- Evaluated predictions counted across rows: 2,005,200

## Main Artifacts

- Paper source: `paper/main.tex`
- Full-scale runner: `scripts/run_full_scale_experiments.py`
- Original simulator: `scripts/run_experiments.py`
- Full-scale results: `results/full_scale/`
- Paper figures: `paper/figures/`
- Literature matrix: `docs/related_work_matrix.csv` with 3,106 entries
- Literature synthesis: `docs/literature_map.md`, `docs/hostile_prior_work.md`, `docs/novelty_boundary_map.md`, `docs/novelty_decision.md`
- Claims/audit docs: `docs/claims.md`, `docs/reviewer_attacks.md`, `docs/final_audit.md`

## Full-Scale Main Result

At alias strength 1.25 in the final main suite:

- Coarse token: 0.140 success
- Raw action charts: 0.605 success
- ESAC hidden context: 0.356 success
- ESAC full context: 0.728 success
- Continuous regression upper: 0.998 success
- Oracle expert: 1.000 success

The supported claim is narrow: action-token interfaces need physical effect audits when many-to-one tokenization collapses commands whose effects matter for control. ESAC requires transition effects during audit/training, a task-relevant effect metric, and observable alias-resolving context at test time.

## Reproduce Full-Scale Evidence

Run suites sequentially to keep memory usage light:

```powershell
python scripts/run_full_scale_experiments.py --suite main --seed-scale 10 --train-rows 2600 --test-rows 1000 --fresh
python scripts/run_full_scale_experiments.py --suite context --seed-scale 10 --train-rows 2600 --test-rows 1000
python scripts/run_full_scale_experiments.py --suite token --seed-scale 8 --train-rows 1600 --test-rows 700
python scripts/run_full_scale_experiments.py --suite charts --seed-scale 8 --train-rows 1600 --test-rows 700
python scripts/run_full_scale_experiments.py --suite data --seed-scale 8 --train-rows 1600 --test-rows 700
python scripts/run_full_scale_experiments.py --suite shift --seed-scale 8 --train-rows 1600 --test-rows 700
python scripts/run_full_scale_experiments.py --suite metric --seed-scale 8 --train-rows 1600 --test-rows 700
python scripts/run_full_scale_experiments.py --suite threshold --seed-scale 8 --train-rows 1600 --test-rows 700
python scripts/run_full_scale_experiments.py --suite negative --seed-scale 8 --train-rows 1600 --test-rows 700
python scripts/run_full_scale_experiments.py --suite summarize --seed-scale 8 --train-rows 1600 --test-rows 700
```

## Rebuild Paper

```powershell
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```
