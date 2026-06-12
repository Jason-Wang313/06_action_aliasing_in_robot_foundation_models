#!/usr/bin/env python3
"""Controlled evidence for action-fiber aliasing and ESAC repair.

The simulator is deliberately small.  It isolates one mechanism: a coarse
language/action token keeps the commanded cardinal motion but discards a
contact-sensitive motor component whose physical effect changes with state.
"""

from __future__ import annotations

import csv
import json
import math
import os
from dataclasses import dataclass
from typing import Dict, List, Tuple

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RESULTS = os.path.join(ROOT, "results")
FIGURES = os.path.join(ROOT, "figures")


def ensure_dirs() -> None:
    os.makedirs(RESULTS, exist_ok=True)
    os.makedirs(FIGURES, exist_ok=True)


@dataclass
class Dataset:
    full_context: np.ndarray
    hidden_context: np.ndarray
    token: np.ndarray
    action: np.ndarray
    effect: np.ndarray
    target: np.ndarray
    meta: Dict[str, np.ndarray]


def cardinal_token(theta: np.ndarray, bins: int = 8) -> np.ndarray:
    wrapped = (theta + 2 * np.pi) % (2 * np.pi)
    return np.floor(wrapped / (2 * np.pi / bins)).astype(int)


def batch_dynamics_matrix(theta: np.ndarray, mode: np.ndarray, contact: np.ndarray, friction: np.ndarray, embodiment: np.ndarray, alias_strength: float) -> np.ndarray:
    """Return n x 2 x 4 local action-effect matrices."""
    n = theta.shape[0]
    b = np.zeros((n, 2, 4), dtype=float)
    # Cartesian command channels.
    b[:, 0, 0] = 1.0 + 0.12 * embodiment
    b[:, 1, 1] = 1.0 - 0.08 * embodiment
    b[:, 0, 1] = 0.08 * contact
    b[:, 1, 0] = -0.06 * contact

    # Hidden motor channels: wrist/force commands are contact-sensitive and
    # grow in importance as alias_strength increases.
    gain = (0.65 + 0.25 * friction) * (0.35 + alias_strength)
    b[:, 0, 2] = gain * (-np.sin(theta)) * mode + 0.12 * contact
    b[:, 1, 2] = gain * (np.cos(theta)) * mode
    b[:, 0, 3] = 0.22 * contact + 0.10 * embodiment
    b[:, 1, 3] = gain * mode + 0.10 * np.sin(2 * theta)
    return b


def generate_dataset(n: int, alias_strength: float, seed: int) -> Dataset:
    rng = np.random.default_rng(seed)
    theta = rng.uniform(0, 2 * np.pi, size=n)
    mode = rng.choice([-1.0, 1.0], size=n)
    contact = rng.choice([-1.0, 1.0], size=n)
    friction = rng.uniform(0.0, 1.0, size=n)
    embodiment = rng.choice([-1.0, 0.0, 1.0], size=n)
    clearance = rng.uniform(-1.0, 1.0, size=n)

    direction = np.column_stack([np.cos(theta), np.sin(theta)])
    orthogonal = np.column_stack([-np.sin(theta), np.cos(theta)])
    fine_contact = np.column_stack([np.cos(2 * theta), np.sin(2 * theta)])

    lateral_gain = alias_strength * (0.72 + 0.36 * friction) * mode
    contact_gain = 0.22 * contact * (1.0 - 0.25 * np.abs(clearance))
    target = direction + lateral_gain[:, None] * orthogonal + contact_gain[:, None] * fine_contact

    b = batch_dynamics_matrix(theta, mode, contact, friction, embodiment, alias_strength)
    # Expert action is the minimum-norm motor command for the desired effect.
    action = np.zeros((n, 4), dtype=float)
    for i in range(n):
        action[i] = np.linalg.pinv(b[i]) @ target[i]
        # Redundant motor nullspace: many low-level commands create the same
        # object motion.  Raw action clustering can chase this nuisance
        # variation, while effect charts ignore it by construction.
        _, _, vt = np.linalg.svd(b[i], full_matrices=True)
        null_basis = vt[2:].T
        null_jitter = rng.normal(scale=0.34 + 0.18 * alias_strength, size=2)
        action[i] += null_basis @ null_jitter
    action += rng.normal(scale=0.035 + 0.015 * alias_strength, size=action.shape)
    effect = np.einsum("nij,nj->ni", b, action)

    token = cardinal_token(theta, bins=8)
    full_context = np.column_stack(
        [
            np.cos(theta),
            np.sin(theta),
            np.cos(2 * theta),
            np.sin(2 * theta),
            mode,
            contact,
            friction,
            embodiment,
            clearance,
            token / 7.0,
        ]
    )
    hidden_context = np.column_stack(
        [
            np.cos(theta),
            np.sin(theta),
            np.cos(2 * theta),
            np.sin(2 * theta),
            friction,
            embodiment,
            clearance,
            token / 7.0,
        ]
    )
    meta = {
        "theta": theta,
        "mode": mode,
        "contact": contact,
        "friction": friction,
        "embodiment": embodiment,
        "clearance": clearance,
        "b": b,
    }
    return Dataset(full_context, hidden_context, token, action, effect, target, meta)


def apply_effect(data: Dataset, predicted_action: np.ndarray) -> np.ndarray:
    return np.einsum("nij,nj->ni", data.meta["b"], predicted_action)


def metrics(data: Dataset, predicted_action: np.ndarray, threshold: float = 0.36) -> Dict[str, float]:
    pred_effect = apply_effect(data, predicted_action)
    err = np.linalg.norm(pred_effect - data.target, axis=1)
    action_err = np.linalg.norm(predicted_action - data.action, axis=1)
    return {
        "success": float(np.mean(err < threshold)),
        "effect_rmse": float(np.sqrt(np.mean(err**2))),
        "action_rmse": float(np.sqrt(np.mean(action_err**2))),
    }


def prototype_by_token(train: Dataset, test: Dataset) -> np.ndarray:
    pred = np.zeros_like(test.action)
    global_mean = train.action.mean(axis=0)
    for token in np.unique(test.token):
        mask = train.token == token
        proto = train.action[mask].mean(axis=0) if np.any(mask) else global_mean
        pred[test.token == token] = proto
    return pred


def per_token_chart_policy(train: Dataset, test: Dataset, *, feature_name: str, chart_space: str, charts: int = 3, seed: int = 0) -> Tuple[np.ndarray, Dict[str, float]]:
    train_x = train.full_context if feature_name == "full" else train.hidden_context
    test_x = test.full_context if feature_name == "full" else test.hidden_context
    pred = np.zeros_like(test.action)
    chart_diameters: List[float] = []
    chart_count = 0

    for token in np.unique(test.token):
        tr_mask = train.token == token
        te_mask = test.token == token
        if not np.any(tr_mask):
            pred[te_mask] = train.action.mean(axis=0)
            continue
        basis = train.effect[tr_mask] if chart_space == "effect" else train.action[tr_mask]
        k = min(charts, max(1, basis.shape[0] // 25))
        if k <= 1:
            labels = np.zeros(basis.shape[0], dtype=int)
            test_labels = np.zeros(np.sum(te_mask), dtype=int)
        else:
            km = KMeans(n_clusters=k, random_state=seed, n_init=10)
            labels = km.fit_predict(basis)
            clf = DecisionTreeClassifier(max_depth=6, min_samples_leaf=12, random_state=seed)
            clf.fit(train_x[tr_mask], labels)
            test_labels = clf.predict(test_x[te_mask])

        token_actions = train.action[tr_mask]
        token_effects = train.effect[tr_mask]
        for label in np.unique(labels):
            local = labels == label
            if np.sum(local) < 2:
                diameter = 0.0
            else:
                centered = token_effects[local] - token_effects[local].mean(axis=0, keepdims=True)
                diameter = float(np.sqrt(np.mean(np.sum(centered**2, axis=1))))
            chart_diameters.append(diameter)
            chart_count += 1
        for label in np.unique(test_labels):
            proto_mask = labels == label
            proto = token_actions[proto_mask].mean(axis=0) if np.any(proto_mask) else token_actions.mean(axis=0)
            local_te = te_mask.copy()
            local_indices = np.where(te_mask)[0]
            pred[local_indices[test_labels == label]] = proto

    audit = {
        "mean_chart_effect_radius": float(np.mean(chart_diameters)) if chart_diameters else 0.0,
        "charts": float(chart_count),
    }
    return pred, audit


def continuous_regression(train: Dataset, test: Dataset, feature_name: str = "full", seed: int = 0) -> np.ndarray:
    train_x = train.full_context if feature_name == "full" else train.hidden_context
    test_x = test.full_context if feature_name == "full" else test.hidden_context
    reg = RandomForestRegressor(n_estimators=80, max_depth=9, min_samples_leaf=5, random_state=seed, n_jobs=1)
    reg.fit(train_x, train.action)
    return reg.predict(test_x)


def with_corrupted_alias_context(data: Dataset, flip_rate: float, seed: int) -> Dataset:
    """Flip the mode/contact features visible to the chart predictor at test time."""
    rng = np.random.default_rng(seed)
    full_context = data.full_context.copy()
    flip_mask = rng.random(full_context.shape[0]) < flip_rate
    # full_context columns 4 and 5 are the alias-resolving mode/contact signs.
    full_context[flip_mask, 4] *= -1.0
    full_context[flip_mask, 5] *= -1.0
    return Dataset(
        full_context=full_context,
        hidden_context=data.hidden_context,
        token=data.token,
        action=data.action,
        effect=data.effect,
        target=data.target,
        meta=data.meta,
    )


def alias_energy(data: Dataset) -> float:
    energies: List[float] = []
    weights: List[int] = []
    for token in np.unique(data.token):
        effects = data.effect[data.token == token]
        if effects.shape[0] < 2:
            continue
        centered = effects - effects.mean(axis=0, keepdims=True)
        energy = float(np.sqrt(np.mean(np.sum(centered**2, axis=1))))
        energies.append(energy)
        weights.append(effects.shape[0])
    return float(np.average(energies, weights=weights)) if energies else 0.0


def run_one(alias_strength: float, seed: int = 0) -> Dict[str, Dict[str, float]]:
    train = generate_dataset(4200, alias_strength, seed=1000 + seed)
    test = generate_dataset(1800, alias_strength, seed=2000 + seed)
    out: Dict[str, Dict[str, float]] = {}
    out["coarse_token"] = metrics(test, prototype_by_token(train, test))
    pred_action_chart, audit_action = per_token_chart_policy(train, test, feature_name="full", chart_space="action", charts=3, seed=seed)
    out["raw_action_charts"] = metrics(test, pred_action_chart)
    out["raw_action_charts"].update(audit_action)
    pred_esac, audit_esac = per_token_chart_policy(train, test, feature_name="full", chart_space="effect", charts=3, seed=seed)
    out["esac_full_context"] = metrics(test, pred_esac)
    out["esac_full_context"].update(audit_esac)
    pred_esac_hidden, audit_hidden = per_token_chart_policy(train, test, feature_name="hidden", chart_space="effect", charts=3, seed=seed)
    out["esac_hidden_alias_ablation"] = metrics(test, pred_esac_hidden)
    out["esac_hidden_alias_ablation"].update(audit_hidden)
    pred_reg = continuous_regression(train, test, feature_name="full", seed=seed)
    out["continuous_regression_upper"] = metrics(test, pred_reg)
    out["oracle_expert"] = metrics(test, test.action)
    out["_audit"] = {
        "alias_strength": alias_strength,
        "alias_energy": alias_energy(train),
        "rows_train": float(train.action.shape[0]),
        "rows_test": float(test.action.shape[0]),
    }
    return out


def run_context_corruption(alias_strength: float = 1.25, seed: int = 606) -> List[Dict[str, float]]:
    train = generate_dataset(4200, alias_strength, seed=3000 + seed)
    test = generate_dataset(1800, alias_strength, seed=4000 + seed)
    rows: List[Dict[str, float]] = []
    for flip_rate in [0.0, 0.05, 0.10, 0.20, 0.40, 1.0]:
        corrupted = with_corrupted_alias_context(test, flip_rate, seed=5000 + seed + int(flip_rate * 1000))
        pred, audit = per_token_chart_policy(train, corrupted, feature_name="full", chart_space="effect", charts=3, seed=seed)
        row = {
            "condition": "flipped_full_context",
            "alias_strength": alias_strength,
            "context_flip_rate": flip_rate,
        }
        row.update(metrics(corrupted, pred))
        row.update(audit)
        rows.append(row)

    pred_hidden, audit_hidden = per_token_chart_policy(train, test, feature_name="hidden", chart_space="effect", charts=3, seed=seed)
    hidden_row = {
        "condition": "hidden_alias_context",
        "alias_strength": alias_strength,
        "context_flip_rate": -1.0,
    }
    hidden_row.update(metrics(test, pred_hidden))
    hidden_row.update(audit_hidden)
    rows.append(hidden_row)
    return rows


def flatten_results(sweep: List[Tuple[float, Dict[str, Dict[str, float]]]]) -> List[Dict[str, float]]:
    rows: List[Dict[str, float]] = []
    for alias_strength, result in sweep:
        alias_energy_value = result["_audit"]["alias_energy"]
        for method, vals in result.items():
            if method == "_audit":
                continue
            row = {"alias_strength": alias_strength, "alias_energy": alias_energy_value, "method": method}
            row.update(vals)
            rows.append(row)
    return rows


def write_csv(path: str, rows: List[Dict[str, float]]) -> None:
    fields = [
        "alias_strength",
        "alias_energy",
        "method",
        "success",
        "effect_rmse",
        "action_rmse",
        "mean_chart_effect_radius",
        "charts",
    ]
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def write_context_csv(path: str, rows: List[Dict[str, float]]) -> None:
    fields = [
        "condition",
        "alias_strength",
        "context_flip_rate",
        "success",
        "effect_rmse",
        "action_rmse",
        "mean_chart_effect_radius",
        "charts",
    ]
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def write_context_table(rows: List[Dict[str, float]]) -> None:
    by_rate = {float(r["context_flip_rate"]): r for r in rows}
    wanted = [0.0, 0.10, 0.20, 0.40, -1.0]
    labels = ["0\\%", "10\\%", "20\\%", "40\\%", "Hidden"]
    values = [100.0 * float(by_rate[rate]["success"]) for rate in wanted]
    lines = [
        "\\begin{tabular}{lrrrrr}",
        "\\toprule",
        "Context condition & " + " & ".join(labels) + " \\\\",
        "\\midrule",
        "ESAC success & " + " & ".join(f"{value:.1f}" for value in values) + " \\\\",
        "\\bottomrule",
        "\\end{tabular}",
    ]
    with open(os.path.join(RESULTS, "context_stress_table.tex"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


def write_summary(rows: List[Dict[str, float]], context_rows: List[Dict[str, float]]) -> None:
    target = [r for r in rows if abs(float(r["alias_strength"]) - 1.25) < 1e-9]
    by_method = {r["method"]: r for r in target}
    methods = [
        "coarse_token",
        "raw_action_charts",
        "esac_hidden_alias_ablation",
        "esac_full_context",
        "continuous_regression_upper",
        "oracle_expert",
    ]
    lines = ["# Experiment Summary", ""]
    lines.append("Synthetic contact-control environment at alias_strength=1.25. Success means one-step physical effect error below 0.36.")
    lines.append("")
    lines.append("| Method | Success | Effect RMSE | Action RMSE | Notes |")
    lines.append("|---|---:|---:|---:|---|")
    notes = {
        "coarse_token": "One decoded prototype per language/action token.",
        "raw_action_charts": "Splits token fibers by raw motor-command clusters.",
        "esac_hidden_alias_ablation": "ESAC charts but hides the alias-resolving mode/contact context.",
        "esac_full_context": "ESAC charts from transition effects with observable context.",
        "continuous_regression_upper": "Continuous-action upper baseline, not a token repair.",
        "oracle_expert": "Expert command replay upper bound.",
    }
    for method in methods:
        r = by_method.get(method, {})
        lines.append(
            f"| {method} | {float(r.get('success', 0.0)):.3f} | {float(r.get('effect_rmse', 0.0)):.3f} | {float(r.get('action_rmse', 0.0)):.3f} | {notes[method]} |"
        )
    lines.append("")
    lines.append("Interpretation: coarse tokens fail as within-token effect diameter grows. ESAC succeeds only when the observation contains the variable that disambiguates the action fiber, which is exactly the intended limitation.")
    lines.append("")
    context_by_rate = {float(r["context_flip_rate"]): r for r in context_rows}
    lines.append("Context corruption stress for ESAC at alias_strength=1.25:")
    lines.append("")
    lines.append("| Alias-context condition | Success | Effect RMSE |")
    lines.append("|---|---:|---:|")
    for label, rate in [("clean", 0.0), ("10% flipped", 0.10), ("20% flipped", 0.20), ("40% flipped", 0.40), ("hidden", -1.0)]:
        r = context_by_rate[rate]
        lines.append(f"| {label} | {float(r['success']):.3f} | {float(r['effect_rmse']):.3f} |")
    lines.append("")
    lines.append("Interpretation: ESAC is an effect-chart repair, not an oracle. It degrades as the alias-resolving observation becomes unreliable and approaches the hidden-context ablation when the needed context is unavailable.")
    with open(os.path.join(RESULTS, "experiment_summary.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


def plot_sweep(rows: List[Dict[str, float]]) -> None:
    methods = [
        ("coarse_token", "Coarse token"),
        ("raw_action_charts", "Raw action charts"),
        ("esac_hidden_alias_ablation", "ESAC, hidden mode"),
        ("esac_full_context", "ESAC"),
        ("continuous_regression_upper", "Continuous upper"),
    ]
    plt.figure(figsize=(7.0, 4.2))
    for method, label in methods:
        xs = [float(r["alias_strength"]) for r in rows if r["method"] == method]
        ys = [float(r["success"]) for r in rows if r["method"] == method]
        plt.plot(xs, ys, marker="o", linewidth=2, label=label)
    plt.xlabel("Alias strength")
    plt.ylabel("Success rate")
    plt.ylim(-0.03, 1.03)
    plt.grid(True, alpha=0.25)
    plt.legend(frameon=False, fontsize=8)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES, "aliasing_sweep.png"), dpi=220)
    plt.savefig(os.path.join(FIGURES, "aliasing_sweep.pdf"))
    plt.close()


def plot_alias_energy(rows: List[Dict[str, float]]) -> None:
    coarse = [r for r in rows if r["method"] == "coarse_token"]
    esac = [r for r in rows if r["method"] == "esac_full_context"]
    plt.figure(figsize=(6.2, 4.0))
    plt.scatter([float(r["alias_energy"]) for r in coarse], [1.0 - float(r["success"]) for r in coarse], s=52, label="Coarse token failure")
    plt.scatter([float(r["alias_energy"]) for r in esac], [1.0 - float(r["success"]) for r in esac], s=52, label="ESAC failure")
    plt.xlabel("Within-token effect radius")
    plt.ylabel("Failure rate")
    plt.ylim(-0.03, 1.03)
    plt.grid(True, alpha=0.25)
    plt.legend(frameon=False, fontsize=8)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES, "alias_energy_failure.png"), dpi=220)
    plt.savefig(os.path.join(FIGURES, "alias_energy_failure.pdf"))
    plt.close()


def plot_fiber_example(alias_strength: float = 1.25) -> None:
    data = generate_dataset(1600, alias_strength, seed=314)
    token = 1
    mask = data.token == token
    effects = data.effect[mask]
    modes = data.meta["mode"][mask]
    plt.figure(figsize=(4.8, 4.3))
    plt.scatter(effects[modes < 0, 0], effects[modes < 0, 1], s=14, alpha=0.7, label="same token, mode -1")
    plt.scatter(effects[modes > 0, 0], effects[modes > 0, 1], s=14, alpha=0.7, label="same token, mode +1")
    center = effects.mean(axis=0)
    plt.scatter([center[0]], [center[1]], marker="x", s=90, color="black", label="coarse decoded mean")
    plt.xlabel("Object-effect x")
    plt.ylabel("Object-effect y")
    plt.title("One token fiber contains two physical effects")
    plt.grid(True, alpha=0.25)
    plt.legend(frameon=False, fontsize=7)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES, "token_fiber_example.png"), dpi=220)
    plt.savefig(os.path.join(FIGURES, "token_fiber_example.pdf"))
    plt.close()


def main() -> int:
    ensure_dirs()
    strengths = [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
    sweep: List[Tuple[float, Dict[str, Dict[str, float]]]] = []
    for i, strength in enumerate(strengths):
        print(f"[experiment] alias_strength={strength}", flush=True)
        sweep.append((strength, run_one(strength, seed=i)))
    rows = flatten_results(sweep)
    write_csv(os.path.join(RESULTS, "sweep_results.csv"), rows)
    context_rows = run_context_corruption()
    write_context_csv(os.path.join(RESULTS, "context_stress_results.csv"), context_rows)
    write_context_table(context_rows)
    write_summary(rows, context_rows)
    plot_sweep(rows)
    plot_alias_energy(rows)
    plot_fiber_example()
    with open(os.path.join(RESULTS, "raw_results.json"), "w", encoding="utf-8") as f:
        json.dump(sweep, f, indent=2)
    print(f"[done] wrote results to {RESULTS} and figures to {FIGURES}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
