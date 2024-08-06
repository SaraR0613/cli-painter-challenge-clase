# TODO: Add code here
import math
import matplotlib.pyplot as plt

class point:

    def __int__(self, x: float, y: float):
        self.x: float = 0
        self.y: float = 0

class circle:

    def __int__(self, center: point, radius: float):
        self.radius: float = radius
        self.center: point = center

    def area(self)-> float:
        Area= math.pi * (self.radius) ** 2
        return (Area)
    
    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

    def _str_ (self):
        circle
        return f" with center at {self.x} {self.y} and radius {self.radius}"

class triangle:

    def __int__(self, point_1: point, point_2: point, point_3: point):
        self.point_1: point = point_1
        self.point_2: point = point_2
        self.point_3: point = point_3

    def area(self)->float:
        area: 1/2 ()


    def draw(self):
        x = [self.point_1.x, self.point_2.x, self.point_3.x, self.point_1.x]
        y = [self.point_1.y, self.point_2.y, self.point_3.y, self.point_1.y]
        plt.fill(x, y, color='b')
        plt.axis("scaled")
        plt.show()

    def _str_(self):
        triangle
        return f"with vertices at {self.point_1.x}, {self.point_1.y}, {self.point_2.x}, {self.point_2.y} and {self.point_3.x}, {self.point_3.y}"


class rectangle:

    def __int__(self, ):


