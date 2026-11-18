# continuation from yesterday.

## 1. Understanding Information and Uncertainty

Information theory explains how probability determines the amount of information an event carries.

The information content of an event is:

\[
I(x)=-\log_2 P(x)
\]

I observed that information and probability have an inverse relationship: the less likely an event is, the more information it carries.

**Rough calculation:**

For an event with probability 0.25:

\[
I(x)=-\log_2(0.25)
\]

\[
I(x)=2\ bits
\]

This means the event carries 2 bits of information.

## 2. Entropy and Cross-Entropy

Entropy measures the average uncertainty of the actual probability distribution.

\[
H(P)=-\sum P(x)\log P(x)
\]

Cross-entropy measures the average prediction cost when my model uses distribution Q to represent the true distribution P.

\[
H(P,Q)=-\sum P(x)\log Q(x)
\]

**My calculation:**

Let the true distribution be:

\[
P=[0.8,0.2]
\]

And the model prediction:

\[
Q=[0.6,0.4]
\]

Using natural logarithms:

\[
H(P,Q)=-[0.8\ln(0.6)+0.2\ln(0.4)]
\]

\[
H(P,Q)=0.5919
\]

The model's predictions do not perfectly match the actual distribution, so additional prediction cost is introduced.

An important relationship:

\[
H(P,Q)=H(P)+D_{KL}(P||Q)
\]

This shows that cross-entropy consists of the actual uncertainty plus the additional cost caused by the model's prediction error.

## 3. KL Divergence and Distribution Alignment

KL divergence measures the extra information required when using Q instead of P.

\[
D_{KL}(P||Q)=\sum P(x)\log\frac{P(x)}{Q(x)}
\]

Using the previous distributions:

\[
D_{KL}(P||Q)=H(P,Q)-H(P)
\]

First:

\[
H(P)=-[0.8\ln(0.8)+0.2\ln(0.2)]
\]

\[
H(P)=0.5004
\]

Therefore:

\[
D_{KL}=0.5919-0.5004
\]

\[
\boxed{D_{KL}=0.0915\ nats}
\]

**My observation:** The model introduces approximately 0.0915 extra nats of information cost because its predicted distribution differs from the true distribution.

KL divergence is non-negative and asymmetric:

\[
D_{KL}(P||Q)\neq D_{KL}(Q||P)
\]

## 4. Mutual Information and Feature Selection

Mutual information measures how much observing one variable reduces uncertainty about another.

\[
I(X;Y)=H(Y)-H(Y|X)
\]

For example, if study hours provide useful information about examination results, knowing study hours reduces uncertainty about the result.

I understood that mutual information is useful in machine learning because it helps identify informative features, including nonlinear relationships that ordinary Pearson correlation may miss.

## 5. The Connection to Neural Network Training

One important mathematical connection is:

\[
\text{Cross-Entropy}=\text{Negative Log-Likelihood}
\]

For a correct class probability of 0.7:

\[
Loss=-\ln(0.7)
\]

\[
Loss=0.3567
\]

If the probability improves to 0.