# continuation from yesterday: NUMERICAL STABILITY
### Focus: Practical Calculations

### 1. Floating-Point Errors

Computers cannot represent every decimal exactly.

\[
0.1+0.2=0.30000000000000004
\]

Error:

\[
=4\times10^{-17}
\]

Small errors can accumulate during training.

### 2. Overflow and Underflow

\[
e^{89}=\infty \quad (float32)
\]

\[
e^{-104}\approx0
\]

Overflow occurs when values are too large, while underflow occurs when values become too small.

### 3. Log-Sum-Exp

Given:

\[
x=[3,4,5]
\]

\[
m=5
\]

\[
e^{[-2,-1,0]}=[0.1353,0.3679,1]
\]

\[
LSE=5+\log(1.5032)
\]

\[
\boxed{5.4076}
\]

### 4. Softmax Calculation

Given logits:

\[
[2,3,4]
\]

After subtracting the maximum:

\[
[-2,-1,0]
\]

Final probabilities:

\[
\boxed{[0.0900,0.2447,0.6652]}
\]

Verification:

\[
0.0900+0.2447+0.6652\approx1
\]

### 5. Cross-Entropy

If the correct class probability is 0.8:

\[
L=-\log(0.8)
\]

\[
\boxed{L=0.2231}
\]

Lower confidence in the correct prediction produces higher loss.

### 6. Gradient Calculation

Given:

\[
f(x,y)=x^2+3xy+y^3
\]

Partial derivatives:

\[
\frac{\partial f}{\partial x}=2x+3y
\]

\[
\frac{\partial f}{\partial y}=3x+3y^2
\]

At \(x=2,y=1\):

\[
\boxed{\nabla f=[7,9]}
\]

### 7. Gradient Clipping

Given:

\[
g=[6,8]
\]

\[
||g||=\sqrt{36+64}=10
\]

Maximum norm = 5.

\[
Scale=\frac{5}{10}=0.5
\]

New gradient:

\[
\boxed{[3,4]}
\]

### 8. Loss Scaling

Given gradient:

\[
g=10^{-8}
\]

Scaling factor = 1024.

\[
10^{-8}\times1024=1.024\times10^{-5}
\]

Divide by 1024 after backward computation to recover the original gradient.

### 9. Today's Understanding

- Stable softmax prevents overflow.
- Cross-entropy measures prediction error.
- Gradient checking verifies derivatives.
- Gradient clipping controls exploding gradients.
- Loss scaling prevents small gradients from disappearing.

### Conclusion

Today's calculations helped me understand how numerical stability connects mathematical operations to neural network training. I now understand why controlling precision and gradient values is important for reliable machine learning.