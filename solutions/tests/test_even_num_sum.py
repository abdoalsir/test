"""
Unit tests for the `sum_of_even_numbers` function.

This module contains a series of test cases to validate the behavior of the
`sum_of_even_numbers` function, including standard, edge, and defensive cases.

Author: OpenAI Assistant
"""

import unittest
from even_num_sum import sum_of_even_numbers

class TestSumOfEvenNumbers(unittest.TestCase):
    """Unit tests for the sum_of_even_numbers function."""

    def test_regular_case(self):
        """It should correctly sum even numbers in a regular list."""
        self.assertEqual(sum_of_even_numbers([1, 2, 3, 4]), 6)

    def test_all_even_numbers(self):
        """It should return the sum when all numbers are even."""
        self.assertEqual(sum_of_even_numbers([2, 4, 6, 8]), 20)

    def test_no_even_numbers(self):
        """It should return 0 when there are no even numbers."""
        self.assertEqual(sum_of_even_numbers([1, 3, 5, 7]), 0)

    def test_mixed_positive_and_negative_numbers(self):
        """It should correctly sum even numbers including negatives."""
        self.assertEqual(sum_of_even_numbers([-2, -4, 3, 5]), -6)

    def test_empty_list(self):
        """It should return 0 for an empty list."""
        self.assertEqual(sum_of_even_numbers([]), 0)

    def test_single_even_number(self):
        """It should return the number itself if the list contains one even number."""
        self.assertEqual(sum_of_even_numbers([2]), 2)

    def test_single_odd_number(self):
        """It should return 0 if the list contains one odd number."""
        self.assertEqual(sum_of_even_numbers([3]), 0)

    def test_non_list_input(self):
        """It should raise TypeError if input is not a list."""
        with self.assertRaises(TypeError):
            sum_of_even_numbers("not a list")

    def test_list_with_non_integer_elements(self):
        """It should raise TypeError if the list contains non-integer elements."""
        with self.assertRaises(TypeError):
            sum_of_even_numbers([1, 2, "three", 4])

if __name__ == "__main__":
    unittest.main()
