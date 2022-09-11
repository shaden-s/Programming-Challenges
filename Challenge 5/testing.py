import unittest

from slayer import *


class MyFirstTests(unittest.TestCase):

    def test_layers(self):
        self.assertEqual(layers(12345), '23451')

if __name__ == '__main__':
    unittest.main()
