from line import Line


class Propagator:
    def __init__(self):
        pass

    def propagate(self, ray, mediums, distance=1000):
        pass


class SimplePropagator(Propagator):
    def propagate(self, ray, mediums, distance=1000, accumulator=0):
        if accumulator > 100:
            return

        line = ray.line(1000)
        hit_points = []

        for m in mediums:
            hit_point = m.polygon.hit_point(line)
            if hit_point is not None:
                hit_points.append(hit_point)
                for r in m.on_hit(ray, hit_point):
                    accumulator += 1
                    self.propagate(r, mediums, distance, accumulator)

        if len(hit_points) == 0:
            l = Line(ray.origin, ray.direction * 1000)
            l.draw()
        else:
            hit_point = min(hit_points, key=lambda poly: line.parametric(poly))
            l = Line(ray.origin, hit_point)
            l.draw()