import unittest


def area(a, h):
    '''Принимает два десятичных числа a и h, возвращает площадь трегольника со стороной a и высотой h проведённой к стороне a'''
    return a * h / 2


def perimeter(a, b, c):
    '''Принимает три десятичных числа a, b и c, возвращает периметр треугольника со сторонами a, b и с'''
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        self.assertEqual(area(0, 0), 0)
    def test_one_area(self):
        self.assertEqual(area(1, 1), 0.5)
    def test_float_area(self):
        self.assertAlmostEqual(area(123.654, 456.987), 28254.135249)
    def test_random_area(self):
        self.assertEqual(area(123654, 456987), 28254135249)

    def test_zero_perimeter(self):
        self.assertEqual(perimeter(0, 0, 0), 0)
    def test_one_perimeter(self):
        self.assertEqual(perimeter(1, 1, 1), 3)
    def test_float_perimeter(self):
        self.assertAlmostEqual(perimeter(123.654, 456.987, 789.321), 1369.962)
    def test_random_perimeter(self):
        self.assertEqual(perimeter(123654, 456987, 789321), 1369962)

