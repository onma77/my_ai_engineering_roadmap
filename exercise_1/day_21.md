# NUMERICAL STABILITY

### 1. Introduction
Numerical stability deals with how computers handle calculations involving decimal numbers. Floating-point errors can affect machine learning training and produce incorrect results.

### 2. Floating-Point Precision
Computers have limited precision when storing numbers.

- float64: 15–16 decimal digits.
- float32: 7–8 decimal digits.
- float16: 3–4 decimal digits.
- bfloat16: 2–3 decimal digits.

Example:

\[
0.1+0.2=0.30000000000000004
\]

This happens because decimal numbers cannot always be represented exactly in binary.

### 3. Overflow and Underflow
- Overflow: A number exceeds the maximum representable value.
- Underflow: A number becomes too small and approaches zero.

Example:

\[
e^{89}=\infty \quad \text{(float32)}
\]

\[
e^{-104}\approx0
\]

### 4. Catastrophic Cancellation
This happens when subtracting two nearly equal numbers, causing significant precision loss.

Example:

\[
1.0000001-1.0000000=0.0000001
\]

Small numerical errors can affect gradient and variance calculations.

### 5. Log-Sum-Exp Trick
Used to prevent exponential overflow.

\[
LSE(x)=m+\log\sum_i e^{x_i-m}
\]

Where:

\[
m=\max(x)
\]

Example:

\[
[100,101,102]-102=[-2,-1,0]
\]

Subtracting the maximum makes the calculation safer.

### 6. Stable Softmax
Softmax converts logits into probabilities.

\[
P(x_i)=\frac{e^{x_i-m}}{\sum_j e^{x_j-m}}
\]

For logits [100,101,102]:

\[
Softmax\approx[0.090,0.245,0.665]
\]

The probabilities sum to approximately 1.

### 7. NaN and Infinity
NaN means Not a Number, while infinity represents an unlimited numerical value.

Examples:

\[
0/0=NaN
\]

\[
\infty-\infty=NaN
\]

Python provides `math.isnan()` and `math.isinf()` for detection.

### 8. Numerical Gradient Checking

Used to verify analytical gradients.

Formula:

\[
f'(x)\approx\frac{f(x+h)-f(x-h)}{2h}
\]

Example:

\[
f(x)=x^2
\]

\[
f'(x)=2x
\]

At \(x=3\):

\[
f'(3)=6
\]

Numerical checking should produce approximately 6.

### 9. Mixed Precision Training
Combines float16 and float32 to improve training speed while maintaining accuracy.

Loss scaling multiplies small gradients before backpropagation to prevent underflow.

### 10. bfloat16 vs float16
- float16 has greater precision but a smaller numerical range.
- bfloat16 has less precision but approximately the same range as float32.

bfloat16 is generally preferred for neural network training.

### 11. Gradient Clipping
Prevents excessively large gradients.

Given:

\[
g=[10,20,30]
\]

\[
||g||=\sqrt{10^2+20^2+30^2}
\]

\[
||g||=\sqrt{1400}=37.42
\]

For maximum norm 5:

\[
Scale=\frac{5}{37.42}=0.1336
\]

Clipping reduces the gradient magnitude while preserving its direction.

### 12. Key Takeaways
- Floating-point calculations have limited precision.
- Overflow and underflow affect model training.
- Stable softmax prevents exponential overflow.
- Gradient checking verifies derivatives.
- Loss scaling prevents gradient underflow.
- Gradient clipping controls exploding gradients.
- Normalization helps maintain stable activations.

### Conclusion
I understood that numerical stability is essential in machine learning because even a correctly designed model can fail when calculations become numerically unstable.