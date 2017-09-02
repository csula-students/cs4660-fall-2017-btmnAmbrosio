"""test_tutorial is a testing specs for basic Python stuff"""

import unittest

from tutorial import lists

class ListTestCase(unittest.TestCase):
    """ListTestCase defines basic list tests"""
    def test_first_item(self):
        """test_first_item test if the method can correctly return the first item"""
        l_1 = [1, 2, 3]
        self.assertEqual(1, lists.get_first_item(l_1))
        l_2 = [4, 5, 6]
        self.assertEqual(4, lists.get_first_item(l_2))

    def test_last_item(self):
        """test retrieving last item"""
        l_1 = [1, 2, 3]
        self.assertEqual(3, lists.get_last_item(l_1))
        l_2 = [4, 5, 6]
        self.assertEqual(6, lists.get_last_item(l_2))

    def test_second_and_third_item(self):
        """test retrieving sublist"""
        l_1 = [1, 2, 3]
        self.assertEqual([2, 3], lists.get_second_and_third_items(l_1))
        l_2 = [5, 6, 7, 8]
        self.assertEqual([6, 7], lists.get_second_and_third_items(l_2))

    def test_get_sum(self):
        """test to get sum of number list"""
        l_1 = [1, 2, 3]
        self.assertEqual(6, lists.get_sum(l_1))
        l_2 = [5, 6, 7]
        self.assertEqual(18, lists.get_sum(l_2))

    def test_get_avg(self):
        """test to get average of the number list"""
        l_1 = [1, 2, 3]
        self.assertEqual(2, lists.get_avg(l_1))
        l_2 = [5, 6, 7]
        self.assertEqual(6, lists.get_avg(l_2))
