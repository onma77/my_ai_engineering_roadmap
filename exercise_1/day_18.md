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


# Singular Value Decomposition (SVD)

### What I Learned
SVD is a matrix factorization technique that breaks any matrix into three components. It helps reveal hidden patterns, reduce data size, remove noise and solve mathematical problems.

### Key Concepts

**1. SVD Decomposition**

\[
A=U\Sigma V^T
\]

- **U:** Represents rotation in the output space.
- **Σ (Sigma):** Contains singular values that determine scaling.
- **Vᵀ:** Represents rotation in the input space.

**2. Singular Values**

Singular values measure how important each direction is. Larger values represent more significant information, while smaller values contribute less.

**3. Truncated SVD**

Keeps only the largest singular values to create a lower-rank approximation of the original matrix. This helps with compression while preserving important information.

**4. Practical Applications**
- Image compression: Reduces storage requirements.
- Recommendation systems: Predicts missing user ratings.
- NLP (LSA): Identifies hidden relationships between words and documents.
- Noise reduction: Removes less significant components.
- Pseudoinverse: Solves least-squares problems.

### Mathematical Rough Work

SVD:

\[
A=U\Sigma V^T
\]

Relationship between singular vectors:

\[
Av_i=\sigma_i u_i
\]

Pseudoinverse:

\[
A^+=V\Sigma^+U^T
\]

Low-rank approximation:

\[
A_k=\sum_{i=1}^{k}\sigma_i u_i v_i^T
\]

### Connection to PCA

I learned that PCA is closely connected to SVD. When the data is centered, SVD identifies the same principal directions used by PCA.

### My Main Takeaway

SVD is useful because it works on matrices of different shapes and reveals their underlying structure. I now understand how keeping only the most important singular values makes compression, dimensionality reduction and noise removal possible.

**Key understanding:** SVD simplifies complex matrices by separating their most important patterns from less significant information.