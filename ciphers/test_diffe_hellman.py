#!/usr/bin/python3
import diffe_hellman
import unittest

class TestDiffeHellman(unittest.TestCase):
    def test_diffe_hellman_1(self):
        x = 3
        e = 218
        m = 1000
        result = 489
        self.assertEqual(fast_power.fast_power(x, e, m), result)

if __name__ == '__main__':
    unittest.main()
