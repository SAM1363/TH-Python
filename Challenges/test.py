import unittest

class SimpleTestCase(unittest.TestCase):
    def test_add(self):
        assert 10 + 10 == 20