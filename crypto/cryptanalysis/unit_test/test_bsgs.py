#!/usr/bin/python3
# Title: Unit Test for Big Step Giant Step Discrete Logarithm
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited:02/02/2020
# Associated Book Page Nuber: 82

import time
import unittest
import random
from crypto.cryptanalysis.bsgs import bsgs
from crypto.src.fast_power import fast_power
from crypto.cryptanalysis.small_primes_generator import small_primes_generator

class TestBSGS(unittest.TestCase):
    def test_bsgs_1(self): # Book Example
        print("\n\nRunning test for cryptanalysis module: bsgs")
        g = 9704
        exp_x =1159
        p = 17389
        h = fast_power(g, exp_x, p)
        xs = bsgs(g, h, p)
        self.assertIn(exp_x, xs)

    def test_bsgs_2(self):
        primes = small_primes_generator(1000) # Change this to increase/decrease duration of test
        del primes[0] # delete 2, all of these are trivial
        del primes[0] # delete 3
        del primes[0] # delte 5

        for prime in primes:
            for j in range(1, 10):
                g = random.randint(2, prime-1)
                for i in range(1, 10):
                    expected_x = random.randint(1, prime-1)
                    h = fast_power(g, expected_x, prime)
                    xs = bsgs(g, h, prime)
                    #print(" | prime: "+str(prime) + " | g: "+str(g) + " | exp_x: "+str(expected_x)+" | h: "+str(h)+ " | xs: " + str(xs))
                    self.assertIn(expected_x, xs)

if __name__ == '__main__':
    unittest.main()

# 10,000 - 243s
# 20,000 - 475s
# 50,000 - 1110s
# 100,000 - 2235s
