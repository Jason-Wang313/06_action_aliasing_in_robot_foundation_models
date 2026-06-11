# Novelty Decision

## Decision
Proceed with Effect-Separating Action Charts (ESAC).

## Chosen Thesis
Robot foundation models that emit language-like or discretized action tokens can be physically non-identifiable: a single token may contain an action fiber whose members cause different next-state effects under the local robot dynamics. The paper introduces Effect-Separating Action Charts (ESAC), which audits each token by its effect diameter and repairs aliased tokens by splitting their fibers according to observed transition signatures.

## Why This Beats The Alternatives
- It changes which mechanism is central: from predicting the right token to preserving physical distinguishability inside a token fiber.
- It gives a formal object to attack: the effect diameter of a token fiber under local dynamics.
- It yields a concrete repair: split a token by observed transition signatures, then decode from a chart-specific prototype.
- It avoids the forbidden weak moves: no bigger model, no bigger dataset, no uncertainty wrapper, no LLM planner, no RL requirement, and not merely a benchmark.

## Literature Pressure
The top-ranked matrix rows make these claims unsafe: generic VLA training, action tokenization, action chunking, diffusion/flow policies, multimodal prompting, cross-embodiment data, and language affordance grounding. The proposed paper must therefore argue specifically about non-identifiability caused by many-to-one action representations.

## Required Evidence
- A theorem or proposition showing token-only decoders inherit irreducible effect error when a fiber has large effect diameter.
- An alias audit that predicts token-policy failure.
- A repair experiment showing ESAC improves success while holding model capacity modest and fixed.
- Honest limitation language: simulation-only evidence in this attempt.
