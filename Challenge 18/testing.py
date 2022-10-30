import unittest

from increment_pw import *


class MyFirstTests(unittest.TestCase):

    def test_generate(self):
        self.assertEqual(find(285,2), 'JP')
        self.assertIsNotNone(find(1,1), "This should return a value")
        self.assertEqual(find(1,1), 'A')
        self.assertEqual(find(28,1), '1')
        

if __name__ == '__main__':
    unittest.main()