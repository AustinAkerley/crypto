#!/usr/bin/python3
# Title: Unit Test for Fast Power
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited: 02/02/2020
# Associated Book Page Nuber: 24

import unittest
from crypto.src.fast_power import fast_power

class TestFastPower(unittest.TestCase):
    def test_fast_power_1(self):
        print("\n\nRunning test for src module: fast_power")
        x = 3
        e = 218
        m = 1000
        result = 489
        self.assertEqual(fast_power(x, e, m), result)

    def test_fast_power_2(self):
        x = 5
        e = 718
        m = 23451
        result = 3739
        self.assertEqual(fast_power(x, e, m), result)

    def test_fast_power_3(self):
        x = 11
        e = 12314
        m = 7234592359
        result = 1369450571
        self.assertEqual(fast_power(x, e, m), result)

    def test_fast_power_4(self):
        x = 11
        e = 7234592359-1
        m = 7234592359
        result = 1
        self.assertEqual(fast_power(x, e, m), result)
        
if __name__ == '__main__':
    unittest.main()
