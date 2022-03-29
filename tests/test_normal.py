import unittest


class NormalTest(unittest.TestCase):
    def test_normal_failure(self):
        self.assertEqual(1, 2)

    @unittest.skip("example")
    def test_skip(self):
        self.assertEqual(1, 2)

    def test_another_failure(self):
        self.assertTrue(False)

    def test_raise(self):
        raise Exception("example")

    def test_sub(self):
        for i in range(0,3):
            with self.subTest(f"i = {i}"):
                self.assertEqual(i % 2, 0)
