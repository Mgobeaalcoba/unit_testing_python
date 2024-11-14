import unittest
from unit_testing_python.calculator import Calculator


class CalculatorTests(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(Calculator.add(1, 1), 2)
        self.assertEqual(Calculator.add(1, -1), 0)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(1, 1), 0)
        self.assertEqual(Calculator.subtract(1, -1), 2)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(1, 1), 1)
        self.assertEqual(Calculator.multiply(1, -1), -1)

    def test_divide(self):
        self.assertEqual(Calculator.divide(1, 1), 1)
        self.assertEqual(Calculator.divide(1, -1), -1)
        self.assertEqual(Calculator.divide(1, 0), 0)

