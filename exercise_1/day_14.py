1. Information Content
Information content measures how surprising an event is.

Formula:
\[
I(x)=-\log_2(P(x))
\]
My understanding:
- Less probability = more surprise.
- Higher probability = less surprise.
- A certain event has zero surprise.
Rough work:

Fair coin:
\[
I(x)=-\log_2(0.5)=1\ bit
\]
Rolling a six:
\[
I(x)=-\log_2(1/6)=2.58\ bits
\]
2. Entropy
Entropy measures the average uncertainty in a probability distribution.
\[
H(P)=-\sum p(x)\log_2 p(x)
\]
Example: Fair coin.
\[
H(P)=-[0.5\log_2(0.5)+0.5\log_2(0.5)]
\]
\[
H(P)=0.5+0.5=1\ bit
\]
A fair coin has higher uncertainty than a biased coin because both outcomes are equally likely.
3. Cross-Entropy
Cross-entropy measures how well my model's predicted probabilities match the actual distribution.
\[
H(P,Q)=-\sum p(x)\log(q(x))
\]
For classification, it becomes:
\[
Loss=-\log(q(\text{correct class}))
\]
My rough example:

If the correct class has a predicted probability of 0.8:
\[
Loss=-\ln(0.8)
\]
\[
Loss=0.223
\]
If the model predicts 0.2 instead:
\[
Loss=-\ln(0.2)=1.609
\]
This shows that incorrect confidence increases the loss.
4. KL Divergence
KL divergence measures the extra information wasted when using the model's distribution instead of the true distribution.
\[
D_{KL}(P||Q)=H(P,Q)-H(P)
\]
What I understood:
- KL divergence is always non-negative.
- It becomes zero when both distributions match.
- It is not symmetrical.
Meaning:
\[
D_{KL}(P||Q)\neq D_{KL}(Q||P)
\]
5. Mutual Information
Mutual information measures how much knowing one variable reduces uncertainty about another.
\[
I(X;Y)=H(X)-H(X|Y)
\]
Example:

If knowing a student's study hours helps predict their exam performance, then study hours contain information about exam performance.

I also learned that mutual information can detect both linear and nonlinear relationships, unlike Pearson correlation, which focuses on linear relationships.
6. Conditional and Joint Entropy
Conditional entropy measures the uncertainty remaining after knowing another variable.
\[
H(Y|X)=H(X,Y)-H(X)
\]
Joint entropy measures the uncertainty of two variables together.
\[
H(X,Y)\leq H(X)+H(Y)
\]
If two variables are independent, their joint entropy equals the sum of their individual entropies.
7. Label Smoothing
I learned that label smoothing changes hard targets into softer probability distributions.

Example:

Hard target:
\[
[0,0,1,0]
\]
Soft target:
\[
[0.025,0.025,0.925,0.025]
\]
This prevents a model from becoming too confident in its predictions and helps improve calibration.
8. Cross-Entropy and Maximum Likelihood
One important connection I understood is:
\[
\text{Cross-Entropy}=\text{Negative Log-Likelihood}
\]
Minimizing cross-entropy means maximizing the likelihood of the correct training labels.

This explains why cross-entropy is commonly used for classification models.
9. Perplexity
Perplexity measures how uncertain a language model is when predicting the next token.
\[
Perplexity=e^{H(P,Q)}
\]
Example:

If a language model has perplexity 50, it is behaving as though it is choosing between 50 equally likely next tokens.

Lower perplexity generally means better predictions.