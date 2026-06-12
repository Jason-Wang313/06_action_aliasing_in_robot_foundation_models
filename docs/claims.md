# Claims

## Supported By Formal Argument
- If two demonstrations share a token but require different next-state effects, any decoder that observes only the token must incur nonzero error on at least one member of the fiber.
- The minimum worst-case one-step effect error of a token-only decoder is at least half the effect diameter of that token fiber.
- Splitting a token fiber into charts with smaller effect diameter tightens that lower bound.

## Supported By Runnable Evidence
- In the synthetic contact-control environment, coarse action tokens collapse physically distinct commands and fail as alias strength increases.
- ESAC uses observed transition effects to split the collapsed token fibers and recovers much of the lost success.
- The measured alias energy correlates with coarse-token failure in the sweep.
- The v2 context-corruption stress shows the required boundary: at alias strength 1.25, ESAC success drops from 74.2% with clean alias context to 60.5% with 20% context corruption, 44.3% with 40% corruption, and 37.7% when the alias context is hidden.

## Unsupported Or Not Claimed
- No claim of real-robot deployment.
- No claim that ESAC dominates continuous-action policies when those policies are allowed to bypass tokenization.
- No claim that all VLA models suffer severe aliasing; the claim is conditional on large effect diameter within action-token fibers.
- No claim that clustering is new by itself; the novelty is the action-fiber/effect-diameter diagnosis and repair target.
- No claim that ESAC can recover an action-fiber split when the observation lacks reliable alias-resolving variables.
