#!/usr/bin/python3
# Title: Unit Test for Elliptic Curve Diffe-Hellman Key Exchange
# Creator: Austin Akerley
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited:12/28/2019
# Associated Book Page Nuber: XXXXXXXX

import unittest
from crypto.src.mod_sqrt import mod_sqrt
from crypto.src.small_primes_generator import small_primes_generator

class TestModSqrt(unittest.TestCase):

    def test_mod_sqrt_1(self):
        #test with prime 1 mod 8
        m = 977
        orig_x = 745
        a = (orig_x*orig_x) % m
        x = mod_sqrt(a, m)
        self.assertIn(orig_x, x)

    def test_mod_sqrt_2(self):
        #test with prime 5 mod 8
        orig_x = None
        primes = small_primes_generator(1000)
        del primes[0]
        for m in primes:
            for i in range(1, m):
                orig_x = i
                a = (orig_x*orig_x) % m
                x = mod_sqrt(a, m)
                self.assertIn(orig_x, x)

    def test_mod_sqrt_3(self):
        #test with prime 3 mod 8
        m = 563
        orig_x = 109
        a = (orig_x*orig_x) % m
        x = mod_sqrt(a, m)
        self.assertIn(orig_x, x)

    def test_mod_sqrt_4(self):
        #test with prime 7 mod 8
        m = 719
        orig_x = 230
        a = (orig_x*orig_x) % m
        x = mod_sqrt(a, m)
        self.assertIn(orig_x, x)

if __name__ == "__main__":
    unittest.main()
