#!/usr/bin/python3
# Title: Unit Test for ECC El-Gammal Cipher
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/20/2020
# Associated Book Page Nuber: XXXXXXXX

from crypto.ecc.ciphers.public.ecc_el_gammal import ecc_el_gammal
from crypto.ecc.src.curve import curve
import unittest

class TestECCElGammalCipher(unittest.TestCase):
    def test_ecc_el_gammal_cipher(self):
        print("\n\nRunning test for ecc cipher class: ecc_el_gammal")
        P = (920, 303)
        E = curve(324, 1287, 3851)
        orig_plaintext = 555
        BobEG1 = ecc_el_gammal(E, P)
        BobEG1.private_keygen();
        BobPub = BobEG1.public_keygen()
        AliceEG1 = ecc_el_gammal(E, P)
        AliceEG1.private_keygen()
        AlicePub = AliceEG1.public_keygen()
        c1, c2 = BobEG1.encrypt(orig_plaintext, AlicePub)
        plaintext = AliceEG1.decrypt(c1, c2)
        self.assertEqual(plaintext, orig_plaintext)

if __name__ == '__main__':
    unittest.main()
