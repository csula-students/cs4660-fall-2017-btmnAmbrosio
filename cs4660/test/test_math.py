import unittest

from math import math

class MathTestCase(unittest.TestCase):
    def test_add_method(self):
        self.assertEqual(3, math.add(1, 2))

