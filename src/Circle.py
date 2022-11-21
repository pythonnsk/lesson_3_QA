import math

from src.Figure import Figure


class Circle(Figure):

    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius should be > 0")
        else:
            self.radius = radius

    @property
    def area(self):
        return (self.radius ** 2) * math.pi

    @property
    def perimeter(self):
        return 2 * (self.radius * math.pi)
