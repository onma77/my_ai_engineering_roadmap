# PROBABILITY & DISTRIBUTIONS

**1. Probability:** Likelihood of an event happening.

Example: Getting an even number on a die.

P(Even) = 3/6 = **0.5**

**2. Conditional Probability:** Probability of an event given that another has happened.

P(A|B) = P(A ∩ B) / P(B)

**3. Independent Events:** One event does not affect another.

Coin toss and die roll:

P(Head and 6) = 1/2 × 1/6 = **1/12**

**4. Distributions**
- Bernoulli – two outcomes.
- Categorical – multiple categories.
- Uniform – equal probability.
- Normal – bell-shaped.
- Poisson – events within a time interval.

**5. Expected Value:** Long-term average.

Fair die:

E(X) = (1+2+3+4+5+6)/6 = **3.5**

**6. Variance:** Measures how spread out values are.

For a fair die:

Var(X) = E(X²) - E(X)²

= 15.1667 - 12.25 = **2.9167**

**7. PMF vs PDF**
- PMF: Discrete values.
- PDF: Continuous values.

**8. Central Limit Theorem:** Averages of large independent samples tend towards a normal distribution under suitable conditions.

**9. Log Probability:** Converts multiplication into addition.

log(ab) = log(a) + log(b)

Useful in machine learning to avoid numerical underflow.

**10. Softmax:** Converts model scores into probabilities.

**11. Cross-Entropy:** Measures prediction error. Lower loss is better.

---

# BAYES' THEOREM

Formula:

P(A|B) = P(B|A) × P(A) / P(B)

- Prior: Initial belief.
- Likelihood: Probability of evidence.
- Evidence: Overall probability.
- Posterior: Updated belief.

**Example: Medical Test**

Prevalence = 0.01%

Sensitivity = 99%

False-positive rate = 1%

P(Disease | Positive)

= (0.99 × 0.0001) / [(0.99 × 0.0001) + (0.01 × 0.9999)]

= **0.98% approximately**

A positive result does not always mean someone has the disease.

**Naive Bayes:** Uses Bayes' Theorem for classification, such as spam detection.

**MLE:** Uses observed data to estimate parameters.

**MAP:** Uses observed data and prior beliefs.

**Frequentist:** Focuses on long-run frequency.

**Bayesian:** Updates beliefs using new evidence.

**Beta Distribution:** Used to model probabilities of two outcomes, such as success and failure.

---

# QUICK PRACTICE

**1. Expected Value**

```python
values = [1, 2, 3, 4, 5, 6]
prob = [1/6] * 6

result = sum(v*p for v, p in zip(values, prob))
print(result)
```

Answer: `3.5`

**2. Conditional Probability**

```python
def conditional(p_ab, p_b):
    return p_ab / p_b

print(conditional(4/52, 12/52))
```

Answer: `0.3333`

**3. Softmax**

```python
import math

def softmax(values):
    exps = [math.exp(x - max(values)) for x in values]
    total = sum(exps)
    return [x / total for x in exps]

print(softmax([2, 1, 0.5]))
```

**Main things learned:** Probability, distributions, expected value, variance, sampling, Bayes' Theorem and how probability is applied in machine learning.