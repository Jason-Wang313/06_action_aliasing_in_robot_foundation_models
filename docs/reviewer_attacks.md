# Reviewer Attacks

## Likely Attacks And Responses

1. **This is synthetic only.** Response: true; the final paper is framed as a mechanism and audit/repair demonstration, not a deployment-ready robot system.
2. **FAST/keypoint action tokens already study action tokenization.** Response: they make tokenization central prior art; the boundary is within-token physical effect diameter and repair after token formation.
3. **Continuous policies avoid discrete token aliasing.** Response: correct; continuous regression is an upper comparator. The claim targets tokenized/language-like action interfaces.
4. **A bigger decoder could learn the hidden distinction.** Response: only if the distinction remains in the representation available to the decoder. The lower bound applies after many-to-one token collapse.
5. **The repair is just clustering.** Response: random charts and raw-action charts are included; effect charts are stronger because the effect metric defines physical aliasing.
6. **The context variable is too easy.** Response: context corruption and hidden context are included. ESAC degrades to 0.356 when alias context is hidden.
7. **The method needs next-state effects.** Response: it uses transition effects during audit/training; test-time chart ids are predicted from observation.
8. **The theorem is obvious.** Response: the theorem is simple by design; its role is to force action-token evaluations to report physical fiber diameter, not just token accuracy.
9. **More action bins solve it.** Response: token granularity controls show better tokenization helps, but over-fine tokenization can become data-hungry. Oracle tokenization is reported as a boundary.
10. **The alias metric is task-dependent.** Response: yes; metric sensitivity is tested and stated as a limitation.

## Closest Hostile Prior Work

- OpenVLA and RT-1/RT-2: broad VLA scaling and action emission.
- FAST, keypoint action tokens, and discrete policies: action tokenization prior art.
- Diffusion Policy and pi0: continuous/diffusion action alternatives.
- ACT and behavior transformers: action chunks and multimodal action prediction.
- VIMA, PaLM-E, SayCan, RoboCat: language-conditioned robot grounding.
- Contact-rich manipulation literature: physical effects can change under small contact differences.
