# Calculus for Machine Learning – My Study Notes

After studying these lessons, I understood that calculus plays an important role in machine learning because it helps models learn from their mistakes and improve their predictions.

Before going through these topics, I mostly saw calculus as a mathematical subject involving differentiation and integration. However, I now understand that it is also used to explain how machine learning models adjust their parameters to produce better results.

## 1. Derivatives

A derivative tells us how much a value changes when its input changes. In simple terms, it helps us understand the rate of change of a function.

For example, if we have:

`f(x) = x²`

Its derivative is:

`f'(x) = 2x`

This means that the rate at which the function changes depends on the value of x.

I learned that derivatives are important in machine learning because they help us understand how changing a model's parameters affects its error.

## 2. Partial Derivatives and Gradients

I also learned that when a function has more than one variable, we can use partial derivatives to check how one variable affects the result while keeping the others constant.

A gradient is simply a collection of these partial derivatives. It tells us the direction in which a function increases the fastest.

In machine learning, we usually want to reduce errors, so instead of moving in the direction of the gradient, we move in the opposite direction.

## 3. Gradient Descent

Gradient descent is one of the most important concepts I learned from this topic. It is a method used to reduce the error of a machine learning model.

The basic idea is that the model makes a prediction, checks how wrong the prediction is, and then adjusts its parameters to reduce that error.

The learning rate determines how big each adjustment should be. If it is too high, the model might skip over the best result. If it is too low, learning can become very slow.

## 4. Numerical and Analytical Derivatives

The lesson explained two ways of finding derivatives.

Analytical differentiation involves solving the derivative mathematically using differentiation rules.

Numerical differentiation estimates the derivative by using nearby values of a function.

I understood that both methods help us find how a function changes, but analytical differentiation gives an exact result when it can be solved correctly, while numerical differentiation gives an approximation.

## 5. The Chain Rule

The chain rule is used when we have a function inside another function. It helps us find the derivative of the entire expression by multiplying the derivatives of the individual functions.

For example:

`y = sin(x²)`

To differentiate this, we first differentiate the outer function and then the inner function.

The result is:

`dy/dx = cos(x²) × 2x`

What I understood is that instead of trying to differentiate the entire expression at once, we break it into smaller parts and multiply their derivatives together.

This becomes especially important in neural networks because they contain many operations connected together. The chain rule allows us to calculate how each operation contributes to the final result.

## 6. Automatic Differentiation and Backpropagation

One thing I learned from the second lesson is that calculating derivatives manually becomes difficult when dealing with large neural networks.

A neural network can contain many connected operations and thousands or even millions of parameters. Calculating the derivative of every parameter by hand would be extremely difficult.

Automatic differentiation solves this problem by tracking the mathematical operations performed and using the chain rule to calculate gradients automatically.

Backpropagation is an example of reverse-mode automatic differentiation. It starts from the final output and works backwards through the network, calculating how much each parameter contributed to the error.

I also learned that this is how frameworks like PyTorch handle gradients internally.

## 7. Computational Graphs

A computational graph is a way of representing the operations that happen when a model performs a calculation.

Each operation becomes a node, and the connections show how values move between operations.

There are two main processes:

- **Forward pass:** The input moves through the operations to produce an output.
- **Backward pass:** The system moves backwards through the graph to calculate gradients.

I understood that the forward pass is responsible for producing the result, while the backward pass helps the model understand how to improve that result.

## 8. Forward Mode and Reverse Mode

The lesson also introduced two approaches to automatic differentiation.

Forward mode starts from the input and moves forward, calculating derivatives as it goes.

Reverse mode starts from the output and works backwards to calculate gradients.

The important difference is where they are most useful.

Forward mode is useful when there are few inputs and many outputs. Reverse mode is more suitable for neural networks because they usually have many parameters but one final loss value.

This explains why neural networks use reverse-mode differentiation for backpropagation.

## 9. Building an Automatic Differentiation Engine

Another interesting part of the lesson was building a simple automatic differentiation engine from scratch using Python.

The lesson introduced a `Value` class that stores three important things:

- The actual numerical value.
- The gradient of that value.
- Information about the operations that produced it.

Each mathematical operation records how its gradient should be calculated during the backward pass.

For example, when two values are multiplied, the engine remembers the multiplication operation and uses its derivative rule when calculating gradients.

The backward method then goes through the computation graph in the correct order and applies the chain rule.

I understood that this is a simplified version of what happens inside automatic differentiation systems such as PyTorch.

## 10. Gradient Accumulation

I also learned why gradients sometimes need to be added instead of replaced.

When a value is used in more than one operation, it can receive gradient contributions from different paths in the computation graph.

These contributions need to be added together to get the correct total gradient.

This is why the lesson uses `+=` instead of `=` when updating gradients in the backward functions.

## 11. Hessian Matrix and Newton's Method

Another concept covered in the first lesson is the Hessian matrix. It contains second-order derivatives and helps us understand the curvature of a function.

While gradients tell us the direction of change, the Hessian gives us more information about how that direction is changing.

The lesson also introduced Newton's method, which uses curvature information to find better optimization steps.

However, calculating the full Hessian can be expensive for large machine learning models.

## 12. Taylor Series

Taylor series is a way of approximating a function around a particular point using its derivatives.

I understood that this is useful because it allows us to estimate how a function behaves without having to calculate everything directly.

The first-order approximation is connected to gradient descent, while the second-order approximation introduces information about curvature, which is useful in methods like Newton's method.

## 13. Integration and Its Uses in Machine Learning

Integration is another part of calculus covered in the lesson. Unlike differentiation, which focuses on how things change, integration deals with accumulation and the area under a curve.

In machine learning, integration is useful in probability calculations, expected values, Bayesian inference, and other areas where we need to work with continuous values.

## 14. Jacobians

The Jacobian is used when dealing with functions that have multiple inputs and multiple outputs.

It contains the partial derivatives that describe how each output changes when each input changes.

I understood that it is an extension of the idea of gradients for situations where we are working with more than one output.

## 15. Neural Network Training

After studying both lessons, I now have a better understanding of how these mathematical concepts work together when training a neural network.

First, the network receives input data and makes a prediction. It then calculates the error between the prediction and the correct answer.

After that, backpropagation uses derivatives and the chain rule to calculate gradients. Gradient descent then uses those gradients to update the model's weights.

This process keeps repeating until the model becomes better at making predictions.

The second lesson also demonstrated this by building a small neural network from scratch and training it to solve the XOR problem.

## 16. Gradient Checking

One final concept I learned from the automatic differentiation lesson is gradient checking.

Gradient checking is a way of testing whether the gradients calculated by our automatic differentiation engine are correct.

It does this by comparing the gradients from automatic differentiation with gradients estimated using numerical differentiation.

If both results are close, it gives us confidence that our backward calculations are working properly.

I understood that this is especially useful when building or debugging an automatic differentiation system.

## My Overall Understanding

My biggest takeaway from these lessons is that calculus is not just about solving mathematical problems. It provides the foundation for how machine learning models learn and improve.

I now understand that derivatives and gradients help us measure changes, gradient descent helps reduce errors, and the chain rule makes it possible to calculate gradients through several connected operations.

I also learned that automatic differentiation makes these calculations easier to handle in large models, while backpropagation allows neural networks to work backwards and determine how their parameters should change.

Although some concepts, especially the Hessian matrix, Taylor series, Jacobian, and automatic differentiation, were difficult to understand at first, I can now see how they connect to the bigger picture of machine learning.