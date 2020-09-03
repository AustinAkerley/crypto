#!/usr/bin/python3
# Title: Unit Test for El-Gammal Cipher
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/20/2020
# Associated Book Page Nuber: 70

from crypto.ciphers.public.el_gammal import el_gammal
import unittest

class TestElGammalCipher(unittest.TestCase):
    def test_el_gammal_cipher(self):
        print("\n\nRunning test for cipher: el_gammal")
        print("el_gammal pub_key generation 1")
        BobEG1 = el_gammal(g=2, private_key=153,modulus=467)
        pub_key_1 = BobEG1.gen_public_key()
        print(str(pub_key_1))
        self.assertEqual(pub_key_1, 224)
        AliceEG1 = el_gammal(g=2, modulus=467, public_key=pub_key_1)
        c1_c2 = AliceEG1.encrypt(message=331, k =197)
        print(str(c1_c2))
        self.assertEqual(c1_c2, [87, 57])
        message = BobEG1.decrypt(cipher_text_1=c1_c2[0], cipher_text_2=c1_c2[1])
        print("message: "+str(message))
        self.assertEqual(message, 331)

if __name__ == '__main__':
    unittest.main()
