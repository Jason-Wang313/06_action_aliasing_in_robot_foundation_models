# Submission Attack Log

## Paper 06 v3

- Attack: ESAC only works because the simulator exposes a clean context variable.
  - Response: The final context-reliability suite flips mode/contact variables and includes hidden context. ESAC drops to 0.582 with 20% both-variable flips, 0.440 with 40%, and 0.356 when hidden.
  - Residual risk: This remains synthetic feature corruption, not perception error on real robot observations.

- Attack: Continuous-action policies avoid the token bottleneck.
  - Response: Continuous regression is reported as an upper comparator and reaches 0.998 at alias strength 1.25. The claim targets tokenized or language-like action interfaces.
  - Residual risk: A real system may prefer continuous bypass rather than token repair.

- Attack: The method is just clustering.
  - Response: Random charts stay near coarse-token performance, raw action charts are weaker than effect charts, and effect-metric sensitivity shows the charting space matters.

- Attack: Better tokenization solves the problem.
  - Response: Oracle mode/contact tokenization is included and raises coarse-token success to 0.760. This is treated as a boundary, not hidden.

- Attack: The metric is arbitrary.
  - Response: The final metric suite compares full effect, partial effect, noisy effect, raw action, and random metrics. Random metric collapses to 0.156.

- Attack: The evidence is synthetic only.
  - Response: The final manuscript frames the work as a synthetic mechanism paper and gives a concrete real-log audit protocol.
