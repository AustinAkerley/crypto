#!/usr/bin/python3
# Title: Unit Test for Tonelli-Shanks Discrete Logarithm Algorithm
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited:12/28/2019
# Associated Book Page Nuber: XXXXXXXX

import time
import unittest
from crypto.cryptanalysis.tonelli_shanks import tonelli_shanks
from crypto.src.fast_power import fast_power

class TestTonelliShanks(unittest.TestCase):
    def test_tonelli_shanks_functional_1(self):
        h = 13896
        g = 9704
        expect_x = 1159
        p = 17389
        expected_h = fast_power(9704, expect_x, 17389)["result"]
        h = 13896
        print("h: "+str(h))
        print("expected_h: "+str(expected_h))
        start = time.time()
        x = tonelli_shanks(9704, h, p) #solving for x, where 9704^x = 13896 (mod 17389)
        stop = time.time()
        print("5 digit prime took: "+str(stop-start)+" seconds")
        self.assertEqual(x, expect_x)

    def test_tonelli_shanks_functional_2(self):
        g = 2
        e = 5621299
        p = 15485863 # 8 digits
        h = fast_power(g, e, p)["result"]
        #print("h: "+str(h))
        start = time.time()
        x = tonelli_shanks(g, h, p)
        stop = time.time()
        print("8 digit prime took: "+str(stop-start)+" seconds")
        #print("x: "+str(x))
        self.assertEqual(x, e)

    def test_tonelli_shanks_functional_3(self):
        g = 42389
        e = 97234565
        p = 160481183 # 9 digits
        h = fast_power(g, e, p)["result"]
        print("h: "+str(h))
        start = time.time()
        x = tonelli_shanks(g, h, p)
        stop = time.time()
        print("9 digit prime took: "+str(stop-start)+" seconds")
        #print("x: "+str(x))
        self.assertEqual(x, e)

    def test_tonelli_shanks_functional_4(self):
        g = 8538429
        e = 293587245
        p = 5915587277 # 9 digits
        h = fast_power(g, e, p)["result"]
        #print("h: "+str(h))
        start = time.time()
        x = tonelli_shanks(g, h, p)
        stop = time.time()
        print("10 digit prime took: "+str(stop-start)+" seconds")
        #print("x: "+str(x))
        self.assertEqual(x, e)
    # This test takes 3 minutes so uncomment if you want a long one
    # def test_tonelli_shanks_5(self):
    #     g = 2
    #     e = 29345563468
    #     p = 1618033988749  # 13 digits
    #     h = fast_power(g, e, p)[0]
    #     #print("h: "+str(h))
    #     start = time.time()
    #     x = tonelli_shanks(g, h, p)
    #     stop = time.time()
    #     #print("12 digit prime took: "+str(stop-start)+" seconds")
    #     #print("x: "+str(x))
    #     self.assertEqual(x, e)

if __name__ == '__main__':
    unittest.main()
