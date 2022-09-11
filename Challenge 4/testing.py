import unittest

from wind_chill import *


class MyFirstTests(unittest.TestCase):

    def test_windchill(self):
        self.assertEqual(calculatewindchill(10,15), -6.5895344209562525)

    def test_windchill2(self):
        self.assertEqual(calculatewindchill(0, 25), -24.093780999553864)

if __name__ == '__main__':
    unittest.main()
