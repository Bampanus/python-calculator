import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Test cases for add()
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)  # Changed to 2 and 3
        self.assertEqual(self.calc.add(-2, -3), -5)  # Changed to -2 and -3

    # Test cases for subtract()
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(8, 5), 3)  # Changed to 8 and 5
        self.assertEqual(self.calc.subtract(2, 6), -4)  # Changed to 2 and 6

    # Test cases for multiply()
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)  # Changed to 4 and 3
        self.assertEqual(self.calc.multiply(0, 7), 0)  # Changed to 0 and 7

    # Test cases for divide()
    def test_divide(self):
        self.assertEqual(self.calc.divide(12, 4), 3)  # Changed to 12 and 4
        with self.assertRaises(ZeroDivisionError):  # Divide by zero
            self.calc.divide(15, 0)  # Changed to 15 and 0

    # Test cases for modulo()
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(14, 5), 4)  # Changed to 14 and 5
        self.assertEqual(self.calc.modulo(9, 2), 1)  # Changed to 9 and 2
    
if __name__ == '__main__':
    unittest.main()
