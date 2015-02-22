from math import pi, atan

from drawable import Drawable
from vector2D import Vector2D


class Line(Drawable):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def direction(self):
        return self.end.dif(self.start).normalized()

    def parametric(self, point):
        return (point.dif(self.start)).dot(self.end.dif(self.start).inverse())

    @property
    def as_lambda(self):
        return lambda t: self.start + (self.end - self.start) * t

    def contains(self, point):
        if not Line(self.start, point).is_parallel(self):
            return False
        return True if 0.0 <= self.parametric(point) <= 1.0 else False

    @property
    def delta_x(self):
        return self.end.x - self.start.x

    @property
    def delta_y(self):
        return self.end.y - self.start.y

    @property
    def angle(self):
        if self.delta_x == 0:
            return pi / 2 if self.delta_y > 0 else - pi / 2

        return atan(self.delta_y / self.delta_x)

    def is_parallel(self, line):
        return self.angle == line.angle

    def __str__(self):
        return 'start=' + str(self.start) + ', end=' + str(self.end) + ')'

    def intersection(self, line):
        if self.is_parallel(line):
            return None

        x1 = self.start.x
        y1 = self.start.y
        x2 = self.end.x
        y2 = self.end.y
        x3 = line.start.x
        y3 = line.start.y
        x4 = line.end.x
        y4 = line.end.y
        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        x = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
        x = x / denominator
        y = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
        y = y / denominator
        intersection = Vector2D(x, y)

        if not self.contains(intersection):
            return None
        if not line.contains(intersection):
            return None

        return intersection

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def draw(self, resolution=100):
        import pylab

        a = pylab.linspace(0, 1, resolution)
        pylab.plot(self.as_lambda(a).x, self.as_lambda(a).y, color='r')


import unittest


class LineTests(unittest.TestCase):
    def setUp(self):
        self.l1 = Line(Vector2D(1, 1), Vector2D(2, 2))
        self.l2 = Line(Vector2D(1, 0), Vector2D(0, 1))
        self.l3 = Line(Vector2D(0, 0), Vector2D(1, 1))

    def test_direction(self):
        self.assertEqual(self.l1.direction(), Vector2D(1, 1).normalized())

    def test_parametric(self):
        self.assertEqual(self.l1.parametric(Vector2D(1, 1)), 0.0)

    def test_contains(self):
        self.assertTrue(self.l3.contains(Vector2D(0.5, 0.5)))

    def test_not_contains(self):
        self.assertFalse(self.l3.contains(Vector2D(0.5, 0.6)))

    def test_is_parallel(self):
        self.assertTrue(self.l1, self.l3)

    def test_intersection(self):
        intersection = self.l2.intersection(self.l3)
        self.assertEqual(intersection, Vector2D(0.5, 0.5))

if __name__ == '__main__':
    unittest.main()
