# Submission Attack Log

## Paper 06 v2

- Attack: ESAC only works because the simulator exposes a clean alias-resolving context variable.
  - Response: Added a context-corruption stress. ESAC success drops from 74.2% clean to 60.5% at 20% corruption, 44.3% at 40% corruption, and 37.7% when alias context is hidden.
  - Residual risk: The stress is still synthetic and uses direct feature flips rather than real perception errors.
- Attack: Continuous-action policies avoid the token bottleneck.
  - Response: Continuous regression remains an upper baseline with 1.000 success at alias strength 1.25; the claim is limited to tokenized or language-like action interfaces.
- Attack: The method is just clustering.
  - Response: The repair clusters within a token by transition effect, and raw action charts remain weaker than ESAC at the main operating point.
- Attack: Real RFMs may not have measurable transition effects or chosen effect metrics.
  - Response: The paper frames ESAC as an audit/repair mechanism requiring task-relevant effect measurements, not a deployment-ready RFM replacement.
