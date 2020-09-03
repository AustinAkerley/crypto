#!/usr/bin/python3
# Title: Unit Test for Elliptic Curve Diffie-Hellman Key Exchange
# Creator: Austin Akerley
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/20/2020
# Associated Book Page Nuber: 316

import unittest
from crypto.ecc.src.curve import curve
from crypto.ecc.ciphers.public.ecc_diffie_hellman import ecc_diffie_hellman

class TestECCDiffieHellman(unittest.TestCase):
    def test_ecc_diffie_1(self):
        print("\n\nRunning test for ecc cipher class: ecc_diffie_hellman")
        P = (920, 303)
        E = curve(324, 1287, 3851)
        diffie_A = ecc_diffie_hellman(E, P)
        QA = diffie_A.public_keygen(private_key=1194)
        diffie_B = ecc_diffie_hellman(E, P)
        QB = diffie_B.public_keygen(private_key=1759)
        key_A = diffie_A.symmetric_keygen(QB, output_type = "whole point")
        key_B = diffie_B.symmetric_keygen(QA, output_type = "whole point")
        self.assertEqual(key_A, key_B)

    def test_ecc_diffie_1(self):
        P = (920, 303)
        E = curve(324, 1287, 3851)
        diffie_A = ecc_diffie_hellman(E, P)
        QA = diffie_A.public_keygen(private_key=1194)
        diffie_B = ecc_diffie_hellman(E, P)
        QB = diffie_B.public_keygen(private_key=1759)
        key_A = diffie_A.symmetric_keygen(QB, output_type = "whole point")
        key_B = diffie_B.symmetric_keygen(QA, output_type = "whole point")
        self.assertEqual(key_A, key_B)

if __name__ == "__main__":
    unittest.main()
