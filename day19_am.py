"""
Assignment — Week 04 · Day 19 (AM Session)
PG Diploma · AI-ML & Agentic AI Engineering · IIT Gandhinagar
Author : Shanmuk Kukati | Roll No. 26171023
Topics : Python Fundamentals (Loops, HOF, List Comprehension), Statistics
"""

from functools import reduce
import math
import numpy as np


# ─────────────────────────────────────────────
# PART A — Concept Application (40%)
# ─────────────────────────────────────────────

# Q1 — Using loops
def mean_loop(data: list) -> float:
    """Compute mean using a loop."""
    total = 0
    for x in data:
        total += x
    return total / len(data)


def median_loop(data: list) -> float:
    """Compute median using a loop (sorts a copy, no built-ins)."""
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]


def variance_loop(data: list) -> float:
    """Compute population variance using a loop."""
    mu = mean_loop(data)
    total = 0
    for x in data:
        total += (x - mu) ** 2
    return total / len(data)


# Q2 — Higher-order functions (map, filter, reduce)
def mean_hof(data: list) -> float:
    """Compute mean using reduce."""
    return reduce(lambda acc, x: acc + x, data) / len(data)


def median_hof(data: list) -> float:
    """Compute median using sorted (functional style)."""
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    return (sorted_data[mid - 1] + sorted_data[mid]) / 2 if n % 2 == 0 else sorted_data[mid]


def variance_hof(data: list) -> float:
    """Compute population variance using map and reduce."""
    mu = mean_hof(data)
    squared_diffs = list(map(lambda x: (x - mu) ** 2, data))
    return reduce(lambda acc, x: acc + x, squared_diffs) / len(squared_diffs)


# Q3 — Student marks: filter above average, assign grades
student_marks = {
    "Alice": 82, "Bob": 55, "Charlie": 70, "Diana": 90,
    "Eve": 48, "Frank": 65, "Grace": 78, "Hank": 38,
}

marks_list = list(student_marks.values())
avg_marks = mean_loop(marks_list)

above_average = {name: score for name, score in student_marks.items() if score > avg_marks}

graded = {
    name: ("A" if score >= 80 else "B" if score >= 60 else "C")
    for name, score in student_marks.items()
}


# Q4 — Standard deviation + NumPy verification
def std_dev(data: list) -> float:
    """Compute standard deviation manually."""
    return math.sqrt(variance_loop(data))


sample_data = [12, 23, 3, 34, 45, 56, 5]
manual_std = std_dev(sample_data)
numpy_std  = np.std(sample_data)   # population std (ddof=0)


# Q5 — Mean, variance, difference in means for groups A & B
A = [12, 23, 3, 34, 45, 56, 5]
B = [12,  1, 3,  1,  1,  2, 3, 4, 5, 3, 4]

mean_A, var_A = mean_loop(A), variance_loop(A)
mean_B, var_B = mean_loop(B), variance_loop(B)
diff_means = mean_A - mean_B


# ─────────────────────────────────────────────
# PART B — Stretch: Two-Sample t-Test (30%)
# ─────────────────────────────────────────────

def two_sample_t_test(sample1: list, sample2: list, alpha: float = 0.05):
    """
    Perform Welch's two-sample t-test (unequal variances).

    Returns
    -------
    dict with keys: t_stat, mean1, mean2, var1, var2, conclusion
    """
    n1, n2   = len(sample1), len(sample2)
    mu1, mu2 = mean_hof(sample1), mean_hof(sample2)
    v1,  v2  = variance_hof(sample1), variance_hof(sample2)

    # Welch's t-statistic
    se = math.sqrt(v1 / n1 + v2 / n2)
    t_stat = (mu1 - mu2) / se

    # Welch-Satterthwaite degrees of freedom
    df = (v1/n1 + v2/n2)**2 / ((v1/n1)**2/(n1-1) + (v2/n2)**2/(n2-1))

    # Compare |t| against critical value at alpha=0.05 (two-tailed, approx)
    # For simplicity use scipy if available, else apply a conservative check
    try:
        from scipy import stats
        p_value = 2 * stats.t.sf(abs(t_stat), df)
        conclusion = (
            f"Reject H₀ — the two samples are significantly different (p={p_value:.4f} < {alpha})."
            if p_value < alpha else
            f"Fail to reject H₀ — no significant difference detected (p={p_value:.4f} ≥ {alpha})."
        )
    except ImportError:
        conclusion = (
            f"|t| = {abs(t_stat):.4f}. scipy not available; compare manually against "
            f"t-table with df ≈ {df:.1f} at α={alpha}."
        )

    return {
        "mean1": mu1, "mean2": mu2,
        "var1":  v1,  "var2":  v2,
        "t_stat": t_stat, "df": df,
        "conclusion": conclusion,
    }


# ─────────────────────────────────────────────
# PART C — Interview Ready (20%)
# ─────────────────────────────────────────────

# Q2 (Coding) — flatten + remove evens using list comprehension
def flatten_and_remove_evens(nested: list) -> list:
    """
    Flatten a nested list and remove all even numbers
    using a single list comprehension.
    """
    return [x for sublist in nested for x in sublist if x % 2 != 0]


# ─────────────────────────────────────────────
# PART D — AI-Augmented Task (10%)
# (see day19_am_ai_task.md for prompt & evaluation)
# ─────────────────────────────────────────────


# ─────────────────────────────────────────────
# DEMO / RUNNER
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  Day 19 AM — Statistics & Python Fundamentals")
    print("=" * 55)

    data = [12, 23, 3, 34, 45, 56, 5]

    print("\n── Part A: Loop-based stats ──")
    print(f"  Data   : {data}")
    print(f"  Mean   : {mean_loop(data):.4f}")
    print(f"  Median : {median_loop(data):.4f}")
    print(f"  Var    : {variance_loop(data):.4f}")

    print("\n── Part A: HOF-based stats ──")
    print(f"  Mean   : {mean_hof(data):.4f}")
    print(f"  Median : {median_hof(data):.4f}")
    print(f"  Var    : {variance_hof(data):.4f}")

    print("\n── Part A Q3: Student grades ──")
    print(f"  Average mark : {avg_marks:.2f}")
    print(f"  Above avg    : {above_average}")
    print(f"  Grades       : {graded}")

    print("\n── Part A Q4: Standard deviation ──")
    print(f"  Manual   : {manual_std:.6f}")
    print(f"  NumPy    : {numpy_std:.6f}")
    print(f"  Match    : {math.isclose(manual_std, numpy_std, rel_tol=1e-9)}")

    print("\n── Part A Q5: Groups A vs B ──")
    print(f"  A → mean={mean_A:.4f}, var={var_A:.4f}")
    print(f"  B → mean={mean_B:.4f}, var={var_B:.4f}")
    print(f"  Diff of means : {diff_means:.4f}")

    print("\n── Part B: Two-Sample t-Test ──")
    result = two_sample_t_test(A, B)
    for k, v in result.items():
        print(f"  {k:<14}: {v}")

    print("\n── Part C Q2: Flatten + remove evens ──")
    nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
    print(f"  Input  : {nested}")
    print(f"  Output : {flatten_and_remove_evens(nested)}")

    print("\n" + "=" * 55)
