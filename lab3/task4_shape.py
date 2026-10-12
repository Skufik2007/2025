# Задание 4. Класс «Фигура» (площадь, периметр)
import math


class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r


shapes = [Rectangle(3, 4), Circle(3)]
for shape in shapes:
    print(type(shape).__name__, "площадь:", round(shape.area(), 2),
          "периметр:", round(shape.perimeter(), 2))
