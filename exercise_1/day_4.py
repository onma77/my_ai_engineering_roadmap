# matrices: grid of  numbers.
- a 2D vector [3,4] points to coordinates(3,4) on a plane. its length(magnitude) is 5 (the 3-4-5 triangle).

- a matrix is a 2D grid. rowws and columns. an m×n matrix has m rows and n columns.


|1 2 3|    2 x 3 matrix (2 rows, 3 columns)
|4 5 6|

- in neural networks, weight  matrices transform input vectors into output vectors. a layer with 784 inputs and 128 outputs uses a 128x784 weight matrix.

# why shapes matter
matrix multiplication has a strict rule: (mxn) @ (nxp) =n(mxp). the inner dimensions must match.

if you get a shape mismatch error in pytorch, this is why.

1. addition: element wise multiplying matching positions. both matrix must be in the same shape.
2. scalar multiply
3. matrix multiply: dot product of rows and columns. inner dimensions must match
4. transpose
5. determinant
6. inverse
7. identity

# broadcasting
when you add a bias vector to a matrix of outputs, the shapes do not match. Broadcasting stretches the smaller array to fit.