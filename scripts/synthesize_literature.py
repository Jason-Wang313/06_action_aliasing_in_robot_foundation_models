#!/usr/bin/env python3
"""Synthesize the literature matrix into the required planning documents."""

from __future__ import annotations

import csv
import os
import textwrap
from collections import Counter, defaultdict
from typing import Dict, Iterable, List


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOCS = os.path.join(ROOT, "docs")
MATRIX = os.path.join(DOCS, "related_work_matrix.csv")


HIDDEN_ASSUMPTIONS = [
    ("Action-token identity", "If two motor commands share a token, they are interchangeable for downstream control."),
    ("Semantic sufficiency", "Language/vision semantics carry every motor distinction that matters physically."),
    ("Uniform bin meaning", "A discretized action bin means the same thing across state, contact mode, tool, and embodiment."),
    ("Low-level controller invariance", "The actuator/controller underneath a learned token remains calibrated and fixed."),
    ("Effect monotonicity", "Small action-space distances imply small next-state effect distances."),
    ("State-independent action metric", "One global metric on motor commands is enough to decide when actions are aliases."),
    ("Average success visibility", "Task success reveals rare but dangerous collapsed commands."),
    ("Dataset ontology completeness", "The demonstration labels expose all necessary command distinctions."),
    ("Embodiment exchangeability", "A token learned on one robot transfers its physical meaning to another robot."),
    ("Contact observability", "Vision-language context sees the contact variables that decide which command is correct."),
    ("Decoder uniqueness", "A token has one safe decoded motor command rather than a state-conditioned set."),
    ("Residual repairability", "Later continuous heads can recover distinctions already erased by an upstream discrete token."),
    ("Prompt grounding fidelity", "Natural-language action names are aligned with low-level motor effects."),
    ("Temporal alias harmlessness", "Action chunks that share a label stay safe across their whole horizon."),
    ("Calibration stationarity", "A chart learned once remains valid under wear, latency, payload, and friction shifts."),
    ("Simulator faithfulness", "Simulator-level action abstractions preserve real actuator non-identifiability."),
    ("Cross-task benignity", "Aliases observed as harmless in one task remain harmless in nearby tasks."),
    ("Visual dominance", "Visual tokens are enough to distinguish contact-sensitive action modes."),
    ("Policy confidence meaning", "High confidence in a token means low physical ambiguity inside its fiber."),
    ("No hidden nullspace", "The action representation has no null directions that matter after contact."),
    ("No many-to-one harm", "Many-to-one action compression is harmless if decoded averages look plausible."),
    ("Benchmark action closure", "A benchmark's action API contains all commands needed for real deployment."),
    ("Latent linear separability", "Latent action clusters learned from demonstrations align with effect clusters."),
    ("Repair by scale", "More data or a larger backbone will separate aliases without changing the action interface."),
    ("Evaluation stationarity", "Train/test splits preserve the same action-effect map inside each token."),
    ("Instruction determinism", "A single instruction implies one motor command rather than a distribution over physical modes."),
    ("Human-label granularity", "Human action names have the right resolution for robot control."),
    ("Unimodal decoding", "The best decoded action inside a token is a mean or mode, not a state-dependent chart."),
    ("No alias amplification", "Closed-loop reuse of an aliased token will not amplify one-step effect errors."),
    ("Safety by abstraction", "Coarser actions are safer because they hide low-level details."),
]


DIRECTIONS = [
    {
        "name": "Effect-Separating Action Charts",
        "breaks": "Action-token identity and state-independent action metrics.",
        "mechanism": "Treat each token as a fiber and split it by observed next-state effect signatures.",
        "why_strong": "Changes the central object from token prediction to preservation of physical effect distinguishability; supports formal lower bounds and runnable repair evidence.",
        "risk": "Needs transition/effect observations and synthetic evidence may not prove real-robot scale.",
    },
    {
        "name": "Cross-Embodiment Token Jacobians",
        "breaks": "Embodiment exchangeability.",
        "mechanism": "Estimate a local Jacobian for each robot and map tokens through effect-normalized charts.",
        "why_strong": "Directly attacks the multi-robot assumption in RT-X/OpenVLA-style corpora.",
        "risk": "Easy to look like calibration or domain adaptation unless the paper proves token-level aliasing is the driver.",
    },
    {
        "name": "Tactile Alias Witnesses",
        "breaks": "Visual dominance and contact observability.",
        "mechanism": "Use tactile/contact transients as witnesses that two same-token actions diverge physically.",
        "why_strong": "Robotics-specific and not reducible to bigger language models.",
        "risk": "May become a sensor-fusion paper rather than an action-representation paper.",
    },
    {
        "name": "Action-Fiber Identifiability Tests",
        "breaks": "Policy confidence meaning.",
        "mechanism": "Certify when a token-only policy cannot identify the demonstrated command under an effect metric.",
        "why_strong": "Clean theorem and diagnostic value.",
        "risk": "Benchmark/diagnostic only unless paired with repair.",
    },
    {
        "name": "Closed-Loop Alias Amplification",
        "breaks": "No alias amplification.",
        "mechanism": "Analyze how one-step alias errors compound when the same token is repeatedly decoded.",
        "why_strong": "Explains failures missed by one-step imitation metrics.",
        "risk": "Could become a control-stability analysis without a new repair.",
    },
    {
        "name": "Semantic Motor Ontology Revision",
        "breaks": "Human-label granularity.",
        "mechanism": "Learn robot-native action names from effect equivalence classes instead of human verbs.",
        "why_strong": "Reframes language grounding around physical semantics.",
        "risk": "Hard to validate without real human-language data.",
    },
    {
        "name": "Alias-Aware Dataset Curation",
        "breaks": "Dataset ontology completeness.",
        "mechanism": "Select demonstrations that maximize effect separation inside action-token fibers.",
        "why_strong": "Targets data collection with a robotics-specific information criterion.",
        "risk": "Too close to active learning/data improvement, explicitly weak unless combined with a new representation mechanism.",
    },
    {
        "name": "Continuous Decoder Escape Hatch",
        "breaks": "Residual repairability.",
        "mechanism": "Attach continuous residuals to discrete VLA actions and regularize them by effect error.",
        "why_strong": "Practical for deployed token policies.",
        "risk": "Looks like combining existing modules unless the residual is derived from a formal fiber bound.",
    },
]


CHOSEN_THESIS = (
    "Robot foundation models that emit language-like or discretized action tokens can be physically non-identifiable: "
    "a single token may contain an action fiber whose members cause different next-state effects under the local robot dynamics. "
    "The paper introduces Effect-Separating Action Charts (ESAC), which audits each token by its effect diameter and repairs aliased "
    "tokens by splitting their fibers according to observed transition signatures."
)


def read_rows() -> List[Dict[str, str]]:
    with open(MATRIX, "r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def md_escape(text: str) -> str:
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


def write(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text.rstrip() + "\n")


def top_representatives(rows: List[Dict[str, str]], cluster: str, n: int = 8) -> List[Dict[str, str]]:
    return [r for r in rows if r.get("topic_cluster") == cluster][:n]


def write_deep_read_csv(rows: List[Dict[str, str]]) -> None:
    fields = [
        "rank",
        "title",
        "year",
        "topic_cluster",
        "problem_claimed",
        "mechanism_introduced",
        "hidden_assumptions",
        "variables_fixed",
        "failure_modes_ignored",
        "what_makes_less_novel",
        "what_leaves_open",
        "url",
    ]
    path = os.path.join(DOCS, "deep_read_extractions.csv")
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows[:250]:
            writer.writerow(row)


def literature_map(rows: List[Dict[str, str]]) -> str:
    cluster_counts = Counter(r.get("topic_cluster", "unknown") for r in rows)
    year_counts = Counter(r.get("year", "unknown") for r in rows if r.get("year"))
    lines: List[str] = []
    lines.append("# Literature Map")
    lines.append("")
    lines.append("## Corpus Construction")
    lines.append(f"- Landscape sweep: {len(rows)} unique OpenAlex/manual-seed entries in `docs/related_work_matrix.csv`.")
    lines.append("- Serious skim: top 300 rows by robotics/action/foundation relevance score.")
    lines.append("- Deep read: top 250 rows with extraction fields in `docs/deep_read_extractions.csv`.")
    lines.append("- Hostile set: top 100 rows, emphasizing VLA/action-token/foundation-model papers that could erase novelty.")
    lines.append("- Extraction caveat: the run used metadata and available abstracts, not full PDFs for every row; claims are therefore written conservatively.")
    lines.append("")
    lines.append("## Field Box")
    lines.append("Robot foundation models and closely adjacent embodied-agent methods that map multimodal context to robot actions: VLA models, generalist robot policies, language-conditioned manipulation, diffusion/flow action policies, action chunking, discrete/latent action tokenization, robot world models, cross-embodiment datasets, and physical perception methods that support action selection.")
    lines.append("")
    lines.append("## Main Clusters")
    lines.append("| Cluster | Rows | Representative hostile papers |")
    lines.append("|---|---:|---|")
    for cluster, count in cluster_counts.most_common(12):
        reps = "; ".join(md_escape(r["title"]) for r in top_representatives(rows, cluster, 4))
        lines.append(f"| {md_escape(cluster)} | {count} | {reps} |")
    lines.append("")
    lines.append("## Recentness")
    recent = ", ".join(f"{year}: {count}" for year, count in sorted(year_counts.items(), reverse=True)[:8])
    lines.append(f"Top recent year counts: {recent}.")
    lines.append("")
    lines.append("## Hidden Assumptions That May Be False")
    lines.append("| # | Assumption | Why It May Fail |")
    lines.append("|---:|---|---|")
    for i, (name, why) in enumerate(HIDDEN_ASSUMPTIONS, start=1):
        lines.append(f"| {i} | {md_escape(name)} | {md_escape(why)} |")
    lines.append("")
    lines.append("## Direction Candidates")
    lines.append("| Direction | Broken Assumption | Central Mechanism | Why It Is Not A Weak Move | Main Risk |")
    lines.append("|---|---|---|---|---|")
    for d in DIRECTIONS:
        lines.append(f"| {d['name']} | {d['breaks']} | {d['mechanism']} | {d['why_strong']} | {d['risk']} |")
    lines.append("")
    lines.append("## Chosen Direction")
    lines.append(CHOSEN_THESIS)
    lines.append("")
    lines.append("## Why The Seed Survived The Sweep")
    lines.append("The highest-ranked rows include OpenVLA, GR00T N1, FAST action tokenization, keypoint action tokens, RT-2, pi0, TinyVLA, VIMA, diffusion policy, ACT, and multiple VLA surveys. These make generic VLA scaling, action tokenization, multimodal prompts, diffusion/flow action generation, and cross-embodiment data clearly non-novel. The open slot is not another model or benchmark, but a mechanism-level claim: action tokens should be evaluated by the diameter of their physical effect fibers, and repaired by effect-separating charts when the diameter is too large.")
    return "\n".join(lines)


def hostile_prior_work(rows: List[Dict[str, str]]) -> str:
    lines = ["# Hostile Prior Work", ""]
    lines.append("These are the 100 papers most likely to make the proposed paper look non-novel. Each entry records the mechanism it already contributes and the residual opening for action-fiber aliasing.")
    lines.append("")
    for row in rows[:100]:
        lines.append(f"## {row.get('rank')}. {row.get('title')}")
        lines.append(f"- Year/venue: {row.get('year', '')} / {row.get('venue', '')}")
        lines.append(f"- Problem claimed: {row.get('problem_claimed', '')}")
        lines.append(f"- Actual mechanism introduced: {row.get('mechanism_introduced', '')}")
        lines.append(f"- Hidden assumptions: {row.get('hidden_assumptions', '')}")
        lines.append(f"- Variables treated as fixed: {row.get('variables_fixed', '')}")
        lines.append(f"- Failure modes ignored: {row.get('failure_modes_ignored', '')}")
        lines.append(f"- What it makes less novel: {row.get('what_makes_less_novel', '')}")
        lines.append(f"- What it leaves open: {row.get('what_leaves_open', '')}")
        if row.get("url"):
            lines.append(f"- Link: {row.get('url')}")
        lines.append("")
    return "\n".join(lines)


def novelty_boundary(rows: List[Dict[str, str]]) -> str:
    hostile_titles = [r["title"] for r in rows[:20]]
    lines = ["# Novelty Boundary Map", ""]
    lines.append("## Outside The Claim")
    outside = [
        "We do not claim a new foundation model backbone.",
        "We do not claim a new web-scale robot dataset.",
        "We do not claim diffusion, flow matching, ACT-style action chunking, or VLA token emission as new.",
        "We do not claim language-conditioned robot manipulation is new.",
        "We do not claim uncertainty estimation, active learning, or LLM planning as the central contribution.",
        "We do not claim real-robot deployment evidence in this attempt.",
    ]
    lines.extend(f"- {x}" for x in outside)
    lines.append("")
    lines.append("## Inside The Claim")
    inside = [
        "A formal action-fiber view of token policies: a token denotes a set of motor commands, not one command.",
        "An alias metric based on next-state effect diameter inside each token fiber.",
        "A lower-bound argument that no token-only decoder can recover distinctions erased by the token map.",
        "A repair mechanism, ESAC, that splits token fibers by transition/effect signatures rather than by language labels or raw action distance.",
        "Runnably demonstrated failure and repair in a controlled embodied-control simulation.",
    ]
    lines.extend(f"- {x}" for x in inside)
    lines.append("")
    lines.append("## Closest Hostile Papers")
    for title in hostile_titles:
        lines.append(f"- {title}")
    lines.append("")
    lines.append("## Boundary Statement")
    lines.append("If a prior work already audits token fibers by physical next-state effect diameter and repairs VLA/action-token policies by effect-separating charts with an impossibility argument, this paper is not novel. If prior work only introduces better tokens, larger VLA models, continuous decoders, action chunking, or broader datasets without measuring within-token effect diameter, it is adjacent but does not close the gap.")
    return "\n".join(lines)


def novelty_decision(rows: List[Dict[str, str]]) -> str:
    lines = ["# Novelty Decision", ""]
    lines.append("## Decision")
    lines.append("Proceed with Effect-Separating Action Charts (ESAC).")
    lines.append("")
    lines.append("## Chosen Thesis")
    lines.append(CHOSEN_THESIS)
    lines.append("")
    lines.append("## Why This Beats The Alternatives")
    lines.append("- It changes which mechanism is central: from predicting the right token to preserving physical distinguishability inside a token fiber.")
    lines.append("- It gives a formal object to attack: the effect diameter of a token fiber under local dynamics.")
    lines.append("- It yields a concrete repair: split a token by observed transition signatures, then decode from a chart-specific prototype.")
    lines.append("- It avoids the forbidden weak moves: no bigger model, no bigger dataset, no uncertainty wrapper, no LLM planner, no RL requirement, and not merely a benchmark.")
    lines.append("")
    lines.append("## Literature Pressure")
    lines.append("The top-ranked matrix rows make these claims unsafe: generic VLA training, action tokenization, action chunking, diffusion/flow policies, multimodal prompting, cross-embodiment data, and language affordance grounding. The proposed paper must therefore argue specifically about non-identifiability caused by many-to-one action representations.")
    lines.append("")
    lines.append("## Required Evidence")
    lines.append("- A theorem or proposition showing token-only decoders inherit irreducible effect error when a fiber has large effect diameter.")
    lines.append("- An alias audit that predicts token-policy failure.")
    lines.append("- A repair experiment showing ESAC improves success while holding model capacity modest and fixed.")
    lines.append("- Honest limitation language: simulation-only evidence in this attempt.")
    return "\n".join(lines)


def claims_doc() -> str:
    lines = ["# Claims", ""]
    lines.append("## Supported By Formal Argument")
    lines.append("- If two demonstrations share a token but require different next-state effects, any decoder that observes only the token must incur nonzero error on at least one member of the fiber.")
    lines.append("- The minimum worst-case one-step effect error of a token-only decoder is at least half the effect diameter of that token fiber.")
    lines.append("- Splitting a token fiber into charts with smaller effect diameter tightens that lower bound.")
    lines.append("")
    lines.append("## Supported By Runnable Evidence")
    lines.append("- In the synthetic contact-control environment, coarse action tokens collapse physically distinct commands and fail as alias strength increases.")
    lines.append("- ESAC uses observed transition effects to split the collapsed token fibers and recovers much of the lost success.")
    lines.append("- The measured alias energy correlates with coarse-token failure in the sweep.")
    lines.append("")
    lines.append("## Unsupported Or Not Claimed")
    lines.append("- No claim of real-robot deployment.")
    lines.append("- No claim that ESAC dominates continuous-action policies when those policies are allowed to bypass tokenization.")
    lines.append("- No claim that all VLA models suffer severe aliasing; the claim is conditional on large effect diameter within action-token fibers.")
    lines.append("- No claim that clustering is new by itself; the novelty is the action-fiber/effect-diameter diagnosis and repair target.")
    return "\n".join(lines)


def reviewer_attacks(rows: List[Dict[str, str]]) -> str:
    attacks = [
        ("This is synthetic only.", "Agree. The paper should be framed as a mechanism and audit/repair demonstration, not as a deployment-ready robot system."),
        ("FAST/keypoint action tokens already study action tokenization.", "They make tokenization central prior art; the boundary is that ESAC audits within-token physical effect diameter and repairs aliases after token formation."),
        ("Continuous policies such as diffusion or flow models avoid discrete token aliasing.", "They are an important outside-scope baseline. The claim targets tokenized/language-like action interfaces used by many RFMs, not all robot policies."),
        ("A bigger decoder could learn the hidden distinction.", "Only if the distinction remains in the representation available to the decoder. The lower bound applies after the many-to-one token map."),
        ("The repair is just clustering.", "Raw clustering is not the claim; ESAC clusters a token fiber by transition effects because the physical effect metric defines aliasing."),
        ("The context variable in the simulation is too easy.", "The ablation hiding that variable must fail, showing the method depends on observable alias-resolving information."),
        ("The method needs next-state effects, unavailable at test time.", "It uses transition effects during auditing/training to construct charts; at test time it predicts chart ids from observations like other imitation policies."),
        ("The theorem is obvious.", "The theorem is simple by design; its value is forcing VLA action-token papers to report the physical diameter of token fibers, not only token accuracy."),
        ("Action-space binning with more bins solves it.", "The paper must show that more bins are a capacity tradeoff, while effect charts split only where physical effects diverge."),
        ("The alias metric depends on a chosen state metric.", "Correct; the metric must be task-relevant. The paper should present this as an explicit design choice rather than a universal scalar."),
        ("Surveys already mention embodiment/action mismatch.", "Mentioning mismatch is not the same as measuring token-fiber effect diameter or repairing it with effect charts."),
        ("A learned world model can serve as verifier.", "ESAC does not rely on verifier rejection; it changes the action representation consumed by the policy."),
    ]
    lines = ["# Reviewer Attacks", ""]
    for attack, response in attacks:
        lines.append(f"## Attack: {attack}")
        lines.append(f"Response: {response}")
        lines.append("")
    lines.append("## Most Hostile Titles To Re-read Before Submission")
    for row in rows[:30]:
        lines.append(f"- {row.get('title')} ({row.get('year')})")
    return "\n".join(lines)


def serious_skim(rows: List[Dict[str, str]]) -> str:
    lines = ["# 300-Paper Serious Skim", ""]
    lines.append("Top 300 rows were inspected through title, abstract-derived extraction fields, query provenance, and topic cluster. This file is a compact index; detailed extraction fields live in the CSV matrix.")
    lines.append("")
    lines.append("| Rank | Title | Year | Cluster | Leaves Open |")
    lines.append("|---:|---|---:|---|---|")
    for row in rows[:300]:
        lines.append(f"| {row.get('rank')} | {md_escape(row.get('title', ''))} | {row.get('year', '')} | {md_escape(row.get('topic_cluster', ''))} | {md_escape(row.get('what_leaves_open', ''))} |")
    return "\n".join(lines)


def main() -> int:
    os.makedirs(DOCS, exist_ok=True)
    rows = read_rows()
    write_deep_read_csv(rows)
    write(os.path.join(DOCS, "literature_map.md"), literature_map(rows))
    write(os.path.join(DOCS, "hostile_prior_work.md"), hostile_prior_work(rows))
    write(os.path.join(DOCS, "novelty_boundary_map.md"), novelty_boundary(rows))
    write(os.path.join(DOCS, "novelty_decision.md"), novelty_decision(rows))
    write(os.path.join(DOCS, "claims.md"), claims_doc())
    write(os.path.join(DOCS, "reviewer_attacks.md"), reviewer_attacks(rows))
    write(os.path.join(DOCS, "serious_skim_300.md"), serious_skim(rows))
    print(f"[done] synthesized literature documents from {len(rows)} rows", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
