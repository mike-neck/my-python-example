import unittest

from example.value import Value, FizzBuzzValue, to_value


class ValueTest(unittest.TestCase):
    def test_something(self):
        value = to_value(10)
        self.assertEqual(value.text, None)
        self.assertEqual(value.original, 10)

    def test_complete(self):
        value = Value(10, "foo")
        self.assertEqual(value.original, 10)
        self.assertEqual(value.text, "foo")

    def test_str_original(self):
        value = to_value(2)
        self.assertEqual(f"{value}", "2")
        self.assertEqual(value.fizz_buzz_value(), "2")

    def test_str_text(self):
        value = Value(5, "bar")
        self.assertEqual(f"{value}", "bar")
        self.assertEqual(value.fizz_buzz_value(), "bar")


class FizzBuzzValueTest(unittest.TestCase):
    def test_str(self):
        fb_value = FizzBuzzValue("foo")
        self.assertEqual(fb_value, "foo")
