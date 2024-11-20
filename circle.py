import math
import unittest


def area(r):
    '''Принимает десятичное число r, возвращает площадь круга радиуса r'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает десятичное число r, возвращает периметр круга радиуса r'''
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        self.assertEqual(area(0), 0)
    def test_one_area(self):
        self.assertEqual(area(1), math.pi)
    def test_float_area(self):
        self.assertAlmostEqual(area(123.654), 15290.311716 * math.pi)
    def test_random_area(self):
        self.assertEqual(area(123654), 15290311716 * math.pi)

    def test_zero_perimeter(self):
        self.assertEqual(perimeter(0), 0)
    def test_one_perimeter(self):
        self.assertEqual(perimeter(1), 2 * math.pi)
    def test_float_perimeter(self):
        self.assertAlmostEqual(perimeter(123.654), 247.308 * math.pi)
    def test_random_perimeter(self):
        self.assertEqual(perimeter(123654), 247308 * math.pi)

