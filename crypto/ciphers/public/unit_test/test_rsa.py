#!/usr/bin/python3
# Title: Unit Test for RSA Public Key Cipher
# Creator: Austin Akerley
# Date Created: 04/19/2020
# Last Editor: Austin Akerley
# Date Last Edited: 04/19/2020
# Associated Book Page Nuber: 123

from crypto.ciphers.public.rsa import rsa
import unittest

class TestRSACipher(unittest.TestCase):
    def test_rsa_cipher_decrypt(self):
        print("\n\nRunning test for cipher: rsa")
        p = 229
        q = 281
        e = 17389
        N = p * q
        my_cipher = rsa()
        c = 43927
        expected_m = 14458
        m = my_cipher.decrypt(c, p, q, e)
        print("N: " + str(my_cipher.N))
        my_cipher.publish_public_info()
        print("d: "+str(my_cipher.d))
        print("m: " + str(m))
        self.assertEqual(m, expected_m)

    def test_rsa_cipher_encrypt(self):
        e = 17389
        N = 64349
        my_cipher = rsa()
        m = 14458
        expected_c = 43927
        c = my_cipher.encrypt(m, N, e)
        print("\nN: " + str(my_cipher.N))
        print("e: " + str(my_cipher.e))
        print("c: "+str(c))
        self.assertEqual(c, expected_c)


if __name__ == '__main__':
    unittest.main()
