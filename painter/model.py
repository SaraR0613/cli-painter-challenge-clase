# TODO: Add code here
import math


class point:

    def __int__(self, x: float, y: float):
        self.x: float = 0
        self.y: float = 0

class circle:

    def __int__(self, center: point, radius: float):
        self.radius: float = 0

    def area(self)-> float:
        Area= math.pi * self.radius

