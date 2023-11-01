#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests edge cases for the function max_integer
    """

    def test_max_integer(self):
        """ This is the test function
        """
        self.assertEqual(max_integer([8, 200, 40, 1000, 20]), 1000)

    def test_none_args(self):
        """Tests for no arguments"""
        self.assertIsNone(max_integer())

    def test_none_list_args(self):
        """Tests if argument is a list"""
        with self.assertRaises(TypeError):
            max_integer(7)

    def test_list_not_homogenous(self):
        """Test if all elements in list are integers"""
        with self.assertRaises(TypeError):
            max_integer([7, 8, 'o', 77])

    def test_list_not_homog(self):
        """Test if all elements in lists"""
        with self.assertRaises(TypeError):
            max_integer([9, 3, 5], [4, 5, 5])

if __name__ == '__main__':
    unittest.main()
