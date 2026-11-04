# continuation from day5 on types of transformation.

### rotation
R(θ) = [
    [cos θ, -sin θ],
    [sin θ,  cos θ]
]

where:
- R means rotation matrix
- θ (theta) represents the angle of rotation.
- sin and cos are mathematical functions used to calculate the new coordinates.

- for a 45 degree rotation we use:   
θ = 45°
```py
import math

def rotation_2d(theta):
    c, s = math.cos(theta), math.sin(theta)
    return [[c, -s], [s, c]]
```
# 3D rotation
- in two dimension we rotate around a centre.
- in three dimension we rotate around an axis.
- the article introduces three rotation matrices:
1. Rz: rotates around the z-axis.
2. Rx: rotates around the x-axis.
3. Ry: rotates around the y-axis.

- For example, rotating around the z-axis changes the x and y coordinates while keeping the z coordinate unchanged.
