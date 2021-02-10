import unittest
from flattener import *


class MyTestCase(unittest.TestCase):
    def test_empty(self):
        test_obj = {}
        expected = {}
        result = flatten(test_obj)
        self.assertEqual(result, expected, "Error not expected result")

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

        test_obj = {
            'a': 1,
            'b': True,
            'k': 10,
            'c': {
                'd': 3,
                'e': "test"
            },
            'l': 25
        }
        expected = {"a": 1, "b": True, "k": 10, "c.d": 3, "c.e": "test", "l": 25}
        result = flatten(test_obj)
        self.assertEqual(result, expected, "Error not expected result")

    def test_flatten_nesting(self):
        test_obj = {
            "a": 1,
            "b": True,
            "c": {
                "d": 3,
                "e": "T",
                "f": {
                    "g": {
                        "h": {
                            "i": 4,
                            "j": 10,
                            "k": 6
                        }
                    }
                }
            }
        }
        expected = {"a": 1, "b": True, "c.d": 3, "c.e": "T", "c.f.g.h.i": 4, "c.f.g.h.j": 10, "c.f.g.h.k": 6}
        result = flatten(test_obj)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
