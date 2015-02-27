from cmath import pi
import re
from collections import OrderedDict

from drawable import Drawable
from line import Line
from matrix2D import Matrix
from vector2D import Vector2D


class Polygon(Drawable):
    def __init__(self, *points):
        self.points = points
        if self.is_valid() is not True:
            raise Exception("Polygon data is not valid")

    def hit_point(self, line):
        ord_intersections = OrderedDict()
        for i in self.intersections(line):
            ord_intersections.update({line.parametric(i): i})

        if len(ord_intersections) == 0:
            return None

        return ord_intersections.get(sorted(ord_intersections.keys())[0])

    def intersections(self, line):
        intersections = []

        for l in self.lines():
            i = l.intersection(line)
            if i is not None:
                if i.close(line.start) or i.close(line.end):
                    continue
                intersections.append(i)
        return intersections

    def lines(self):
        length = len(self.points)

        for i in range(0, length - 1):
            yield Line(self.points[i], self.points[i + 1])
        yield Line(self.points[length - 1], self.points[0])

    def is_valid(self):
        for l1 in self.lines():
            for l2 in self.lines():
                if l1 == l2:
                    continue
                i = l1.intersection(l2)
                if i is not None and i not in self.points:
                    return False
        return True

    def rotated(self, angle):
        rotation_matrix = Matrix.rotation_matrix(angle)
        points = []
        for p in self.points:
            points.append(rotation_matrix.dot(p))
        return Polygon(*points)

    @staticmethod
    def circle(radius=1, resolution=100):
        points = [Vector2D(radius, 0)]
        rotation_matrix = Matrix.rotation_matrix(2 * pi / resolution)
        for angle in range(1, resolution):
            new_point = rotation_matrix.dot(points[-1])
            points.append(new_point)
        return Polygon(*points)

    @staticmethod
    def from_file(file_path):
        f = None
        points = []

        try:
            f = open(file_path, 'r')
            for line in f:
                values = re.split(r'[ \t]+', line)
                points.append(Vector2D(float(values[0]), float(values[1])))
        except IOError:
            print("Error reading file")
        finally:
            if f:
                f.close()

        return Polygon(*points)

    def __str__(self, *args, **kwargs):
        s = ""
        for p in self.points:
            s += str(p) + "\n"
        return s

    def draw(self, resolution=100):
        from matplotlib.patches import Polygon
        import matplotlib.pyplot as plt

        xs = map(lambda p: p.x, self.points)
        ys = map(lambda p: p.y, self.points)
        poly = Polygon(list(zip(xs, ys)))
        plt.gca().add_patch(poly)


import unittest


class LineTests(unittest.TestCase):
    def setUp(self):
        points = [Vector2D(0, 0), Vector2D(0, 1), Vector2D(1, 1), Vector2D(1, 0)]
        self.p = Polygon(*points)
        self.l1 = Line(Vector2D(-1, 0.5), Vector2D(2, 0.5))
        self.l2 = Line(Vector2D(-1, 2), Vector2D(2, 2))

    def test_hit_test1(self):
        self.assertEqual(self.p.hit_point(self.l1), Vector2D(0, 0.5))

    def test_hit_test2(self):
        self.assertIsNone(self.p.hit_point(self.l2))

    def test_intersection(self):
        intersections = self.p.intersections(self.l1)
        self.assertEqual(intersections[0], Vector2D(0, 0.5))
        self.assertEqual(intersections[1], Vector2D(1, 0.5))


if __name__ == '__main__':
    unittest.main()
