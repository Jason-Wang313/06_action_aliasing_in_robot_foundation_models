# Plan

## Operating rules
- Keep all work inside this repository unless writing the required final PDF to `C:/Users/wangz/Downloads/06.pdf`.
- Maintain `child_status.md` after every major stage with commands, failures, and recovery steps.
- Use non-interactive, failure-tolerant commands; wrap expected failures and record them instead of aborting.
- Prefer reusable scripts and cached artifacts over one-off shell probes.

## Stages
1. Initialize run metadata and status tracking.
2. Inspect existing repository state, available tools, and any cached artifacts from earlier attempts.
3. Build a broad literature corpus:
   - 1000-paper landscape sweep saved to `docs/related_work_matrix.csv`.
   - 300-paper serious skim.
   - 200-250-paper deep-read extraction.
   - 100-paper hostile prior-work set.
4. Synthesize the field box:
   - hidden assumptions, direction candidates, novelty boundary, hostile prior work, and reviewer attacks.
5. Choose the strongest paper idea only after the literature synthesis.
6. Build runnable evidence:
   - minimal simulation or analytic experiment demonstrating the broken assumption.
   - scripts, cached outputs, figures, and reproducibility notes.
7. Write an anonymous ICLR-style paper with honest claims and limitations.
8. Fetch or reconstruct the latest official ICLR LaTeX template available at runtime, then compile with direct `pdflatex`/`bibtex`.
9. Save final PDF to `C:/Users/wangz/Downloads/06.pdf`.
10. Create public GitHub repo `06_action_aliasing_in_robot_foundation_models`, commit, and push, documenting any authentication or network failure.
11. Write `docs/final_audit.md` answering all required audit questions.

## Expected artifacts
- `child_status.md`
- `docs/related_work_matrix.csv`
- `docs/literature_map.md`
- `docs/hostile_prior_work.md`
- `docs/novelty_boundary_map.md`
- `docs/novelty_decision.md`
- `docs/claims.md`
- `docs/reviewer_attacks.md`
- `docs/final_audit.md`
- runnable scripts and experiment outputs
- compiled anonymous ICLR-style paper
