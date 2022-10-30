import unittest

from richter.py import *


class MyFirstTests(unittest.TestCase):

    def test_energy(self):
        self.assertEqual(energy(1), 1995262.3149688789)
        self.assertIsNotNone(energy(5), "This should return a value")
        self.assertEqual(energy(5), 1995262314968.8828)

    def test_tnt(self):
        self.assertEqual(tnt(10), 15080242458.895658)
        self.assertIsNotNone(energy(5), "This should return a value")
        self.assertEqual(energy(5), 476.87913837688404)

if __name__ == '__main__':
    unittest.main()
