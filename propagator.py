class Propagator:
    def __init__(self, *polygons, *rays, iterations=1000):
        self.polygons = polygons
        self.rays = rays
        self.iterations = iterations
        pass