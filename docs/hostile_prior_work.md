# Hostile Prior Work

These are the 100 papers most likely to make the proposed paper look non-novel. Each entry records the mechanism it already contributes and the residual opening for action-fiber aliasing.

## 1. OpenVLA: An Open-Source Vision-Language-Action Model
- Year/venue: 2024 / arXiv (Cornell University)
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: http://arxiv.org/abs/2406.09246

## 2. Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review
- Year/venue: 2025 / Information Fusion
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment. - Uncertainty estimates are calibrated after representation collapse.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: https://doi.org/10.1016/j.inffus.2025.104062

## 3. Language Conditioned Imitation Learning Over Unstructured Data
- Year/venue: 2021 / 
- Problem claimed: Build generalist robot policies that transfer across tasks, scenes, and embodiments.
- Actual mechanism introduced: Large-scale pretrained transformer or multimodal policy trained on heterogeneous robot data.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes broad robot-data scaling and generalist policy training prior art.
- What it leaves open: How action-space mismatch and many-to-one tokenization change the learned physical semantics.
- Link: https://doi.org/10.15607/rss.2021.xvii.047

## 4. GR00T N1: An Open Foundation Model for Generalist Humanoid Robots
- Year/venue: 2025 / ArXiv.org
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: http://arxiv.org/abs/2503.14734

## 5. A Survey of Robot Intelligence with Large Language Models
- Year/venue: 2024 / Applied Sciences
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: https://doi.org/10.3390/app14198868

## 6. TinyVLA: Toward Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation
- Year/venue: 2025 / IEEE Robotics and Automation Letters
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: https://doi.org/10.1109/lra.2025.3544909

## 7. Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics
- Year/venue: 2024 / 
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: https://doi.org/10.15607/rss.2024.xx.096

## 8. RT-2: Vision-Language-Action Models for Generalizable Robotic Control: A Comprehensive Review
- Year/venue: 2025 / Advances in Engineering Technology Research
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: https://doi.org/10.56028/aetr.15.1.1423.2025

## 9. Any-point Trajectory Modeling for Policy Learning
- Year/venue: 2024 / 
- Problem claimed: Ground natural-language task descriptions in feasible robot behavior.
- Actual mechanism introduced: Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art.
- What it leaves open: Whether the grounded language interface hides control-equivalent but physically divergent commands.
- Link: https://doi.org/10.15607/rss.2024.xx.092

## 10. Language-Conditioned Imitation Learning for Robot Manipulation Tasks
- Year/venue: 2020 / arXiv (Cornell University)
- Problem claimed: Ground natural-language task descriptions in feasible robot behavior.
- Actual mechanism introduced: Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art.
- What it leaves open: Whether the grounded language interface hides control-equivalent but physically divergent commands.
- Link: http://arxiv.org/abs/2010.12083

## 11. FAST: Efficient Action Tokenization for Vision-Language-Action Models
- Year/venue: 2025 / 
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: https://doi.org/10.15607/rss.2025.xxi.012

## 12. RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control
- Year/venue: 2023 / arXiv (Cornell University)
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: http://arxiv.org/abs/2307.15818

## 13. Discrete Policy: Learning Disentangled Action Space for Multi-Task Robotic Manipulation
- Year/venue: 2025 / 
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: https://doi.org/10.1109/icra55743.2025.11127630

## 14. Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics
- Year/venue: 2024 / arXiv (Cornell University)
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: http://arxiv.org/abs/2403.19578

## 15. $π_0$: A Vision-Language-Action Flow Model for General Robot Control
- Year/venue: 2024 / arXiv (Cornell University)
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: http://arxiv.org/abs/2410.24164

## 16. Large language models for chemistry robotics
- Year/venue: 2023 / Autonomous Robots
- Problem claimed: Ground natural-language task descriptions in feasible robot behavior.
- Actual mechanism introduced: Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art.
- What it leaves open: Whether the grounded language interface hides control-equivalent but physically divergent commands.
- Link: https://doi.org/10.1007/s10514-023-10136-2

## 17. Language Conditioned Multi-Finger Dexterous Manipulation Enabled by Physical Compliance and Switching of Controllers
- Year/venue: 2024 / arXiv (Cornell University)
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: http://arxiv.org/abs/2410.14022

## 18. Survey of Vision-Language-Action Models for Embodied Manipulation
- Year/venue: 2025 / ArXiv.org
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: http://arxiv.org/abs/2508.15201

## 19. QUAR-VLA: Vision-Language-Action Model for Quadruped Robots
- Year/venue: 2023 / arXiv (Cornell University)
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: http://arxiv.org/abs/2312.14457

## 20. TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation
- Year/venue: 2024 / arXiv (Cornell University)
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: http://arxiv.org/abs/2409.12514

## 21. Scaling Cross-Embodied Learning: One Policy for Manipulation, Navigation, Locomotion and Aviation
- Year/venue: 2024 / arXiv (Cornell University)
- Problem claimed: Improve embodied-agent perception, learning, control, or physical reasoning.
- Actual mechanism introduced: Task-specific representation, policy, dataset, benchmark, or planning method.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Contributes background methods that constrain claims about general embodied intelligence.
- What it leaves open: Whether the method treats motor-command identity as preserved through learned representations.
- Link: http://arxiv.org/abs/2408.11812

## 22. Octo: An Open-Source Generalist Robot Policy
- Year/venue: 2024 / arXiv (Cornell University)
- Problem claimed: Build generalist robot policies that transfer across tasks, scenes, and embodiments.
- Actual mechanism introduced: Large-scale pretrained transformer or multimodal policy trained on heterogeneous robot data.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes broad robot-data scaling and generalist policy training prior art.
- What it leaves open: How action-space mismatch and many-to-one tokenization change the learned physical semantics.
- Link: http://arxiv.org/abs/2405.12213

## 23. NaVILA: Legged Robot Vision-Language-Action Model for Navigation
- Year/venue: 2024 / arXiv (Cornell University)
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: http://arxiv.org/abs/2412.04453

## 24. Diffusion policy: Visuomotor policy learning via action diffusion
- Year/venue: 2024 / The International Journal of Robotics Research
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: https://doi.org/10.1177/02783649241273668

## 25. Learning Insertion Primitives with Discrete-Continuous Hybrid Action Space for Robotic Assembly Tasks
- Year/venue: 2022 / 2022 International Conference on Robotics and Automation (ICRA)
- Problem claimed: Improve embodied-agent perception, learning, control, or physical reasoning.
- Actual mechanism introduced: Task-specific representation, policy, dataset, benchmark, or planning method.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Contributes background methods that constrain claims about general embodied intelligence.
- What it leaves open: Whether the method treats motor-command identity as preserved through learned representations.
- Link: https://doi.org/10.1109/icra46639.2022.9811973

## 26. 3D-VLA: A 3D Vision-Language-Action Generative World Model
- Year/venue: 2024 / arXiv (Cornell University)
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: http://arxiv.org/abs/2403.09631

## 27. Open X-Embodiment: Robotic Learning Datasets and RT-X Models
- Year/venue: 2023 / arXiv (Cornell University)
- Problem claimed: Build generalist robot policies that transfer across tasks, scenes, and embodiments.
- Actual mechanism introduced: Large-scale pretrained transformer or multimodal policy trained on heterogeneous robot data.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes broad robot-data scaling and generalist policy training prior art.
- What it leaves open: How action-space mismatch and many-to-one tokenization change the learned physical semantics.
- Link: http://arxiv.org/abs/2310.08864

## 28. Active Haptic Perception in Robots: A Review
- Year/venue: 2019 / Frontiers in Neurorobotics
- Problem claimed: Predict future physical states or plan actions under learned dynamics.
- Actual mechanism introduced: Latent dynamics, video prediction, model-predictive control, or planning over learned representations.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes learned physical prediction and planning over latent states prior art.
- What it leaves open: Whether action aliases in the latent interface make plans non-identifiable.
- Link: https://doi.org/10.3389/fnbot.2019.00053

## 29. Continuous control actions learning and adaptation for robotic manipulation through reinforcement learning
- Year/venue: 2022 / Autonomous Robots
- Problem claimed: Improve embodied-agent perception, learning, control, or physical reasoning.
- Actual mechanism introduced: Task-specific representation, policy, dataset, benchmark, or planning method.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Contributes background methods that constrain claims about general embodied intelligence.
- What it leaves open: Whether the method treats motor-command identity as preserved through learned representations.
- Link: https://doi.org/10.1007/s10514-022-10034-z

## 30. Skill Transformer: A Monolithic Policy for Mobile Manipulation
- Year/venue: 2023 / 
- Problem claimed: Ground natural-language task descriptions in feasible robot behavior.
- Actual mechanism introduced: Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art.
- What it leaves open: Whether the grounded language interface hides control-equivalent but physically divergent commands.
- Link: https://doi.org/10.1109/iccv51070.2023.00996

## 31. ChatGPT for Robotics: Design Principles and Model Abilities
- Year/venue: 2024 / IEEE Access
- Problem claimed: Ground natural-language task descriptions in feasible robot behavior.
- Actual mechanism introduced: Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art.
- What it leaves open: Whether the grounded language interface hides control-equivalent but physically divergent commands.
- Link: https://doi.org/10.1109/access.2024.3387941

## 32. Discrete Policy: Learning Disentangled Action Space for Multi-Task Robotic Manipulation
- Year/venue: 2024 / arXiv (Cornell University)
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: http://arxiv.org/abs/2409.18707

## 33. X-Nav: Learning End-to-End Cross-Embodiment Navigation for Mobile Robots
- Year/venue: 2025 / IEEE Robotics and Automation Letters
- Problem claimed: Improve embodied-agent perception, learning, control, or physical reasoning.
- Actual mechanism introduced: Task-specific representation, policy, dataset, benchmark, or planning method.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Contributes background methods that constrain claims about general embodied intelligence.
- What it leaves open: Whether the method treats motor-command identity as preserved through learned representations.
- Link: https://doi.org/10.1109/lra.2025.3632119

## 34. Language Reasoning in Vision-Language-Action Model for Robotic Grasping
- Year/venue: 2024 / 
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: https://doi.org/10.1109/cac63892.2024.10865585

## 35. Demonstrating OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics
- Year/venue: 2024 / 
- Problem claimed: Ground natural-language task descriptions in feasible robot behavior.
- Actual mechanism introduced: Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art.
- What it leaves open: Whether the grounded language interface hides control-equivalent but physically divergent commands.
- Link: https://doi.org/10.15607/rss.2024.xx.091

## 36. Vision Language Action Models in Robotic Manipulation: A Systematic Review
- Year/venue: 2025 / ArXiv.org
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: http://arxiv.org/abs/2507.10672

## 37. HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation
- Year/venue: 2025 / ArXiv.org
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: http://arxiv.org/abs/2502.05485

## 38. RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation
- Year/venue: 2023 / arXiv (Cornell University)
- Problem claimed: Build generalist robot policies that transfer across tasks, scenes, and embodiments.
- Actual mechanism introduced: Large-scale pretrained transformer or multimodal policy trained on heterogeneous robot data.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes broad robot-data scaling and generalist policy training prior art.
- What it leaves open: How action-space mismatch and many-to-one tokenization change the learned physical semantics.
- Link: http://arxiv.org/abs/2306.11706

## 39. Rethinking the Practicality of Vision-language-action Model: A Comprehensive Benchmark and An Improved Baseline
- Year/venue: 2026 / ArXiv.org
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: http://arxiv.org/abs/2602.22663

## 40. Language-Driven Representation Learning for Robotics
- Year/venue: 2023 / 
- Problem claimed: Ground natural-language task descriptions in feasible robot behavior.
- Actual mechanism introduced: Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art.
- What it leaves open: Whether the grounded language interface hides control-equivalent but physically divergent commands.
- Link: https://doi.org/10.15607/rss.2023.xix.032

## 41. Bridging Embodiment Gaps: Deploying Vision-Language-Action Models on Soft Robots
- Year/venue: 2025 / ArXiv.org
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: http://arxiv.org/abs/2510.17369

## 42. Code as Policies: Language Model Programs for Embodied Control
- Year/venue: 2022 / arXiv (Cornell University)
- Problem claimed: Ground natural-language task descriptions in feasible robot behavior.
- Actual mechanism introduced: Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art.
- What it leaves open: Whether the grounded language interface hides control-equivalent but physically divergent commands.
- Link: http://arxiv.org/abs/2209.07753

## 43. Learning Diffusion Policy from Primitive Skills for Robot Manipulation
- Year/venue: 2026 / ArXiv.org
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: http://arxiv.org/abs/2601.01948

## 44. A Robotic Skill Learning System Built Upon Diffusion Policies and Foundation Models
- Year/venue: 2024 / 
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: https://doi.org/10.1109/ro-man60168.2024.10731242

## 45. Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation
- Year/venue: 2025 / 
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them. Tactile/contact cues may expose aliases that vision-language tokens miss.
- Link: https://doi.org/10.15607/rss.2025.xxi.052

## 46. A Survey on Diffusion Policy for Robotic Manipulation: Taxonomy, Analysis, and Future Directions
- Year/venue: 2025 / 
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: https://doi.org/10.36227/techrxiv.174378343.39356214/v1

## 47. OXE-AugE: A Large-Scale Robot Augmentation of OXE for Scaling Cross-Embodiment Policy Learning
- Year/venue: 2025 / ArXiv.org
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: http://arxiv.org/abs/2512.13100

## 48. RISE: 3D Perception Makes Real-World Robot Imitation Simple and Effective
- Year/venue: 2024 / 
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: https://doi.org/10.1109/iros58592.2024.10801678

## 49. Autoregressive Action Sequence Learning for Robotic Manipulation
- Year/venue: 2025 / IEEE Robotics and Automation Letters
- Problem claimed: Ground natural-language task descriptions in feasible robot behavior.
- Actual mechanism introduced: Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art.
- What it leaves open: Whether the grounded language interface hides control-equivalent but physically divergent commands.
- Link: https://doi.org/10.1109/lra.2025.3550849

## 50. Diffusion Policy: Visuomotor Policy Learning via Action Diffusion
- Year/venue: 2023 / arXiv (Cornell University)
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: http://arxiv.org/abs/2303.04137

## 51. Lifelong Robot Library Learning: Bootstrapping Composable and Generalizable Skills for Embodied Control with Language Models
- Year/venue: 2024 / arXiv (Cornell University)
- Problem claimed: Ground natural-language task descriptions in feasible robot behavior.
- Actual mechanism introduced: Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art.
- What it leaves open: Whether the grounded language interface hides control-equivalent but physically divergent commands.
- Link: http://arxiv.org/abs/2406.18746

## 52. Language, Camera, Autonomy! Prompt-engineered Robot Control for Rapidly Evolving Deployment
- Year/venue: 2024 / 
- Problem claimed: Ground natural-language task descriptions in feasible robot behavior.
- Actual mechanism introduced: Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art.
- What it leaves open: Whether the grounded language interface hides control-equivalent but physically divergent commands.
- Link: https://doi.org/10.1145/3610978.3640671

## 53. Multimodal Human–Robot Interaction for Human‐Centric Smart Manufacturing: A Survey
- Year/venue: 2023 / Advanced Intelligent Systems
- Problem claimed: Ground natural-language task descriptions in feasible robot behavior.
- Actual mechanism introduced: Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art.
- What it leaves open: Whether the grounded language interface hides control-equivalent but physically divergent commands.
- Link: https://doi.org/10.1002/aisy.202300359

## 54. AnyPos: Automated Task-Agnostic Actions for Bimanual Manipulation
- Year/venue: 2025 / ArXiv.org
- Problem claimed: Build generalist robot policies that transfer across tasks, scenes, and embodiments.
- Actual mechanism introduced: Large-scale pretrained transformer or multimodal policy trained on heterogeneous robot data.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes broad robot-data scaling and generalist policy training prior art.
- What it leaves open: How action-space mismatch and many-to-one tokenization change the learned physical semantics.
- Link: https://arxiv.org/abs/2507.12768

## 55. Zero-Shot Robotic Manipulation with Pretrained Image-Editing Diffusion Models
- Year/venue: 2023 / arXiv (Cornell University)
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: http://arxiv.org/abs/2310.10639

## 56. MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation
- Year/venue: 2025 / 
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: https://doi.org/10.1109/cvpr52734.2025.00167

## 57. RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation
- Year/venue: 2024 / arXiv (Cornell University)
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: http://arxiv.org/abs/2406.04339

## 58. Learning Variable Compliance Control From a Few Demonstrations for Bimanual Robot with Haptic Feedback Teleoperation System
- Year/venue: 2024 / 
- Problem claimed: Improve embodied-agent perception, learning, control, or physical reasoning.
- Actual mechanism introduced: Task-specific representation, policy, dataset, benchmark, or planning method.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Contributes background methods that constrain claims about general embodied intelligence.
- What it leaves open: Whether the method treats motor-command identity as preserved through learned representations.
- Link: https://doi.org/10.1109/iros58592.2024.10801731

## 59. CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation
- Year/venue: 2024 / arXiv (Cornell University)
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: http://arxiv.org/abs/2411.19650

## 60. Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success
- Year/venue: 2025 / 
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: https://doi.org/10.15607/rss.2025.xxi.017

## 61. Hierarchical Diffusion Policy: Manipulation Trajectory Generation via Contact Guidance
- Year/venue: 2025 / IEEE Transactions on Robotics
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: https://doi.org/10.1109/tro.2025.3547272

## 62. Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications
- Year/venue: 2025 / IEEE Access
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: https://doi.org/10.1109/access.2025.3609980

## 63. CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision
- Year/venue: 2025 / 
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: https://doi.org/10.15607/rss.2025.xxi.016

## 64. ProgVLA: Progress-Aware Robot Manipulation Skill Learning
- Year/venue: 2026 / arXiv (Cornell University)
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: https://arxiv.org/abs/2605.28231

## 65. Towards learning hierarchical skills for multi-phase manipulation tasks
- Year/venue: 2015 / 
- Problem claimed: Improve embodied-agent perception, learning, control, or physical reasoning.
- Actual mechanism introduced: Task-specific representation, policy, dataset, benchmark, or planning method.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Contributes background methods that constrain claims about general embodied intelligence.
- What it leaves open: Whether the method treats motor-command identity as preserved through learned representations.
- Link: https://doi.org/10.1109/icra.2015.7139389

## 66. Language-Conditioned Imitation Learning for Robot Manipulation Tasks
- Year/venue: 2020 / neural information processing systems
- Problem claimed: Ground natural-language task descriptions in feasible robot behavior.
- Actual mechanism introduced: Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art.
- What it leaves open: Whether the grounded language interface hides control-equivalent but physically divergent commands.
- Link: https://papers.nips.cc/paper/2020/file/9909794d52985cbc5d95c26e31125d1a-Paper.pdf

## 67. Cross-Embodiment Robot Manipulation Skill Transfer using Latent Space Alignment
- Year/venue: 2024 / arXiv (Cornell University)
- Problem claimed: Improve embodied-agent perception, learning, control, or physical reasoning.
- Actual mechanism introduced: Task-specific representation, policy, dataset, benchmark, or planning method.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Contributes background methods that constrain claims about general embodied intelligence.
- What it leaves open: Whether the method treats motor-command identity as preserved through learned representations.
- Link: http://arxiv.org/abs/2406.01968

## 68. PoCo: Policy Composition from and for Heterogeneous Robot Learning
- Year/venue: 2024 / 
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them. Tactile/contact cues may expose aliases that vision-language tokens miss.
- Link: https://doi.org/10.15607/rss.2024.xx.127

## 69. Turning Video Models into Generalist Robot Policies
- Year/venue: 2026 / ArXiv.org
- Problem claimed: Build generalist robot policies that transfer across tasks, scenes, and embodiments.
- Actual mechanism introduced: Large-scale pretrained transformer or multimodal policy trained on heterogeneous robot data.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes broad robot-data scaling and generalist policy training prior art.
- What it leaves open: How action-space mismatch and many-to-one tokenization change the learned physical semantics.
- Link: https://arxiv.org/abs/2605.27817

## 70. Open X-Embodiment: Robotic Learning Datasets and RT-X Models : Open X-Embodiment Collaboration<sup>0</sup>
- Year/venue: 2024 / 
- Problem claimed: Build generalist robot policies that transfer across tasks, scenes, and embodiments.
- Actual mechanism introduced: Large-scale pretrained transformer or multimodal policy trained on heterogeneous robot data.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes broad robot-data scaling and generalist policy training prior art.
- What it leaves open: How action-space mismatch and many-to-one tokenization change the learned physical semantics.
- Link: https://doi.org/10.1109/icra57147.2024.10611477

## 71. Robot Control Stack: A Lean Ecosystem for Robot Learning at Scale
- Year/venue: 2025 / arXiv (Cornell University)
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: http://arxiv.org/abs/2509.14932

## 72. Turning Video Models into Generalist Robot Policies
- Year/venue: 2026 / arXiv (Cornell University)
- Problem claimed: Build generalist robot policies that transfer across tasks, scenes, and embodiments.
- Actual mechanism introduced: Large-scale pretrained transformer or multimodal policy trained on heterogeneous robot data.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes broad robot-data scaling and generalist policy training prior art.
- What it leaves open: How action-space mismatch and many-to-one tokenization change the learned physical semantics.
- Link: https://doi.org/10.48550/arxiv.2605.27817

## 73. ChatGPT for Robotics: Design Principles and Model Abilities
- Year/venue: 2023 / arXiv (Cornell University)
- Problem claimed: Ground natural-language task descriptions in feasible robot behavior.
- Actual mechanism introduced: Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art.
- What it leaves open: Whether the grounded language interface hides control-equivalent but physically divergent commands.
- Link: http://arxiv.org/abs/2306.17582

## 74. Scaling Robot Learning with Semantically Imagined Experience
- Year/venue: 2023 / 
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: https://doi.org/10.15607/rss.2023.xix.027

## 75. From LLMs to Actions: Latent Codes as Bridges in Hierarchical Robot Control
- Year/venue: 2024 / arXiv (Cornell University)
- Problem claimed: Ground natural-language task descriptions in feasible robot behavior.
- Actual mechanism introduced: Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art.
- What it leaves open: Whether the grounded language interface hides control-equivalent but physically divergent commands.
- Link: http://arxiv.org/abs/2405.04798

## 76. InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy
- Year/venue: 2025 / ArXiv.org
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: http://arxiv.org/abs/2510.13778

## 77. Augmenting Reinforcement Learning with Behavior Primitives for Diverse Manipulation Tasks
- Year/venue: 2022 / 2022 International Conference on Robotics and Automation (ICRA)
- Problem claimed: Improve embodied-agent perception, learning, control, or physical reasoning.
- Actual mechanism introduced: Task-specific representation, policy, dataset, benchmark, or planning method.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Contributes background methods that constrain claims about general embodied intelligence.
- What it leaves open: Whether the method treats motor-command identity as preserved through learned representations.
- Link: https://doi.org/10.1109/icra46639.2022.9812140

## 78. OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics
- Year/venue: 2024 / arXiv (Cornell University)
- Problem claimed: Ground natural-language task descriptions in feasible robot behavior.
- Actual mechanism introduced: Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art.
- What it leaves open: Whether the grounded language interface hides control-equivalent but physically divergent commands.
- Link: http://arxiv.org/abs/2401.12202

## 79. Robotic Skill Acquisition via Instruction Augmentation with Vision-Language Models
- Year/venue: 2023 / 
- Problem claimed: Ground natural-language task descriptions in feasible robot behavior.
- Actual mechanism introduced: Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art.
- What it leaves open: Whether the grounded language interface hides control-equivalent but physically divergent commands.
- Link: https://doi.org/10.15607/rss.2023.xix.029

## 80. Integrating Large Language Models into Robotic Autonomy: A Review of Motion, Voice, and Training Pipelines
- Year/venue: 2025 / AI
- Problem claimed: Ground natural-language task descriptions in feasible robot behavior.
- Actual mechanism introduced: Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment. - Uncertainty estimates are calibrated after representation collapse.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art.
- What it leaves open: Whether the grounded language interface hides control-equivalent but physically divergent commands.
- Link: https://doi.org/10.3390/ai6070158

## 81. Interactive Language: Talking to Robots in Real Time
- Year/venue: 2022 / arXiv (Cornell University)
- Problem claimed: Ground natural-language task descriptions in feasible robot behavior.
- Actual mechanism introduced: Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art.
- What it leaves open: Whether the grounded language interface hides control-equivalent but physically divergent commands.
- Link: http://arxiv.org/abs/2210.06407

## 82. ALPHA- α and Bi-ACT Are All You Need: Importance of Position and Force Information/ Control for Imitation Learning of Unimanual and Bimanual Robotic Manipulation With Low-Cost System
- Year/venue: 2025 / IEEE Access
- Problem claimed: Improve embodied-agent perception, learning, control, or physical reasoning.
- Actual mechanism introduced: Task-specific representation, policy, dataset, benchmark, or planning method.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Contributes background methods that constrain claims about general embodied intelligence.
- What it leaves open: Whether the method treats motor-command identity as preserved through learned representations.
- Link: https://doi.org/10.1109/access.2025.3541200

## 83. PolyTouch: A Robust Multi-Modal Tactile Sensor for Contact-Rich Manipulation Using Tactile-Diffusion Policies
- Year/venue: 2025 / 
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them. Tactile/contact cues may expose aliases that vision-language tokens miss.
- Link: https://doi.org/10.1109/icra55743.2025.11128816

## 84. Augmented Reality for RObots (ARRO): Pointing Visuomotor Policies Towards Visual Robustness
- Year/venue: 2026 / IEEE Robotics and Automation Letters
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: https://doi.org/10.1109/lra.2026.3665444

## 85. CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision
- Year/venue: 2024 / arXiv (Cornell University)
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: http://arxiv.org/abs/2411.00508

## 86. JUICER: Data-Efficient Imitation Learning for Robotic Assembly
- Year/venue: 2024 / arXiv (Cornell University)
- Problem claimed: Improve embodied-agent perception, learning, control, or physical reasoning.
- Actual mechanism introduced: Task-specific representation, policy, dataset, benchmark, or planning method.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Contributes background methods that constrain claims about general embodied intelligence.
- What it leaves open: Whether the method treats motor-command identity as preserved through learned representations.
- Link: http://arxiv.org/abs/2404.03729

## 87. Artificial Intelligence and the Future of Surgical Robotics
- Year/venue: 2019 / Annals of Surgery
- Problem claimed: Improve embodied-agent perception, learning, control, or physical reasoning.
- Actual mechanism introduced: Task-specific representation, policy, dataset, benchmark, or planning method.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Contributes background methods that constrain claims about general embodied intelligence.
- What it leaves open: Whether the method treats motor-command identity as preserved through learned representations. Tactile/contact cues may expose aliases that vision-language tokens miss.
- Link: https://doi.org/10.1097/sla.0000000000003262

## 88. RoboNurse-VLA: Robotic Scrub Nurse System based on Vision-Language-Action Model
- Year/venue: 2025 / 
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: https://doi.org/10.1109/iros60139.2025.11246030

## 89. VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks
- Year/venue: 2025 / 
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: https://doi.org/10.1109/iccv51701.2025.01037

## 90. Large Language Models for Robotics: A Survey
- Year/venue: 2023 / arXiv (Cornell University)
- Problem claimed: Ground natural-language task descriptions in feasible robot behavior.
- Actual mechanism introduced: Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art.
- What it leaves open: Whether the grounded language interface hides control-equivalent but physically divergent commands.
- Link: http://arxiv.org/abs/2311.07226

## 91. Scaling Diffusion Policy in Transformer to 1 Billion Parameters for Robotic Manipulation
- Year/venue: 2025 / 
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: https://doi.org/10.1109/icra55743.2025.11128074

## 92. Riemannian Flow Matching Policy for Robot Motion Learning
- Year/venue: 2024 / 
- Problem claimed: Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation.
- Actual mechanism introduced: Conditional denoising or flow model generates action sequences from visual state.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes sequence-level continuous action generation and multimodal action distributions well established.
- What it leaves open: How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them.
- Link: https://doi.org/10.1109/iros58592.2024.10801521

## 93. Object Manipulation with an Anthropomorphic Robotic Hand via Deep Reinforcement Learning with a Synergy Space of Natural Hand Poses
- Year/venue: 2021 / Sensors
- Problem claimed: Improve embodied-agent perception, learning, control, or physical reasoning.
- Actual mechanism introduced: Task-specific representation, policy, dataset, benchmark, or planning method.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Contributes background methods that constrain claims about general embodied intelligence.
- What it leaves open: Whether the method treats motor-command identity as preserved through learned representations.
- Link: https://doi.org/10.3390/s21165301

## 94. Instruct2Act: Mapping Multi-modality Instructions to Robotic Actions with Large Language Model
- Year/venue: 2023 / arXiv (Cornell University)
- Problem claimed: Scale robot control by reusing vision-language representations for language-conditioned manipulation.
- Actual mechanism introduced: Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization; benchmark action ontology
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Shows that large pretrained multimodal backbones can be adapted to robot action prediction.
- What it leaves open: Whether semantically similar tokens preserve distinctions between physically different motor commands.
- Link: http://arxiv.org/abs/2305.11176

## 95. PointACT: Automatic Robot Manipulation with Cross-Modal Action Chunking Transformer on Image-Point Cloud
- Year/venue: 2025 / 
- Problem claimed: Improve embodied-agent perception, learning, control, or physical reasoning.
- Actual mechanism introduced: Task-specific representation, policy, dataset, benchmark, or planning method.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Contributes background methods that constrain claims about general embodied intelligence.
- What it leaves open: Whether the method treats motor-command identity as preserved through learned representations.
- Link: https://doi.org/10.1109/swc65939.2025.00225

## 96. Dynamic movement primitives in robotics: A tutorial survey
- Year/venue: 2023 / The International Journal of Robotics Research
- Problem claimed: Improve embodied-agent perception, learning, control, or physical reasoning.
- Actual mechanism introduced: Task-specific representation, policy, dataset, benchmark, or planning method.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Contributes background methods that constrain claims about general embodied intelligence.
- What it leaves open: Whether the method treats motor-command identity as preserved through learned representations.
- Link: https://doi.org/10.1177/02783649231201196

## 97. Enhancing the LLM-Based Robot Manipulation Through Human-Robot Collaboration
- Year/venue: 2024 / IEEE Robotics and Automation Letters
- Problem claimed: Ground natural-language task descriptions in feasible robot behavior.
- Actual mechanism introduced: Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art.
- What it leaves open: Whether the grounded language interface hides control-equivalent but physically divergent commands.
- Link: https://doi.org/10.1109/lra.2024.3415931

## 98. Tube-NeRF: Efficient Imitation Learning of Visuomotor Policies From MPC via Tube-Guided Data Augmentation and NeRFs
- Year/venue: 2024 / IEEE Robotics and Automation Letters
- Problem claimed: Improve embodied-agent perception, learning, control, or physical reasoning.
- Actual mechanism introduced: Task-specific representation, policy, dataset, benchmark, or planning method.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Contributes background methods that constrain claims about general embodied intelligence.
- What it leaves open: Whether the method treats motor-command identity as preserved through learned representations.
- Link: https://doi.org/10.1109/lra.2024.3386053

## 99. Nonparametric Online Learning Control for Soft Continuum Robot: An Enabling Technique for Effective Endoscopic Navigation
- Year/venue: 2017 / Soft Robotics
- Problem claimed: Improve embodied-agent perception, learning, control, or physical reasoning.
- Actual mechanism introduced: Task-specific representation, policy, dataset, benchmark, or planning method.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token; simulator discretization hides real actuator non-identifiability
- What it makes less novel: Contributes background methods that constrain claims about general embodied intelligence.
- What it leaves open: Whether the method treats motor-command identity as preserved through learned representations.
- Link: https://doi.org/10.1089/soro.2016.0065

## 100. GR-2: A Generative Video-Language-Action Model with Web-Scale Knowledge for Robot Manipulation
- Year/venue: 2024 / arXiv (Cornell University)
- Problem claimed: Build generalist robot policies that transfer across tasks, scenes, and embodiments.
- Actual mechanism introduced: Large-scale pretrained transformer or multimodal policy trained on heterogeneous robot data.
- Hidden assumptions: - The chosen action interface is sufficiently expressive for the physical task. - Different motor commands that matter downstream remain separable after tokenization or latent encoding. - Dataset labels reveal the action distinctions needed at deployment.
- Variables treated as fixed: embodiment calibration; low-level controller semantics; action binning or policy-head parameterization
- Failure modes ignored: physically distinct commands collapse to one representation; rare contact-sensitive distinctions vanish in average success metrics; cross-embodiment transfer changes the meaning of the same token
- What it makes less novel: Makes broad robot-data scaling and generalist policy training prior art.
- What it leaves open: How action-space mismatch and many-to-one tokenization change the learned physical semantics.
- Link: http://arxiv.org/abs/2410.06158
