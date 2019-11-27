#!/usr/bin/python3
from crypto.ciphers.substitution import substitution
import unittest

class TestSubstitutionCipher(unittest.TestCase):
    def test_substituion_cipher_decrypt_1(self):
        print("Initial Decrypt 1")
        cipher_text = ["Rjjy%rj%gjmnsi%ymj%ywjj%ts%fsi%\\fqq", "lmn8y5>|tls:8~FK", "56789:;<=>"]
        expected_plain_text = ["Meet me behind the tree on and Wall", "ghi3t09wogn53yAF", "0123456789"]
        key = 5
        sub_cipher = substitution(key, None, cipher_text)
        print(sub_cipher.cipher_text)
        sub_cipher.decrypt()
        print("Actual Output:")
        print(sub_cipher.plain_text)
        print("Expected Output:")
        print(expected_plain_text)
        self.assertEqual(sub_cipher.plain_text, expected_plain_text)
        print("Test Finished: Initial Decrypt in test_substituion_cipher_decrypt\n")

    def test_substituion_cipher_decrypt_2(self):
        print("Key Change, Cipher Text Change, Decrypt 2")
        cipher_text = ["Woo~*wo*lorsxn*~ro*~|oo*yx*=C~r*kxn*akvv", "qrs=~:C\x01yqx?=\x03KP", ":;<=>?@ABC"]
        expected_plain_text = ["Meet me behind the tree on 39th and Wall", "ghi3t09wogn53yAF", "0123456789"]
        key = 5
        sub_cipher = substitution(key, None, cipher_text)
        sub_cipher.set_key(10)
        sub_cipher.set_cipher_text(cipher_text)
        sub_cipher.decrypt()
        print("Actual Output:")
        print(sub_cipher.plain_text)
        print("Expected Output:")
        print(expected_plain_text)
        self.assertEqual(sub_cipher.plain_text, expected_plain_text)
        print("Test Finished: Key Change and Cipher Text Change 1 in test_substituion_cipher_decrypt\n")

    def test_substituion_cipher_decrypt_3(self):
        print("Key Change, Cipher Text Change, Decrypt 3")
        cipher_text = ["\x13++:f3+f(+./4*f:.+f:8++f54fy\x7f:.f'4*f\x1d'22", "-./y:v\x7f=5-4{y?\x07\x0c", "vwxyz{|}~\x7f"]
        expected_plain_text = ["Meet me behind the tree on 39th and Wall", "ghi3t09wogn53yAF", "0123456789"]
        key = 5
        sub_cipher = substitution(key, None, cipher_text)
        sub_cipher.set_key(70)
        sub_cipher.set_cipher_text(cipher_text)
        sub_cipher.decrypt()
        print("Actual Output:")
        print(sub_cipher.plain_text)
        print("Expected Output:")
        print(expected_plain_text)
        self.assertEqual(sub_cipher.plain_text, expected_plain_text)
        print("Test Finished: Key Change and Cipher Text Change 2 in test_substituion_cipher_decrypt\n")

    def test_substituion_cipher_encrypt_1(self):
        print("Initial Encrypt Default 1")
        plain_text = ["Meet me behind the tree on and Wall", "ghi3t09wogn53yAF", "0123456789"]
        expected_cipher_text = ["Rjjy%rj%gjmnsi%ymj%ywjj%ts%fsi%\\fqq", "lmn8y5>|tls:8~FK", "56789:;<=>"]
        key = 5
        sub_cipher = substitution(key, plain_text, None)
        sub_cipher.encrypt()
        print("Actual Output:")
        print(sub_cipher.cipher_text)
        print("Expected Output:")
        print(expected_cipher_text)
        self.assertEqual(sub_cipher.cipher_text, expected_cipher_text)
        print("Test Finished: Initial Encrypt in test_substituion_cipher_encrypt\n")

    def test_substituion_cipher_encrypt_2(self):
        print("Key Change and Encrypt 2")
        expected_cipher_text = ["Woo~*wo*lorsxn*~ro*~|oo*yx*=C~r*kxn*akvv", "qrs=~:C\x01yqx?=\x03KP", ":;<=>?@ABC"]
        plain_text = ["Meet me behind the tree on 39th and Wall", "ghi3t09wogn53yAF", "0123456789"]
        key = 5
        sub_cipher = substitution(key, plain_text)
        sub_cipher.set_key(10)
        sub_cipher.encrypt()
        print("Actual Output:")
        print(sub_cipher.cipher_text)
        print("Expected Output:")
        print(expected_cipher_text)
        self.assertEqual(sub_cipher.cipher_text, expected_cipher_text)
        print("Test Finished: Key Change and Encrypt 1 in test_substituion_cipher_encrypt\n")

    def test_substituion_cipher_encrypt_3(self):
        print("Key Change and Encrypt 3")
        expected_cipher_text = ["\x13++:f3+f(+./4*f:.+f:8++f54fy\x7f:.f'4*f\x1d'22", "-./y:v\x7f=5-4{y?\x07\x0c", "vwxyz{|}~\x7f"]
        plain_text = ["Meet me behind the tree on 39th and Wall", "ghi3t09wogn53yAF", "0123456789"]
        key = 5
        sub_cipher = substitution(key, plain_text)
        sub_cipher.set_key(70)
        sub_cipher.encrypt()
        print("Actual Output:")
        print(sub_cipher.cipher_text)
        print("Expected Output:")
        print(expected_cipher_text)
        self.assertEqual(sub_cipher.cipher_text, expected_cipher_text)
        print("Test Finished: Key Change and Encrypt 2 in test_substituion_cipher_encrypt\n")

    def test_substituion_cipher_encrypt_4(self):
        print("Initial Encrypt Alphabetic 4")
        plain_text = ["Meet me behind the tree on and Wall", "ghi3t09wogn53yAF", "0123456789"]
        expected_cipher_text = ['Rjjy rj gjmnsi ymj ywjj ts fsi Bfqq', '', '']
        key = 5
        sub_cipher = substitution(key, plain_text, None, "alphabetic")
        sub_cipher.encrypt()
        print("Actual Output:")
        print(sub_cipher.cipher_text)
        print("Expected Output:")
        print(expected_cipher_text)
        self.assertEqual(sub_cipher.cipher_text, expected_cipher_text)
        print("Test Finished: Initial Encrypt in test_substituion_cipher_encrypt\n")
    def test_substituion_cipher_encrypt_5(self):
        print("Initial Encrypt Alphabetic 4")
        plain_text = ["Meet me behind the tree on and Wall", "Walk past the tree and turn left", "hi tommy"]
        expected_cipher_text = ['Rjjy rj gjmnsi ymj ywjj ts fsi Bfqq', 'Bfqp ufxy ymj ywjj fsi yzws qjky', 'mn ytrrd']
        key = 5
        sub_cipher = substitution(key, plain_text, None, "alphabetic")
        sub_cipher.encrypt()
        print("Actual Output:")
        print(sub_cipher.cipher_text)
        print("Expected Output:")
        print(expected_cipher_text)
        self.assertEqual(sub_cipher.cipher_text, expected_cipher_text)
        print("Test Finished: Initial Encrypt in test_substituion_cipher_encrypt\n")

    def test_substituion_cipher_encrypt_5(self):
        print("Initial Encrypt Alphabetic 5")
        plain_text = ["Meet me behind the tree on and Wall", "Walk past the tree and turn left", "hi tommy"]
        expected_cipher_text = ['Wood wo lorsxn dro dboo yx kxn Gkvv', 'Gkvu zkcd dro dboo kxn debx vopd', 'rs dywwi']
        key = 5
        sub_cipher = substitution(key, plain_text, None, "alphabetic")
        sub_cipher.encrypt()
        key = 10
        sub_cipher.set_key(key)
        sub_cipher.encrypt()
        print("Actual Output:")
        print(sub_cipher.cipher_text)
        print("Expected Output:")
        print(expected_cipher_text)
        self.assertEqual(sub_cipher.cipher_text, expected_cipher_text)
        print("Test Finished: Initial Encrypt in test_substituion_cipher_encrypt\n")

    def test_substituion_cipher_encrypt_and_decrypt_1(self):
        print("Initial Encrypt and Decrypt Alphabetic 1")
        plain_text = ["Meet me behind the tree on and Wall", "Walk past the tree and turn left", "hi tommy"]
        expected_cipher_text = ['Wood wo lorsxn dro dboo yx kxn Gkvv', 'Gkvu zkcd dro dboo kxn debx vopd', 'rs dywwi']
        key = 5
        sub_cipher = substitution(key, plain_text, None, "alphabetic")
        cipher_text = sub_cipher.encrypt()
        plain_text1 = sub_cipher.decrypt()
        self.assertEqual(plain_text1, plain_text)
        print("Actual Output:")
        print(plain_text)
        print("Expected Output:")
        print(plain_text1)
        key = 10
        sub_cipher.set_key(key)
        sub_cipher.encrypt()
        cipher_text = sub_cipher.encrypt()
        plain_text2 = sub_cipher.decrypt()
        self.assertEqual(plain_text2, plain_text)
        print("Actual Output:")
        print(plain_text2)
        print("Expected Output:")
        print(plain_text)
        self.assertEqual(sub_cipher.cipher_text, expected_cipher_text)
        print("Test Finished: Initial Encryptand Decrypt in test_substituion_cipher_encrypt\n")

    def test_substituion_cipher_encrypt_and_decrypt_2(self):
        print("Initial Encrypt and Decrypt Alphabetic 2")
        plain_text = "I came to town to find a free heart but only got to the border"
        expected_cipher_text = ["V pnzr gb gbja gb svaq n serr urneg ohg bayl tbg gb gur obeqre"]
        key = "n"
        sub_cipher = substitution(key, plain_text, None, "alphabetic")
        cipher_text = sub_cipher.encrypt()
        self.assertEqual(cipher_text, expected_cipher_text)
        print("Actual Output:")
        print(cipher_text)
        print("Expected Output:")
        print(expected_cipher_text)

        plain_text = [plain_text]
        sub_cipher.set_cipher_text(cipher_text)
        sub_cipher.decrypt()
        self.assertEqual(sub_cipher.plain_text, plain_text)
        print("Actual Output:")
        print(sub_cipher.plain_text)
        print("Expected Output:")
        print(plain_text)
        print("Test Finished: Initial Encryptand Decrypt Alphabetic 2 in test_substituion_cipher_encrypt\n")

    def test_substituion_cipher_encrypt_and_decrypt_3(self):
        print("Initial Encrypt and Decrypt Alphabetic 3")
        plain_text = "I came to town to find a free heart but only got to the border"
        expected_cipher_text = ["V pnzr gb gbja gb svaq n serr urneg ohg bayl tbg gb gur obeqre"]
        key = 845
        sub_cipher = substitution(key, plain_text, None, "alphabetic")
        cipher_text = sub_cipher.encrypt()
        self.assertEqual(cipher_text, expected_cipher_text)
        print("Actual Output:")
        print(cipher_text)
        print("Expected Output:")
        print(expected_cipher_text)

        plain_text = [plain_text]
        sub_cipher.set_cipher_text(cipher_text)
        sub_cipher.decrypt()
        self.assertEqual(sub_cipher.plain_text, plain_text)
        print("Actual Output:")
        print(sub_cipher.plain_text)
        print("Expected Output:")
        print(plain_text)
        print("Test Finished: Initial Encryptand Decrypt Alphabetic 3 in test_substituion_cipher_encrypt\n")

    def test_substituion_cipher_encrypt_and_decrypt_4(self):
        print("Initial Encrypt and Decrypt Alphabetic 4")
        plain_text = "I came to town to find a free heart but only got to the border"
        expected_cipher_text = ["V pnzr gb gbja gb svaq n serr urneg ohg bayl tbg gb gur obeqre"]
        key = "845"
        sub_cipher = substitution(key, plain_text, None, "alphabetic")
        cipher_text = sub_cipher.encrypt()
        self.assertEqual(cipher_text, expected_cipher_text)
        print("Actual Output:")
        print(cipher_text)
        print("Expected Output:")
        print(expected_cipher_text)
        print("Test Finished: Initial Encryptand Decrypt Alphabetic 4 in test_substituion_cipher_encrypt\n")

        plain_text = [plain_text]
        sub_cipher.set_cipher_text(cipher_text)
        sub_cipher.decrypt()
        self.assertEqual(sub_cipher.plain_text, plain_text)
        print("Actual Output:")
        print(sub_cipher.plain_text)
        print("Expected Output:")
        print(plain_text)
        print("Test Finished: Initial Encryptand Decrypt Alphabetic 4 in test_substituion_cipher_encrypt\n")

if __name__ == '__main__':
    unittest.main()
