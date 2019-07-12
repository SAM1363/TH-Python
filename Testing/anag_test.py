import unittest

from anagrams import get_anagrams


class AnagramTests(unittest.TestCase):
    def test_in_anagrams(self):
        self.assertIn('house', get_anagrams('treehouses'))