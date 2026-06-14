# Final Audit

## 1. Chosen Thesis

Robot foundation models that emit language-like or discretized action tokens can be physically non-identifiable: one token may contain an action fiber whose members cause different next-state effects under local robot dynamics.

## 2. Field Assumption Broken

The broken assumption is action-token identity: if two motor commands share a language/action token, they are interchangeable for downstream control.

## 3. New Central Mechanism

Effect-Separating Action Charts (ESAC). ESAC audits each token by the physical effect diameter of its action fiber, then repairs aliased fibers by splitting them into charts using observed transition/effect signatures.

## 4. Literature Coverage

`docs/related_work_matrix.csv` contains 3,106 entries from OpenAlex/manual seeds. The run produced a 300-paper serious skim, a 250-paper extraction table, and a 100-paper hostile prior-work document. The closest hostile areas are VLA models, action tokenization, action chunking, diffusion/flow action policies, and language-conditioned robot grounding.

## 5. Proof/Formal-Claim Status

The paper proves a token-fiber lower bound: any decoder that observes only a token has worst-case one-step effect error at least half the effect diameter of that token fiber. This is a formal impossibility claim for collapsed token interfaces, not a theorem about all robot policies.

## 6. Final Evidence

The final full-scale run contains nine suites, 2,526 compact metric rows, and 2,005,200 evaluated predictions counted across rows. At alias strength 1.25, coarse token decoding reaches 0.140 success, raw action charts 0.605, ESAC hidden context 0.356, ESAC full context 0.728, continuous regression upper 0.998, and oracle expert 1.000.

## 7. Boundary Findings

ESAC needs the right conditions. Hidden alias context gives 0.356. Mode/contact corruption at 20% gives 0.582 and at 40% gives 0.440. Oracle mode/contact tokenization raises coarse token success to 0.760. Random effect metrics collapse performance to 0.156.

## 8. Biggest Weaknesses

- Evidence is synthetic only.
- No real-robot or real-VLA intervention is shown.
- ESAC requires transition/effect observations during audit/training.
- ESAC requires observable alias-resolving context at test time.
- The effect metric is task-dependent.
- Continuous-action policies can avoid this exact token bottleneck if they bypass many-to-one action tokenization.

## 9. Paper-Readiness Judgment

Final full-scale synthetic mechanism paper, ready under the batch standard. It should be framed as a mechanism and audit paper, not as a deployed robot/VLA result.

## 10. Exact Canonical PDF Path

`C:/Users/wangz/Downloads/06.pdf`

Verified page count: 25 pages.

Verified PDF size: 940,447 bytes.

## 11. GitHub URL

`https://github.com/Jason-Wang313/06_action_aliasing_in_robot_foundation_models`
