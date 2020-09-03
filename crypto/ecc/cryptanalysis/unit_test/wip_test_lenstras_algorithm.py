#!/usr/bin/python3
# Title: Unit Test for Lenstras Algorithm
# Creator: Austin Akerley
# Date Created: 12/31/2019
# Last Editor: Austin Akerley
# Date Last Edited:12/31/2019
# Associated Book Page Nuber: 327

import time
import unittest
from crypto.ecc.cryptanalysis.lenstras_algorithm import lenstras_algorithm

class TestLenstrasAlgorithm(unittest.TestCase):
    def test_lenstras_algorithm_1(self):
        print("\n\nRunning test for ecc cryptanalysis module: lentras_algorithm")
        p = 7103
        q = 3769
        n = p * q
        start = time.time()
        d = lenstras_algorithm(n)
        stop = time.time()
        print("4 digit primes took: "+str(stop-start)+" seconds")
        print("d: "+str(d))
        self.assertIn(d, [p,q])

    def test_lenstras_algorithm_2(self):
        p = 160481183
        q = 5915587277
        n = p * q
        start = time.time()
        d = lenstras_algorithm(n)
        stop = time.time()
        print("9 digit prime took: "+str(stop-start)+" seconds")
        print("d: "+str(d))
        self.assertIn(d, [p,q])

    def test_lenstras_algorithm_3(self):
        p = 5463458053
        q = 1618033988749
        n = p * q
        start = time.time()
        d = lenstras_algorithm(n)
        stop = time.time()
        print("12 digit prime took: "+str(stop-start)+" seconds")
        print("d: "+str(d))
        self.assertIn(d, [p,q])

    # def test_lenstras_algorithm_functional_4(self):
    #     p = 54673257461630679457
    #     q = 12764787846358441471
    #     n = p * q
    #     start = time.time()
    #     d = lenstras_algorithm(n)
    #     stop = time.time()
    #     print("~40 digit composite took: "+str(stop-start)+" seconds")
    #     print("d: "+str(d))
    #     self.assertIn(d, [p,q])

if __name__ == '__main__':
    unittest.main()
