import csv
import math
from typing import List, Tuple


class Shape:
    def area(self) -> float:
        raise NotImplementedError

    def perimeter(self) -> float:
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
        self.s = (a + b + c) / 2  # Semi-perimeter

    def area(self) -> float:
        return math.sqrt(self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c))

    def perimeter(self) -> float:
        return self.a + self.b + self.c


class Shape3D:
    def volume(self) -> float:
        raise NotImplementedError


class Sphere(Shape3D):
    def __init__(self, radius: float):
        self.radius = radius

    def volume(self) -> float:
        return (4/3) * math.pi * self.radius**3


class Cube(Shape3D):
    def __init__(self, side: float):
        self.side = side

    def volume(self) -> float:
        return self.side**3


class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str, parameters: List[float]) -> Shape:
        if shape_type == 'rectangle' and len(parameters) == 2:
            return Rectangle(*parameters)
        elif shape_type == 'circle' and len(parameters) == 1:
            return Circle(parameters[0])
        elif shape_type == 'triangle' and len(parameters) == 3:
            return Triangle(*parameters)
        else:
            raise ValueError(f"Unsupported shape or incorrect parameters: {shape_type} {parameters}")



def read_shapes_from_csv(file_path: str) -> List[Tuple[str, List[float]]]:
    shapes = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            shape_type = row[0].lower()
            parameters = [float(p) for p in row[1:] if p.strip()]
            shapes.append((shape_type, parameters))
    return shapes


def process_shapes(file_path: str):
    shapes = read_shapes_from_csv(file_path)
    for shape_type, params in shapes:
        try:
            if shape_type in ['rectangle', 'circle', 'triangle']:
                shape = ShapeFactory.create_shape(shape_type, params)
                print(f"Фігура: {shape_type.capitalize()} | Параметри: {params} | Площа: {shape.area():.2f} | Периметр: {shape.perimeter():.2f}")
        except ValueError as e:
            print(f"Помилка: {e}")


if __name__ == "__main__":
    process_shapes("shapes.csv")
