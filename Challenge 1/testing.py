import unittest

from rod_conversion import *


class MyFirstTests(unittest.TestCase):

    def test_metres(self):
        self.assertEqual(metres(1), 5.0292)

    def test_furlong(self):
        self.assertEqual(furlong(10), 0.25)

if __name__ == '__main__':
    unittest.main()
