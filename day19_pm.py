"""
Assignment — Week 04 · Day 19 (PM Session)
PG Diploma · AI-ML & Agentic AI Engineering · IIT Gandhinagar
Author : Shanmuk Kukati | Roll No. 26171023
Topics : Probability Distributions, Descriptive Statistics
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from collections import Counter


# ─────────────────────────────────────────────
# PART A — Concept Application (40%)
# ─────────────────────────────────────────────

# Q1 — Synthetic normal dataset (n=1000)
np.random.seed(42)
normal_data = np.random.normal(loc=0, scale=1, size=1000)

q1_mean = np.mean(normal_data)
q1_var  = np.var(normal_data)
q1_std  = np.std(normal_data)


def plot_q1_histogram(data, save_path="q1_normal_histogram.png"):
    """Plot and save histogram of normal dataset."""
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(data, bins=40, color="#4f72c4", edgecolor="white", linewidth=0.5)
    ax.axvline(np.mean(data), color="#e04b4b", linewidth=1.8, label=f"Mean = {np.mean(data):.3f}")
    ax.set_title("Normal Distribution — Synthetic Dataset (n=1000)", fontsize=13, pad=12)
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.legend()
    fig.tight_layout()
    fig.savefig(save_path, dpi=150)
    plt.close(fig)
    print(f"  Saved → {save_path}")


# Q2 — PMF for Binomial distribution
def binomial_pmf(n: int, p: float) -> dict:
    """
    Compute Binomial PMF for k = 0, 1, …, n.
    Returns a dict {k: P(X=k)}.
    """
    def comb(n, k):
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

    pmf = {k: comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in range(n + 1)}
    return pmf


# Q3 — Manual PDF of Normal distribution
def normal_pdf(x: float, mu: float = 0.0, sigma: float = 1.0) -> float:
    """Compute Normal PDF at point x without using built-in distributions."""
    coeff = 1 / (sigma * math.sqrt(2 * math.pi))
    exponent = -((x - mu) ** 2) / (2 * sigma ** 2)
    return coeff * math.exp(exponent)


# Q4 — Descriptive statistics + skewness
def descriptive_stats(data: list) -> dict:
    """Compute mean, median, mode, and skewness."""
    n = len(data)
    mu = sum(data) / n
    sorted_d = sorted(data)
    mid = n // 2
    median = (sorted_d[mid - 1] + sorted_d[mid]) / 2 if n % 2 == 0 else sorted_d[mid]

    count = Counter(data)
    mode = max(count, key=count.get)

    # Pearson's skewness
    sigma = math.sqrt(sum((x - mu) ** 2 for x in data) / n)
    skewness = (3 * (mu - median)) / sigma if sigma != 0 else 0

    return {
        "mean": mu, "median": median, "mode": mode,
        "std_dev": sigma, "skewness": skewness,
        "skew_interpretation": (
            "Left-skewed (negative)" if skewness < -0.5 else
            "Right-skewed (positive)" if skewness > 0.5 else
            "Approximately symmetric"
        ),
    }


sample_marks = [55, 60, 65, 70, 72, 72, 75, 80, 85, 90, 92, 95]
desc = descriptive_stats(sample_marks)


# Q5 — Coin-toss simulation
np.random.seed(0)
tosses = np.random.choice([0, 1], size=1000)   # 0=tails, 1=heads
estimated_prob_heads = np.sum(tosses) / len(tosses)
theoretical_prob     = 0.5


# ─────────────────────────────────────────────
# PART B — Stretch: Compare Distributions (30%)
# ─────────────────────────────────────────────

def plot_distributions(save_path="q_distributions_comparison.png"):
    """Generate and plot Normal vs Uniform distributions side by side."""
    np.random.seed(42)
    normal_samples  = np.random.normal(loc=0, scale=1, size=1000)
    uniform_samples = np.random.uniform(low=-3, high=3, size=1000)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4), sharey=False)

    for ax, data, label, color in zip(
        axes,
        [normal_samples, uniform_samples],
        ["Normal (μ=0, σ=1)", "Uniform (low=-3, high=3)"],
        ["#4f72c4", "#e04b4b"],
    ):
        ax.hist(data, bins=40, color=color, edgecolor="white", linewidth=0.4, alpha=0.85)
        ax.axvline(np.mean(data), color="black", linewidth=1.5, linestyle="--",
                   label=f"Mean={np.mean(data):.3f}")
        ax.set_title(label, fontsize=12, pad=10)
        ax.set_xlabel("Value")
        ax.set_ylabel("Frequency")
        ax.legend(fontsize=9)

    fig.suptitle("Normal vs Uniform Distribution — n=1000 Samples", fontsize=13, y=1.02)
    fig.tight_layout()
    fig.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved → {save_path}")

    return {
        "normal":  {"mean": np.mean(normal_samples),  "std": np.std(normal_samples)},
        "uniform": {"mean": np.mean(uniform_samples), "std": np.std(uniform_samples)},
    }


# ─────────────────────────────────────────────
# PART C — Interview Ready (20%)
# ─────────────────────────────────────────────

def relative_frequency_probability(events: list, target) -> float:
    """
    Estimate probability of a target event using relative frequency.

    P(event) = count(target) / total observations
    """
    return events.count(target) / len(events)


# ─────────────────────────────────────────────
# PART D — AI-Augmented Task (10%)
# (see day19_pm_ai_task.md for prompt & evaluation)
# ─────────────────────────────────────────────


# ─────────────────────────────────────────────
# DEMO / RUNNER
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  Day 19 PM — Probability Distributions & Stats")
    print("=" * 55)

    # Q1
    print("\n── Part A Q1: Normal Dataset ──")
    print(f"  Mean     : {q1_mean:.4f}")
    print(f"  Variance : {q1_var:.4f}")
    print(f"  Std Dev  : {q1_std:.4f}")
    plot_q1_histogram(normal_data)

    # Q2
    print("\n── Part A Q2: Binomial PMF (n=10, p=0.5) ──")
    pmf = binomial_pmf(n=10, p=0.5)
    total_prob = sum(pmf.values())
    print(f"  Sum of all PMF values : {total_prob:.6f}  (should be 1.0)")
    for k, v in pmf.items():
        print(f"    P(X={k:2d}) = {v:.6f}")

    # Q3
    print("\n── Part A Q3: Normal PDF (manual) ──")
    test_points = [-2, -1, 0, 1, 2]
    for x in test_points:
        print(f"  PDF({x:+d}) = {normal_pdf(x):.6f}")

    # Q4
    print("\n── Part A Q4: Descriptive Stats ──")
    print(f"  Data : {sample_marks}")
    for k, v in desc.items():
        print(f"  {k:<24}: {v}")

    # Q5
    print("\n── Part A Q5: Coin Toss Simulation ──")
    print(f"  Estimated P(Heads)   : {estimated_prob_heads:.4f}")
    print(f"  Theoretical P(Heads) : {theoretical_prob:.4f}")
    print(f"  Difference           : {abs(estimated_prob_heads - theoretical_prob):.4f}")

    # Part B
    print("\n── Part B: Distribution Comparison ──")
    stats_b = plot_distributions()
    for dist, vals in stats_b.items():
        print(f"  {dist:<8} → mean={vals['mean']:.4f}, std={vals['std']:.4f}")

    # Part C Q2
    print("\n── Part C Q2: Relative Frequency ──")
    outcomes = ["H", "T", "H", "H", "T", "T", "H", "T", "H", "H"]
    ph = relative_frequency_probability(outcomes, "H")
    print(f"  Outcomes : {outcomes}")
    print(f"  P(Heads) : {ph:.2f}")

    print("\n" + "=" * 55)
