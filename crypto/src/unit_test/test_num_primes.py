#!/usr/bin/python3
# Title: Unit Test for Approximate Number of Primes Between Two Numbers
# Creator: Austin Akerley
# Date Created: 04/04/2020
# Last Editor: Austin Akerley
# Date Last Edited: 04/04/2020
# Associated Book Page Nuber: 133

import unittest
from crypto.src.num_primes import num_primes

class TestNumPrimes(unittest.TestCase):
    def test_num_primes_1(self):
        print("\n\nRunning test for src module: num_primes")
        apprx_primes = num_primes(900000, 1000000)
        expected_apprx_primes = 6738
        self.assertEqual(apprx_primes, expected_apprx_primes)


if __name__ == '__main__':
    unittest.main()
