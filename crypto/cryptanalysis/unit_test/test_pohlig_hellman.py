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

    def test_pohlig_hellman_functional_2(self):
        prime = 15377 # 5 digit weak prime
        g = 3
        h = 13575
        x = pohlig_hellman(g, h, prime)
        expected_x = 6025
        self.assertEqual(x, expected_x)

if __name__ == '__main__':
    unittest.main()
