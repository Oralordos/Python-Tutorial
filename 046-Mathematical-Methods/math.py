class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scale):
        return Vector(self.x * scale, self.y * scale)

    def __rmul__(self, scale):
        return Vector(scale * self.x, scale * self.y)

    def __imul__(self, scale):
        self.x *= scale
        self.y *= scale
        return self

x = Vector(2, 5)
y = Vector(7, 2)

print(x + y)
print(x - y)
print(x * 5)
print(2 * y)

print('-----------')

a = x
x *= 5
print(x)
print(a)
