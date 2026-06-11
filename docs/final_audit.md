# Final Audit

1. Chosen thesis:
   Robot foundation models that emit language-like or discretized action tokens can be physically non-identifiable: one token may contain an action fiber whose members cause different next-state effects under local robot dynamics.

2. Field assumption broken:
   The broken assumption is action-token identity: if two motor commands share a language/action token, they are interchangeable for downstream control.

3. New central mechanism:
   Effect-Separating Action Charts (ESAC). ESAC audits each token by the physical effect diameter of its action fiber, then repairs aliased fibers by splitting them into charts using observed transition/effect signatures.

4. Genuine novelty:
   The contribution is not a larger model, more data, a benchmark, uncertainty, active learning, a verifier, LLM planning, or reinforcement learning. The novel mechanism is treating an action token as a physical fiber and making next-state effect diameter the criterion for both diagnosis and repair.

5. Closest hostile prior work:
   Closest hostile work includes OpenVLA, RT-1/RT-2, Open X-Embodiment/RT-X, Octo, pi0, FAST action tokenization, Keypoint Action Tokens, Discrete Policy, ACT, Diffusion Policy, VIMA, PaLM-E, SayCan, RoboCat, and VLA surveys. These cover VLA scaling, robot data scaling, action tokenization, action chunking, diffusion/flow action policies, and language-conditioned robot grounding. They do not, in this run's boundary reading, close the specific effect-diameter/action-fiber audit and repair claim.

6. Literature coverage:
   `docs/related_work_matrix.csv` contains 3106 entries from OpenAlex/manual seeds. The run produced a 300-paper serious skim (`docs/serious_skim_300.md`), a 250-paper extraction table (`docs/deep_read_extractions.csv`), and a 100-paper hostile prior-work document (`docs/hostile_prior_work.md`). Limitation: extraction was based on metadata and available abstracts at scale, not manual full-PDF reading for all entries.

7. Proof/formal-claim status:
   The paper proves a simple token-fiber lower bound: any decoder that observes only a token has worst-case one-step effect error at least half the effect diameter of that token fiber. This is a formal impossibility claim for collapsed token interfaces, not a theorem about all robot policies.

8. Strongest evidence:
   Runnable synthetic contact-control evidence in `scripts/run_experiments.py`. At alias strength 1.25, coarse token decoding achieved 0.148 success, raw action charts 0.631, ESAC with full context 0.743, ESAC with hidden alias-resolving context 0.374, and a continuous regression upper baseline 1.000. The sweep and figures are saved in `results/` and `figures/`.

9. Biggest weaknesses:
   Evidence is synthetic only; no real-robot or real-VLA intervention is shown. ESAC requires transition/effect observations during audit/training and observable alias-resolving context at test time. The effect metric is task-dependent. Continuous-action policies can avoid this exact token bottleneck if they bypass many-to-one action tokenization.

10. Paper-readiness judgment:
   Workshop. The mechanism, formal boundary, and runnable evidence are coherent, but a main-conference submission would need real robot/VLA audits, stronger baselines on existing action tokenizers, and manual full-paper verification of the closest hostile prior work.

11. Exact Downloads PDF path:
   `C:/Users/wangz/Downloads/06.pdf`

12. GitHub URL:
   `https://github.com/Jason-Wang313/06_action_aliasing_in_robot_foundation_models`

13. Desktop PDF copy status:
   pending orchestrator copy

Additional build/publish status:
- Official ICLR template source used at runtime: ICLR 2026 Author Guide pointing to `https://github.com/ICLR/Master-Template/raw/master/iclr2026.zip`.
- `paper/main.pdf` compiled successfully with direct `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Public GitHub repo was created and initial commit pushed to `master`.
