# scaling 
means making something bigger or smaller.
- imagine you have a square.
- if you increases its widtth and height, you scaling it up.
- if you decreases them, you are scaling it down.
- the article gives this example.

sx = 2
sy = 0.5

- this means 
- multiply the horizontal coordinate by 2.
- multiply the vertical coordinate by 0.5

- the scaling matrix is:
s = [
    [2, 0]
    [0, 0.5]
]

- suppose we have:
```py
A = [2,1]
```
- after scaling:
x = 2*2 = 4
y = 1*0.5 = 0.5 

- the new point becomes
A' = [4, 0.5]

- the python implementation is:
```py
def scaling_2d(sx, sy):
    return [[sx, 0], [0,sy]]
```
- sx controls the horizontal scaling.
- sy controls vertical scaling. 
- return produces the scaling matrix.

