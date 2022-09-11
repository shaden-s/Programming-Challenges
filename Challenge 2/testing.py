import unittest

from richter.py import *


class MyFirstTests(unittest.TestCase):

    def test_energy(self):
        self.assertEqual(energy(1), 1995262.3149688789)

    def test_tnt(self):
        self.assertEqual(tnt(10), 15080242458.895658)

if __name__ == '__main__':
    unittest.main()
