#!/usr/bin/python3

import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_middle(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    
    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

    def test_max_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_max(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_max_empty(self):
        self.assertEqual(max_integer([]), None)
    
if __name__ == '__main__':
    unittest.main()
