class Medium:
    def __init__(self, refractive_index, polygon):
        self.refractiveIndex = refractive_index
        self.polygon = polygon

    def raycast(self, ray, distance=1000):
        return self.polygon.hit_point(ray.line(distance))


class Detector(Medium):

    def __init__(self, refractive_index, polygon):
        super().__init__(refractive_index, polygon)
        self.detections = {}

    def raycast(self, ray, distance=1000):
        hit_point = super().raycast(ray)
        if hit_point is not None:
            self.__count(hit_point, ray)

    def __count(self, hit_point, ray):
        if hit_point not in self.detections.keys():
            self.detections[hit_point] = []

        self.detections[hit_point].append(ray)


class Reflector(Medium):

    def __init__(self, refractive_index, polygon):
        super().__init__(refractive_index, polygon)

    def raycast(self, ray, distance=1000):
        if super().raycast(ray):
            self.__reflect(ray)

    def __reflect(self, ray):
        pass