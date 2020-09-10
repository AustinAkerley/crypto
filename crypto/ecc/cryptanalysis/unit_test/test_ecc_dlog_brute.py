#!/usr/bin/python3
# Title: Unit Test for Brute Force Elliptic Curve Discrete Logarithm
# Creator: Daniel Gerthe
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/20/2020
# Associated Book Page Nuber: 310

import unittest
from crypto.ecc.src.curve import curve
from crypto.ecc.cryptanalysis.ecc_dlog_brute import ecc_dlog_brute

class TestECCDLogBrute(unittest.TestCase):
    def test_brute_ecc_dlog_functional_1(self):
        print("\n\nRunning test for ecc cryptanalysis module: ecc_dlog_brute")
        E = curve(8,7,73);
        P = (32 , 53)
        R = (39, 17)
        n = ecc_dlog_brute(P, R, E)
        print("n: " + str(n));
        self.assertEqual(n, 11)

    def test_brute_ecc_dlog_functional_2(self):
        E = curve(8,7,73);
        P = (32 , 53)
        R = (35, 47)
        n = ecc_dlog_brute(P, R, E)
        print("n: " + str(n));
        self.assertEqual(n, 37)

    def test_brute_ecc_dlog_functional_3(self):
        E = curve(8,7,73);
        P = (32 , 53)
        R = (58, 4)
        n = ecc_dlog_brute(P, R, E)
        print("n: " + str(n));
        self.assertEqual(n, 28)

    def test_brute_ecc_dlog_functional_4(self):
        E = curve(8,7,73);
        P = (32 , 53)
        R = (35, 47)
        n = ecc_dlog_brute(P, R, E)
        print("n: " + str(n));
        self.assertEqual(n, 37)

if __name__ == "__main__":
    unittest.main()
