# Literature Map

## Corpus Construction
- Landscape sweep: 3106 unique OpenAlex/manual-seed entries in `docs/related_work_matrix.csv`.
- Serious skim: top 300 rows by robotics/action/foundation relevance score.
- Deep read: top 250 rows with extraction fields in `docs/deep_read_extractions.csv`.
- Hostile set: top 100 rows, emphasizing VLA/action-token/foundation-model papers that could erase novelty.
- Extraction caveat: the run used metadata and available abstracts, not full PDFs for every row; claims are therefore written conservatively.

## Field Box
Robot foundation models and closely adjacent embodied-agent methods that map multimodal context to robot actions: VLA models, generalist robot policies, language-conditioned manipulation, diffusion/flow action policies, action chunking, discrete/latent action tokenization, robot world models, cross-embodiment datasets, and physical perception methods that support action selection.

## Main Clusters
| Cluster | Rows | Representative hostile papers |
|---|---:|---|
| language-conditioned robot grounding | 764 | Any-point Trajectory Modeling for Policy Learning; Language-Conditioned Imitation Learning for Robot Manipulation Tasks; Large language models for chemistry robotics; Skill Transformer: A Monolithic Policy for Mobile Manipulation |
| robot reinforcement learning | 627 | Scaling Cross-Embodied Learning: One Policy for Manipulation, Navigation, Locomotion and Aviation; Learning Insertion Primitives with Discrete-Continuous Hybrid Action Space for Robotic Assembly Tasks; Continuous control actions learning and adaptation for robotic manipulation through reinforcement learning; X-Nav: Learning End-to-End Cross-Embodiment Navigation for Mobile Robots |
| action representation and control | 499 | Learned parametrized dynamic movement primitives with shared synergies for controlling robotic and musculoskeletal systems; Multimodal Human-Robot Interface for Accessible Remote Robotic Interventions in Hazardous Environments; Trends of Human-Robot Collaboration in Industry Contexts: Handover, Learning, and Metrics; Soft Robotic Grippers |
| robot foundation model scaling | 251 | Language Conditioned Imitation Learning Over Unstructured Data; Octo: An Open-Source Generalist Robot Policy; Open X-Embodiment: Robotic Learning Datasets and RT-X Models; RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation |
| robot world models and planning | 240 | Active Haptic Perception in Robots: A Review; Robot learning from demonstration by constructing skill trees; Pre- and post-contact policy decomposition for planar contact manipulation under uncertainty; Learning compositional models of robot skills for task and motion planning |
| supporting embodied intelligence | 222 | HTC-Grasp: A Hybrid Transformer-CNN Architecture for Robotic Grasp Detection; iSDF: Real-Time Neural Signed Distance Fields for Robot Perception; A Review of High-Throughput Field Phenotyping Systems: Focusing on Ground Robots; Design and Modeling of a Parallel-Pipe-Crawling Pneumatic Soft Robot |
| multimodal physical perception | 184 | JUICER: Data-Efficient Imitation Learning for Robotic Assembly; Artificial Intelligence and the Future of Surgical Robotics; Object Manipulation with an Anthropomorphic Robotic Hand via Deep Reinforcement Learning with a Synergy Space of Natural Hand Poses; PointACT: Automatic Robot Manipulation with Cross-Modal Action Chunking Transformer on Image-Point Cloud |
| diffusion visuomotor policies | 134 | OpenVLA: An Open-Source Vision-Language-Action Model; Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review; GR00T N1: An Open Foundation Model for Generalist Humanoid Robots; TinyVLA: Toward Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation |
| vision-language-action robot foundation models | 115 | A Survey of Robot Intelligence with Large Language Models; RT-2: Vision-Language-Action Models for Generalizable Robotic Control: A Comprehensive Review; RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control; $π_0$: A Vision-Language-Action Flow Model for General Robot Control |
| imitation learning and demonstrations | 70 | Toward Teaching by Demonstration for Robot-Assisted Minimally Invasive Surgery; Dynamic Movement Primitives Based Robot Skills Learning; Autonomous Needle Manipulation for Robotic Surgical Suturing Based on Skills Learned from Demonstration; Adaptive Model-Based Myoelectric Control for a Soft Wearable Arm Exosuit: A New Generation of Wearable Robot Control |

## Recentness
Top recent year counts: 2026: 67, 2025: 203, 2024: 450, 2023: 486, 2022: 273, 2021: 254, 2020: 251, 2019: 212.

## Hidden Assumptions That May Be False
| # | Assumption | Why It May Fail |
|---:|---|---|
| 1 | Action-token identity | If two motor commands share a token, they are interchangeable for downstream control. |
| 2 | Semantic sufficiency | Language/vision semantics carry every motor distinction that matters physically. |
| 3 | Uniform bin meaning | A discretized action bin means the same thing across state, contact mode, tool, and embodiment. |
| 4 | Low-level controller invariance | The actuator/controller underneath a learned token remains calibrated and fixed. |
| 5 | Effect monotonicity | Small action-space distances imply small next-state effect distances. |
| 6 | State-independent action metric | One global metric on motor commands is enough to decide when actions are aliases. |
| 7 | Average success visibility | Task success reveals rare but dangerous collapsed commands. |
| 8 | Dataset ontology completeness | The demonstration labels expose all necessary command distinctions. |
| 9 | Embodiment exchangeability | A token learned on one robot transfers its physical meaning to another robot. |
| 10 | Contact observability | Vision-language context sees the contact variables that decide which command is correct. |
| 11 | Decoder uniqueness | A token has one safe decoded motor command rather than a state-conditioned set. |
| 12 | Residual repairability | Later continuous heads can recover distinctions already erased by an upstream discrete token. |
| 13 | Prompt grounding fidelity | Natural-language action names are aligned with low-level motor effects. |
| 14 | Temporal alias harmlessness | Action chunks that share a label stay safe across their whole horizon. |
| 15 | Calibration stationarity | A chart learned once remains valid under wear, latency, payload, and friction shifts. |
| 16 | Simulator faithfulness | Simulator-level action abstractions preserve real actuator non-identifiability. |
| 17 | Cross-task benignity | Aliases observed as harmless in one task remain harmless in nearby tasks. |
| 18 | Visual dominance | Visual tokens are enough to distinguish contact-sensitive action modes. |
| 19 | Policy confidence meaning | High confidence in a token means low physical ambiguity inside its fiber. |
| 20 | No hidden nullspace | The action representation has no null directions that matter after contact. |
| 21 | No many-to-one harm | Many-to-one action compression is harmless if decoded averages look plausible. |
| 22 | Benchmark action closure | A benchmark's action API contains all commands needed for real deployment. |
| 23 | Latent linear separability | Latent action clusters learned from demonstrations align with effect clusters. |
| 24 | Repair by scale | More data or a larger backbone will separate aliases without changing the action interface. |
| 25 | Evaluation stationarity | Train/test splits preserve the same action-effect map inside each token. |
| 26 | Instruction determinism | A single instruction implies one motor command rather than a distribution over physical modes. |
| 27 | Human-label granularity | Human action names have the right resolution for robot control. |
| 28 | Unimodal decoding | The best decoded action inside a token is a mean or mode, not a state-dependent chart. |
| 29 | No alias amplification | Closed-loop reuse of an aliased token will not amplify one-step effect errors. |
| 30 | Safety by abstraction | Coarser actions are safer because they hide low-level details. |

## Direction Candidates
| Direction | Broken Assumption | Central Mechanism | Why It Is Not A Weak Move | Main Risk |
|---|---|---|---|---|
| Effect-Separating Action Charts | Action-token identity and state-independent action metrics. | Treat each token as a fiber and split it by observed next-state effect signatures. | Changes the central object from token prediction to preservation of physical effect distinguishability; supports formal lower bounds and runnable repair evidence. | Needs transition/effect observations and synthetic evidence may not prove real-robot scale. |
| Cross-Embodiment Token Jacobians | Embodiment exchangeability. | Estimate a local Jacobian for each robot and map tokens through effect-normalized charts. | Directly attacks the multi-robot assumption in RT-X/OpenVLA-style corpora. | Easy to look like calibration or domain adaptation unless the paper proves token-level aliasing is the driver. |
| Tactile Alias Witnesses | Visual dominance and contact observability. | Use tactile/contact transients as witnesses that two same-token actions diverge physically. | Robotics-specific and not reducible to bigger language models. | May become a sensor-fusion paper rather than an action-representation paper. |
| Action-Fiber Identifiability Tests | Policy confidence meaning. | Certify when a token-only policy cannot identify the demonstrated command under an effect metric. | Clean theorem and diagnostic value. | Benchmark/diagnostic only unless paired with repair. |
| Closed-Loop Alias Amplification | No alias amplification. | Analyze how one-step alias errors compound when the same token is repeatedly decoded. | Explains failures missed by one-step imitation metrics. | Could become a control-stability analysis without a new repair. |
| Semantic Motor Ontology Revision | Human-label granularity. | Learn robot-native action names from effect equivalence classes instead of human verbs. | Reframes language grounding around physical semantics. | Hard to validate without real human-language data. |
| Alias-Aware Dataset Curation | Dataset ontology completeness. | Select demonstrations that maximize effect separation inside action-token fibers. | Targets data collection with a robotics-specific information criterion. | Too close to active learning/data improvement, explicitly weak unless combined with a new representation mechanism. |
| Continuous Decoder Escape Hatch | Residual repairability. | Attach continuous residuals to discrete VLA actions and regularize them by effect error. | Practical for deployed token policies. | Looks like combining existing modules unless the residual is derived from a formal fiber bound. |

## Chosen Direction
Robot foundation models that emit language-like or discretized action tokens can be physically non-identifiable: a single token may contain an action fiber whose members cause different next-state effects under the local robot dynamics. The paper introduces Effect-Separating Action Charts (ESAC), which audits each token by its effect diameter and repairs aliased tokens by splitting their fibers according to observed transition signatures.

## Why The Seed Survived The Sweep
The highest-ranked rows include OpenVLA, GR00T N1, FAST action tokenization, keypoint action tokens, RT-2, pi0, TinyVLA, VIMA, diffusion policy, ACT, and multiple VLA surveys. These make generic VLA scaling, action tokenization, multimodal prompts, diffusion/flow action generation, and cross-embodiment data clearly non-novel. The open slot is not another model or benchmark, but a mechanism-level claim: action tokens should be evaluated by the diameter of their physical effect fibers, and repaired by effect-separating charts when the diameter is too large.
