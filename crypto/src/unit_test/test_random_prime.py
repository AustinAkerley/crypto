#!/usr/bin/python3
# Title: Unit Test for Random Prime Generator
# Creator: Austin Akerley
# Date Created: 09/09/2020
# Last Editor: Austin Akerley
# Date Last Edited: 09/09/2020
# Associated Book Page Nuber:

import unittest
from crypto.src.random_prime import random_prime
from crypto.src.primality_test import primality_test

class TestRandomPrimeGenerator(unittest.TestCase):
    def test_random_prime_1(self):
        print("\n\nRunning test for src module: random_prime")
        rand_prime = random_prime(64)
        self.assertEqual(primality_test(rand_prime), True)

    def test_random_prime_2(self):
        rand_prime = random_prime(128)
        self.assertEqual(primality_test(rand_prime), True)

    def test_random_prime_3(self):
        rand_prime = random_prime(256)
        self.assertEqual(primality_test(rand_prime), True)

    def test_random_prime_4(self):
        rand_prime = random_prime(512)
        self.assertEqual(primality_test(rand_prime), True)

if __name__ == '__main__':
    unittest.main()
