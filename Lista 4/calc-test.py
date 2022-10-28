import unittest
import calc


class MyTestCase(unittest.TestCase):
    def test_division_by_0(self):
        dividend = 1
        divisor = 0
        # Must raise ValueError
        self.assertRaises(ValueError, calc.divide, dividend, divisor)


if __name__ == "__main__":
    unittest.main(verbosity=2)
