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


if __name__ == "__main__":
    unittest.main(verbosity=2)
