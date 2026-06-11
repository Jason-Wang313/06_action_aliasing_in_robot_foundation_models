# Experiment Summary

Synthetic contact-control environment at alias_strength=1.25. Success means one-step physical effect error below 0.36.

| Method | Success | Effect RMSE | Action RMSE | Notes |
|---|---:|---:|---:|---|
| coarse_token | 0.148 | 0.653 | 1.040 | One decoded prototype per language/action token. |
| raw_action_charts | 0.631 | 0.380 | 0.966 | Splits token fibers by raw motor-command clusters. |
| esac_hidden_alias_ablation | 0.374 | 0.856 | 1.171 | ESAC charts but hides the alias-resolving mode/contact context. |
| esac_full_context | 0.743 | 0.317 | 0.868 | ESAC charts from transition effects with observable context. |
| continuous_regression_upper | 1.000 | 0.119 | 0.846 | Continuous-action upper baseline, not a token repair. |
| oracle_expert | 0.999 | 0.121 | 0.000 | Expert command replay upper bound. |

Interpretation: coarse tokens fail as within-token effect diameter grows. ESAC succeeds only when the observation contains the variable that disambiguates the action fiber, which is exactly the intended limitation.
