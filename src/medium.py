from math import pi

from drawable import Drawable
from matrix2D import Matrix
from ray import Ray


class Medium(Drawable):
    def __init__(self, refractive_index, polygon):
        self.refractiveIndex = refractive_index
        self.polygon = polygon

    def on_hit(self, ray, hit_point):
        pass

    def draw(self, resolution=100):
        self.polygon.draw(resolution)


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
        if alpha > pi:
            alpha -= pi
        reflection_matrix = Matrix.reflection_matrix(alpha)
        new_direction = reflection_matrix.dot(ray.direction)
        return [Ray(new_direction, hit_point, ray.energy, ray.phase)]