#!/usr/bin/python3
# Title: Unit Test for Modular Square Root
# Creator: Austin Akerley
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/19/2020
# Associated Book Page Nuber: 169

import unittest
from crypto.src.mod_sqrt import mod_sqrt
from crypto.cryptanalysis.small_primes_generator import small_primes_generator

class TestModSqrt(unittest.TestCase):
    def test_mod_sqrt_1(self):
        print("\n\nRunning test for src module: mod_sqrt")
        # test with prime 1 mod 8, where there is a sqrt for a
        m = 977
        orig_x = 745
        a = (orig_x*orig_x) % m
        x = mod_sqrt(a, m)
        self.assertIn(orig_x, x)

    def test_mod_sqrt_2(self):
        # Bulk test with all the primes under 1000
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
        #test with prime 3 mod 8, where there is a sqrt for a
        m = 563
        orig_x = 109
        a = (orig_x*orig_x) % m
        x = mod_sqrt(a, m)
        self.assertIn(orig_x, x)

    def test_mod_sqrt_4(self):
        #test with prime 7 mod 8, where there is a sqrt for a
        m = 719
        orig_x = 230
        a = (orig_x*orig_x) % m
        x = mod_sqrt(a, m)
        self.assertIn(orig_x, x)

    def test_mod_sqrt_5(self):
        # Test where there is no sqrt
        m = 3623
        a = 88
        expected_x = (None,None)
        x = mod_sqrt(a, m)
        self.assertEqual(expected_x, x)

if __name__ == "__main__":
    unittest.main()
