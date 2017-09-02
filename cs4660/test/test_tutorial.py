"""test_tutorial is a testing specs for basic Python stuff"""

import unittest

from tutorial import lists
from tutorial import files

class ListTestCase(unittest.TestCase):
    """ListTestCase defines basic list tests"""

    def setUp(self):
        self.l_1 = [1, 2, 3]
        self.l_2 = [4, 5, 6]
        self.l_3 = [5, 6, 7, 8]

    def test_first_item(self):
        """test_first_item test if the method can correctly return the first item"""
        self.assertEqual(1, lists.get_first_item(self.l_1))
        self.assertEqual(4, lists.get_first_item(self.l_2))

    def test_last_item(self):
        """test retrieving last item"""
        self.assertEqual(3, lists.get_last_item(self.l_1))
        self.assertEqual(6, lists.get_last_item(self.l_2))

    def test_second_and_third_item(self):
        """test retrieving sublist"""
        self.assertEqual([2, 3], lists.get_second_and_third_items(self.l_1))
        self.assertEqual([6, 7], lists.get_second_and_third_items(self.l_3))

    def test_get_sum(self):
        """test to get sum of number list"""
        self.assertEqual(6, lists.get_sum(self.l_1))
        self.assertEqual(15, lists.get_sum(self.l_2))

    def test_get_avg(self):
        """test to get average of the number list"""
        self.assertEqual(2, lists.get_avg(self.l_1))
        self.assertEqual(5, lists.get_avg(self.l_2))

class SimpleFileTestCase(unittest.TestCase):
    """SimplefileTestCase tests the file read implementation"""

    def setUp(self):
        file_path = './test/fixtures/array.txt'
        self.simple_file = files.SimpleFile(file_path)

    def test_mean(self):
        """test_mean tests to see if file can get mean properly"""
        self.assertEqual(4.125, self.simple_file.get_mean(0))

    def test_max(self):
        """test_max tests to see if the file can retrieve max value"""
        self.assertEqual(9, self.simple_file.get_max(3))

    def test_min(self):
        """test_min tests to see if the file can retrieve min value"""
        self.assertEqual(-5, self.simple_file.get_min(4))

    def test_sum(self):
        """test_sum tests to see if the file can retrieve sum value"""
        self.assertEqual(36, self.simple_file.get_sum(1))
