#!/usr/bin/python3
import unittest
from crypto.ecc.curve import curve
from crypto.ciphers.ecc_diffie_hellman import ecc_diffie_hellman

class Test(unittest.TestCase):

    def test_ecc_diffie_1(self):
        P = (920, 303)
        E = curve(324, 1287, 3851)

        diffie_A = ecc_diffie_hellman(E, P)
        QA = diffie_A.public_keygen(private_key=1194)

        diffie_B = ecc_diffie_hellman(E, P)
        QB = diffie_B.public_keygen(private_key=1759)

        key_A = diffie_A.symmetric_keygen(QB)
        key_B = diffie_B.symmetric_keygen(QA)
        self.assertEqual(key_A, key_B)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
