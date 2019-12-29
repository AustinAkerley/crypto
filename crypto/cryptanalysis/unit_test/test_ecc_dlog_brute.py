#!/usr/bin/python3
# Title: Unit Test for Brute Force Elliptic Curve Discrete Logarithm
# Creator: Daniel Gerthe
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited:12/28/2019
# Associated Book Page Nuber: XXXXXXXX

import unittest
from crypto.ecc.curve import curve
from crypto.cryptanalysis.ecc_dlog_brute import ecc_brute

class TestECCDLogBrute(unittest.TestCase):
    def test_brute_ecc_dlog_1(self):
        E = curve(8,7,73);
        P = (32 , 53)
        R = (39, 17)
        n = ecc_brute(P, R, E)
        print("n: " + str(n));
        self.assertEqual(n, 11)

    def test_brute_ecc_dlog_2(self):
        E = curve(8,7,73);
        P = (32 , 53)
        R = (35, 47)
        n = ecc_brute(P, R, E)
        print("n: " + str(n));
        self.assertEqual(n, 37)

    def test_brute_ecc_dlog_3(self):
        E = curve(8,7,73);
        P = (32 , 53)
        R = (58, 4)
        n = ecc_brute(P, R, E)
        print("n: " + str(n));
        self.assertEqual(n, 28)

if __name__ == "__main__":
    unittest.main()
