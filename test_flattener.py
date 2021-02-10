import unittest
from flattener import *


class MyTestCase(unittest.TestCase):
    # test an empty json file, should return an empty file
    def test_empty(self):
        test_obj = {}
        expected = {}
        result = flatten(test_obj)
        self.assertEqual(result, expected, "Error not expected result")

    # test the sample json given
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

        # testing sample json with a new key-value pair
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

    # test jsons with a lot of nesting
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
                            "j": {
                                "k": {
                                    "L": "Dog"
                                }
                            },
                            "m": 6
                        }
                    }
                }
            }
        }
        expected = {'a': 1, 'b': True, 'c.d': 3, 'c.e': 'T', 'c.f.g.h.i': 4, 'c.f.g.h.j.k.L': 'Dog', 'c.f.g.h.m': 6}
        result = flatten(test_obj)
        self.assertEqual(result, expected)

    # test a json that is already flat
    def test_already_flat(self):
        test_obj = {
            'a': 1,
            'b': True,
            'c': 3,
            'd': "test",
        }
        expected = {'a': 1, 'b': True, 'c': 3, 'd': "test"}
        result = flatten(test_obj)
        self.assertEqual(result, expected, "Error not expected result")

    # test a json with a duplicate key
    # Not sure if this is the desired behaviour but it was not specified so I chose to implement it this way
    def test_duplicate_key(self):
        test_obj = {
            'a': 1,
            'b': True,
            'c': {
                'd': 3,
                'e': "test"
            },
            'a': 3
        }
        expected = {"b": True, "c.d": 3, "c.e": "test", "a": 3}
        result = flatten(test_obj)
        self.assertEqual(result, expected, "Error not expected result")


if __name__ == '__main__':
    unittest.main()
