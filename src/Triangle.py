from src.Figure import Figure


class Triangle(Figure):

    def __init__(self, a, b, c):
        if ((a < b + c) and (b < a + c) and
                (c < b + a) and a > 0 and b > 0 and c > 0):
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError

    @property
    def area(self):
        p = (self.a + self.b + self.c) / 2
        s = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return s

    @property
    def perimeter(self):
        return self.a + self.b + self.c
