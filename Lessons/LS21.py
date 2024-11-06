import math


class Circle:
    radius: float

    def __init__(self, r):
        self.radius = r

    def area(self) -> float:
        return math.pi * (self.radius**2)


class Rectangle:
    width: float
    height: float

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height
