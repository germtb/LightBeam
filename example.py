from math import pi
from matplotlib.pyplot import subplot, axis, show
from numpy import arange
import sys

from medium import Reflector, Detector
from propagator import SimplePropagator
import polygon
from ray import Ray
from vector2D import Vector2D
sys.setrecursionlimit(1001)



subplot(111)
axis([-3, 3, -3, 3])

detector = Detector(1.0, polygon.Polygon.circle(1.1, resolution=100))
detector.draw()
mediums = [detector]
base_polygon = polygon.Polygon.from_file('shapes/lobster_eye.pol')

for angle in arange(0, 2 * pi, 0.05):
    p = base_polygon.rotated(angle)
    p.draw()
    mediums.append(Reflector(1.0, p))

propagator = SimplePropagator()
for y in arange(-3, 3, 0.04):
    ray = Ray(direction=Vector2D(1, -1), origin=Vector2D(-3, y + 3))
    propagator.propagate(ray, mediums, distance=100)

show()
