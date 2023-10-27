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
        list = [8, 200, 40, 1000, 20]
        self.assertIsNone(max_integer())
        self.assertEqual(max_integer(list), 1000)

        with self.assertRaises(TypeError):
            max_integer(7)
            max_integer([7, 8, 'o', 77])
            max_integer([9, 3, 5], [4, 5, 5])


if __name__ == '__main__':
    unittest.main()
