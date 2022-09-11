import unittest

from latin_squares import *


class MyFirstTests(unittest.TestCase):

    def test_generate(self):
        self.assertEqual(generatelatin(3,1), ['1', '2', '3', '2', '3', '1', '3', '1', '2'])

if __name__ == '__main__':
    unittest.main()
