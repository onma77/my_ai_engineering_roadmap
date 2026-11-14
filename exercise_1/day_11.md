# Chain Rule and Automatic Differentiation

### 1. Chain Rule
I learned that the chain rule helps differentiate functions inside other functions by multiplying their individual derivatives.

Example:

\[
y=\sin(x^2)
\]

\[
\frac{dy}{dx}=\cos(x^2)\times 2x
\]

At \(x=2\):

\[
=4\cos(4)
\]

### 2. Computational Graphs
A computational graph breaks mathematical expressions into smaller operations.

- Forward pass: Calculates the output.
- Backward pass: Calculates gradients.

Example:

\[
y=(2\times3)+1=7
\]

\[
\frac{dy}{dx_1}=3,\quad \frac{dy}{dx_2}=2
\]

### 3. Forward vs Reverse Mode
- Forward mode moves derivatives from inputs to outputs.
- Reverse mode moves gradients from outputs to inputs.

Reverse mode is useful in neural networks because it calculates gradients for many parameters in one backward pass.

### 4. Automatic Differentiation
I understood that autograd automatically calculates gradients by tracking mathematical operations.

The `Value` class stores:
- `data`: Actual value.
- `grad`: Gradient.
- `_backward`: Backward calculation.
- `_prev`: Previous values.
- `_op`: Operation performed.

### 5. Gradient Accumulation

I learned why `+=` is used instead of `=`.

Example:

\[
y=x^2+x
\]

\[
\frac{dy}{dx}=2x+1
\]

At \(x=3\):

\[
=6+1=\boxed{7}
\]

Both gradient contributions must be added.

### 6. Neural Networks and Gradient Descent

A neuron calculates:

\[
y=\tanh(w_1x_1+w_2x_2+b)
\]

Gradient descent updates weights:

\[
w_{\text{new}}=w-\alpha\frac{dL}{dw}
\]

Example:

\[
0.8-(0.05\times2)=\boxed{0.7}
\]

### 7. Gradient Checking

Gradient checking compares automatic derivatives with numerical derivatives to confirm correctness.

Formula:

\[
f'(x)\approx\frac{f(x+h)-f(x-h)}{2h}
\]

For \(f(x)=x^2\), at \(x=2\):

\[
f'(2)=2(2)=\boxed{4}
\]

### Final Understanding

My major takeaway is that derivatives are not just mathematical calculations. They are what allow neural networks to understand their errors and adjust their weights during training.

I now understand how the chain rule, computational graphs and automatic differentiation work together during backpropagation.