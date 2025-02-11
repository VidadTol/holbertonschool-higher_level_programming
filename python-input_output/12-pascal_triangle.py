#!/usr/bin/python3
"""
This module defines a function pascal_triangle that
returns a list of lists of integers representing Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            sum_value = triangle
            row.append(sum_value)
