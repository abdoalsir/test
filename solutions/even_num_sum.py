"""
Module to compute the sum of all even numbers in a list.

This module provides a function `sum_of_even_numbers` that takes a list of integers
and returns the sum of all even numbers in the list. The implementation ensures that
defensive assertions are in place to handle invalid inputs.

Example usage:
    >>> sum_of_even_numbers([1, 2, 3, 4])
    6
    >>> sum_of_even_numbers([-2, 5, 7, 8])
    6
"""

def sum_of_even_numbers(numbers: list[int]) -> int:
    """
    Calculate the sum of all even numbers in a list.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        int: The sum of all even numbers in the list.

    Raises:
        TypeError: If `numbers` is not a list or contains non-integer elements.

    Example:
        >>> sum_of_even_numbers([2, 4, 6])
        12
        >>> sum_of_even_numbers([1, 3, 5])
        0
        >>> sum_of_even_numbers([])
        0
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements in the list must be integers")

    # Strategy: Iterate through the list and sum up even numbers
    even_sum = sum(num for num in numbers if num % 2 == 0)
    return even_sum

print(sum_of_even_numbers([1, 2, 3, 4]))