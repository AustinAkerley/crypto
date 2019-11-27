#!/usr/bin/python3
from crypto.ciphers.el_gammal import el_gammal
import unittest

class TestElGammalCipher(unittest.TestCase):
    def test_el_gammal_cipher(self):
        print("el_gammal pub_key generation 1")
        BobEG1 = el_gammal(generator=2, private_key=153,modulus=467)
        pub_key_1 = BobEG1.gen_public_key()
        print(str(pub_key_1))
        self.assertEqual(pub_key_1, 224)

        AliceEG1 = el_gammal(generator=2, modulus=467, public_key=pub_key_1)
        c1_c2 = AliceEG1.encrypt(message=331, k =197)
        print(str(c1_c2))
        self.assertEqual(c1_c2, [87, 57])

        message = BobEG1.decrypt(cipher_text_1=c1_c2[0], cipher_text_2=c1_c2[1])
        print("message: "+str(message))
        self.assertEqual(message, 331)


if __name__ == '__main__':
    unittest.main()
