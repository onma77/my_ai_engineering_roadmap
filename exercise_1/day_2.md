# how to calculate dot product.
for example you have :
```py
a = [1,2,3]
b = [4,5,6]
```

- you first of all starts from with the first row, pick the first number and multiply it by the first number of the second row. 
- 1 * 4 = 4
- 2 * 5 = 10
- 3 * 6 = 18
- add the results which is 4 + 10 + 18 = 32.
- the dot product is 32.

# here is how its calculated in python
```py
a = [1, 2, 3]
b = [4, 5, 6]
result = sum(x * y for x, y in zip(a, b))
print(result)
```

### to break down the important part.
- zip(a, b): pairs corresponding elements(1,4),(2,5),(3,6).
- x * y :multiplies each pair.
- sum(...): adds all the products.

# why does AI care about the dot product?
it can help measure how aligned two vectors are.
- the dot product multiplies corresponding numbers and add the result.

# linear independence
vectors are linearly independent when none of them can be created by combining the others.
* for example:
v3 = 2 × v1 + v2
- 2 × [1,0, 0] = [2, 0, 0]
[2, 0, 0] + [0, 1, 0] = [2, 1, 0]
- the result is exactly v3.
- therefore, v3 doesn't introduce a new independent direction. it can already be constructed from v1 and v2.
# why does this matter 
Imagine a dataset contains three features:
- feature_1: Hours studied.
- feature_2: Hours slept.
- feature_3: A value calculated from the first two features.
If the third feature is entirely determined by the first two, it provides no new independent information.


# what are basis and rank
- basis is a minimal set of linearly independent vectors that can represent every direction in a particular space.




- rank tells us how many independent directions a matrix contains.