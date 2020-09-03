#!/usr/bin/python3
# Title: Unit Test for Pohlig Hellman
# Creator: Austin Akerley
# Date Created: 02/02/2020
# Last Editor: Austin Akerley
# Date Last Edited: 02/02/2020
# Associated Book Page Nuber: 94

import time
import unittest
from crypto.cryptanalysis.pohlig_hellman import pohlig_hellman

class TestPohligHellman(unittest.TestCase):
    def test_pohlig_hellman_1(self):
        print("\n\nRunning test for cryptanalysis module: pohlig_hellman")
        prime = 31 # 5 digit weak prime
        g = 2
        h = 8
        xs= pohlig_hellman(g, h, prime)
        expected_x = 13
        self.assertIn(expected_x, xs)

    def test_pohlig_hellman_2(self):
        prime = 15377 # 5 digit weak prime
        g = 3
        h = 13572
        xs = pohlig_hellman(g, h, prime)
        expected_x = 6025
        self.assertIn(expected_x, xs)

    def test_pohlig_hellman_3(self):
        prime = 11251 # 5 digit weak prime
        g = 23
        h = 9689
        xs = pohlig_hellman(g, h, prime)
        expected_x = 4261
        self.assertIn(expected_x, xs)

if __name__ == '__main__':
    unittest.main()
