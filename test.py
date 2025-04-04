import unittest

from main import Rectangle, Circle, Triangle, Sphere, Cube, ShapeFactory


class TestShapes(unittest.TestCase):

    # Тести для 2D фігур
    def test_rectangle_area(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)

    def test_rectangle_perimeter(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.perimeter(), 18)

    def test_circle_area(self):
        circle = Circle(7)
        self.assertAlmostEqual(circle.area(), 153.93804002589985, places=5)

    def test_circle_perimeter(self):
        circle = Circle(7)
        self.assertAlmostEqual(circle.perimeter(), 43.982297150257104, places=5)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.area(), 6)

    def test_triangle_perimeter(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.perimeter(), 12)

    # Тести для 3D фігур
    def test_sphere_volume(self):
        sphere = Sphere(3)
        self.assertAlmostEqual(sphere.volume(), 113.097335, places=6)

    def test_cube_volume(self):
        cube = Cube(4)
        self.assertEqual(cube.volume(), 64)

    # Тести для фабрики
    def test_create_rectangle(self):
        shape = ShapeFactory.create_shape('rectangle', [4, 5])
        self.assertIsInstance(shape, Rectangle)
        self.assertEqual(shape.area(), 20)
        self.assertEqual(shape.perimeter(), 18)

    def test_create_circle(self):
        shape = ShapeFactory.create_shape('circle', [7])
        self.assertIsInstance(shape, Circle)
        self.assertAlmostEqual(shape.area(), 153.93804002589985, places=5)
        self.assertAlmostEqual(shape.perimeter(), 43.982297150257104, places=5)

    def test_create_triangle(self):
        shape = ShapeFactory.create_shape('triangle', [3, 4, 5])
        self.assertIsInstance(shape, Triangle)
        self.assertEqual(shape.area(), 6)
        self.assertEqual(shape.perimeter(), 12)

    def test_create_sphere(self):
        shape = ShapeFactory.create_shape_3d('sphere', [3])
        self.assertIsInstance(shape, Sphere)
        self.assertAlmostEqual(shape.volume(), 113.097335, places=6)

    def test_create_cube(self):
        shape = ShapeFactory.create_shape_3d('cube', [4])
        self.assertIsInstance(shape, Cube)
        self.assertEqual(shape.volume(), 64)

    # Тести на некоректні вхідні дані
    def test_invalid_shape(self):
        with self.assertRaises(ValueError):
            ShapeFactory.create_shape('rectangle', [4])  # Не вистачає параметрів

        with self.assertRaises(ValueError):
            ShapeFactory.create_shape_3d('sphere', [3, 4])  # Занадто багато параметрів


if __name__ == "__main__":
    unittest.main()
