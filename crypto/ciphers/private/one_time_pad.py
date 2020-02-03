# Title: Shift Cipher
# Creator: Austin Akerley
# Date Created: 01/24/2020
# Last Editor: Austin Akerley
# Date Last Edited: 01/24/2020
# Associated Book Page Nuber: 1

# INPUT(s) -
# key - type: int
# plain_text - type: int
# cipher_text - type: int


class one_time_pad:
    def __init__(self):
        print("Created new one time pad cipher")

    def encrypt(self, plain_text, key): 
        return (plain_text ^ key)

    def decrypt(self, cipher_text, key):
        return (cipher_text ^ key)
