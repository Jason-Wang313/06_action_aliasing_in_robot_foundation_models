# Action Aliasing in Robot Foundation Models

This repository contains the paper run for assigned paper `06_action_aliasing_in_robot_foundation_models`.

## Thesis

Robot foundation models that emit language-like or discretized action tokens can be physically non-identifiable: a single token may contain an action fiber whose members cause different next-state effects under local robot dynamics. The proposed repair is Effect-Separating Action Charts (ESAC), which audits each token by effect diameter and splits aliased token fibers by observed transition signatures.

## Main Artifacts

- Paper source: `paper/main.tex`
- Compiled paper: `paper/main.pdf`
- Required final PDF copy: `C:/Users/wangz/Downloads/06.pdf`
- Literature matrix: `docs/related_work_matrix.csv` with 3106 entries
- Literature synthesis: `docs/literature_map.md`, `docs/hostile_prior_work.md`, `docs/novelty_boundary_map.md`, `docs/novelty_decision.md`
- Claims/audit docs: `docs/claims.md`, `docs/reviewer_attacks.md`, `docs/final_audit.md`
- Evidence script: `scripts/run_experiments.py`
- Results: `results/sweep_results.csv`, `results/experiment_summary.md`
- Figures: `figures/aliasing_sweep.*`, `figures/alias_energy_failure.*`, `figures/token_fiber_example.*`

## Reproduce Experiments

```powershell
pip install -r requirements.txt
python scripts/run_experiments.py
```

## Rebuild Paper

The paper uses the official ICLR 2026 style files from `https://github.com/ICLR/Master-Template/raw/master/iclr2026.zip`, copied into `paper/`.

```powershell
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Rebuild Literature Artifacts

The literature builder queries OpenAlex and may take a few minutes:

```powershell
python scripts/build_literature.py
python scripts/synthesize_literature.py
```

The current run used metadata and available abstracts at scale; it did not manually read every full PDF.
