from math import sin, cos, pi
from medium import Detector
from propagator import SimplePropagator
from ray import Ray
from vector2D import Vector2D
from polygon import Polygon

polygon1 = Polygon.from_file('square.pol')
polygon2 = Polygon.from_file('test.pol')

detector1 = Detector(1.0, polygon1)
detector2 = Detector(1.0, polygon2)
mediums = [detector1]

ray1 = Ray(direction=Vector2D(0.5, 0.3), origin=Vector2D(-0.5, 0))
ray2 = Ray(direction=Vector2D(0.5, 0.1), origin=Vector2D(-0.5, 0))
propagator = SimplePropagator()

from pylab import *

subplot(111)

axis([-1, 2, -1, 2])

# for i in arange(0, 2 * pi, 0.05):
for i in arange(pi / 2 + 2 * 0.05, (pi / 2) + 0.15, 0.05):
    x = sin(i)
    y = -cos(i)
    ray = Ray(direction=Vector2D(x, y), origin=Vector2D(-0.5, 0))
    l = propagator.propagate(ray, mediums)
    l.draw()

polygon1.draw()
polygon2.draw()
show()