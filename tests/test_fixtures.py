import unittest


class Fixtures(unittest.TestCase):
    def setUp(self) -> None:
        raise Exception("example")

    def test_not_failure(self):
        self.assertEqual(1, 1)

    def test_another(self):
        self.assertEqual(1, 1)
