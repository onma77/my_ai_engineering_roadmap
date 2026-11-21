# PERSONAL MATHEMATICAL STUDY: DIMENSIONALITY REDUCTION

### 1. PCA and Variance

I focused on understanding how PCA identifies directions with maximum variance using eigenvalues and eigenvectors.

The fundamental equation:

\[
\Sigma v = \lambda v
\]

Where:
- \(\Sigma\) = Covariance matrix
- \(v\) = Eigenvector
- \(\lambda\) = Eigenvalue

### 2. Eigenvalue Calculation (Rough Work)

Given:

\[
\Sigma =
\begin{bmatrix}
4&2\\
2&4
\end{bmatrix}
\]

Characteristic equation:

\[
\det(\Sigma-\lambda I)=0
\]

\[
(4-\lambda)^2-4=0
\]

\[
\lambda^2-8\lambda+12=0
\]

\[
(\lambda-6)(\lambda-2)=0
\]

Therefore:

\[
\lambda_1=6,\quad \lambda_2=2
\]

### 3. Explained Variance

Total variance:

\[
6+2=8
\]

\[
EVR_1=\frac{6}{8}\times100=75\%
\]

\[
EVR_2=\frac{2}{8}\times100=25\%
\]

PC1 preserves 75% of the total variance. Reducing to one component therefore loses 25% of the variance.

### 4. Data Projection

Given:

\[
X=[3,4],\quad v=[0.6,0.8]
\]

Projection:

\[
Xv^T=(3\times0.6)+(4\times0.8)
\]

\[
=1.8+3.2=5
\]

A two-dimensional observation is reduced to one dimension.

### 5. Reconstruction Error

The reconstruction error measures the difference between original and reconstructed data.

\[
MSE=\frac{1}{n}\sum_{i=1}^{n}(x_i-\hat{x}_i)^2
\]

Example:

\[
X=[5,8,10]
\]

\[
\hat X=[4,7,9]
\]

\[
MSE=\frac{1+1+1}{3}=1
\]

### 6. Deeper Observations

- Larger eigenvalues indicate directions containing more variance.
- PCA prioritizes components with the highest variance.
- t-SNE preserves local neighbourhood relationships.
- UMAP attempts to preserve local and global structure.
- Kernel PCA uses nonlinear kernel transformations.
- Reducing dimensions introduces a trade-off between compression and information preservation.

### Final Understanding

My main mathematical understanding is that PCA transforms data using the eigenvectors of its covariance matrix, ranks those directions using eigenvalues, and projects the data onto the most informative components.

**The central idea: Dimensionality reduction is a mathematical process of finding a lower-dimensional representation while minimizing the loss of important data structure.**