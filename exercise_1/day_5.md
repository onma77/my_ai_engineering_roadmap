# matrix tranformation
# eigenvector and eigenvalue
- eigenvector: is a vector that the matrix only scales(never rotates) when multiplied.
(is a special non-zero vector whose direction does not change when a linear transformation (matrix multiplication)is applied to it)
- eigenvalue: is the scaling factor (a scalar, ussally written as λ) by which that vector is stretched or shrunk during the transformation
- Av = λv 
- cap A bold v equals lambda bold v
-  A is a square matrix representing the transformtion. 
- v is the generator.
- λ is the eigenvalue.

# what determinant of a 2D transformation matrix represent geometrically
- is the factor by which the matrix scales area.

# transformation as matrix
- is simply using a matrix to change a vector's position, direction, or representation.
(every linear transformation in 2D can be written as a 2x2 matrix).

# how do matrices perform transformation
1. a vector is a list of numbers.
2. a matirx is a table of numbers.
- for example:

```py
vector = [2,1]
matrix =[
    [2,0],
    [0, 3]
]
```

The first column is [2, 0], and the second column is [0, 3].

* This means:
- The original horizontal direction is stretched to [2, 0].
- The original vertical direction is stretched to [0, 3].
That's how a matrix describes a transformation.

-the matrix can transform the vector.
- the mathematical operation is:
(New vector = matrix x original vector)

# using basic vectors
in two-dimensional space, we have:

```py
e1 = [1,0]
e2 = [0,1]
```
- e1 points horizontally along the x-axis.
- e2 points vertically along the y-axis.


# types of transformation
1. rotation: means turning a point or object around a fixed centre.(Imagine the hands of a clock moving around its centre. That's rotation.)

2. reflection: means creating a mirror image.
- Imagine looking into a mirror. Your reflection appears on the opposite side.

3. dillation/scaling: scaling means making something bigger or smaller.

- If you increase its width and height, you're scaling it up.

- If you decrease them, you're scaling it down.

4. translation: sliding an object or point a specific distance aloong a straight vector without changing its size, shape, or orientation.

5. shearing/mathematical transformation.
 In spatial design, shearing slants the shape of an object, while in signals and systems  mathematical transforms like the Laplace Transform or Fourier transform convert time-domain functions into frequency-domain representations to simplify differential equations.