#!/usr/bin/python3
# Title: Functional Unit Test for Chinese Remainder Theorem
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/19/2020
# Associated Book Page Nuber: 84

import unittest
import random
from crypto.cryptanalysis.crt import crt
from crypto.cryptanalysis.small_primes_generator import small_primes_generator

class TestCRT(unittest.TestCase):
    def test_crt_1(self):
        print("\n\nRunning test for cryptanalysis module: crt")
        ax_px0 = (1,5) # x = 1 (mod 5)
        ax_px1 = (9, 11) # x = 9 (mod 11)
        equivalencies = [ax_px0, ax_px1]
        x = 31
        self.assertEqual(crt(equivalencies), x)

    def test_crt_2(self):
        ax_px0 = (2, 3) # x = 2 (mod 3)
        ax_px1 = (3, 7) # x = 3 (mod 7)
        ax_px2 = (4, 16) # x = 4 (mod 16)
        equivalencies = [ax_px0, ax_px1, ax_px2]
        x = 164
        self.assertEqual(crt(equivalencies), x)

    def test_crt_3(self):
        ax_px0 = (4196, 4423)
        ax_px1 = (345, 6917)
        equivalencies = [ax_px0, ax_px1]
        x = 6917345
        self.assertEqual(crt(equivalencies), x)

if __name__ == '__main__':
    unittest.main()
