from medium import Detector
from ray import Ray
from vector2D import Vector2D
from polygon import Polygon

polygon = Polygon.from_file('square.pol')
ray1 = Ray(Vector2D(1, 0), Vector2D(0, 0.5))
ray2 = Ray(Vector2D(1, 0), Vector2D(0, 0.8))

detector = Detector(1.0, polygon)
detector.raycast(ray1)
detector.raycast(ray1)
detector.raycast(ray2)

from pylab import *

a = linspace(0, 1, 100)

subplot(111)
polygon.plot()

axis([-0.1, 1.1, -0.1, 1.1])

show()