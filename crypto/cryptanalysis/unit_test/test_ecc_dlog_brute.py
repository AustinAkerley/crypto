#!/usr/bin/python3

import unittest
from crypto.ecc.curve import curve
from crypto.cryptanalysis.ecc_dlog_brute import ecc_brute

class Test(unittest.TestCase):

    def test_brute_1(self):
        E = curve(8,7,73);
        P = (32 , 53)
        R = (39, 17)
        n = ecc_brute(P, R, E)
        
        print("n: " + str(n));
        self.assertEqual(n, 11)

    def test_brute_2(self):
        E = curve(8,7,73);
        P = (32 , 53)
        R = (35, 47)
        n = ecc_brute(P, R, E)
        
        print("n: " + str(n));
        self.assertEqual(n, 37)

    def test_brute_3(self):
        E = curve(8,7,73);
        P = (32 , 53)
        R = (58, 4)
        n = ecc_brute(P, R, E)
        
        print("n: " + str(n));
        self.assertEqual(n, 28)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()