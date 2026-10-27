class Vector:
    def __init__(self, data):
        self.data = list(data)
        self.size = len(self.data)

    def __repr__(self):
        return f"Vector({self.data})"

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.data, other.data)])

    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.data, other.data)])

    def __mul__(self, scalar):
        return Vector([x * scalar for x in self.data])

    def dot(self, other):
        return sum(a * b for a, b in zip(self.data, other.data))

    def magnitude(self):
        return sum(x ** 2 for x in self.data) ** 0.5



v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("Vector 1:", v1)
print("Vector 2:", v2)

print("Addition:", v1 + v2)
print("Subtraction:", v1 - v2)
print("Multiplication:", v1 * 2)

print("Dot product:", v1.dot(v2))
print("Magnitude:", v1.magnitude())
