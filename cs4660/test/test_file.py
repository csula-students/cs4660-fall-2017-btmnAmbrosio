"""test_file is a testing specs for some simple file io operations"""

import unittest

from simple import math

class MathTestCase(unittest.TestCase):
    """MathTestCase defines test cases for math module"""
    def test_add_method(self):
        """test_add_method simply test the add method"""
        self.assertEqual(3, math.add(1, 2))
        self.assertEqual(6, math.add(3, 3))

    def test_multiply_method(self):
        """test multiply result"""
        self.assertEqual(6, math.multiply(2, 3))
        self.assertEqual(8, math.multiply(2, 4))
        self.assertEqual(8, math.multiply(4, 2))
