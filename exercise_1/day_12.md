Study Work: Optimization
I learned that optimization is about finding the best values for a model's weights so that the loss becomes smaller.

My understanding:
- Gradient Descent moves weights in the opposite direction of the gradient.
- Learning rate controls how big each step is.
- If the learning rate is too high, it can overshoot. If too low, learning becomes slow.
- Momentum uses previous gradients to make movement smoother.
- Adam adjusts learning rates for individual weights.
- Mini-batch SGD uses small groups of data during training.
My rough calculation:

Using:
\[
w = w - lr \times gradient
\]
Given:
- Weight = 10
- Learning rate = 0.1
- Gradient = 2
\[
w = 10 - (0.1 \times 2)
\]
\[
w = 10 - 0.2 = 9.8
\]
New weight = 9.8

What I understood: Optimization helps a model reduce its errors gradually. Adam, Momentum and Gradient Descent all help achieve this, but they update weights differently.