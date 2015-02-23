from math import pi, cos, sin
from ray import Ray
from vector2D import Vector2D


class Medium:
    def __init__(self, refractive_index, polygon):
        self.refractiveIndex = refractive_index
        self.polygon = polygon

    def on_hit(self, ray, hit_point):
        pass


class Detector(Medium):
    def __init__(self, refractive_index, polygon):
        super().__init__(refractive_index, polygon)
        self.detections = {}

    def on_hit(self, ray, hit_point):
        if hit_point not in self.detections.keys():
            self.detections[hit_point] = []

        self.detections[hit_point].append(ray)
        return []


class Reflector(Medium):
    def __init__(self, refractive_index, polygon):
        super().__init__(refractive_index, polygon)

    def on_hit(self, ray, hit_point):
        line = filter(lambda l: l.contains(hit_point), self.polygon.lines()).__next__()
        alpha = line.angle
        beta = ray.line(distance=1).angle
        new_angle = pi / 2 - beta - alpha
        return [Ray(Vector2D(cos(new_angle), sin(new_angle)), hit_point, ray.energy, ray.phase)]