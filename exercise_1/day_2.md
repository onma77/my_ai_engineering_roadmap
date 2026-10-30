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

