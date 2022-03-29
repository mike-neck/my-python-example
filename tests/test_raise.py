import unittest

from example.value import to_value


class RaiseTest(unittest.TestCase):
    def test_raise(self):
        with self.assertRaises(Exception):
            to_value(5)

