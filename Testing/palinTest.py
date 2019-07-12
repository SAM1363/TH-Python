import unittest

from palindrome import is_palindrome

class PalindromeTestCase(unittest.TestCase):
    def test_ok_palin(self):
        self.assertTrue(is_palindrome('dad'))

    def test_bad_plain(self):
        self.assertFalse(is_palindrome('vndzkvnoibsnz'))