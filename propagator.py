from collections import OrderedDict
from line import Line


class Propagator:
    def __init__(self):
        pass

    def propagate(self, ray, mediums, distance=100):
        pass


class SimplePropagator(Propagator):
    def __propagate(self, ray, mediums, distance=100, accumulator=0):
        if accumulator > 1000:
            raise Exception("Too many iterations")

        line = ray.line(distance)
        hit_points = []

        for m in mediums:
            hit_point = m.polygon.hit_point(line)
            if hit_point is not None:
                hit_points.append(hit_point)
                for r in m.on_hit(ray, hit_point):
                    accumulator += 1
                    self.propagate(r, mediums, distance, accumulator)

        if len(hit_points) == 0:
            l = Line(ray.origin, ray.direction * distance)
            l.draw()
        else:
            hit_point = min(hit_points, key=lambda poly: line.parametric(poly))
            l = Line(ray.origin, hit_point)
            l.draw()

    def propagate(self, ray, mediums, distance=100, accumulator=0):
        if accumulator > 1000:
            return
        line = ray.line(distance)
        hit_points = OrderedDict()

        for m in mediums:
            hit_point = m.polygon.hit_point(line)
            if hit_point is not None:
                hit_points.update({hit_point: m})

        if len(hit_points) == 0:
            l = Line(ray.origin, ray.origin + ray.direction * distance)
            l.draw()
        else:
            hit_point = min(hit_points.keys(), key=lambda poly: line.parametric(poly))
            m = hit_points[hit_point]
            for r in m.on_hit(ray, hit_point):
                    accumulator += 1
                    self.propagate(r, mediums, distance, accumulator)
            l = Line(ray.origin, hit_point)
            l.draw()

