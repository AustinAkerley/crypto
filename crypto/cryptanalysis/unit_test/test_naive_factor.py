#!/usr/bin/python3
# Title: Unit Test for Naive Factor
# Creator: Austin Akerley
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/20/2020
# Associated Book Page Nuber: XXXXXXXX

import time
import unittest
from crypto.cryptanalysis.naive_factor import naive_factor

class TestNaiveFactor(unittest.TestCase):
    def test_naive_factor_functional_1(self):
        print("\n\nRunning test for cryptanalysis module: naive_factor")
        h = 523854
        expected_prime_factors = [2, 3, 3, 3, 89, 109]
        prime_factors = naive_factor(h).get("prime_factors")
        self.assertEqual(prime_factors, expected_prime_factors)

    def test_naive_factor_functional_2(self):
        h = 732451
        expected_prime_factors = [509, 1439]
        prime_factors = naive_factor(h).get("prime_factors")
        self.assertEqual(prime_factors, expected_prime_factors)

if __name__ == '__main__':
    unittest.main()
