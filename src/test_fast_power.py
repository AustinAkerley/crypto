#!/usr/bin/python3
import fast_power
import unittest

class TestFastPower(unittest.TestCase):
    def test_fast_power_1(self):
        x = 3
        e = 218
        m = 1000
        result = 489
        self.assertEqual(fast_power.fast_power(x, e, m), result)

    def test_fast_power_2(self):
        x = 5
        e = 718
        m = 23451
        result = 3739
        self.assertEqual(fast_power.fast_power(x, e, m), result)

    def test_fast_power_3(self):
        x = 11
        e = 12314
        m = 7234592359
        result = 1369450571
        self.assertEqual(fast_power.fast_power(x, e, m), result)

if __name__ == '__main__':
    unittest.main()
