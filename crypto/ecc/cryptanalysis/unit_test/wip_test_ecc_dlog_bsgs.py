#!/usr/bin/python3
# Title: Unit Test for Baby Step Giant Step (bsgs) Elliptic Curve Discrete Logarithm
# Creator: Daniel Gerthe
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/20/2020
# Associated Book Page Nuber: XXXXXXXX
# WARNING: This doesn't really work yet

import unittest
from crypto.ecc.src.curve import curve
from crypto.ecc.cryptanalysis.ecc_dlog_bsgs import ecc_dlog_bsgs

class TestECCDLogBSGS(unittest.TestCase):
    def test_ecc_dlog_bsgs_functional_1(self):
        print("\n\nRunning test for cryptanalysis module: ecc_dlog_bsgs")
        E = curve(8,7,73);
        P = (32 , 53)
        R = (39, 17)
        n = ecc_dlog_bsgs(P, R, E)
        print(E.multiply(P, 43))
        print("n: " + str(n));
        self.assertEqual(n, 11)

    def test_ecc_dlog_bsgs_functional_2(self):
        E = curve(8,7,73);
        P = (32 , 53)
        R = (35, 47)
        n = ecc_dlog_bsgs(P, R, E)
        print("n: " + str(n));
        self.assertEqual(n, 37)

    def test_ecc_dlog_bsgs_functional_3(self):
        E = curve(8,7,73);
        P = (32 , 53)
        R = (58, 4)
        n = ecc_dlog_bsgs(P, R, E)
        print("n: " + str(n));
        self.assertEqual(n, 28)

if __name__ == "__main__":
    unittest.main()
