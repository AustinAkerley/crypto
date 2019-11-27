#!/usr/bin/python3
# Author: Austin Akerley
# Date Last Edited: 10/31/2019
#
from crypto.src.fast_power import fast_power
import unittest

class TestFastPower(unittest.TestCase):
    def test_fast_power_1(self):
        x = 3
        e = 218
        m = 1000
        result = 489
        self.assertEqual(fast_power(x, e, m)[0], result)

    def test_fast_power_2(self):
        x = 5
        e = 718
        m = 23451
        result = 3739
        self.assertEqual(fast_power(x, e, m)[0], result)

    def test_fast_power_3(self):
        x = 11
        e = 12314
        m = 7234592359
        result = 1369450571
        self.assertEqual(fast_power(x, e, m)[0], result)

    def test_fast_power_4(self):
        x = 11
        e = 7234592359 -1
        m = 7234592359
        result = 1
        self.assertEqual(fast_power(x, e, m)[0], result)

    def test_fast_power_5(self):
        x = 11
        e = 7234592359
        m = 7234592359
        result = 0
        self.assertEqual(fast_power(x, e, m)[0], result)

if __name__ == '__main__':
    unittest.main()
