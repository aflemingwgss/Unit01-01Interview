# test_factorial.py

import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial_of_zero(self):
        """Test that the factorial of 0 is 1."""
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_one(self):
        """Test that the factorial of 1 is 1."""
        self.assertEqual(factorial(1), 1)

    def test_factorial_of_positive_integers(self):
        """Test that the factorial of positive integers is calculated correctly."""
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_negative_input(self):
        """Test that the factorial function raises an exception for negative input."""
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_non_integer_input(self):
        """Test that the factorial function raises an exception for non-integer input."""
        with self.assertRaises(TypeError):
            factorial(3.5)
        with self.assertRaises(TypeError):
            factorial("string")

if __name__ == "__main__":
    unittest.main()

