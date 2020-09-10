#!/usr/bin/python3
# Title: Unit Test for Extended Euclidean Algorithm
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited: 02/09/2020

import unittest
from crypto.src.eea import eea #UUT

class TestEEA(unittest.TestCase):
        def test_eea_1(self):
            print("\n\nRunning test for src module: eea")
            x = 3
            y = 21
            self.assertEqual(eea(x, y),{"gcd":3, "a":1, "x":x, "b":0, "y":y})

        def test_eea_2(self):
            x = 63451367846845
            y = 52352467468873425
            self.assertEqual(eea(x, y), {"gcd":5, "a":4310308599955094, "x":x, "b":-5224108618601, "y":y})

if __name__ == '__main__':
    unittest.main()
