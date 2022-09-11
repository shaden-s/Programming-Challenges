import unittest

from o196 import *


class MyFirstTests(unittest.TestCase):

    def test_generate(self):
        self.assertEqual(palindrome(121), True)
        self.assertEqual(palindrome(123), False)
    
    def test_reverse(self):
        self.assertEqual(revadd(56), 121)

if __name__ == '__main__':
    unittest.main()
