#!/usr/bin/env python3
"""Full-scale, compact experiment suite for action-token aliasing.

The runner reuses the original simulator helpers but writes only aggregate
rows. Suites run sequentially, keep sklearn jobs at 1, and avoid storing raw
datasets or trajectories.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
from dataclasses import replace
from typing import Dict, Iterable, List, Sequence, Tuple

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier

import run_experiments as base


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RESULTS = os.path.join(ROOT, "results", "full_scale")
FIGURES = os.path.join(ROOT, "figures", "full_scale")
PAPER_FIGURES = os.path.join(ROOT, "paper", "figures")

CSV_FIELDS = [
    "suite",
    "seed",
    "method",
    "alias_strength",
    "train_alias_strength",
    "test_alias_strength",
    "alias_energy",
    "success",
    "effect_rmse",
    "action_rmse",
    "mean_chart_effect_radius",
    "charts",
    "charts_requested",
    "token_bins",
    "token_mode",
    "context_condition",
    "context_flip_rate",
    "train_rows",
    "test_rows",
    "threshold",
    "effect_metric",
    "control",
    "evaluated_predictions",
]


def ensure_dirs() -> None:
    os.makedirs(RESULTS, exist_ok=True)
    os.makedirs(FIGURES, exist_ok=True)
    os.makedirs(PAPER_FIGURES, exist_ok=True)


def stable_seed(seed: int, offset: int) -> int:
    return 100000 + seed * 1009 + offset


def normalize_token(token: np.ndarray) -> np.ndarray:
    denom = float(max(1, int(np.max(token))))
    return token.astype(float) / denom


def retokenize(data: base.Dataset, bins: int = 8, mode: str = "cardinal") -> base.Dataset:
    theta = data.meta["theta"]
    token = base.cardinal_token(theta, bins=bins)
    if mode == "oracle_mode_contact":
        mode_bit = (data.meta["mode"] > 0).astype(int)
        contact_bit = (data.meta["contact"] > 0).astype(int)
        token = token + bins * (mode_bit + 2 * contact_bit)
    elif mode == "oracle_mode":
        mode_bit = (data.meta["mode"] > 0).astype(int)
        token = token + bins * mode_bit
    elif mode == "single_token":
        token = np.zeros_like(token)
    elif mode != "cardinal":
        raise ValueError(f"unknown token mode {mode}")

    full_context = data.full_context.copy()
    hidden_context = data.hidden_context.copy()
    full_context[:, -1] = normalize_token(token)
    hidden_context[:, -1] = normalize_token(token)
    return replace(data, full_context=full_context, hidden_context=hidden_context, token=token)


def generate_pair(
    train_n: int,
    test_n: int,
    train_alias: float,
    test_alias: float,
    seed: int,
    *,
    bins: int = 8,
    token_mode: str = "cardinal",
) -> Tuple[base.Dataset, base.Dataset]:
    train = base.generate_dataset(train_n, train_alias, seed=stable_seed(seed, 11))
    test = base.generate_dataset(test_n, test_alias, seed=stable_seed(seed, 29))
    return retokenize(train, bins=bins, mode=token_mode), retokenize(test, bins=bins, mode=token_mode)


def continuous_regression_light(train: base.Dataset, test: base.Dataset, feature_name: str = "full", seed: int = 0) -> np.ndarray:
    train_x = train.full_context if feature_name == "full" else train.hidden_context
    test_x = test.full_context if feature_name == "full" else test.hidden_context
    reg = RandomForestRegressor(
        n_estimators=48,
        max_depth=9,
        min_samples_leaf=5,
        random_state=stable_seed(seed, 47),
        n_jobs=1,
    )
    reg.fit(train_x, train.action)
    return reg.predict(test_x)


def chart_policy_with_basis(
    train: base.Dataset,
    test: base.Dataset,
    *,
    chart_basis: np.ndarray,
    feature_name: str,
    charts: int,
    seed: int,
) -> Tuple[np.ndarray, Dict[str, float]]:
    train_x = train.full_context if feature_name == "full" else train.hidden_context
    test_x = test.full_context if feature_name == "full" else test.hidden_context
    pred = np.zeros_like(test.action)
    chart_radii: List[float] = []
    chart_count = 0

    for token in np.unique(test.token):
        tr_mask = train.token == token
        te_mask = test.token == token
        if not np.any(tr_mask):
            pred[te_mask] = train.action.mean(axis=0)
            continue

        basis = chart_basis[tr_mask]
        k = min(charts, max(1, basis.shape[0] // 30))
        if k <= 1:
            labels = np.zeros(basis.shape[0], dtype=int)
            test_labels = np.zeros(np.sum(te_mask), dtype=int)
        else:
            km = KMeans(n_clusters=k, random_state=stable_seed(seed, int(token) + 61), n_init=8)
            labels = km.fit_predict(basis)
            clf = DecisionTreeClassifier(max_depth=7, min_samples_leaf=10, random_state=stable_seed(seed, int(token) + 71))
            clf.fit(train_x[tr_mask], labels)
            test_labels = clf.predict(test_x[te_mask])

        token_actions = train.action[tr_mask]
        token_effects = train.effect[tr_mask]
        for label in np.unique(labels):
            local = labels == label
            if np.sum(local) < 2:
                radius = 0.0
            else:
                centered = token_effects[local] - token_effects[local].mean(axis=0, keepdims=True)
                radius = float(np.sqrt(np.mean(np.sum(centered**2, axis=1))))
            chart_radii.append(radius)
            chart_count += 1

        local_indices = np.where(te_mask)[0]
        for label in np.unique(test_labels):
            proto_mask = labels == label
            proto = token_actions[proto_mask].mean(axis=0) if np.any(proto_mask) else token_actions.mean(axis=0)
            pred[local_indices[test_labels == label]] = proto

    return pred, {
        "mean_chart_effect_radius": float(np.mean(chart_radii)) if chart_radii else 0.0,
        "charts": float(chart_count),
    }


def random_chart_policy(train: base.Dataset, test: base.Dataset, *, feature_name: str, charts: int, seed: int) -> Tuple[np.ndarray, Dict[str, float]]:
    rng = np.random.default_rng(stable_seed(seed, 83))
    train_x = train.full_context if feature_name == "full" else train.hidden_context
    test_x = test.full_context if feature_name == "full" else test.hidden_context
    pred = np.zeros_like(test.action)
    radii: List[float] = []
    chart_count = 0

    for token in np.unique(test.token):
        tr_mask = train.token == token
        te_mask = test.token == token
        if not np.any(tr_mask):
            pred[te_mask] = train.action.mean(axis=0)
            continue
        k = min(charts, max(1, int(np.sum(tr_mask)) // 30))
        labels = rng.integers(0, k, size=int(np.sum(tr_mask))) if k > 1 else np.zeros(int(np.sum(tr_mask)), dtype=int)
        if k > 1:
            clf = DecisionTreeClassifier(max_depth=7, min_samples_leaf=10, random_state=stable_seed(seed, int(token) + 97))
            clf.fit(train_x[tr_mask], labels)
            test_labels = clf.predict(test_x[te_mask])
        else:
            test_labels = np.zeros(np.sum(te_mask), dtype=int)
        token_actions = train.action[tr_mask]
        token_effects = train.effect[tr_mask]
        for label in np.unique(labels):
            local = labels == label
            if np.sum(local) < 2:
                radius = 0.0
            else:
                centered = token_effects[local] - token_effects[local].mean(axis=0, keepdims=True)
                radius = float(np.sqrt(np.mean(np.sum(centered**2, axis=1))))
            radii.append(radius)
            chart_count += 1
        local_indices = np.where(te_mask)[0]
        for label in np.unique(test_labels):
            proto_mask = labels == label
            proto = token_actions[proto_mask].mean(axis=0) if np.any(proto_mask) else token_actions.mean(axis=0)
            pred[local_indices[test_labels == label]] = proto
    return pred, {
        "mean_chart_effect_radius": float(np.mean(radii)) if radii else 0.0,
        "charts": float(chart_count),
    }


def corrupt_context(data: base.Dataset, condition: str, rate: float, seed: int) -> base.Dataset:
    rng = np.random.default_rng(stable_seed(seed, 109))
    full_context = data.full_context.copy()
    if condition == "clean":
        return data
    if condition in {"flip_both", "flip_mode", "flip_contact"}:
        mask = rng.random(full_context.shape[0]) < rate
        if condition in {"flip_both", "flip_mode"}:
            full_context[mask, 4] *= -1.0
        if condition in {"flip_both", "flip_contact"}:
            full_context[mask, 5] *= -1.0
    elif condition == "gaussian_alias_features":
        full_context[:, 4:6] += rng.normal(scale=rate, size=(full_context.shape[0], 2))
    else:
        raise ValueError(f"unknown context corruption {condition}")
    return replace(data, full_context=full_context)


def effect_basis(train: base.Dataset, metric: str, seed: int) -> np.ndarray:
    rng = np.random.default_rng(stable_seed(seed, 131))
    if metric == "full_effect":
        return train.effect
    if metric == "x_only":
        return train.effect[:, :1]
    if metric == "y_only":
        return train.effect[:, 1:2]
    if metric == "raw_action":
        return train.action
    if metric == "noisy_effect":
        return train.effect + rng.normal(scale=0.45, size=train.effect.shape)
    if metric == "random_metric":
        return rng.normal(size=train.effect.shape)
    raise ValueError(f"unknown effect metric {metric}")


def metric_row(
    suite: str,
    seed: int,
    method: str,
    train: base.Dataset,
    test: base.Dataset,
    predicted_action: np.ndarray,
    *,
    alias_strength: float,
    train_alias: float | None = None,
    test_alias: float | None = None,
    audit: Dict[str, float] | None = None,
    charts_requested: int | None = None,
    token_bins: int | None = None,
    token_mode: str | None = None,
    context_condition: str | None = None,
    context_flip_rate: float | None = None,
    threshold: float = 0.36,
    effect_metric_name: str | None = None,
    control: str | None = None,
) -> Dict[str, float | str]:
    vals = base.metrics(test, predicted_action, threshold=threshold)
    row: Dict[str, float | str] = {
        "suite": suite,
        "seed": seed,
        "method": method,
        "alias_strength": alias_strength,
        "train_alias_strength": train_alias if train_alias is not None else alias_strength,
        "test_alias_strength": test_alias if test_alias is not None else alias_strength,
        "alias_energy": base.alias_energy(train),
        "train_rows": float(train.action.shape[0]),
        "test_rows": float(test.action.shape[0]),
        "threshold": threshold,
        "evaluated_predictions": float(test.action.shape[0]),
    }
    row.update(vals)
    if audit:
        row.update(audit)
    if charts_requested is not None:
        row["charts_requested"] = float(charts_requested)
    if token_bins is not None:
        row["token_bins"] = float(token_bins)
    if token_mode is not None:
        row["token_mode"] = token_mode
    if context_condition is not None:
        row["context_condition"] = context_condition
    if context_flip_rate is not None:
        row["context_flip_rate"] = context_flip_rate
    if effect_metric_name is not None:
        row["effect_metric"] = effect_metric_name
    if control is not None:
        row["control"] = control
    return row


def standard_method_rows(
    suite: str,
    seed: int,
    train: base.Dataset,
    test: base.Dataset,
    *,
    alias_strength: float,
    charts: int = 3,
    include_continuous: bool = True,
    train_alias: float | None = None,
    test_alias: float | None = None,
    token_bins: int | None = None,
    token_mode: str | None = None,
) -> List[Dict[str, float | str]]:
    rows: List[Dict[str, float | str]] = []
    rows.append(metric_row(suite, seed, "coarse_token", train, test, base.prototype_by_token(train, test), alias_strength=alias_strength, train_alias=train_alias, test_alias=test_alias, token_bins=token_bins, token_mode=token_mode))
    pred_raw, audit_raw = base.per_token_chart_policy(train, test, feature_name="full", chart_space="action", charts=charts, seed=stable_seed(seed, 151))
    rows.append(metric_row(suite, seed, "raw_action_charts", train, test, pred_raw, alias_strength=alias_strength, train_alias=train_alias, test_alias=test_alias, audit=audit_raw, charts_requested=charts, token_bins=token_bins, token_mode=token_mode))
    pred_esac, audit_esac = base.per_token_chart_policy(train, test, feature_name="full", chart_space="effect", charts=charts, seed=stable_seed(seed, 157))
    rows.append(metric_row(suite, seed, "esac_full_context", train, test, pred_esac, alias_strength=alias_strength, train_alias=train_alias, test_alias=test_alias, audit=audit_esac, charts_requested=charts, token_bins=token_bins, token_mode=token_mode))
    pred_hidden, audit_hidden = base.per_token_chart_policy(train, test, feature_name="hidden", chart_space="effect", charts=charts, seed=stable_seed(seed, 163))
    rows.append(metric_row(suite, seed, "esac_hidden_context", train, test, pred_hidden, alias_strength=alias_strength, train_alias=train_alias, test_alias=test_alias, audit=audit_hidden, charts_requested=charts, token_bins=token_bins, token_mode=token_mode))
    if include_continuous:
        rows.append(metric_row(suite, seed, "continuous_regression_upper", train, test, continuous_regression_light(train, test, seed=seed), alias_strength=alias_strength, train_alias=train_alias, test_alias=test_alias, token_bins=token_bins, token_mode=token_mode))
        rows.append(metric_row(suite, seed, "oracle_expert", train, test, test.action, alias_strength=alias_strength, train_alias=train_alias, test_alias=test_alias, token_bins=token_bins, token_mode=token_mode))
    return rows


def write_rows(path: str, rows: Sequence[Dict[str, float | str]]) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def run_main(seed_scale: int, train_n: int, test_n: int) -> List[Dict[str, float | str]]:
    rows: List[Dict[str, float | str]] = []
    strengths = [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
    for seed in range(seed_scale):
        for strength in strengths:
            train, test = generate_pair(train_n, test_n, strength, strength, seed)
            rows.extend(standard_method_rows("main_sweep", seed, train, test, alias_strength=strength, include_continuous=True, token_bins=8, token_mode="cardinal"))
    write_rows(os.path.join(RESULTS, "main_sweep.csv"), rows)
    return rows


def run_context(seed_scale: int, train_n: int, test_n: int) -> List[Dict[str, float | str]]:
    rows: List[Dict[str, float | str]] = []
    alias_strength = 1.25
    flip_rates = [0.0, 0.05, 0.10, 0.20, 0.40, 0.60]
    conditions = ["flip_both", "flip_mode", "flip_contact", "gaussian_alias_features"]
    for seed in range(seed_scale):
        train, clean_test = generate_pair(train_n, test_n, alias_strength, alias_strength, seed)
        for condition in conditions:
            for rate in flip_rates:
                corrupted = corrupt_context(clean_test, "clean" if rate == 0.0 else condition, rate, seed)
                pred, audit = base.per_token_chart_policy(train, corrupted, feature_name="full", chart_space="effect", charts=3, seed=stable_seed(seed, 181))
                rows.append(metric_row("context_reliability", seed, "esac_full_context", train, corrupted, pred, alias_strength=alias_strength, audit=audit, charts_requested=3, context_condition=condition if rate > 0.0 else "clean", context_flip_rate=rate))
        pred_hidden, audit_hidden = base.per_token_chart_policy(train, clean_test, feature_name="hidden", chart_space="effect", charts=3, seed=stable_seed(seed, 191))
        rows.append(metric_row("context_reliability", seed, "esac_hidden_context", train, clean_test, pred_hidden, alias_strength=alias_strength, audit=audit_hidden, charts_requested=3, context_condition="hidden_alias_context", context_flip_rate=-1.0))
    write_rows(os.path.join(RESULTS, "context_reliability.csv"), rows)
    return rows


def run_token_granularity(seed_scale: int, train_n: int, test_n: int) -> List[Dict[str, float | str]]:
    rows: List[Dict[str, float | str]] = []
    strengths = [0.75, 1.25, 1.75]
    token_settings = [(4, "cardinal"), (8, "cardinal"), (16, "cardinal"), (32, "cardinal"), (8, "oracle_mode_contact"), (1, "single_token")]
    for seed in range(seed_scale):
        for strength in strengths:
            for bins, mode in token_settings:
                train, test = generate_pair(train_n, test_n, strength, strength, seed, bins=bins, token_mode=mode)
                rows.extend(standard_method_rows("token_granularity", seed, train, test, alias_strength=strength, include_continuous=False, token_bins=bins, token_mode=mode))
    write_rows(os.path.join(RESULTS, "token_granularity.csv"), rows)
    return rows


def run_chart_ablation(seed_scale: int, train_n: int, test_n: int) -> List[Dict[str, float | str]]:
    rows: List[Dict[str, float | str]] = []
    alias_strength = 1.25
    for seed in range(seed_scale):
        train, test = generate_pair(train_n, test_n, alias_strength, alias_strength, seed)
        for charts in [1, 2, 3, 4, 6, 8]:
            rows.append(metric_row("chart_ablation", seed, "coarse_token", train, test, base.prototype_by_token(train, test), alias_strength=alias_strength, charts_requested=charts))
            pred_random, audit_random = random_chart_policy(train, test, feature_name="full", charts=charts, seed=stable_seed(seed, 211 + charts))
            rows.append(metric_row("chart_ablation", seed, "random_charts", train, test, pred_random, alias_strength=alias_strength, audit=audit_random, charts_requested=charts))
            pred_raw, audit_raw = base.per_token_chart_policy(train, test, feature_name="full", chart_space="action", charts=charts, seed=stable_seed(seed, 223 + charts))
            rows.append(metric_row("chart_ablation", seed, "raw_action_charts", train, test, pred_raw, alias_strength=alias_strength, audit=audit_raw, charts_requested=charts))
            pred_esac, audit_esac = base.per_token_chart_policy(train, test, feature_name="full", chart_space="effect", charts=charts, seed=stable_seed(seed, 229 + charts))
            rows.append(metric_row("chart_ablation", seed, "esac_full_context", train, test, pred_esac, alias_strength=alias_strength, audit=audit_esac, charts_requested=charts))
    write_rows(os.path.join(RESULTS, "chart_ablation.csv"), rows)
    return rows


def run_data_scale(seed_scale: int, test_n: int) -> List[Dict[str, float | str]]:
    rows: List[Dict[str, float | str]] = []
    alias_strength = 1.25
    for seed in range(seed_scale):
        for train_n in [500, 1000, 2000, 4000]:
            train, test = generate_pair(train_n, test_n, alias_strength, alias_strength, seed)
            rows.extend(standard_method_rows("data_scale", seed, train, test, alias_strength=alias_strength, include_continuous=True, token_bins=8, token_mode="cardinal"))
    write_rows(os.path.join(RESULTS, "data_scale.csv"), rows)
    return rows


def run_alias_shift(seed_scale: int, train_n: int, test_n: int) -> List[Dict[str, float | str]]:
    rows: List[Dict[str, float | str]] = []
    train_strengths = [0.75, 1.25, 1.75]
    test_strengths = [0.75, 1.25, 1.75, 2.0]
    for seed in range(seed_scale):
        for train_strength in train_strengths:
            for test_strength in test_strengths:
                train, test = generate_pair(train_n, test_n, train_strength, test_strength, seed)
                rows.extend(standard_method_rows("alias_shift", seed, train, test, alias_strength=test_strength, train_alias=train_strength, test_alias=test_strength, include_continuous=False, token_bins=8, token_mode="cardinal"))
    write_rows(os.path.join(RESULTS, "alias_shift.csv"), rows)
    return rows


def run_effect_metric(seed_scale: int, train_n: int, test_n: int) -> List[Dict[str, float | str]]:
    rows: List[Dict[str, float | str]] = []
    alias_strength = 1.25
    metrics_to_test = ["full_effect", "x_only", "y_only", "raw_action", "noisy_effect", "random_metric"]
    for seed in range(seed_scale):
        train, test = generate_pair(train_n, test_n, alias_strength, alias_strength, seed)
        for metric_name in metrics_to_test:
            basis = effect_basis(train, metric_name, seed)
            pred, audit = chart_policy_with_basis(train, test, chart_basis=basis, feature_name="full", charts=3, seed=stable_seed(seed, 251))
            rows.append(metric_row("effect_metric", seed, f"chart_{metric_name}", train, test, pred, alias_strength=alias_strength, audit=audit, charts_requested=3, effect_metric_name=metric_name))
    write_rows(os.path.join(RESULTS, "effect_metric.csv"), rows)
    return rows


def run_threshold(seed_scale: int, train_n: int, test_n: int) -> List[Dict[str, float | str]]:
    rows: List[Dict[str, float | str]] = []
    alias_strength = 1.25
    thresholds = [0.20, 0.28, 0.36, 0.44, 0.52, 0.64, 0.80]
    for seed in range(seed_scale):
        train, test = generate_pair(train_n, test_n, alias_strength, alias_strength, seed)
        predictions: List[Tuple[str, np.ndarray, Dict[str, float] | None]] = []
        predictions.append(("coarse_token", base.prototype_by_token(train, test), None))
        pred_raw, audit_raw = base.per_token_chart_policy(train, test, feature_name="full", chart_space="action", charts=3, seed=stable_seed(seed, 271))
        predictions.append(("raw_action_charts", pred_raw, audit_raw))
        pred_esac, audit_esac = base.per_token_chart_policy(train, test, feature_name="full", chart_space="effect", charts=3, seed=stable_seed(seed, 277))
        predictions.append(("esac_full_context", pred_esac, audit_esac))
        predictions.append(("continuous_regression_upper", continuous_regression_light(train, test, seed=seed), None))
        for threshold in thresholds:
            for method, pred, audit in predictions:
                rows.append(metric_row("threshold_sensitivity", seed, method, train, test, pred, alias_strength=alias_strength, audit=audit, charts_requested=3 if audit else None, threshold=threshold))
    write_rows(os.path.join(RESULTS, "threshold_sensitivity.csv"), rows)
    return rows


def run_negative_controls(seed_scale: int, train_n: int, test_n: int) -> List[Dict[str, float | str]]:
    rows: List[Dict[str, float | str]] = []
    controls = [
        ("no_alias", 0.0, 8, "cardinal"),
        ("oracle_mode_token", 1.25, 8, "oracle_mode"),
        ("oracle_mode_contact_token", 1.25, 8, "oracle_mode_contact"),
        ("single_token_alias", 1.25, 1, "single_token"),
        ("strong_alias_hidden_context", 1.75, 8, "cardinal"),
    ]
    for seed in range(seed_scale):
        for control, strength, bins, mode in controls:
            train, test = generate_pair(train_n, test_n, strength, strength, seed, bins=bins, token_mode=mode)
            rows.append(metric_row("negative_controls", seed, "coarse_token", train, test, base.prototype_by_token(train, test), alias_strength=strength, token_bins=bins, token_mode=mode, control=control))
            pred_esac, audit_esac = base.per_token_chart_policy(train, test, feature_name="full", chart_space="effect", charts=3, seed=stable_seed(seed, 301))
            rows.append(metric_row("negative_controls", seed, "esac_full_context", train, test, pred_esac, alias_strength=strength, audit=audit_esac, charts_requested=3, token_bins=bins, token_mode=mode, control=control))
            pred_hidden, audit_hidden = base.per_token_chart_policy(train, test, feature_name="hidden", chart_space="effect", charts=3, seed=stable_seed(seed, 307))
            rows.append(metric_row("negative_controls", seed, "esac_hidden_context", train, test, pred_hidden, alias_strength=strength, audit=audit_hidden, charts_requested=3, token_bins=bins, token_mode=mode, control=control))
    write_rows(os.path.join(RESULTS, "negative_controls.csv"), rows)
    return rows


def group_mean(rows: Sequence[Dict[str, float | str]], key_fields: Sequence[str], value: str = "success") -> Dict[Tuple[str, ...], float]:
    buckets: Dict[Tuple[str, ...], List[float]] = {}
    for row in rows:
        key = tuple(str(row.get(k, "")) for k in key_fields)
        buckets.setdefault(key, []).append(float(row.get(value, 0.0)))
    return {key: float(np.mean(vals)) for key, vals in buckets.items()}


def mean_rows(rows: Sequence[Dict[str, float | str]], filters: Dict[str, str]) -> List[Dict[str, float | str]]:
    out = []
    for row in rows:
        ok = True
        for key, expected in filters.items():
            if str(row.get(key, "")) != expected:
                ok = False
                break
        if ok:
            out.append(row)
    return out


def plot_line(rows: Sequence[Dict[str, float | str]], *, x_field: str, methods: Sequence[str], title: str, xlabel: str, ylabel: str, filename: str, filters: Dict[str, str] | None = None) -> None:
    filters = filters or {}
    plt.figure(figsize=(7.2, 4.3))
    for method in methods:
        selected = [r for r in rows if str(r.get("method")) == method and all(str(r.get(k, "")) == v for k, v in filters.items())]
        if not selected:
            continue
        xs = sorted({float(r[x_field]) for r in selected})
        ys = []
        for x in xs:
            vals = [float(r["success"]) for r in selected if abs(float(r[x_field]) - x) < 1e-9]
            ys.append(float(np.mean(vals)))
        plt.plot(xs, ys, marker="o", linewidth=2, label=method.replace("_", " "))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.ylim(-0.03, 1.03)
    plt.grid(True, alpha=0.25)
    plt.legend(frameon=False, fontsize=8)
    plt.tight_layout()
    path = os.path.join(FIGURES, filename)
    plt.savefig(path, dpi=220)
    plt.close()
    copy_to_paper(path)


def copy_to_paper(path: str) -> None:
    target = os.path.join(PAPER_FIGURES, os.path.basename(path))
    with open(path, "rb") as src, open(target, "wb") as dst:
        dst.write(src.read())


def make_figures(all_rows: Dict[str, List[Dict[str, float | str]]]) -> None:
    main = all_rows.get("main_sweep", [])
    plot_line(main, x_field="alias_strength", methods=["coarse_token", "raw_action_charts", "esac_hidden_context", "esac_full_context", "continuous_regression_upper"], title="Main alias-strength sweep", xlabel="Alias strength", ylabel="Success", filename="main_alias_sweep.png")

    plt.figure(figsize=(6.6, 4.2))
    for method in ["coarse_token", "esac_full_context"]:
        selected = [r for r in main if str(r.get("method")) == method]
        xs = [float(r["alias_energy"]) for r in selected]
        ys = [1.0 - float(r["success"]) for r in selected]
        plt.scatter(xs, ys, s=26, alpha=0.7, label=method.replace("_", " "))
    plt.xlabel("Within-token effect radius")
    plt.ylabel("Failure rate")
    plt.ylim(-0.03, 1.03)
    plt.grid(True, alpha=0.25)
    plt.legend(frameon=False, fontsize=8)
    plt.tight_layout()
    path = os.path.join(FIGURES, "alias_energy_diagnostic.png")
    plt.savefig(path, dpi=220)
    plt.close()
    copy_to_paper(path)

    context = all_rows.get("context_reliability", [])
    plt.figure(figsize=(7.2, 4.3))
    for condition in ["flip_both", "flip_mode", "flip_contact", "gaussian_alias_features", "hidden_alias_context"]:
        selected = [r for r in context if str(r.get("context_condition")) == condition]
        if not selected:
            continue
        xs = sorted({float(r["context_flip_rate"]) for r in selected})
        ys = [float(np.mean([float(r["success"]) for r in selected if abs(float(r["context_flip_rate"]) - x) < 1e-9])) for x in xs]
        plt.plot(xs, ys, marker="o", linewidth=2, label=condition.replace("_", " "))
    plt.xlabel("Context corruption rate")
    plt.ylabel("ESAC success")
    plt.ylim(-0.03, 1.03)
    plt.grid(True, alpha=0.25)
    plt.legend(frameon=False, fontsize=8)
    plt.tight_layout()
    path = os.path.join(FIGURES, "context_reliability.png")
    plt.savefig(path, dpi=220)
    plt.close()
    copy_to_paper(path)

    token = all_rows.get("token_granularity", [])
    plot_line(token, x_field="token_bins", methods=["coarse_token", "esac_full_context"], title="Token granularity at cardinal tokenizations", xlabel="Token bins", ylabel="Success", filename="token_granularity.png", filters={"token_mode": "cardinal"})

    chart = all_rows.get("chart_ablation", [])
    plot_line(chart, x_field="charts_requested", methods=["coarse_token", "random_charts", "raw_action_charts", "esac_full_context"], title="Chart-count ablation", xlabel="Charts per token", ylabel="Success", filename="chart_count_ablation.png")

    data = all_rows.get("data_scale", [])
    plot_line(data, x_field="train_rows", methods=["coarse_token", "raw_action_charts", "esac_full_context", "continuous_regression_upper"], title="Data-scale sweep", xlabel="Training transitions", ylabel="Success", filename="data_scale.png")

    shift = all_rows.get("alias_shift", [])
    plot_line(shift, x_field="test_alias_strength", methods=["coarse_token", "raw_action_charts", "esac_full_context"], title="Alias-strength train/test shift", xlabel="Test alias strength", ylabel="Success", filename="alias_shift.png", filters={"train_alias_strength": "1.25"})

    metric = all_rows.get("effect_metric", [])
    means = group_mean(metric, ["effect_metric"], value="success")
    labels = [key[0] for key in sorted(means.keys())]
    vals = [means[(label,)] for label in labels]
    plt.figure(figsize=(7.2, 4.3))
    plt.bar(range(len(labels)), vals)
    plt.xticks(range(len(labels)), [x.replace("_", "\n") for x in labels], fontsize=8)
    plt.ylabel("Success")
    plt.ylim(0.0, 1.03)
    plt.title("Effect metric sensitivity")
    plt.tight_layout()
    path = os.path.join(FIGURES, "effect_metric_sensitivity.png")
    plt.savefig(path, dpi=220)
    plt.close()
    copy_to_paper(path)

    threshold = all_rows.get("threshold_sensitivity", [])
    plot_line(threshold, x_field="threshold", methods=["coarse_token", "raw_action_charts", "esac_full_context", "continuous_regression_upper"], title="Success-threshold sensitivity", xlabel="Effect-error threshold", ylabel="Success", filename="threshold_sensitivity.png")


def load_csv(path: str) -> List[Dict[str, str]]:
    with open(path, "r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def summarize(all_rows: Dict[str, List[Dict[str, float | str]]], seed_scale: int, train_n: int, test_n: int) -> Dict[str, float | str | List[str]]:
    csv_files = sorted([f for f in os.listdir(RESULTS) if f.endswith(".csv")])
    compact_rows = 0
    evaluated_predictions = 0.0
    suite_seed_counts: Dict[str, int] = {}
    suite_compact_rows: Dict[str, int] = {}
    suite_train_rows: Dict[str, List[int]] = {}
    suite_test_rows: Dict[str, List[int]] = {}
    for filename in csv_files:
        path = os.path.join(RESULTS, filename)
        rows = load_csv(path)
        compact_rows += len(rows)
        suite_compact_rows[filename] = len(rows)
        seeds = set()
        train_values = set()
        test_values = set()
        for row in rows:
            if row.get("seed", "") != "":
                seeds.add(int(float(row["seed"])))
            if row.get("train_rows", "") != "":
                train_values.add(int(float(row["train_rows"])))
            if row.get("test_rows", "") != "":
                test_values.add(int(float(row["test_rows"])))
            try:
                evaluated_predictions += float(row.get("evaluated_predictions", 0.0))
            except ValueError:
                pass
        suite_seed_counts[filename] = len(seeds)
        suite_train_rows[filename] = sorted(train_values)
        suite_test_rows[filename] = sorted(test_values)

    main = load_csv(os.path.join(RESULTS, "main_sweep.csv"))
    def mean_for(method: str, strength: float) -> float:
        vals = [float(r["success"]) for r in main if r["method"] == method and abs(float(r["alias_strength"]) - strength) < 1e-9]
        return float(np.mean(vals)) if vals else 0.0

    context_path = os.path.join(RESULTS, "context_reliability.csv")
    context = load_csv(context_path) if os.path.exists(context_path) else []
    def context_mean(condition: str, rate: float) -> float:
        vals = [float(r["success"]) for r in context if r["context_condition"] == condition and abs(float(r["context_flip_rate"]) - rate) < 1e-9]
        return float(np.mean(vals)) if vals else 0.0

    summary: Dict[str, float | str | List[str]] = {
        "summary_command_seed_scale": seed_scale,
        "summary_command_train_rows": train_n,
        "summary_command_test_rows": test_n,
        "csv_files": csv_files,
        "figure_files": sorted([f for f in os.listdir(FIGURES) if f.endswith(".png")]),
        "suite_seed_counts": suite_seed_counts,  # type: ignore[dict-item]
        "suite_compact_rows": suite_compact_rows,  # type: ignore[dict-item]
        "suite_train_rows": suite_train_rows,  # type: ignore[dict-item]
        "suite_test_rows": suite_test_rows,  # type: ignore[dict-item]
        "compact_metric_rows": compact_rows,
        "evaluated_predictions_counting_rows": evaluated_predictions,
        "main_b125_coarse_token": mean_for("coarse_token", 1.25),
        "main_b125_raw_action_charts": mean_for("raw_action_charts", 1.25),
        "main_b125_esac_hidden_context": mean_for("esac_hidden_context", 1.25),
        "main_b125_esac_full_context": mean_for("esac_full_context", 1.25),
        "main_b125_continuous_upper": mean_for("continuous_regression_upper", 1.25),
        "main_b125_oracle_expert": mean_for("oracle_expert", 1.25),
        "context_flip_both_20": context_mean("flip_both", 0.20),
        "context_flip_both_40": context_mean("flip_both", 0.40),
        "context_hidden": context_mean("hidden_alias_context", -1.0),
    }
    with open(os.path.join(RESULTS, "full_scale_summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, sort_keys=True)
    write_markdown_summary(summary)
    return summary


def write_markdown_summary(summary: Dict[str, float | str | List[str]]) -> None:
    lines = ["# Full-Scale Action Aliasing Results Summary", ""]
    lines.append("The expanded suite remains synthetic. It tests when action tokens collapse physically different low-level commands and when ESAC can repair those token fibers by effect-separating charts.")
    lines.append("")
    lines.append("## Scale")
    lines.append(f"- Compact metric rows: `{int(summary['compact_metric_rows'])}`.")
    lines.append(f"- Evaluated predictions counted across rows: `{int(float(summary['evaluated_predictions_counting_rows']))}`.")
    lines.append("- Suite seed counts:")
    for filename, count in sorted(summary["suite_seed_counts"].items()):  # type: ignore[union-attr]
        lines.append(f"  - `{filename}`: `{count}` seeds.")
    lines.append("")
    lines.append("## Main Alias Strength 1.25")
    for key, label in [
        ("main_b125_coarse_token", "coarse token"),
        ("main_b125_raw_action_charts", "raw action charts"),
        ("main_b125_esac_hidden_context", "ESAC hidden context"),
        ("main_b125_esac_full_context", "ESAC full context"),
        ("main_b125_continuous_upper", "continuous upper"),
        ("main_b125_oracle_expert", "oracle expert"),
    ]:
        lines.append(f"- `{label}` success: `{float(summary[key]):.3f}`.")
    lines.append("")
    lines.append("## Context Reliability")
    lines.append(f"- ESAC with both alias variables flipped at 20%: `{float(summary['context_flip_both_20']):.3f}`.")
    lines.append(f"- ESAC with both alias variables flipped at 40%: `{float(summary['context_flip_both_40']):.3f}`.")
    lines.append(f"- ESAC with hidden alias context: `{float(summary['context_hidden']):.3f}`.")
    lines.append("")
    lines.append("## Figures")
    for filename in summary["figure_files"]:  # type: ignore[index]
        lines.append(f"- `paper/figures/{filename}`")
    with open(os.path.join(RESULTS, "full_scale_results_summary.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


def run_suite(name: str, seed_scale: int, train_n: int, test_n: int) -> List[Dict[str, float | str]]:
    print(f"[suite] {name}", flush=True)
    if name == "main":
        return run_main(seed_scale, train_n, test_n)
    if name == "context":
        return run_context(seed_scale, train_n, test_n)
    if name == "token":
        return run_token_granularity(seed_scale, train_n, test_n)
    if name == "charts":
        return run_chart_ablation(seed_scale, train_n, test_n)
    if name == "data":
        return run_data_scale(seed_scale, test_n)
    if name == "shift":
        return run_alias_shift(seed_scale, train_n, test_n)
    if name == "metric":
        return run_effect_metric(seed_scale, train_n, test_n)
    if name == "threshold":
        return run_threshold(seed_scale, train_n, test_n)
    if name == "negative":
        return run_negative_controls(seed_scale, train_n, test_n)
    raise ValueError(f"unknown suite {name}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--suite", default="all", choices=["all", "main", "context", "token", "charts", "data", "shift", "metric", "threshold", "negative", "summarize"])
    parser.add_argument("--seed-scale", type=int, default=10)
    parser.add_argument("--train-rows", type=int, default=2600)
    parser.add_argument("--test-rows", type=int, default=1000)
    parser.add_argument("--fresh", action="store_true")
    args = parser.parse_args()

    ensure_dirs()
    if args.fresh:
        for folder in [RESULTS, FIGURES, PAPER_FIGURES]:
            for filename in os.listdir(folder):
                if filename.endswith((".csv", ".json", ".md", ".png")):
                    os.remove(os.path.join(folder, filename))

    if args.suite == "summarize":
        all_rows: Dict[str, List[Dict[str, float | str]]] = {}
    else:
        suite_names = ["main", "context", "token", "charts", "data", "shift", "metric", "threshold", "negative"] if args.suite == "all" else [args.suite]
        for suite_name in suite_names:
            run_suite(suite_name, args.seed_scale, args.train_rows, args.test_rows)

    all_rows = {}
    suite_file_map = {
        "main_sweep": "main_sweep.csv",
        "context_reliability": "context_reliability.csv",
        "token_granularity": "token_granularity.csv",
        "chart_ablation": "chart_ablation.csv",
        "data_scale": "data_scale.csv",
        "alias_shift": "alias_shift.csv",
        "effect_metric": "effect_metric.csv",
        "threshold_sensitivity": "threshold_sensitivity.csv",
        "negative_controls": "negative_controls.csv",
    }
    for suite_key, filename in suite_file_map.items():
        path = os.path.join(RESULTS, filename)
        if os.path.exists(path):
            all_rows[suite_key] = load_csv(path)  # type: ignore[assignment]

    make_figures(all_rows)
    summary = summarize(all_rows, args.seed_scale, args.train_rows, args.test_rows)
    print(json.dumps(summary, indent=2, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
