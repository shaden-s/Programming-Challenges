import unittest

from n99_trick import *


class MyFirstTests(unittest.TestCase):

    def test_minusnine(self):
        self.assertEqual(minusnine(45), 54)

    def test_furlong(self):
        self.assertEqual(result(54, 60), 45)

if __name__ == '__main__':
    unittest.main()
