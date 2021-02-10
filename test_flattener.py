import unittest
from flattener import *


class MyTestCase(unittest.TestCase):

    def test_empty(self):
        test_obj = {}
        expected = {}
        result2 = flatten(test_obj, {})
        self.assertEqual(result2, expected, "Error not expected result")

    def test_flatten(self):
        test_obj = {
            'a': 1,
            'b': True,
            'c': {
                'd': 3,
                'e': "test"
            }
        }
        expected = {"a": 1, "b": True, "c.d": 3, "c.e": "test"}
        result = flatten(test_obj)
        self.assertEqual(result, expected, "Error not expected result")
