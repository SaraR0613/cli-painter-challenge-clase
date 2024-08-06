# TODO: Add code here
import math
import matplotlib.pyplot as plt
import pickle


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
        area: 1/2


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

    def __int__(self,point_1:point, point_2:point):
        self.point_1: point = point_1
        self.point_2: point = point_2

    def area(self)-> float:
        area: 00

    def draw(self):
        x = [self.point_1.x, self.point_2.x, self.point_2.x, self.point_1.x, self.point_1.x]
        y = [self.point_1.y, self.point_1.y, self.point_2.y, self.point_2.y, self.point_1.y]
        plt.fill(x, y, color='g')
        plt.axis("scaled")
        plt.show()

    def _str_(self):
        return f"Rectangle with vertices at {self.point_1.x}, {self.point_1.y}  and {self.point_2.x}, {self.point_2.y}"


class painter:

    FILE = ".painter"

    def __init__(self) -> None:
        self.shapes: list = []
        self._load()

    def _load(self) -> None:
        try:
            with open(painter.FILE, "rb") as f:
                self.shapes = pickle.load(f)
        except (EOFError, FileNotFoundError):
            self.shapes = []

    def _save(self) -> None:
        with open(painter.FILE, "wb") as f:
            pickle.dump(self.shapes, f)

    def add_shape(self, shape) -> None:
        self.shapes.append(shape)
        self._save()

    def total_area(self) -> float:
        return sum(shape.area() for shape in self.shapes)

    def clear(self) -> None:
        self.shapes = []
        self._save()