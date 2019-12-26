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
        self.assertEqual(fast_power(x, e, m)["result"], result)

    def test_fast_power_2(self):
        x = 5
        e = 718
        m = 23451
        result = 3739
        self.assertEqual(fast_power(x, e, m)["result"], result)

    def test_fast_power_3(self):
        x = 11
        e = 12314
        m = 7234592359
        result = 1369450571
        self.assertEqual(fast_power(x, e, m)["result"], result)

    def test_fast_power_4(self):
        x = 11
        e = 7234592359-1
        m = 7234592359
        result = 1
        self.assertEqual(fast_power(x, e, m)["result"], result)

    def test_fast_power_5(self):
        x = 11
        e = 7234592359
        m = 7234592359
        result = 0
        self.assertEqual(fast_power(x, e, m)["result"], result)

    def test_fast_power_6(self):
        g = 11
        e = 2134628
        m = 7234592359
        result = fast_power(g, e, m)
        e = 12314
        result2 = fast_power(g, e, m, result["known_powers"])
        result3 = fast_power(g, e, m)
        print("result2: "+str(result2["result"]))
        print("result3: "+str(result3["result"]))
        exp_result = 1369450571
        self.assertEqual(result2["result"], exp_result)

if __name__ == '__main__':
    unittest.main()
