import math
import unittest
import calc


class MyTestCase(unittest.TestCase):
    def test_division_by_0(self):
        dividend = 1
        divisor = 0
        # Must raise ValueError
        self.assertRaises(ValueError, calc.divide, dividend, divisor)

    def test_two_plus_two(self):
        a = 2
        b = 2
        result = calc.add(a, b)
        # Two plus two must make four
        self.assertEqual(result, 4)

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
