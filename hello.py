from math import sin, cos, pi
from medium import Detector, Reflector
from propagator import SimplePropagator
from ray import Ray
from vector2D import Vector2D
from polygon import Polygon

polygon1 = Polygon.from_file('square.pol')
polygon2 = Polygon.from_file('test1.pol')
polygon3 = Polygon.from_file('test2.pol')

detector1 = Reflector(1.0, polygon1)
detector2 = Detector(1.0, polygon2)
detector3 = Detector(1.0, polygon3)
mediums = [detector1, detector2]

ray1 = Ray(direction=Vector2D(0.5, 0.3), origin=Vector2D(-0.5, 0))
ray2 = Ray(direction=Vector2D(0.5, 0.1), origin=Vector2D(-0.5, 0))
propagator = SimplePropagator()

from pylab import *

subplot(111)

axis([-1, 2, -1, 2])

for i in arange(0.2, pi / 6, 0.01):
    x = cos(i)
    y = sin(i)
    ray = Ray(direction=Vector2D(x, y), origin=Vector2D(-0.5, 0.3))
    propagator.propagate(ray, mediums, distance=5)

polygon1.draw()
polygon2.draw()
polygon3.draw()
show()