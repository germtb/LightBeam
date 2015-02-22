from line import Line


class Propagator:
    def __init__(self):
        pass

    def propagate(self, ray, mediums, distance=1000):
        pass


class SimplePropagator(Propagator):
    def propagate(self, ray, mediums, distance=1000):
        line = ray.line(1000)
        hit_points = []
        for m in mediums:
            hit_point = m.polygon.hit_point(line)
            if hit_point is not None:
                hit_points.append(hit_point)



                # for r in m.on_hit(ray, hit_point):
                #   self.propagate(r, mediums, distance)

        if len(hit_points) is 0:
            return Line(ray.origin, ray.direction * 1000)

        hit_point = min(hit_points, key=lambda poly: line.parametric(poly))
        return Line(ray.origin, hit_point)