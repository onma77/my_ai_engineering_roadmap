## 1. What I Learned

Today, I studied dimensionality reduction and how it helps simplify high-dimensional datasets without losing the most important information.

My understanding is that datasets can contain hundreds or thousands of features, but not all these features contribute equally to the information we need.

For example, an image of a handwritten digit can contain 784 pixel features. However, many of these pixels may be redundant. Dimensionality reduction helps identify the important patterns and represent the data using fewer dimensions.

The main idea I took from this lesson is that reducing dimensions is not simply deleting data. It is about preserving meaningful information while removing unnecessary complexity.

## 2. The Curse of Dimensionality

I learned that as the number of dimensions increases, data becomes harder to analyze.

Three important problems stood out to me:

- Distances between data points become less meaningful.
- Data becomes increasingly spread across high-dimensional space.
- More dimensions require exponentially more samples to maintain data density.

This explains why working with too many features can make machine learning models less effective.

## 3. Principal Component Analysis (PCA)

PCA was one of the most important concepts I studied.

It identifies the directions in which data varies the most and uses those directions to represent the original dataset.

I understood the PCA process in five stages:

1. Center the data by subtracting the mean.
2. Calculate the covariance matrix.
3. Perform eigendecomposition.
4. Sort eigenvalues from largest to smallest.
5. Project the data onto the selected principal components.

The important relationship I noticed is:

- Eigenvectors determine the direction of each principal component.
- Eigenvalues determine how much variance each direction captures.

Therefore, the component with the largest eigenvalue captures the greatest variance.

## 4. Explained Variance

I studied how explained variance helps determine how many principal components should be retained.

For example:

PC1 = 47.3%

PC2 = 25.1%

PC3 = 11.2%

PC4 = 8.9%

Cumulative variance:

47.3 + 25.1 = 72.4%

72.4 + 11.2 = 83.6%

83.6 + 8.9 = 92.5%

My observation is that the first four components capture 92.5% of the total variance.

This means we can represent the dataset using four components while retaining most of its original variance.

I also learned about the elbow method, which helps identify where adding more components produces diminishing returns.

## 5. Comparing PCA, t-SNE and UMAP

I studied three dimensionality reduction techniques and understood that they serve different purposes.

**PCA:** Mainly useful for preprocessing, compression and preserving global variance.

**t-SNE:** Useful for visualizing nearby data points and identifying local clusters. However, distances between clusters should not be interpreted as meaningful.

**UMAP:** Useful for visualization because it preserves local structure and some global structure. It is also generally faster than t-SNE.

My conclusion is that PCA is more suitable for general feature reduction, while t-SNE and UMAP are more useful when exploring complex data visually.

## 6. Kernel PCA

I learned that standard PCA works mainly with linear relationships.

However, some datasets contain nonlinear structures that cannot be separated using ordinary linear transformations.

Kernel PCA addresses this by using kernel functions to represent data in a higher-dimensional feature space without explicitly calculating those coordinates.

The RBF kernel is particularly useful for nonlinear structures.

An example is concentric circles, where one circle exists inside another. Standard PCA may fail to separate them, while Kernel PCA can capture their nonlinear structure.

## 7. Reconstruction Error

Another concept I studied was reconstruction error.

After reducing dimensions, we can reconstruct the original data and measure how much information was lost.

The formula is:

MSE = Mean((Original Data - Reconstructed Data)²)

A smaller reconstruction error means the reduced representation retains more of the original information.

I also learned that reconstruction error can help detect anomalies because unusual data points may have significantly higher reconstruction errors.

## 8. My Main Takeaways

- Dimensionality reduction helps simplify complex datasets.
- PCA identifies directions of maximum variance.
- Eigenvectors represent directions, while eigenvalues represent variance.
- Explained variance helps determine the number of components to retain.
- t-SNE and UMAP are useful for visualizing complex data structures.
- Kernel PCA handles nonlinear relationships.
- Reconstruction error measures information lost during dimensionality reduction.

The biggest thing I understood today is that reducing the number of features does not necessarily mean reducing the usefulness of a dataset. What matters is retaining the most meaningful structure.

---


### 1. Explained Variance Calculation

Given:

PC1 = 0.473

PC2 = 0.251

PC3 = 0.112

PC4 = 0.089

Total variance captured:

= 0.473 + 0.251 + 0.112 + 0.089

= 0.925

= 92.5%

Therefore, four principal components capture 92.5% of the variance.

### 2. Simple PCA Projection Example

Suppose I have a data point:

X = [4, 6]

Mean = [2, 2]

First, center the data:

X_centered = [4-2, 6-2]

X_centered = [2, 4]

Assume the first principal component is:

PC1 = [0.6, 0.8]

Project onto PC1:

= (2 × 0.6) + (4 × 0.8)

= 1.2 + 3.2

= 4.4

The original two-dimensional point is now represented by one value: 4.4.

This demonstrates how PCA can reduce dimensions through projection.

### 3. Reconstruction Error

Original value = 10

Reconstructed value = 8

Error:

= (10 - 8)²

= 2²

= 4

This shows that reconstruction error increases when the reconstructed data moves further away from the original.

### 4. My Final Observation

If I have 784 features and PCA reduces them to 50 while preserving 95% of the variance, I have significantly reduced the dimensionality without losing most of the original variance.

This is useful because the model has fewer features to process while retaining most of the information represented in the original dataset.