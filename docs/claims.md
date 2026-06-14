# Claims

## Supported By Formal Argument

- If two commands share a token but require different next-state effects, any decoder that observes only the token must incur nonzero error on at least one member of the fiber.
- The minimum worst-case one-step effect error of a token-only decoder is at least half the effect diameter of that token fiber.
- Splitting a token fiber into charts with smaller effect diameter tightens the bound, provided the chart id is predictable from observation.

## Supported By Final Full-Scale Evidence

- The final artifact contains 2,526 compact metric rows and 2,005,200 evaluated predictions counted across rows.
- At alias strength 1.25, coarse token decoding reaches 0.140 success, raw action charts 0.605, ESAC hidden context 0.356, ESAC full context 0.728, continuous upper 0.998, and oracle replay 1.000.
- Context reliability is a real boundary: ESAC full-context success falls to 0.582 with 20% mode/contact flips, 0.440 with 40% flips, and 0.356 when alias context is hidden.
- Oracle mode/contact tokenization raises coarse-token success to 0.760, showing that better tokenization can remove much of the bottleneck.
- Random charting remains near coarse-token performance, while effect charts improve with chart count, showing that ESAC is not merely adding clusters.
- Effect metric sensitivity is material: full-effect charting reaches 0.718, raw-action charting 0.580, and random-metric charting 0.156 in the metric suite.

## Unsupported Or Not Claimed

- No claim of real-robot deployment.
- No claim that ESAC dominates continuous-action policies that bypass tokenization.
- No claim that all VLA/RFM models suffer severe action aliasing.
- No claim that clustering is new by itself.
- No claim that ESAC can recover a split when observations lack reliable alias-resolving variables.
