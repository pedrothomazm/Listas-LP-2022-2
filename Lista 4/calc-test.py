import math
import unittest

import calc


class MyTestCase(unittest.TestCase):
    def test_division_by_0(self):
        dividend = 1
        divisor = 0
        # Must raise ValueError
        with self.assertRaises(ValueError):
            calc.divide(dividend, divisor)
    
    def test_two_divided_by_two(self):
        dividend = 2
        divisor = 2
        result = calc.divide(dividend, divisor)
        # 2 / 2 = 1
        self.assertEqual(result, 1)
    
    def test_one_divided_by_half(self):
        dividend = 1
        divisor = 0.5
        result = calc.divide(dividend, divisor)
        # 1 / 0.5 = 2
        self.assertEqual(result, 2)

    def test_two_plus_two(self):
        a = 2
        b = 2
        result = calc.add(a, b)
        # Two plus two must make four
        self.assertEqual(result, 4)

    def test_negative_plus_negative(self):
        a = -2
        b = -1
        result = calc.add(a, b)
        # -2 + (-1) = -3
        self.assertEqual(result, -3)

    def test_positive_plus_negative(self):
        a = 3
        b = -2
        result = calc.add(a, b)
        # 3 + (-2) = 1
        self.assertEqual(result, 1)
    
    def test_subtract_positive_positive(self):
        a = 4
        b = 2
        result = calc.subtract(a, b)
        # 4 - 2 = 2
        self.assertEqual(result, 2)
    
    def test_subtract_positive_negative(self):
        a = 3
        b = -3
        result = calc.subtract(a, b)
        # 3 - (-3) = 6
        self.assertEqual(result, 6)
    
    def test_subtract_negative_negative(self):
        a = -2
        b = -5
        result = calc.subtract(a, b)
        # -2 - (-5) = 3
        self.assertEqual(result, 3)

    def test_exp_of_sqr_root(self):
        number = 2

        sqr_root_exp = 1 / 2
        sqr_root = calc.exp(sqr_root_exp, number)

        sqr_exp = 2
        sqr_of_sqr_root = calc.exp(sqr_exp, sqr_root)

        # sqr_root must be the square root of the original number
        self.assertAlmostEqual(sqr_root, math.sqrt(number))

        # The square of the square root must be the original number
        self.assertAlmostEqual(sqr_of_sqr_root, number)


if __name__ == "__main__":
    unittest.main(verbosity=2)
