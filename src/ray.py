from line import Line


class Ray:
    def __init__(self, direction, origin, energy=1, phase=0):
        self.direction = direction
        self.origin = origin
        self.energy = energy
        self.phase = phase

    def line(self, distance=1000):
        return Line(self.origin, self.origin + self.direction * distance)

    def __str__(self, *args, **kwargs):
        s = "[direction: " + str(self.direction) + ", "
        s += "origin: " + str(self.origin) + ", "
        s += "energy: " + str(self.energy) + ", "
        s += "phase: " + str(self.phase) + "]"
        return s

    def __repr__(self, *args, **kwargs):
        return self.__str__(*args, **kwargs)


