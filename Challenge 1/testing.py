import unittest

from rod_conversion import *


class MyFirstTests(unittest.TestCase):

      def test_joules(self):
        self.assertIsNotNone(joules(1), "This should return a value")
        self.assertEqual(joules(1), 1995262.3149688789)
        self.assertEqual(joules(3.4251), 8662634684.989311)
        
    def test_tnt(self):
        self.assertIsNotNone(tnt(1), "This should return a value")
        self.assertEqual(tnt(10), 15080242351.8)
        self.assertEqual(tnt(1), 0.00047687913)
        self.assertEqual(tnt(3.4251), 2.07041937978)

if __name__ == '__main__':
    unittest.main()
