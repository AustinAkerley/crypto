#!/usr/bin/python3
# Title: Unit Test for Diffie-Hellman Key Exchange
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/20/2020
# Associated Book Page Nuber: 67

import unittest
from crypto.ciphers.public.diffie_hellman import diffie_hellman

class TestDiffieHellman(unittest.TestCase):
    def test_diffie_hellman_1(self):
        print("\n\nRunning test for cipher: diffie_hellman")
        A = diffie_hellman(g=627, private_key=347, p=941)
        B = diffie_hellman(g=627, private_key=781, p=941)
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
