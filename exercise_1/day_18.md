# Dimensionality Reduction

### What I Learned
Dimensionality reduction is the process of reducing the number of features in a dataset while preserving the most important information.

I learned that high-dimensional data creates the curse of dimensionality, where distances become less meaningful and models require significantly more data.

### Key Concepts

**1. PCA (Principal Component Analysis)**
- Reduces dimensions by identifying directions of maximum variance.
- Uses covariance matrices and eigendecomposition.
- Eigenvectors represent principal directions.
- Eigenvalues measure the variance captured by each direction.

**2. Explained Variance**
Measures how much information each principal component retains. Cumulative explained variance helps determine how many components to keep.

**3. t-SNE**
A nonlinear technique mainly used to visualize high-dimensional data while preserving local neighbourhood relationships.

**4. UMAP**
Similar to t-SNE but generally faster and better at preserving some global structure.

**5. Kernel PCA**
Extends PCA to nonlinear data using kernel functions such as RBF.

### Mathematical Rough Work

Covariance matrix:

\[
C=\frac{1}{n-1}X_c^TX_c
\]

Explained variance ratio:

\[
EVR_i=\frac{\lambda_i}{\sum_j\lambda_j}
\]

Cumulative explained variance:

\[
CEV_k=\sum_{i=1}^{k}EVR_i
\]

For example:

\[
EVR = 0.473+0.251+0.112
\]

\[
CEV_3=0.836=83.6\%
\]

This means the first three principal components preserve 83.6% of the total variance.

### My Main Takeaway

I now understand that dimensionality reduction is not simply deleting features. It is finding a lower-dimensional representation that preserves meaningful information.

- PCA: Data compression and preprocessing.
- t-SNE: Local structure visualization.
- UMAP: Scalable nonlinear visualization.
- Kernel PCA: Nonlinear dimensionality reduction.

**Key understanding:** Fewer dimensions can produce simpler, faster models without necessarily losing significant information.