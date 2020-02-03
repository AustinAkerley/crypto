#!/usr/bin/python3
# Title: Unit Test for One Time Pad Cipher
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/20/2020
# Associated Book Page Nuber: 1

import unittest
from crypto.ciphers.private.one_time_pad import one_time_pad

class TestShiftCipher(unittest.TestCase):
    def test_shift_cipher_encrypt_1(self):
        print("Test Starting: test_shift_cipher_encrypt_1")
        expected_cipher_text = "Rjjy%rj%gjmnsi%ymj%ywjj%ts%fsi%\\fqq"
        plain_text = "Meet me behind the tree on and Wall"
        key = 5
        shift_cipher = shift()
        cipher_text = shift_cipher.encrypt(plain_text, key)
        self.assertEqual(cipher_text, expected_cipher_text)
        print("Test Finished: test_shift_cipher_encrypt_1\n")

    def test_shift_cipher_decrypt_1(self):
        print("Test Starting: test_shift_cipher_decrypt_1")
        cipher_text = "Rjjy%rj%gjmnsi%ymj%ywjj%ts%fsi%\\fqq"
        expected_plain_text = "Meet me behind the tree on and Wall"
        key = 5
        shift_cipher = shift()
        plain_text = shift_cipher.decrypt(cipher_text, key)
        self.assertEqual(plain_text, expected_plain_text)
        print("Test Finished: test_shift_cipher_decrypt_1\n")

if __name__ == '__main__':
    unittest.main()
