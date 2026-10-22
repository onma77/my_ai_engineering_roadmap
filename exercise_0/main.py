weights = [0.5, -1.2, 3.0]
alias = list(weights)
print(alias)

alias[0] = 99.0
print(f"this is the changed alias {alias}")

print(weights)

# independent = list(weights)
# independent[1] = 0.0
# print(weights, independent)

# grid = [[0] * 3] * 2
# grid[0][0] = 1
# print(grid)

# grid = [[0] * 3 for _ in range(2)]
# grid[0][0] = 1
# print(grid)