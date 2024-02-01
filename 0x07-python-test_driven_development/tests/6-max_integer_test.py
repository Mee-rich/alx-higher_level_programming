#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function"""

    def test_normal(self):
        "Test with a normal list of ints: should return the max result"""

        x = [1, 2, 3, 4, 5, 6]
        result = max_integer(x)
        self.assertEqual(result, 6)

    def test_not_int(self):
        """Test with a mixed datatype: raise a TypeError exception"""
        x = ['d', 'a', 3, '5']
        self.assertRaises(TypeError, max_integer, x)

    def test_empty(self):
        """Test with an empty list: should return None"""
        x = []
        result = max_integer(x)
        self.assertEqual(result, None)

    def test_negative(self):
        """Test with a list of negative values: shoulf return the max"""
        x = [-3, -5, -10]
        result = max_integer(x)
        self.assertEqual(result, -3)

    def test_float(self):
        """Test with a list of mixed ints and floats: return the max"""
        x = [3.2, 4, 1.2, 5]
        result = max_integer(x)
        self.assertEqual(result, 5)

    def test_not_list(self):
        """Test with a parameter that is not a list"""
        self.assertRaises(TypeError, max_integer, 9)

    def test_unique(self):
        """Test with a list of one int: should return the int"""
        x = [30]
        result = max_integer(x)
        self.assertEqual(result, 30)

    def test_identical(self):
        """Test with a list of identical values: return the value"""
        x = [6, 6, 6, 6]
        result = max_integer(x)
        self.assertEqual(result, 6)

    def test_max_in_the_middle(self):
        """ Test when the max number is in the middle of the list"""
        x = [1, 3, 4, 17, 10, 4, 2]
        result = max_integer(x)
        self.assertEqual(result, 17)

    def test_strings(self):
        """Test with a list of strings: should return the first string"""
        x = ["hi", "hello"]
        result = max_integer(x)
        self.assertEqual(result, "hi")

    def test_none(self):
        """Test with a Noe as parameter:should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)

    if __name__ == '__main__':
        unittest.main()
