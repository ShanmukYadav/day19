# Week 04 · Day 19 — Assignment

**PG Diploma · AI-ML & Agentic AI Engineering · IIT Gandhinagar**

| Field | Detail |
|---|---|
| **Student** | Shanmuk Kukati |
| **Roll No.** | 26171023 |
| **Study Group** | 4 |
| **Week / Day** | Week 04 · Day 19 |
| **Deadline** | Day 20 · 09:15 AM |
| **Submission** | LMS + GitHub Repository |

---

## Repository Structure

```
Week04_Day19/
├── AM_Session/
│   ├── day19_am.py              # All AM parts: loops, HOF, comprehension, stats, t-test
│   └── day19_am_ai_task.md      # Part D — AI prompt, output & evaluation
│
├── PM_Session/
│   ├── day19_pm.py              # All PM parts: probability distributions, descriptive stats
│   ├── day19_pm_ai_task.md      # Part D — AI prompt, output & evaluation
│   ├── q1_normal_histogram.png  # Generated: Normal distribution histogram
│   └── q_distributions_comparison.png  # Generated: Normal vs Uniform comparison
│
└── README.md                    # This file
```

---

## AM Session

**Topics:** Python Fundamentals (Loops, Higher-Order Functions, List Comprehension) · Statistics (Descriptive Statistics, Hypothesis Testing)

### Coverage

| Part | Description | Weight |
|---|---|---|
| **A** | Mean / Median / Variance via loops and HOF; student grade filtering; standard deviation verification; group comparison | 40% |
| **B** | `two_sample_t_test()` — Welch's t-test with manual t-statistic and p-value interpretation | 30% |
| **C** | Conceptual answers (Q1, Q3) + coding: flatten nested list & remove evens via list comprehension | 20% |
| **D** | AI prompt on descriptive stats & hypothesis testing — documented and evaluated | 10% |

### How to Run

```bash
cd AM_Session
python day19_am.py
```

**Expected output:**
- Printed stats (mean, median, variance) for sample data
- Student grade table above-average filter
- NumPy verification of manual standard deviation
- Group A vs B comparison (means, variances, difference)
- Two-sample t-test result with conclusion
- Flatten + remove-evens demonstration

---

## PM Session

**Topics:** Probability Distributions · Descriptive Statistics

### Coverage

| Part | Description | Weight |
|---|---|---|
| **A** | Normal dataset (n=1000); Binomial PMF (verified sum=1); manual Normal PDF; descriptive stats + skewness; coin-toss simulation | 40% |
| **B** | Normal vs Uniform distribution — sample, plot, and compare shape, spread, and central tendency | 30% |
| **C** | Conceptual answers (Q1, Q3) + `relative_frequency_probability()` function | 20% |
| **D** | AI prompt on probability distributions with Python visualisations — documented and evaluated | 10% |

### How to Run

```bash
cd PM_Session
python day19_pm.py
```

**Expected output:**
- Descriptive stats for synthetic normal dataset
- PMF table for Binomial(n=10, p=0.5) with total probability verification
- Manual Normal PDF values at x = −2, −1, 0, 1, 2
- Descriptive stats + skewness interpretation for sample marks
- Coin-toss simulation vs theoretical probability
- `q1_normal_histogram.png` — histogram of normal dataset
- `q_distributions_comparison.png` — Normal vs Uniform side-by-side

---

## Dependencies

```bash
pip install numpy matplotlib scipy
```

| Library | Version | Purpose |
|---|---|---|
| `numpy` | ≥ 1.24 | Array operations, random sampling |
| `matplotlib` | ≥ 3.7 | Plotting and saving figures |
| `scipy` | ≥ 1.11 | p-value computation in t-test (optional — gracefully handled if absent) |

> **Note:** `scipy` is optional. The AM session t-test will still compute the t-statistic and degrees of freedom; it will print a manual comparison note instead of a p-value if `scipy` is not installed.

---

## Key Concepts Covered

### AM Session
- **Loops vs Higher-Order Functions vs List Comprehension** — three approaches to the same computation; loops for explicit control, HOF (map/filter/reduce) for functional pipelines, comprehensions for concise transformations
- **Descriptive Statistics** — mean, median, variance, standard deviation from first principles
- **Hypothesis Testing** — null hypothesis, alternative hypothesis, t-statistic, p-value, significance level (α = 0.05), Welch's correction for unequal variances

### PM Session
- **Probability Distributions** — Normal (continuous, bell-shaped), Binomial (discrete, count of successes), Uniform (flat, equal probability)
- **PMF vs PDF** — PMF for discrete variables (sums to 1), PDF for continuous variables (integrates to 1)
- **Central Limit Theorem** — sample means of any distribution approach a normal distribution as n → ∞; foundational to inference and ML model assumptions
- **Skewness** — direction and degree of asymmetry; left-skewed (long left tail), right-skewed (long right tail), symmetric (≈ 0)

---

## Interview Answers

### AM — Q1: Loops vs List Comprehension vs Higher-Order Functions

| Approach | When to Use |
|---|---|
| **Loops** | Complex logic, stateful iteration, early exit, debugging step-by-step |
| **List comprehension** | Concise filtering/transformation of a single iterable; preferred in Python for readability |
| **HOF (map/filter/reduce)** | Functional pipelines, applying a function across collections, composing transformations |

### AM — Q3: Hypothesis Testing

Hypothesis testing is a formal framework for making data-driven decisions under uncertainty.

- **Null Hypothesis (H₀):** Assumes no effect or difference exists (e.g., "the two group means are equal").
- **Alternative Hypothesis (H₁):** Asserts that a difference does exist.
- **p-value:** The probability of observing a result as extreme as the data, *if H₀ were true*. A small p-value is evidence against H₀.
- **Significance Level (α):** The decision threshold (typically 0.05). If p < α → reject H₀.

*Example:* Testing whether a new teaching method improves exam scores. H₀: mean scores are equal. If p = 0.02 < 0.05, we reject H₀ and conclude the method has a statistically significant effect.

### PM — Q1: PMF vs PDF

| | PMF | PDF |
|---|---|---|
| **Variable type** | Discrete (countable) | Continuous (uncountable) |
| **Output** | Exact probability P(X = k) | Probability density (not direct probability) |
| **Sum / Integral** | Σ P(X=k) = 1 | ∫ f(x) dx = 1 |
| **Example** | Binomial, Poisson | Normal, Exponential |

### PM — Q3: Central Limit Theorem

The CLT states that the distribution of sample means approaches a Normal distribution as sample size n increases, regardless of the population's shape.

**Why it matters in ML:**
- Justifies using Normal-assumption-based tests (t-tests, z-tests) on real-world data
- Underpins confidence intervals and standard error estimates
- Explains why many ML model errors are approximately Gaussian
- Enables statistical inference on large datasets without knowing the true population distribution

---

*Submitted by Shanmuk Kukati · Roll No. 26171023 · Week 04 · Day 19*
