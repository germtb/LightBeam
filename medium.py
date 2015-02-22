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
        line = filter(lambda l: l.contains(hit_point), self.polygon.lines())
        pass