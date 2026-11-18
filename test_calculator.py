import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -7), -12)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(-4, -6), 2)

    ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(10, 4), 40)
        self.assertEqual(mul(5, -6), -30)
        self.assertEqual(mul(-5, -6), 30)
        self.assertEqual(mul(5, 0), 0)
        self.assertNotEqual(mul(5, 1), 0)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(10, 3), 3.33)
        self.assertEqual(div(5, -1), -5)
        self.assertEqual(div(-30, -6), 5)
        self.assertEqual(div(0, 7), 0)
        self.assertNotEqual(div(5, 0), 0)

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):  # 3 assertions
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(3, 27), 3)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    ##########################

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 0), 5)
        self.assertEqual(hypotenuse(-3, 4), 5)
        self.assertEqual(hypotenuse(3, -4), 5)
        self.assertEqual(hypotenuse(-3, -4), 5)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-3)


if __name__ == '__main__':
    unittest.main()
