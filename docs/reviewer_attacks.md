# Reviewer Attacks

## Attack: This is synthetic only.
Response: Agree. The paper should be framed as a mechanism and audit/repair demonstration, not as a deployment-ready robot system.

## Attack: FAST/keypoint action tokens already study action tokenization.
Response: They make tokenization central prior art; the boundary is that ESAC audits within-token physical effect diameter and repairs aliases after token formation.

## Attack: Continuous policies such as diffusion or flow models avoid discrete token aliasing.
Response: They are an important outside-scope baseline. The claim targets tokenized/language-like action interfaces used by many RFMs, not all robot policies.

## Attack: A bigger decoder could learn the hidden distinction.
Response: Only if the distinction remains in the representation available to the decoder. The lower bound applies after the many-to-one token map.

## Attack: The repair is just clustering.
Response: Raw clustering is not the claim; ESAC clusters a token fiber by transition effects because the physical effect metric defines aliasing.

## Attack: The context variable in the simulation is too easy.
Response: The v2 stress corrupts the alias-resolving mode/contact context at test time. ESAC falls from 74.2% clean success to 60.5% at 20% corruption, 44.3% at 40% corruption, and 37.7% when the alias context is hidden. The paper now treats reliable context as a required condition, not a solved problem.

## Attack: The method needs next-state effects, unavailable at test time.
Response: It uses transition effects during auditing/training to construct charts; at test time it predicts chart ids from observations like other imitation policies.

## Attack: The theorem is obvious.
Response: The theorem is simple by design; its value is forcing VLA action-token papers to report the physical diameter of token fibers, not only token accuracy.

## Attack: Action-space binning with more bins solves it.
Response: The paper must show that more bins are a capacity tradeoff, while effect charts split only where physical effects diverge.

## Attack: The alias metric depends on a chosen state metric.
Response: Correct; the metric must be task-relevant. The paper should present this as an explicit design choice rather than a universal scalar.

## Attack: Surveys already mention embodiment/action mismatch.
Response: Mentioning mismatch is not the same as measuring token-fiber effect diameter or repairing it with effect charts.

## Attack: A learned world model can serve as verifier.
Response: ESAC does not rely on verifier rejection; it changes the action representation consumed by the policy.

## Most Hostile Titles To Re-read Before Submission
- OpenVLA: An Open-Source Vision-Language-Action Model (2024)
- Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review (2025)
- Language Conditioned Imitation Learning Over Unstructured Data (2021)
- GR00T N1: An Open Foundation Model for Generalist Humanoid Robots (2025)
- A Survey of Robot Intelligence with Large Language Models (2024)
- TinyVLA: Toward Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation (2025)
- Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics (2024)
- RT-2: Vision-Language-Action Models for Generalizable Robotic Control: A Comprehensive Review (2025)
- Any-point Trajectory Modeling for Policy Learning (2024)
- Language-Conditioned Imitation Learning for Robot Manipulation Tasks (2020)
- FAST: Efficient Action Tokenization for Vision-Language-Action Models (2025)
- RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control (2023)
- Discrete Policy: Learning Disentangled Action Space for Multi-Task Robotic Manipulation (2025)
- Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics (2024)
- $π_0$: A Vision-Language-Action Flow Model for General Robot Control (2024)
- Large language models for chemistry robotics (2023)
- Language Conditioned Multi-Finger Dexterous Manipulation Enabled by Physical Compliance and Switching of Controllers (2024)
- Survey of Vision-Language-Action Models for Embodied Manipulation (2025)
- QUAR-VLA: Vision-Language-Action Model for Quadruped Robots (2023)
- TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation (2024)
- Scaling Cross-Embodied Learning: One Policy for Manipulation, Navigation, Locomotion and Aviation (2024)
- Octo: An Open-Source Generalist Robot Policy (2024)
- NaVILA: Legged Robot Vision-Language-Action Model for Navigation (2024)
- Diffusion policy: Visuomotor policy learning via action diffusion (2024)
- Learning Insertion Primitives with Discrete-Continuous Hybrid Action Space for Robotic Assembly Tasks (2022)
- 3D-VLA: A 3D Vision-Language-Action Generative World Model (2024)
- Open X-Embodiment: Robotic Learning Datasets and RT-X Models (2023)
- Active Haptic Perception in Robots: A Review (2019)
- Continuous control actions learning and adaptation for robotic manipulation through reinforcement learning (2022)
- Skill Transformer: A Monolithic Policy for Mobile Manipulation (2023)
