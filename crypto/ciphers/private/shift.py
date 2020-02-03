# Title: Shift Cipher
# Creator: Austin Akerley
# Date Created: 01/24/2020
# Last Editor: Austin Akerley
# Date Last Edited: 01/24/2020
# Associated Book Page Nuber: 1

# INPUT(s) -
# key - type: int, desc: This is the key by which to shift the plain_text
# plain_text - type: int, desc: This the plaintext in whatever structure you want to encrypt
# cipher_text - type: int, desc: This is the cipher text by which you should decrypt

class shift: # 256 ASCII mode only
    def __init__(self):
        print("Created new shift cipher")

    def encrypt(self, plain_text, key): # plain_text must be a string, key must be an int
        encoded_plain_text = self.encode(plain_text)
        encrypted_plain_text = []
        for ascii_val in encoded_plain_text:
            encrypted_plain_text.append((ascii_val+key)%256)
        cipher_text = self.decode(encrypted_plain_text)
        self.cipher_text = cipher_text
        return cipher_text

    def decrypt(self, cipher_text, key): # cipher_text must be a string, key must be an int
        encoded_cipher_text = self.encode(cipher_text)
        decrypted_cipher_text = []
        for ascii_val in encoded_cipher_text:
            decrypted_cipher_text.append((ascii_val-key)%256)
        plain_text = self.decode(decrypted_cipher_text)
        self.plain_text = plain_text
        return plain_text

    def encode(self, string):
        encoding = []
        for char in string:
            ascii_val = ord(char)
            if ascii_val>255:
                print("Error: Not an ASCII value")
                return None
            encoding.append(ascii_val)
        self.encoding = encoding
        return encoding

    def decode(self, encoding):
        string = ""
        for ascii_val in encoding:
            if ascii_val>255:
                print("Error: Not an ASCII value")
                return None
            string += chr(ascii_val)
        self.string = string
        return string
