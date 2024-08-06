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
        Area= math.pi * (self.radius)** 2
        return (Area)
    
    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

    def  _str_ (self):
        circle
        with center at (x, y) and radius r
        return f "{x}{y}{e}"
