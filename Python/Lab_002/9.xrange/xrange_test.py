import random
import unittest
import xrange


class Xrange_test(unittest.TestCase):

    def setUp(self):
        self.start = random.choice([1, -1, 25, -5, 3, 10])
        self.stop = random.choice([3, -4, 5, 3, -30, 42])
        self.step = random.choice([1, 3, -1, -3])

    def test1(self):
        self.assertEqual(list(xrange.XRange(self.start, self.stop, self.step)),
                         list(range(self.start, self.stop, self.step)))

    def test2(self):
        self.assertEqual(list(xrange.XRange(self.start, self.stop)),
                         list(range(self.start, self.stop)))

    def test3(self):
        self.assertEqual(list(xrange.XRange(self.stop, self.start)),
                         list(range(self.stop, self.start)))

if __name__ == '__main__':
    unittest.main()
