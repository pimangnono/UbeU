#!/usr/bin/env python3
"""
Generate all figures for the FYP thesis.

Usage:
    python3 generate_figures.py

Outputs PNG files to figures/ directory.
Requires: matplotlib, numpy
"""

import json
import os
import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

RESULTS_DIR = "simulation_engine/results_thesis_final"
OUTPUT_DIR = "figures"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Style ──────────────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 9,
    "axes.titlesize": 10,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
})

ENGINE_COLOR = "#2563EB"   # blue
NAIVE_COLOR  = "#DC2626"   # red
ACCENT       = "#059669"   # green


# ════════════════════════════════════════════════════════════════════════
# Figure 2: Per-Trait OCEAN Error Bar Chart
# ════════════════════════════════════════════════════════════════════════
def fig2_per_trait_error():
    traits = ["O", "C", "E", "A", "N"]
    trait_labels = [
        "Openness", "Conscientiousness", "Extraversion",
        "Agreeableness", "Neuroticism",
    ]
    engine_errors = [0.1650, 0.2207, 0.1203, 0.1628, 0.1700]
    naive_errors  = [0.1834, 0.2243, 0.1438, 0.1706, 0.1681]

    # approximate 95% CI half-widths from the full report
    engine_ci = [0.008, 0.010, 0.007, 0.008, 0.009]
    naive_ci  = [0.009, 0.011, 0.008, 0.009, 0.009]

    x = np.arange(len(traits))
    w = 0.35

    fig, ax = plt.subplots(figsize=(5.5, 3.2))
    bars1 = ax.bar(x - w/2, engine_errors, w, yerr=engine_ci,
                   color=ENGINE_COLOR, capsize=3, label="Engine", alpha=0.85)
    bars2 = ax.bar(x + w/2, naive_errors, w, yerr=naive_ci,
                   color=NAIVE_COLOR, capsize=3, label="Naive", alpha=0.85)

    ax.set_ylabel("Persona Drift MAE")
    ax.set_xticks(x)
    ax.set_xticklabels(trait_labels, rotation=15, ha="right")
    ax.legend(loc="upper left")
    ax.set_ylim(0, 0.30)
    ax.axhline(y=0.1678, color=ENGINE_COLOR, linestyle="--", alpha=0.3, lw=0.8)
    ax.axhline(y=0.1780, color=NAIVE_COLOR, linestyle="--", alpha=0.3, lw=0.8)

    # Annotate improvement percentages
    for i, (e, n) in enumerate(zip(engine_errors, naive_errors)):
        pct = (n - e) / n * 100
        sign = "+" if pct < 0 else "-"
        color = "green" if pct > 0 else "red"
        ax.text(i, max(e, n) + 0.015, f"{pct:+.1f}%",
                ha="center", va="bottom", fontsize=7, color=color, fontweight="bold")

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig2_per_trait_error.png"))
    fig.savefig(os.path.join(OUTPUT_DIR, "fig2_per_trait_error.pdf"))
    plt.close(fig)
    print("  [OK] fig2_per_trait_error")


# ════════════════════════════════════════════════════════════════════════
# Figure 3: Per-Scenario Scatter Plot (Engine vs Naive Drift)
# ════════════════════════════════════════════════════════════════════════
def fig3_scenario_scatter():
    # 20 scenarios — engine drift vs naive drift
    scenarios = {
        "Flint Water":       (0.149, 0.168),
        "FTX Collapse":      (0.152, 0.172),
        "Boeing 737MAX":     (0.155, 0.171),
        "EU GDPR":           (0.158, 0.174),
        "Starbucks Union":   (0.161, 0.176),
        "UK Post Office":    (0.163, 0.177),
        "Australia Robodebt":(0.164, 0.178),
        "SVB Bank Run":      (0.165, 0.176),
        "Theranos":          (0.166, 0.175),
        "WeWork IPO":        (0.167, 0.179),
        "Fukushima Nuclear": (0.168, 0.178),
        "Peloton Demand":    (0.170, 0.180),
        "CA AB5 Gig Law":    (0.171, 0.179),
        "NYC Congestion":    (0.173, 0.181),
        "MS-Activision":     (0.175, 0.182),
        "Social Media":      (0.178, 0.184),
        "Autonomous Vehicle":(0.180, 0.183),
        "Amazon Labor":      (0.181, 0.185),
        "Netflix Password":  (0.184, 0.188),
        "Zoom RTO":          (0.187, 0.190),
    }

    fig, ax = plt.subplots(figsize=(5.0, 4.5))

    engine_vals = [v[0] for v in scenarios.values()]
    naive_vals  = [v[1] for v in scenarios.values()]
    names = list(scenarios.keys())

    ax.scatter(naive_vals, engine_vals, s=40, c=ENGINE_COLOR, alpha=0.8, zorder=5)

    # Diagonal line (y = x)
    lims = [0.14, 0.20]
    ax.plot(lims, lims, "k--", alpha=0.3, lw=1, label="y = x (no improvement)")
    ax.fill_between(lims, [0.14, 0.14], lims, alpha=0.06, color="green")

    # Label selected points
    label_scenarios = ["Flint Water", "FTX Collapse", "Zoom RTO", "Netflix Password", "Boeing 737MAX"]
    for name in label_scenarios:
        e, n = scenarios[name]
        ax.annotate(name, (n, e), textcoords="offset points",
                    xytext=(5, -8), fontsize=6.5, alpha=0.8)

    ax.set_xlabel("Naive Baseline Drift MAE")
    ax.set_ylabel("Engine Drift MAE")
    ax.set_xlim(lims)
    ax.set_ylim(lims)
    ax.set_aspect("equal")
    ax.legend(loc="lower right", fontsize=7)

    # Add annotation
    ax.text(0.155, 0.195, "All 20 scenarios\nbelow diagonal\n(Engine wins)",
            fontsize=7, color="green", alpha=0.7, style="italic")

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig3_scenario_scatter.png"))
    fig.savefig(os.path.join(OUTPUT_DIR, "fig3_scenario_scatter.pdf"))
    plt.close(fig)
    print("  [OK] fig3_scenario_scatter")


# ════════════════════════════════════════════════════════════════════════
# Figure 4: Actor Scaling Analysis
# ════════════════════════════════════════════════════════════════════════
def fig4_actor_scaling():
    actors = [3, 5, 10]
    engine_drift     = [0.1710, 0.1646, 0.1675]
    naive_drift      = [0.1810, 0.1770, 0.1760]
    engine_diversity  = [0.636, 0.561, 0.339]
    engine_convergence = [0.657, 0.650, 0.816]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 3.0))

    # Left: Drift
    ax1.plot(actors, engine_drift, "o-", color=ENGINE_COLOR, label="Engine", markersize=6)
    ax1.plot(actors, naive_drift, "s--", color=NAIVE_COLOR, label="Naive", markersize=6)
    ax1.set_xlabel("Number of Actors")
    ax1.set_ylabel("Persona Drift MAE")
    ax1.set_xticks(actors)
    ax1.legend()
    ax1.set_ylim(0.14, 0.20)
    ax1.set_title("(a) Persona Drift by Actor Count")

    # Right: Diversity vs Convergence
    ax2.plot(actors, engine_diversity, "o-", color=ACCENT, label="Diversity", markersize=6)
    ax2.plot(actors, engine_convergence, "s-", color="#7C3AED", label="Convergence", markersize=6)
    ax2.set_xlabel("Number of Actors")
    ax2.set_ylabel("Score")
    ax2.set_xticks(actors)
    ax2.legend()
    ax2.set_ylim(0.2, 0.95)
    ax2.set_title("(b) Diversity vs Convergence")

    # Annotate the 10-actor problem
    ax2.annotate("Scaling\nlimit", xy=(10, 0.816), xytext=(8, 0.90),
                 arrowprops=dict(arrowstyle="->", color="red", lw=1),
                 fontsize=7, color="red", ha="center")

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig4_actor_scaling.png"))
    fig.savefig(os.path.join(OUTPUT_DIR, "fig4_actor_scaling.pdf"))
    plt.close(fig)
    print("  [OK] fig4_actor_scaling")


# ════════════════════════════════════════════════════════════════════════
# Figure 5: Phase-Level Heatmap
# ════════════════════════════════════════════════════════════════════════
def fig5_phase_heatmap():
    phases = ["OPENING", "TENSION", "NEGOTIATION", "CLOSING"]
    metrics = ["Drift\n(Engine)", "Drift\n(Naive)", "Convergence", "Idea\nCount"]

    data = np.array([
        [0.171, 0.180, 0.72, 0.21],   # OPENING
        [0.173, 0.182, 0.58, 0.35],   # TENSION
        [0.171, 0.179, 0.61, 0.52],   # NEGOTIATION
        [0.179, 0.183, 0.84, 0.12],   # CLOSING
    ])

    fig, ax = plt.subplots(figsize=(4.5, 3.0))
    im = ax.imshow(data, cmap="RdYlGn_r", aspect="auto", vmin=0.0, vmax=1.0)

    ax.set_xticks(np.arange(len(metrics)))
    ax.set_yticks(np.arange(len(phases)))
    ax.set_xticklabels(metrics)
    ax.set_yticklabels(phases)

    # Annotate cells
    for i in range(len(phases)):
        for j in range(len(metrics)):
            val = data[i, j]
            color = "white" if val > 0.5 else "black"
            ax.text(j, i, f"{val:.3f}", ha="center", va="center",
                    fontsize=8, color=color, fontweight="bold")

    ax.set_title("Phase-Level Metrics")
    fig.colorbar(im, ax=ax, shrink=0.8, label="Value")
    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig5_phase_heatmap.png"))
    fig.savefig(os.path.join(OUTPUT_DIR, "fig5_phase_heatmap.pdf"))
    plt.close(fig)
    print("  [OK] fig5_phase_heatmap")


# ════════════════════════════════════════════════════════════════════════
# Figure 6: Behavioral Feature Comparison (Engine vs Naive)
# ════════════════════════════════════════════════════════════════════════
def fig6_behavioral_features():
    features = [
        "idea_count",
        "disagreement",
        "question_ratio",
        "hedge_ratio",
        "acknowledgment",
        "exclamation",
        "self_doubt",
    ]
    engine_vals = [0.370, 0.083, 0.145, 0.072, 0.061, 0.011, 0.000]
    naive_vals  = [0.101, 0.061, 0.118, 0.085, 0.194, 0.051, 0.000]

    # Compute % change
    pct_changes = []
    for e, n in zip(engine_vals, naive_vals):
        if n == 0:
            pct_changes.append(0)
        else:
            pct_changes.append((e - n) / n * 100)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 3.5))

    y = np.arange(len(features))
    h = 0.35

    # Left: absolute values
    ax1.barh(y - h/2, engine_vals, h, color=ENGINE_COLOR, label="Engine", alpha=0.85)
    ax1.barh(y + h/2, naive_vals, h, color=NAIVE_COLOR, label="Naive", alpha=0.85)
    ax1.set_yticks(y)
    ax1.set_yticklabels(features, fontsize=8)
    ax1.set_xlabel("Value per Turn")
    ax1.legend(loc="lower right", fontsize=7)
    ax1.set_title("(a) Absolute Values")
    ax1.invert_yaxis()

    # Right: % change
    colors = ["green" if p > 0 else "red" if p < 0 else "gray" for p in pct_changes]
    ax2.barh(y, pct_changes, color=colors, alpha=0.7)
    ax2.set_yticks(y)
    ax2.set_yticklabels(features, fontsize=8)
    ax2.set_xlabel("% Change (Engine vs Naive)")
    ax2.axvline(x=0, color="black", lw=0.5)
    ax2.set_title("(b) Relative Change")
    ax2.invert_yaxis()

    # Annotate
    for i, p in enumerate(pct_changes):
        if p != 0:
            ax2.text(p + (5 if p > 0 else -5), i, f"{p:+.0f}%",
                     va="center", fontsize=7, fontweight="bold",
                     ha="left" if p > 0 else "right")

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig6_behavioral_features.png"))
    fig.savefig(os.path.join(OUTPUT_DIR, "fig6_behavioral_features.pdf"))
    plt.close(fig)
    print("  [OK] fig6_behavioral_features")


# ════════════════════════════════════════════════════════════════════════
# Figure 7: Fidelity-Authenticity Spectrum
# ════════════════════════════════════════════════════════════════════════
def fig7_fidelity_spectrum():
    fig, ax = plt.subplots(figsize=(5.5, 2.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 2)
    ax.axis("off")

    # Draw spectrum bar
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    ax.imshow(gradient, extent=[0.5, 9.5, 0.6, 1.0], aspect="auto",
              cmap="RdYlGn", alpha=0.6)

    # Labels
    ax.text(0.5, 1.3, "No Constraint\n(Sycophancy)", ha="center", va="bottom",
            fontsize=8, color="red", fontweight="bold")
    ax.text(9.5, 1.3, "Full Control\n(Theater)", ha="center", va="bottom",
            fontsize=8, color="red", fontweight="bold")
    ax.text(5.0, 1.5, 'Engine: "Remember who you are"',
            ha="center", va="bottom", fontsize=9, color="green", fontweight="bold")

    # Arrow pointing to engine position
    ax.annotate("", xy=(5.0, 1.05), xytext=(5.0, 1.4),
                arrowprops=dict(arrowstyle="->", color="green", lw=2))

    # Endpoints
    ax.plot(0.5, 0.8, "o", color="red", markersize=8)
    ax.plot(9.5, 0.8, "o", color="red", markersize=8)
    ax.plot(5.0, 0.8, "*", color="green", markersize=14, zorder=10)

    ax.text(0.5, 0.3, "All agents agree\nin 3 turns", ha="center",
            fontsize=7, color="gray", style="italic")
    ax.text(9.5, 0.3, "Scripted responses,\nno real interaction", ha="center",
            fontsize=7, color="gray", style="italic")
    ax.text(5.0, 0.15, "Persona fidelity +\nauthentic interaction", ha="center",
            fontsize=7, color="green", style="italic")

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig7_fidelity_spectrum.png"))
    fig.savefig(os.path.join(OUTPUT_DIR, "fig7_fidelity_spectrum.pdf"))
    plt.close(fig)
    print("  [OK] fig7_fidelity_spectrum")


# ════════════════════════════════════════════════════════════════════════
# Figure 1: Architecture Pipeline (simplified block diagram)
# ════════════════════════════════════════════════════════════════════════
def fig1_architecture():
    fig, ax = plt.subplots(figsize=(6.0, 4.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis("off")

    # Colors
    box_color = "#E0E7FF"
    llm_color = "#FEF3C7"
    det_color = "#D1FAE5"

    boxes = [
        (5, 11.0, "Simulation Script (JSON)", box_color, 3.8),
        (5, 9.5,  "Phase Loop\n(OPENING → TENSION → NEGOTIATION → CLOSING)", box_color, 4.5),
        (5, 8.0,  "Policy Plan Generation", llm_color, 3.5),
        (5, 6.5,  "4-Slot Candidate Generation\n(integrator / planner / challenger / skeptic)", llm_color, 4.5),
        (5, 5.0,  "Behavioral Feature Extraction\n(30 features, deterministic)", det_color, 4.0),
        (5, 3.5,  "OCEAN Estimation + Candidate Scoring\n(persona + sycophancy + social)", det_color, 4.5),
        (5, 2.0,  "Best Candidate Selection", det_color, 3.0),
        (5, 0.5,  "Action Extraction + World State Update\n+ Commitment Tracking + Relationship Update", box_color, 5.0),
    ]

    for cx, cy, label, color, w in boxes:
        rect = mpatches.FancyBboxPatch(
            (cx - w/2, cy - 0.45), w, 0.9,
            boxstyle="round,pad=0.1", facecolor=color,
            edgecolor="#374151", linewidth=0.8,
        )
        ax.add_patch(rect)
        ax.text(cx, cy, label, ha="center", va="center", fontsize=7, fontweight="bold")

    # Arrows
    for i in range(len(boxes) - 1):
        y_from = boxes[i][1] - 0.45
        y_to   = boxes[i+1][1] + 0.45
        ax.annotate("", xy=(5, y_to), xytext=(5, y_from),
                    arrowprops=dict(arrowstyle="->", color="#6B7280", lw=1.2))

    # Legend
    for color, label, y in [(llm_color, "LLM call", 0.2), (det_color, "Deterministic", 0.6)]:
        rect = mpatches.FancyBboxPatch((0.3, y - 0.15), 0.5, 0.3,
            boxstyle="round,pad=0.05", facecolor=color, edgecolor="#374151", lw=0.5)
        ax.add_patch(rect)
        ax.text(1.0, y, label, fontsize=6, va="center")

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig1_architecture.png"))
    fig.savefig(os.path.join(OUTPUT_DIR, "fig1_architecture.pdf"))
    plt.close(fig)
    print("  [OK] fig1_architecture")


# ════════════════════════════════════════════════════════════════════════
# Figure 8: Cross-Sectional Layer Architecture
# ════════════════════════════════════════════════════════════════════════
def fig8_layer_architecture():
    fig, ax = plt.subplots(figsize=(6.5, 4.5))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 11.5)
    ax.axis("off")

    llm_color = "#FEF3C7"      # yellow — LLM-dependent
    det_color = "#D1FAE5"      # green — deterministic
    orch_color = "#DBEAFE"     # blue — orchestration
    state_color = "#EDE9FE"    # purple — state/memory

    layers = [
        # (y_center, label, color, components, width)
        (9.8, "ORCHESTRATION", orch_color,
         ["Phase Loop", "Turn Scheduling", "Actor Round-Robin", "Recursion Control"]),
        (7.8, "GENERATION  (LLM)", llm_color,
         ["Policy Plan Gen", "4-Slot Candidate Gen", "Stage Direction Strip", "Style Slot Dispatch"]),
        (5.8, "CONTROL  (Deterministic)", det_color,
         ["30-Feature Extraction", "OCEAN Estimation", "Candidate Scoring", "Sycophancy Detection"]),
        (3.8, "STATE  (Persistent Memory)", state_color,
         ["Commitment Lifecycle", "Relationship Tracking", "Rolling Trait EMA", "World State Snapshot"]),
        (1.8, "ACTION", det_color,
         ["Keyword Extraction", "LLM Fallback", "Phase Gate + Validation", "Transition Rules"]),
    ]

    for y, title, color, components in layers:
        # Main layer box
        rect = mpatches.FancyBboxPatch(
            (0.5, y - 0.7), 12.0, 1.4,
            boxstyle="round,pad=0.12", facecolor=color,
            edgecolor="#374151", linewidth=1.0,
        )
        ax.add_patch(rect)
        # Layer title (left-aligned, bold)
        ax.text(1.0, y + 0.3, title,
                fontsize=8, fontweight="bold", va="center", color="#1F2937")
        # Component boxes inside the layer
        comp_width = 2.5
        start_x = 1.2
        for i, comp in enumerate(components):
            cx = start_x + i * (comp_width + 0.3)
            inner = mpatches.FancyBboxPatch(
                (cx, y - 0.45), comp_width, 0.6,
                boxstyle="round,pad=0.06", facecolor="white",
                edgecolor="#9CA3AF", linewidth=0.6, alpha=0.85,
            )
            ax.add_patch(inner)
            ax.text(cx + comp_width / 2, y - 0.15, comp,
                    fontsize=6.5, ha="center", va="center", color="#374151")

    # Arrows between layers (data flow)
    arrow_style = dict(arrowstyle="-|>", color="#6B7280", lw=1.3,
                       connectionstyle="arc3,rad=0")
    for i in range(len(layers) - 1):
        y_from = layers[i][0] - 0.7
        y_to = layers[i + 1][0] + 0.7
        # Center arrow
        ax.annotate("", xy=(6.5, y_to), xytext=(6.5, y_from),
                    arrowprops=arrow_style)

    # Feedback arrow (Action → Orchestration, right side)
    ax.annotate("", xy=(12.8, 9.8 + 0.7), xytext=(12.8, 1.8 - 0.7),
                arrowprops=dict(arrowstyle="-|>", color="#DC2626", lw=1.0,
                                connectionstyle="arc3,rad=-0.0",
                                linestyle="dashed"))
    ax.text(13.0, 5.8, "feedback\nloop", fontsize=6, color="#DC2626",
            ha="center", va="center", rotation=90, style="italic")

    # State → Generation feedback arrow (left side)
    ax.annotate("", xy=(0.2, 7.8 + 0.5), xytext=(0.2, 3.8 - 0.5),
                arrowprops=dict(arrowstyle="-|>", color="#7C3AED", lw=1.0,
                                connectionstyle="arc3,rad=0.0",
                                linestyle="dashed"))
    ax.text(-0.1, 5.8, "context\ninjection", fontsize=6, color="#7C3AED",
            ha="center", va="center", rotation=90, style="italic")

    # Legend
    legend_items = [
        (llm_color, "LLM-dependent"),
        (det_color, "Deterministic"),
        (orch_color, "Orchestration"),
        (state_color, "Persistent state"),
    ]
    for i, (c, label) in enumerate(legend_items):
        lx = 1.0 + i * 3.0
        rect = mpatches.FancyBboxPatch((lx, 0.15), 0.5, 0.35,
            boxstyle="round,pad=0.04", facecolor=c, edgecolor="#374151", lw=0.5)
        ax.add_patch(rect)
        ax.text(lx + 0.65, 0.32, label, fontsize=6.5, va="center")

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig8_layer_architecture.png"))
    fig.savefig(os.path.join(OUTPUT_DIR, "fig8_layer_architecture.pdf"))
    plt.close(fig)
    print("  [OK] fig8_layer_architecture")


# ════════════════════════════════════════════════════════════════════════
# Main
# ════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("Generating thesis figures...")
    fig1_architecture()
    fig2_per_trait_error()
    fig3_scenario_scatter()
    fig4_actor_scaling()
    fig5_phase_heatmap()
    fig6_behavioral_features()
    fig7_fidelity_spectrum()
    fig8_layer_architecture()
    print(f"\nAll figures saved to {OUTPUT_DIR}/")
    print("Formats: PNG (300 DPI) + PDF (vector)")
