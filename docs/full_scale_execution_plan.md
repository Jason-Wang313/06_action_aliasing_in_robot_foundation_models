# Full-Scale Execution Plan

Paper 06: Action Aliasing in Robot Foundation Models

## Current Claim

The current paper claims that robot foundation models or VLA-style systems that emit language-like/discretized action tokens can be physically non-identifiable. A single token may denote a fiber of low-level motor commands whose members induce different next-state effects under local robot dynamics. The proposed repair is Effect-Separating Action Charts (ESAC): audit each token by effect diameter and split aliased token fibers by observed transition signatures.

The existing artifact is a 6-page v2 manuscript. Its strongest result is a synthetic contact-control experiment at alias strength 1.25: coarse token decoding reaches 0.148 success, raw action charts 0.631, ESAC with full alias context 0.743, ESAC with hidden alias context 0.374, continuous regression upper 1.000, and oracle replay 0.999. The v2 hardening added a context-corruption stress: ESAC falls from 0.742 clean success to 0.605 at 20% corrupted mode/contact context, 0.443 at 40%, and 0.377 when the alias context is hidden.

This is a crisp mechanism, but it is far below the final batch standard. It has too little experimental scope, too few stress tests, no broad ablations over chart count/token granularity/data scale/effect metrics, and too much draft-history language in the manuscript.

## Main Gaps To Close

1. The current PDF is only 6 pages; final target is at least 25 pages with real content, not padding.
2. Evidence currently depends on one synthetic environment family, one train/test size, one token bin count, one ESAC chart count, and one context-corruption stress.
3. The paper needs stronger boundary controls showing when token aliasing disappears, when ESAC should match coarse tokens, and when continuous policies bypass the bottleneck.
4. The paper needs stronger negative controls showing ESAC fails when alias-resolving variables are absent, corrupted, shifted, or when the effect metric is wrong.
5. The paper needs ablations over token granularity, chart count, sample size, context feature availability, observation noise, dynamics/embodiment shift, effect-threshold sensitivity, and effect-metric misspecification.
6. The paper should report compact row counts, evaluated test counts, suite descriptions, figures, tables, formal details, failure narratives, and reproducibility commands.
7. The final manuscript must remove internal hardening/version/workshop language and read like a paper.

## Target Experiments

1. Main alias-strength sweep
   - Alias strengths from 0.0 to at least 1.75.
   - Multiple deterministic seeds.
   - Methods: coarse token, raw action charts, ESAC full context, ESAC hidden context, continuous regression upper, oracle replay.
   - Metrics: success, effect RMSE, action RMSE, alias energy, mean chart effect radius, chart count.

2. Context reliability taxonomy
   - Flip rates for mode/contact context from 0% through 60% plus hidden-context ablation.
   - Separate corruption of mode only, contact only, both, and random Gaussian feature noise.
   - Report when ESAC collapses toward hidden-context performance.

3. Token granularity sweep
   - Vary cardinal token bins, e.g. 4, 8, 16, 32.
   - Show that too-coarse tokens have large effect diameter, while sufficiently fine/oracle tokens reduce the failure.
   - Include an oracle tokenization that includes alias-resolving mode/contact context as a boundary control.

4. Chart-count and charting-space ablation
   - Sweep charts per token, e.g. 1, 2, 3, 4, 6.
   - Compare effect-space charts, raw-action charts, random charts, and token-only prototypes.
   - Report diminishing returns and over-splitting risk.

5. Data-scale sweep
   - Vary train rows/test rows while keeping memory bounded.
   - Confirm ESAC improves with enough transitions but degrades when chart predictors are data-starved.
   - Use compact summary rows only.

6. Dynamics and embodiment shift
   - Train at one alias-strength/friction/embodiment distribution and test under shifted friction, shifted embodiment mix, or shifted alias strength.
   - Distinguish representation repair from distribution-robust control.

7. Effect metric sensitivity
   - Compare task-relevant object-effect metric, raw action metric, partial-effect metric, and intentionally wrong/noisy effect metric.
   - Show ESAC depends on measuring the right physical effect.

8. Success-threshold sensitivity
   - Sweep one-step effect-error thresholds.
   - Report curves or tables so the main result is not tied to 0.36 only.

9. Alias-energy diagnostic calibration
   - Correlate within-token effect radius with coarse-token failure across suites.
   - Include calibration bins or rank correlation.
   - Show alias energy is a diagnostic, not merely a plotting variable.

10. Negative controls
   - Alias strength 0: coarse tokens should be much less damaged.
   - Oracle tokenization: adding mode/contact to the token should reduce or remove aliasing.
   - Hidden alias context: ESAC cannot recover reliable chart choice.
   - Random effect labels or wrong metric: charting without the right effect signal should not look like ESAC.

## Baselines And Comparators

Required methods:

1. Coarse token prototype.
2. Raw action charts.
3. Random charts within token.
4. ESAC effect charts with full context.
5. ESAC effect charts with hidden alias context.
6. ESAC under corrupted alias context.
7. Oracle tokenization that includes mode/contact.
8. Continuous regression upper baseline.
9. Oracle expert replay.

Optional if lightweight:

1. Larger random forest continuous upper.
2. Nearest-neighbor transition-effect decoder.
3. Chart predictor variants such as decision tree vs random forest classifier.

## Figures And Tables

Target final figures:

1. Main alias-strength success sweep.
2. Alias energy versus coarse-token/ESAC failure.
3. Token-fiber example showing one token with multiple physical effect clusters.
4. Context reliability stress.
5. Token granularity sweep.
6. Chart-count ablation.
7. Data-scale sweep.
8. Dynamics/embodiment shift.
9. Effect metric sensitivity.
10. Threshold sensitivity.

Target tables:

1. Main operating-point table at alias strength 1.25.
2. Full-scale artifact inventory and compact row counts.
3. Boundary controls and their interpretation.
4. Negative controls and failure modes.
5. Reproducibility commands.

## Writing Expansion Plan

The final manuscript should be rewritten as a full-scale mechanism paper:

1. Remove internal hardening/version lines.
2. Expand the introduction with the action-token identity assumption and why it matters for robot foundation models.
3. Deepen related work around VLA action tokenization, action chunking, continuous policies, contact-rich control, affordance grounding, and representation identifiability.
4. Add formal definitions for token fibers, effect diameter, alias energy, chart splits, oracle tokenization, and metric misspecification.
5. Add a fuller theorem/proposition section with lower-bound proof and practical diagnostic implications.
6. Add an ESAC algorithm box or step-by-step recipe.
7. Add full suite descriptions, figures, tables, and interpretation.
8. Add boundary controls, failure narratives, and what would falsify the claim.
9. Add implementation guidance for auditing real VLA datasets.
10. Add reproducibility statement, artifact inventory, and appendix material.

## RAM-Light Execution Strategy

1. Run suites sequentially from one full-scale script.
2. Keep `n_jobs=1` for sklearn models unless a lightweight local parallelism test is explicitly needed.
3. Store only compact per-condition metric rows plus summary JSON and figures.
4. Do not store raw train/test arrays or per-trial trajectories.
5. Reuse suite helpers and avoid keeping all datasets in memory at once.
6. Use modest train/test sizes per condition but many conditions/seeds for breadth.
7. Use deterministic seeds and stable CSV ordering.

## Final Acceptance Checklist

1. `docs/full_scale_execution_plan.md` exists before any other paper-06 edits.
2. Full-scale runner produces compact outputs and summary JSON.
3. Final result set includes main positives, boundary controls, and negative controls.
4. Manuscript compiles cleanly with no unresolved references/citations, fatal errors, or overfull boxes that materially damage layout.
5. Final manuscript is at least 25 pages.
6. Extracted PDF text contains the full-scale scale/result claims and no internal hardening/workshop/version markers.
7. `C:/Users/wangz/Downloads/06.pdf` is overwritten only after the final manuscript satisfies the threshold.
8. Docs/logs/readme/reproducibility/audits are updated to the final full-scale state.
9. Local `paper/main.pdf` is removed after copying the final canonical PDF.
10. Repo is committed, pushed, clean, and upstream-matched before moving to paper 07.
