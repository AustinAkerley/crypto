#!/usr/bin/python3
# Title: RSA Digital Signature
# Creator: Austin Akerley
# Date Created: 09/09/2020
# Last Editor: Austin Akerley
# Date Last Edited: 09/09/2020
# Associated Book Page Nuber: 197

from crypto.signatures.rsa_sig import rsa_sig
from crypto.src.random_prime import random_prime
import unittest

class TestRSASignature(unittest.TestCase):
    def test_rsa_signature_1(self):
        print("\n\nRunning test for cipher: rsa_sig")
        p = random_prime(64)
        q = random_prime(64)
        N = p*q
        new_signature = rsa_sig(p, q)
        new_signature.gen_e()
        e = new_signature.e
        signature = new_signature.sign("./crypto/signatures/unit_test/example_doc.txt")

        signature_verifier = rsa_sig()
        is_signature_valid = signature_verifier.verify(signature, "./crypto/signatures/unit_test/example_doc.txt", e, N)
        self.assertEqual(is_signature_valid, True)

    def test_rsa_signature_2(self):
        print("\n\nRunning test for cipher: rsa_sig")
        p = random_prime(128)
        q = random_prime(128)
        N = p*q
        new_signature = rsa_sig(p, q)
        new_signature.gen_e()
        e = new_signature.e
        signature = new_signature.sign("./crypto/signatures/unit_test/example_doc.txt") 

        signature_verifier = rsa_sig()
        is_signature_valid = signature_verifier.verify(signature, "./crypto/signatures/unit_test/example_doc_bad.txt", e, N)
        self.assertEqual(is_signature_valid, False)

if __name__ == '__main__':
    unittest.main()
