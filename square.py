import unittest


def area(a):
    '''Принимает десятичное число a, возвращает площадь квадрата со стороной a'''
    return a * a


def perimeter(a):
    '''Принимает десятичное число a, возвращает периметр квадрата со стороной a'''
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        self.assertEqual(area(0), 0)
    def test_one_area(self):
        self.assertEqual(area(1), 1)
    def test_float_area(self):
        self.assertAlmostEqual(area(123.654), 15290.311716)
    def test_random_area(self):
        self.assertEqual(area(123654), 15290311716)

    def test_zero_perimeter(self):
        self.assertEqual(perimeter(0), 0)
    def test_one_perimeter(self):
        self.assertEqual(perimeter(1), 4)
    def test_float_perimeter(self):
        self.assertAlmostEqual(perimeter(123.654), 494.616)
    def test_random_perimeter(self):
        self.assertEqual(perimeter(123654), 494616)

