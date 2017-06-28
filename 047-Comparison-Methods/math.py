from math import sqrt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)

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

    def size(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __lt__(self, other):
        return self.size() < other.size()

    def __le__(self, other):
        return self.size() <= other.size()

    def __gt__(self, other):
        return self.size() > other.size()

    def __ge__(self, other):
        return self.size() >= other.size()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

x = Vector(2, 5)
y = Vector(7, 2)

print(x < y)
print(x > y)
print(x <= y)
print(x >= y)
print(x == y)
print(x != y)
