from cmath import sqrt
from math import hypot
from utils import near_equal


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def normalized(self):
        modulus = sqrt(self.x * self.x + self.y * self.y)
        return Vector2D(self.x / modulus, self.y / modulus)

    def dot(self, point):
        return self.x * point.x + self.y * point.y

    def dif(self, point):
        return Vector2D(self.x - point.x, self.y - point.y)

    def inverse(self):
        x = 0 if self.x == 0 else 1 / self.x
        y = 0 if self.y == 0 else 1 / self.y
        return Vector2D(x, y) * (1 / Vector2D(x, y).dot(self))

    def close(self, point):
        return near_equal(self.x, point.x) and near_equal(self.y, point.y)

    def __repr__(self, *args, **kwargs):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return type(self)(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return type(self)(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return type(self)(self.x * other, self.y * other)

    def distance_to(self, other):
        return hypot((self.x - other.x), (self.y - other.y))

    def __hash__(self, *args, **kwargs):
        return hash(str(self))


import unittest


class Vector2DTests(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector2D(1, 1)
        self.v2 = Vector2D(2, 2)
        self.v3 = Vector2D(3, 0)

    def test_normalized(self):
        self.assertEqual(self.v3.normalized(), Vector2D(1, 0))

    def test_dot(self):
        self.assertEqual(self.v1.dot(self.v2), 4)

    def test_dif(self):
        self.assertEqual(self.v1 - self.v2, Vector2D(-1, -1))

    def test_inverse(self):
        self.assertEqual(self.v3.inverse(), Vector2D(1 / 3, 0))

    def test_mul(self):
        self.assertEqual(self.v1 * 2, Vector2D(2, 2))

    def test_sum(self):
        self.assertEqual(self.v1 + self.v2, Vector2D(3, 3))


if __name__ == '__main__':
    unittest.main()
