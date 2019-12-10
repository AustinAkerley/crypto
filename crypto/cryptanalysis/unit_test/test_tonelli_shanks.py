#!/usr/bin/python3
# Author: Austin Akerley
# Date Last Edited: 10/31/2019
#
from crypto import tonelli_shanks
from crypto import fast_power
import time
import unittest

class TestTonelliShanks(unittest.TestCase):
    def test_tonelli_shanks_1(self):
        h = 13896
        p = 17389
        g = 9704
        expected_h = fast_power(9704, 2401, 17389)[0]
        print("expected_h: "+str(expected_h))
        print("h: "+str(h))
        print("expected_h: "+str(expected_h))
        start = time.time()
        x = tonelli_shanks(9704, 13896, 17389) #solving for x, where 9704^x = 13896 (mod 17389)
        stop = time.time()
        print("5 digit prime took: "+str(stop-start)+" seconds")
        self.assertEqual(x, 2401)

    def test_tonelli_shanks_2(self):
        g = 2
        e = 5621299
        p = 15485863 # 8 digits
        h = fast_power(g, e, p)[0]
        print("h: "+str(h))
        start = time.time()
        x = tonelli_shanks(g, h, p)
        stop = time.time()
        print("8 digit prime took: "+str(stop-start)+" seconds")
        print("x: "+str(x))
        self.assertEqual(x, e)

    def test_tonelli_shanks_3(self):
        g = 42389
        e = 97234565
        p = 160481183 # 9 digits
        h = fast_power(g, e, p)[0]
        print("h: "+str(h))
        start = time.time()
        x = tonelli_shanks(g, h, p)
        stop = time.time()
        print("9 digit prime took: "+str(stop-start)+" seconds")
        print("x: "+str(x))
        self.assertEqual(x, e)

    def test_tonelli_shanks_4(self):
        g = 8538429
        e = 293587245
        p = 5915587277 # 9 digits
        h = fast_power(g, e, p)[0]
        print("h: "+str(h))
        start = time.time()
        x = tonelli_shanks(g, h, p)
        stop = time.time()
        print("10 digit prime took: "+str(stop-start)+" seconds")
        print("x: "+str(x))
        self.assertEqual(x, e)

    def test_tonelli_shanks_5(self):
        g = 3
        e = 29345563468
        p = 1618033988749  # 9 digits
        h = fast_power(g, e, p)[0]
        print("h: "+str(h))
        start = time.time()
        x = tonelli_shanks(g, h, p)
        stop = time.time()
        print("12 digit prime took: "+str(stop-start)+" seconds")
        print("x: "+str(x))
        self.assertEqual(x, e)



if __name__ == '__main__':
    unittest.main()
