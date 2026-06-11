# Novelty Boundary Map

## Outside The Claim
- We do not claim a new foundation model backbone.
- We do not claim a new web-scale robot dataset.
- We do not claim diffusion, flow matching, ACT-style action chunking, or VLA token emission as new.
- We do not claim language-conditioned robot manipulation is new.
- We do not claim uncertainty estimation, active learning, or LLM planning as the central contribution.
- We do not claim real-robot deployment evidence in this attempt.

## Inside The Claim
- A formal action-fiber view of token policies: a token denotes a set of motor commands, not one command.
- An alias metric based on next-state effect diameter inside each token fiber.
- A lower-bound argument that no token-only decoder can recover distinctions erased by the token map.
- A repair mechanism, ESAC, that splits token fibers by transition/effect signatures rather than by language labels or raw action distance.
- Runnably demonstrated failure and repair in a controlled embodied-control simulation.

## Closest Hostile Papers
- OpenVLA: An Open-Source Vision-Language-Action Model
- Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review
- Language Conditioned Imitation Learning Over Unstructured Data
- GR00T N1: An Open Foundation Model for Generalist Humanoid Robots
- A Survey of Robot Intelligence with Large Language Models
- TinyVLA: Toward Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation
- Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics
- RT-2: Vision-Language-Action Models for Generalizable Robotic Control: A Comprehensive Review
- Any-point Trajectory Modeling for Policy Learning
- Language-Conditioned Imitation Learning for Robot Manipulation Tasks
- FAST: Efficient Action Tokenization for Vision-Language-Action Models
- RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control
- Discrete Policy: Learning Disentangled Action Space for Multi-Task Robotic Manipulation
- Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics
- $π_0$: A Vision-Language-Action Flow Model for General Robot Control
- Large language models for chemistry robotics
- Language Conditioned Multi-Finger Dexterous Manipulation Enabled by Physical Compliance and Switching of Controllers
- Survey of Vision-Language-Action Models for Embodied Manipulation
- QUAR-VLA: Vision-Language-Action Model for Quadruped Robots
- TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation

## Boundary Statement
If a prior work already audits token fibers by physical next-state effect diameter and repairs VLA/action-token policies by effect-separating charts with an impossibility argument, this paper is not novel. If prior work only introduces better tokens, larger VLA models, continuous decoders, action chunking, or broader datasets without measuring within-token effect diameter, it is adjacent but does not close the gap.
