from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Triangle(Shape):  # Новый тип фигуры без изменения AreaCalculator
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class AreaCalculator:
    def calculate_area(self, shape: Shape):
        return shape.area()  # Не зависит от конкретного типа фигуры


# Использование
calculator = AreaCalculator()
shapes = [Rectangle(2, 3), Circle(5), Triangle(4, 6)]

for shape in shapes:
    print(f"Area: {calculator.calculate_area(shape)}")