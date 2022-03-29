from unittest import TestCase

from example.rule import fizz_rule, buzz_rule
from example.value import to_value, Value


class FizzRuleTest(TestCase):
    def test_fizz_rule_on_3(self):
        value = fizz_rule(to_value(3))
        self.assertEqual(value, Value(3, "Fizz"))

    def test_fizz_rule_on_5(self):
        value = fizz_rule(to_value(5))
        self.assertEqual(value, to_value(5))

    def test_fizz_rul_on_pre(self):
        value = fizz_rule(Value(9, "foo"))
        expected = Value(9, "fooFizz")
        self.assertEqual(value, expected, f"{value} to be {expected}")


class BuzzRuleTest(TestCase):
    def test_on_5(self):
        value = buzz_rule(to_value(5))
        self.assertEqual(value, Value(5, "Buzz"))

    def test_on_3(self):
        value = buzz_rule(to_value(3))
        self.assertEqual(value, to_value(3))

    def test_on_pre(self):
        value = buzz_rule(Value(30, "Fizz"))
        self.assertEqual(value, Value(30, "FizzBuzz"))
