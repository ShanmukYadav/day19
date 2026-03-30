# Part D — AI-Augmented Task (PM Session)

## Prompt Used

> "Explain probability distributions (normal, uniform, binomial) with Python visualizations."

---

## AI Output (Summary)

### Normal Distribution
A continuous distribution defined by its mean (μ) and standard deviation (σ). The bell curve — symmetric, with most values clustering around the mean.

```python
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=0, scale=1, size=1000)
plt.hist(data, bins=40, color="#4f72c4", edgecolor="white")
plt.title("Normal Distribution (μ=0, σ=1)")
plt.xlabel("Value"); plt.ylabel("Frequency")
plt.show()
```

**Real-world use:** Heights, test scores, measurement errors, stock returns.

---

### Uniform Distribution
Every value in a range [a, b] is equally likely. The histogram is flat.

```python
data = np.random.uniform(low=-3, high=3, size=1000)
plt.hist(data, bins=40, color="#e04b4b", edgecolor="white")
plt.title("Uniform Distribution (a=-3, b=3)")
plt.show()
```

**Real-world use:** Random number generation, simulation inputs, lottery draws.

---

### Binomial Distribution
Discrete distribution modelling the number of successes in n independent Bernoulli trials, each with probability p.

```python
from scipy.stats import binom
import matplotlib.pyplot as plt

n, p = 10, 0.5
x = range(n + 1)
probs = [binom.pmf(k, n, p) for k in x]

plt.bar(x, probs, color="#59b89a", edgecolor="white")
plt.title("Binomial PMF (n=10, p=0.5)")
plt.xlabel("k (successes)"); plt.ylabel("P(X=k)")
plt.show()
```

**Real-world use:** Defect counts in manufacturing, email click-through rates, A/B testing.

---

## Evaluation

| Criterion | Assessment |
|---|---|
| **Correctness of Explanations** | ✅ Accurate — all three distributions defined correctly with proper parameters |
| **Visualization Quality** | ✅ Plots are meaningful; colour-coded and labelled for clarity |
| **Real-World Relevance** | ✅ Each distribution paired with a practical use-case |
| **Code Runnability** | ✅ All snippets are self-contained and execute without modification |
| **Areas to Improve** | Could overlay the theoretical PDF/PMF curve on the histogram for richer comparison |

**Verdict:** The AI output is pedagogically complete. The visualizations clearly differentiate the three distributions by shape (bell curve vs flat vs bar chart), making the differences intuitive. The code is production-grade and directly usable.
