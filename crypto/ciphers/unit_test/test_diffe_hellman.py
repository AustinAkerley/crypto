#!/usr/bin/python3
# Title: Unit Test for Diffe-Hellman Key Exchange
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited:12/28/2019
# Associated Book Page Nuber: XXXXXXXX

import unittest
from crypto.ciphers.diffe_hellman import diffe_hellman

class TestDiffeHellman(unittest.TestCase):
    def test_diffe_hellman_1(self):
        A = diffe_hellman(g=627, private_key=347, p=941)
        B = diffe_hellman(g=627, private_key=781, p=941)
        print("A: " + str(A.A)+" | B: " + str(B.A))
        self.assertEqual(A.A, 390)
        self.assertEqual(B.A, 691)
        A_sym_key = A.gen_symmetric_key(B.A)
        B_sym_key = B.gen_symmetric_key(A.A)
        print("A_sym_key: "+str(A_sym_key)+" | B_sym_key: "+str(B_sym_key))
        self.assertEqual(A_sym_key, 470)
        self.assertEqual(B_sym_key, 470)

if __name__ == '__main__':
    unittest.main()
