# Study Work: Understanding Gradients Through a Real-World Business Example
1. Scenario: Optimizing Business Profit
Imagine I run a bottled water business. I want to determine the best selling price that will maximize my profit.

Instead of randomly changing prices, I can use mathematics (gradients) to understand how changing the price affects my profit.

Assume my profit function is:
\[
P(x)=-x^2+400x-10000
\]
Where:
- \(x\) = selling price (in naira).
- \(P(x)\) = profit (in naira, using a simplified model).
2. Finding the Gradient
To understand how profit changes as price changes, I differentiate the function.
\[
P(x)=-x^2+400x-10000
\]
Differentiating:
\[
P'(x)=-2x+400
\]
This derivative is the gradient.
3. Testing Different Prices
At ₦100:
\[
P'(100)=-2(100)+400
\]
\[
= -200+400=200
\]
Gradient = +200.

Meaning: Increasing the price slightly will increase profit.

At ₦150:
\[
P'(150)=-300+400=100
\]
Gradient = +100.

Profit is still increasing, but the rate of increase is slowing down.

At ₦200:
\[
P'(200)=-400+400=0
\]
Gradient = 0.

This is the maximum profit point.

At ₦250:
\[
P'(250)=-500+400=-100
\]
Gradient = -100.

Increasing the price further will reduce profit.
4. Calculating the Maximum Profit
At the optimal price:
\[
x=200
\]
Substitute into the original function:
\[
P(200)=-(200)^2+400(200)-10000
\]
\[
=-40000+80000-10000
\]
\[
P(200)=30,000
\]
Maximum profit = ₦30,000.
5. Connecting This to Machine Learning
This is where I see the relationship between gradients and optimization.

In machine learning, instead of adjusting a selling price, we adjust model weights to reduce prediction errors (loss).

The gradient tells us how the loss changes when a weight changes.

The update rule is:
\[
w_{\text{new}}=w_{\text{old}}-lr\times gradient
\]
For example:
- Current weight = 5
- Learning rate = 0.1
- Gradient = 4
\[
w=5-(0.1\times4)
\]
\[
w=5-0.4=4.6
\]
New weight = 4.6.

The weight moves in the opposite direction of the gradient to reduce the loss.
My Final Understanding
I understand that a gradient is more than just a derivative. It tells us the direction and rate at which a function changes.

In business, it helps identify how price changes affect profit. In machine learning, it helps a model adjust its weights to minimize errors.

Key lesson: Gradient tells us where we are going wrong and gives us a mathematical direction for improvement.