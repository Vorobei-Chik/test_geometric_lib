import unittest


def area(a, b):
    '''Принимает два десятичных числа a и b, возвращает площадь прямоугольника со сторонами a и b'''
    return a * b


def perimeter(a, b):
    '''Принимает два десятичных числа a и b, возвращает периметр прямоугольника со сторонами a и b'''
    return (a + b) * 2


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        self.assertEqual(area(0, 0), 0)
    def test_one_area(self):
        self.assertEqual(area(1, 1), 1)
    def test_float_area(self):
        self.assertAlmostEqual(area(1.2, 3.4), 4.08)
    def test_square_area(self):
        self.assertEqual(area(8, 8), 64)
    def test_random_area(self):
        self.assertEqual(area(123, 654), 80442)

    def test_zero_perimeter(self):
        self.assertEqual(perimeter(0, 0), 0)
    def test_one_perimeter(self):
        self.assertEqual(perimeter(1, 1), 4)
    def test_float_perimeter(self):
        self.assertAlmostEqual(perimeter(123.654, 456.987), 1161.282)
    def test_square_perimeter(self):
        self.assertEqual(perimeter(8, 8), 32)
    def test_random_perimeter(self):
        self.assertEqual(perimeter(123654, 456987), 1161282)

