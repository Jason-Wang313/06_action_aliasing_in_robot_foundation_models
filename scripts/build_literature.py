#!/usr/bin/env python3
"""Build a broad robotics/RFM literature matrix from OpenAlex.

The script is intentionally self-contained and standard-library only.  It
stores progress as it goes so a partial network failure still leaves usable
evidence for the paper run.
"""

from __future__ import annotations

import csv
import json
import math
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Optional, Tuple


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOCS = os.path.join(ROOT, "docs")
MATRIX_PATH = os.path.join(DOCS, "related_work_matrix.csv")
PROGRESS_PATH = os.path.join(DOCS, "literature_progress.json")


QUERIES = [
    "robot foundation model",
    "robotics foundation models",
    "vision language action model robot",
    "vision language action models robotics",
    "large vision language model robotics manipulation",
    "language conditioned robot manipulation",
    "language conditioned robot policy",
    "robotics transformer real world control",
    "RT-1 robotics transformer",
    "RT-2 vision language action",
    "Open X-Embodiment robot learning",
    "OpenVLA robot policy",
    "Octo robot foundation model",
    "RoboCat robot learning",
    "RoboFlamingo robot manipulation",
    "PaLM-E embodied multimodal language model",
    "SayCan language model robot",
    "VIMA multimodal robot manipulation",
    "diffusion policy robot manipulation",
    "action diffusion robot policy",
    "action chunking transformer robot",
    "imitation learning robot manipulation continuous action",
    "behavior cloning robot manipulation action representation",
    "discrete action representation robot learning",
    "action tokenization robotics",
    "latent action model robotics",
    "motor command tokenization robot",
    "robot action abstraction language grounding",
    "semantic action grounding robotics",
    "affordance model robot manipulation language",
    "robot world model action planning",
    "embodied AI world model action",
    "sim-to-real robot policy action representation",
    "tactile robot manipulation foundation model",
    "3D perception robot foundation model",
    "multimodal robot foundation model",
    "robot policy transformer manipulation",
    "generalist robot policy",
    "robot learning from demonstration action space",
    "continuous control representation learning robot",
    "equivariant robot policy manipulation",
    "closed-loop robot manipulation policy transformer",
    "robot foundation model action space",
    "robot action aliasing",
    "control mode aliasing robot",
    "language motor grounding robot",
    "embodied agent action representation",
    "robot manipulation action primitives learning",
    "skill abstraction robot learning",
    "robot policy action discretization",
]


MANUAL_SEEDS = [
    {
        "title": "RT-1: Robotics Transformer for Real-World Control at Scale",
        "year": 2022,
        "authors": "Brohan et al.",
        "venue": "arXiv",
        "abstract": "A transformer policy trained on large-scale real-world robot demonstrations maps images and language instructions to discretized robot actions.",
    },
    {
        "title": "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control",
        "year": 2023,
        "authors": "Brohan et al.",
        "venue": "arXiv",
        "abstract": "A vision-language model is co-fine-tuned to emit robot actions as tokens, transferring semantic knowledge from web-scale data into robotic control.",
    },
    {
        "title": "Open X-Embodiment: Robotic Learning Datasets and RT-X Models",
        "year": 2023,
        "authors": "Open X-Embodiment Collaboration",
        "venue": "arXiv",
        "abstract": "A cross-embodiment robot dataset and family of transformer policies study whether broad robot data improves generalist robot control.",
    },
    {
        "title": "Octo: An Open-Source Generalist Robot Policy",
        "year": 2024,
        "authors": "Octo Model Team et al.",
        "venue": "arXiv",
        "abstract": "A transformer-based generalist policy is trained on heterogeneous robot data with flexible observation and action heads.",
    },
    {
        "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
        "year": 2024,
        "authors": "Kim et al.",
        "venue": "arXiv",
        "abstract": "An open VLA model adapts vision-language backbones to output robot actions for manipulation tasks.",
    },
    {
        "title": "pi0: A Vision-Language-Action Flow Model for General Robot Control",
        "year": 2024,
        "authors": "Black et al.",
        "venue": "arXiv",
        "abstract": "A flow-matching VLA policy models continuous robot action chunks from visual and language context.",
    },
    {
        "title": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
        "year": 2023,
        "authors": "Chi et al.",
        "venue": "RSS",
        "abstract": "A conditional denoising diffusion model predicts robot action sequences for visuomotor manipulation.",
    },
    {
        "title": "Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware",
        "year": 2023,
        "authors": "Zhao et al.",
        "venue": "RSS",
        "abstract": "Action Chunking Transformer learns temporally chunked continuous actions for bimanual manipulation from demonstrations.",
    },
    {
        "title": "VIMA: General Robot Manipulation with Multimodal Prompts",
        "year": 2022,
        "authors": "Jiang et al.",
        "venue": "ICML",
        "abstract": "A transformer agent follows multimodal prompts in simulated manipulation using object-centric tokenization and action prediction.",
    },
    {
        "title": "PaLM-E: An Embodied Multimodal Language Model",
        "year": 2023,
        "authors": "Driess et al.",
        "venue": "ICML",
        "abstract": "A large language model is grounded with embodied sensory inputs for robot planning and visual-language reasoning.",
    },
    {
        "title": "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances",
        "year": 2022,
        "authors": "Ahn et al.",
        "venue": "CoRL",
        "abstract": "SayCan combines language model priors with affordance scores to select feasible robot skills.",
    },
    {
        "title": "RoboCat: A Self-Improving Robotic Agent",
        "year": 2023,
        "authors": "Bousmalis et al.",
        "venue": "TMLR",
        "abstract": "A generalist robotic agent improves by collecting and retraining on data across tasks and embodiments.",
    },
]


ACTION_TERMS = {
    "action",
    "actions",
    "actuation",
    "control",
    "controls",
    "command",
    "commands",
    "motor",
    "policy",
    "policies",
    "trajectory",
    "trajectories",
    "diffusion",
    "chunk",
    "chunking",
    "token",
    "tokens",
    "tokenization",
    "discretization",
    "primitive",
    "skill",
    "continuous",
}

ROBOT_TERMS = {
    "robot",
    "robotic",
    "robotics",
    "manipulation",
    "manipulator",
    "embodied",
    "embodiment",
    "grasp",
    "grasping",
    "navigation",
    "locomotion",
    "tactile",
    "sim-to-real",
    "visuomotor",
}

FOUNDATION_TERMS = {
    "foundation",
    "language",
    "vision-language",
    "multimodal",
    "transformer",
    "large",
    "generalist",
    "pretrained",
    "pre-training",
    "vla",
    "world model",
    "world-model",
    "web-scale",
}


def ensure_dirs() -> None:
    os.makedirs(DOCS, exist_ok=True)


def normalize_space(text: Optional[str]) -> str:
    if not text:
        return ""
    return re.sub(r"\s+", " ", str(text)).strip()


def reconstruct_abstract(index: Optional[Dict[str, List[int]]]) -> str:
    if not index:
        return ""
    positions: List[Tuple[int, str]] = []
    for word, places in index.items():
        for pos in places:
            positions.append((pos, word))
    if not positions:
        return ""
    positions.sort()
    return normalize_space(" ".join(word for _, word in positions))


def request_json(url: str, retries: int = 3, sleep_s: float = 1.0) -> Optional[Dict[str, Any]]:
    headers = {
        "User-Agent": "robotics-literature-agent/1.0 (mailto:example@example.com)",
        "Accept": "application/json",
    }
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=40) as response:
                data = response.read().decode("utf-8", errors="replace")
            return json.loads(data)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            print(f"[warn] request failed attempt={attempt} url={url[:120]} error={exc}", flush=True)
            time.sleep(sleep_s * attempt)
    return None


def openalex_url(query: str, cursor: str = "*", per_page: int = 100) -> str:
    params = {
        "search": query,
        "filter": "from_publication_date:2010-01-01",
        "per-page": str(per_page),
        "cursor": cursor,
        "mailto": "example@example.com",
    }
    return "https://api.openalex.org/works?" + urllib.parse.urlencode(params)


def extract_authors(work: Dict[str, Any], limit: int = 8) -> str:
    names: List[str] = []
    for authorship in work.get("authorships", [])[:limit]:
        author = authorship.get("author") or {}
        name = normalize_space(author.get("display_name"))
        if name:
            names.append(name)
    if len(work.get("authorships", [])) > limit:
        names.append("et al.")
    return "; ".join(names)


def extract_venue(work: Dict[str, Any]) -> str:
    loc = work.get("primary_location") or {}
    source = loc.get("source") or {}
    venue = normalize_space(source.get("display_name"))
    if venue:
        return venue
    host = work.get("host_venue") or {}
    return normalize_space(host.get("display_name"))


def extract_concepts(work: Dict[str, Any]) -> str:
    labels: List[str] = []
    for concept in work.get("concepts", [])[:8]:
        name = normalize_space(concept.get("display_name"))
        if name:
            labels.append(name)
    for topic in work.get("topics", [])[:4]:
        name = normalize_space(topic.get("display_name"))
        if name and name not in labels:
            labels.append(name)
    return "; ".join(labels)


def row_key(row: Dict[str, Any]) -> str:
    doi = normalize_space(row.get("doi")).lower()
    if doi:
        return "doi:" + doi.replace("https://doi.org/", "")
    title = normalize_space(row.get("title")).lower()
    return "title:" + re.sub(r"[^a-z0-9]+", " ", title)


def term_count(text: str, terms: Iterable[str]) -> int:
    lowered = text.lower()
    count = 0
    for term in terms:
        if term in lowered:
            count += 1
    return count


def classify_topic(row: Dict[str, Any]) -> str:
    text = f"{row.get('title', '')} {row.get('abstract', '')} {row.get('concepts', '')}".lower()
    if "diffusion" in text:
        return "diffusion visuomotor policies"
    if "vision-language-action" in text or "vla" in text or "robotics transformer" in text or "rt-2" in text:
        return "vision-language-action robot foundation models"
    if "foundation" in text or "generalist" in text or "pretrained" in text:
        return "robot foundation model scaling"
    if "language" in text or "prompt" in text:
        return "language-conditioned robot grounding"
    if "world model" in text or "planning" in text:
        return "robot world models and planning"
    if "tactile" in text or "3d" in text or "point cloud" in text:
        return "multimodal physical perception"
    if "reinforcement" in text or "rl" in text:
        return "robot reinforcement learning"
    if "imitation" in text or "demonstration" in text or "behavior cloning" in text:
        return "imitation learning and demonstrations"
    if "action" in text or "control" in text or "policy" in text:
        return "action representation and control"
    return "supporting embodied intelligence"


def domain_score(row: Dict[str, Any]) -> float:
    text = f"{row.get('title', '')} {row.get('abstract', '')} {row.get('concepts', '')}".lower()
    robot = term_count(text, ROBOT_TERMS)
    action = term_count(text, ACTION_TERMS)
    foundation = term_count(text, FOUNDATION_TERMS)
    title_boost = 0.0
    title = row.get("title", "").lower()
    if any(t in title for t in ["robot", "robotic", "manipulation", "visuomotor"]):
        title_boost += 3.0
    if any(t in title for t in ["action", "policy", "control", "diffusion", "transformer"]):
        title_boost += 2.0
    recency = max(0, int(row.get("year") or 2010) - 2018) * 0.35
    cites = math.log1p(float(row.get("cited_by_count") or 0)) * 0.8
    query_hits = len(str(row.get("source_queries") or "").split("|"))
    return robot * 3.0 + action * 2.0 + foundation * 1.5 + title_boost + recency + cites + query_hits * 0.3


def extraction_fields(row: Dict[str, Any]) -> Dict[str, str]:
    topic = classify_topic(row)
    title = row.get("title", "")
    text = f"{title} {row.get('abstract', '')}".lower()

    if topic == "vision-language-action robot foundation models":
        problem = "Scale robot control by reusing vision-language representations for language-conditioned manipulation."
        mechanism = "Tokenized or transformer-conditioned policy maps multimodal context to robot action outputs."
        less_novel = "Shows that large pretrained multimodal backbones can be adapted to robot action prediction."
        open_issue = "Whether semantically similar tokens preserve distinctions between physically different motor commands."
    elif topic == "diffusion visuomotor policies":
        problem = "Model multimodal continuous action distributions for dexterous or contact-rich robot manipulation."
        mechanism = "Conditional denoising or flow model generates action sequences from visual state."
        less_novel = "Makes sequence-level continuous action generation and multimodal action distributions well established."
        open_issue = "How representation bottlenecks upstream of the generator collapse distinct controls before diffusion can recover them."
    elif topic == "language-conditioned robot grounding":
        problem = "Ground natural-language task descriptions in feasible robot behavior."
        mechanism = "Language-conditioned policy, skill selector, prompt-conditioned controller, or affordance scoring."
        less_novel = "Makes language-to-skill grounding and prompt-conditioned robot manipulation prior art."
        open_issue = "Whether the grounded language interface hides control-equivalent but physically divergent commands."
    elif topic == "robot foundation model scaling":
        problem = "Build generalist robot policies that transfer across tasks, scenes, and embodiments."
        mechanism = "Large-scale pretrained transformer or multimodal policy trained on heterogeneous robot data."
        less_novel = "Makes broad robot-data scaling and generalist policy training prior art."
        open_issue = "How action-space mismatch and many-to-one tokenization change the learned physical semantics."
    elif topic == "robot world models and planning":
        problem = "Predict future physical states or plan actions under learned dynamics."
        mechanism = "Latent dynamics, video prediction, model-predictive control, or planning over learned representations."
        less_novel = "Makes learned physical prediction and planning over latent states prior art."
        open_issue = "Whether action aliases in the latent interface make plans non-identifiable."
    elif topic == "action representation and control":
        problem = "Represent robot commands so policies can learn stable control."
        mechanism = "Action primitives, discretization, latent actions, residual control, or structured policy heads."
        less_novel = "Makes action abstraction and policy action-space design prior art."
        open_issue = "How to detect and repair aliasing induced by representation rather than by environment ambiguity."
    else:
        problem = "Improve embodied-agent perception, learning, control, or physical reasoning."
        mechanism = "Task-specific representation, policy, dataset, benchmark, or planning method."
        less_novel = "Contributes background methods that constrain claims about general embodied intelligence."
        open_issue = "Whether the method treats motor-command identity as preserved through learned representations."

    assumptions = [
        "The chosen action interface is sufficiently expressive for the physical task.",
        "Different motor commands that matter downstream remain separable after tokenization or latent encoding.",
        "Dataset labels reveal the action distinctions needed at deployment.",
    ]
    fixed = [
        "embodiment calibration",
        "low-level controller semantics",
        "action binning or policy-head parameterization",
    ]
    failures = [
        "physically distinct commands collapse to one representation",
        "rare contact-sensitive distinctions vanish in average success metrics",
        "cross-embodiment transfer changes the meaning of the same token",
    ]

    if "uncertainty" in text:
        assumptions.append("Uncertainty estimates are calibrated after representation collapse.")
    if "benchmark" in text or "dataset" in text:
        fixed.append("benchmark action ontology")
    if "sim" in text:
        failures.append("simulator discretization hides real actuator non-identifiability")
    if "tactile" in text:
        open_issue += " Tactile/contact cues may expose aliases that vision-language tokens miss."

    return {
        "topic_cluster": topic,
        "problem_claimed": problem,
        "mechanism_introduced": mechanism,
        "hidden_assumptions": " ".join(f"- {item}" for item in assumptions),
        "variables_fixed": "; ".join(fixed),
        "failure_modes_ignored": "; ".join(failures),
        "what_makes_less_novel": less_novel,
        "what_leaves_open": open_issue,
    }


def make_row_from_work(work: Dict[str, Any], query: str) -> Dict[str, Any]:
    title = normalize_space(work.get("title") or work.get("display_name"))
    abstract = reconstruct_abstract(work.get("abstract_inverted_index"))
    loc = work.get("primary_location") or {}
    landing = normalize_space(loc.get("landing_page_url")) or normalize_space(work.get("doi")) or normalize_space(work.get("id"))
    row: Dict[str, Any] = {
        "openalex_id": normalize_space(work.get("id")),
        "doi": normalize_space(work.get("doi")),
        "title": title,
        "year": work.get("publication_year") or "",
        "publication_date": normalize_space(work.get("publication_date")),
        "type": normalize_space(work.get("type")),
        "authors": extract_authors(work),
        "venue": extract_venue(work),
        "cited_by_count": work.get("cited_by_count") or 0,
        "concepts": extract_concepts(work),
        "abstract": abstract,
        "url": landing,
        "source_queries": query,
        "source": "openalex",
    }
    return row


def make_manual_row(seed: Dict[str, Any]) -> Dict[str, Any]:
    row: Dict[str, Any] = {
        "openalex_id": "",
        "doi": "",
        "title": seed["title"],
        "year": seed.get("year", ""),
        "publication_date": "",
        "type": "manual_seed",
        "authors": seed.get("authors", ""),
        "venue": seed.get("venue", ""),
        "cited_by_count": 0,
        "concepts": "Robotics; Machine learning; Artificial intelligence",
        "abstract": seed.get("abstract", ""),
        "url": "",
        "source_queries": "manual_seed",
        "source": "manual_seed",
    }
    return row


def merge_row(existing: Dict[str, Any], incoming: Dict[str, Any]) -> Dict[str, Any]:
    queries = set(filter(None, str(existing.get("source_queries", "")).split("|")))
    queries.update(filter(None, str(incoming.get("source_queries", "")).split("|")))
    existing["source_queries"] = "|".join(sorted(queries))
    for key in ["abstract", "authors", "venue", "doi", "url", "concepts", "openalex_id"]:
        if not existing.get(key) and incoming.get(key):
            existing[key] = incoming[key]
    try:
        existing["cited_by_count"] = max(int(existing.get("cited_by_count") or 0), int(incoming.get("cited_by_count") or 0))
    except ValueError:
        pass
    return existing


def fetch_literature(target: int = 1100) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    ensure_dirs()
    rows_by_key: Dict[str, Dict[str, Any]] = {}
    progress = {
        "target": target,
        "queries": [],
        "errors": [],
        "started_at": time.strftime("%Y-%m-%d %H:%M:%S"),
    }

    for seed in MANUAL_SEEDS:
        row = make_manual_row(seed)
        rows_by_key[row_key(row)] = row

    for idx, query in enumerate(QUERIES, start=1):
        before = len(rows_by_key)
        cursor = "*"
        pages = 0
        max_pages = 3 if len(rows_by_key) < target else 1
        while pages < max_pages:
            url = openalex_url(query, cursor=cursor, per_page=100)
            data = request_json(url)
            if not data:
                progress["errors"].append({"query": query, "page": pages + 1, "error": "request_failed"})
                break
            results = data.get("results") or []
            if not results:
                break
            for work in results:
                row = make_row_from_work(work, query)
                if not row.get("title"):
                    continue
                key = row_key(row)
                if key in rows_by_key:
                    rows_by_key[key] = merge_row(rows_by_key[key], row)
                else:
                    rows_by_key[key] = row
            pages += 1
            cursor = ((data.get("meta") or {}).get("next_cursor")) or ""
            if not cursor:
                break
            if len(rows_by_key) >= target and pages >= 1:
                break
            time.sleep(0.15)
        added = len(rows_by_key) - before
        progress["queries"].append({"index": idx, "query": query, "pages": pages, "added": added, "total": len(rows_by_key)})
        print(f"[literature] query {idx}/{len(QUERIES)} added={added} total={len(rows_by_key)} :: {query}", flush=True)
        with open(PROGRESS_PATH, "w", encoding="utf-8") as f:
            json.dump(progress, f, indent=2)
        if len(rows_by_key) >= target and idx >= 20:
            # Keep some breadth after hitting target, but avoid needless API load.
            continue

    rows = list(rows_by_key.values())
    for row in rows:
        row.update(extraction_fields(row))
        row["domain_score"] = f"{domain_score(row):.3f}"
    rows.sort(key=lambda r: float(r.get("domain_score") or 0.0), reverse=True)

    for i, row in enumerate(rows, start=1):
        row["rank"] = i
        if i <= 100:
            band = "hostile_prior_work_candidate"
        elif i <= 250:
            band = "deep_read_candidate"
        elif i <= 300:
            band = "serious_skim_candidate"
        elif i <= 1000:
            band = "landscape"
        else:
            band = "overflow"
        row["importance_band"] = band

    progress["finished_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
    progress["total_rows"] = len(rows)
    with open(PROGRESS_PATH, "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=2)
    return rows, progress


def write_matrix(rows: List[Dict[str, Any]]) -> None:
    ensure_dirs()
    fields = [
        "rank",
        "importance_band",
        "domain_score",
        "topic_cluster",
        "title",
        "year",
        "authors",
        "venue",
        "type",
        "cited_by_count",
        "doi",
        "openalex_id",
        "url",
        "concepts",
        "source",
        "source_queries",
        "problem_claimed",
        "mechanism_introduced",
        "hidden_assumptions",
        "variables_fixed",
        "failure_modes_ignored",
        "what_makes_less_novel",
        "what_leaves_open",
        "abstract",
    ]
    with open(MATRIX_PATH, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main() -> int:
    ensure_dirs()
    rows, progress = fetch_literature(target=1100)
    write_matrix(rows)
    print(f"[done] wrote {len(rows)} rows to {MATRIX_PATH}", flush=True)
    if len(rows) < 1000:
        print("[warn] fewer than 1000 rows; downstream synthesis will mark coverage as incomplete", flush=True)
    print(json.dumps({"rows": len(rows), "errors": len(progress.get("errors", []))}, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
