# Title: Diffie-Hellman Key Exchange
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/20/2020
# Associated Book Page Nuber: 67

# INPUT(s) -
# g - type: int, desc: generator
# private_key - type: int, desc: private key, a
# p - type: int, desc: modulus for this, should be prime, hence p
# B - type: int, desc: other person's public key, g^b mod p
# A - type: int, desc: my public key created from my private key, g^a mod p
#symmetric_key - type: int, desc: the shared key between you and the other person

from crypto.src.fast_power import fast_power

class diffie_hellman: #The major return value of this class is the symmetric_key which can be used in AES and DES
    def __init__(self, g=None, private_key=None, p=None, B=None, A=None, symmetric_key=None):
        self.set_generator(g)
        self.set_private_key(private_key)
        self.set_modulus(p)
        self.set_public_key(B)
        if A is not None:
            self.set_my_public_key(A)
        else:
            self.gen_my_public_key(self.g, self.private_key, self.p)
        self.set_symmetric_key(symmetric_key)

    def set_generator(self, g):
        self.g = g

    def set_private_key(self, private_key):
        self.private_key = private_key

    def set_modulus(self, p):
        self.p = p

    def set_my_public_key(self, A):
        self.A = A

    def set_public_key(self, B):
        self.B = B

    def set_symmetric_key(self, symmetric_key):
        self.symmetric_key = symmetric_key

    def gen_my_public_key(self, g=None, private_key=None, p=None):
        if g is not None: self.set_generator(g)
        if private_key is not None: self.set_private_key(private_key)
        if p is not None: self.set_modulus(p)
        if None not in (self.g, self.private_key, self.p):
            self.A = fast_power(self.g, self.private_key, self.p)
            return self.A
        else:
            return None

    def get_public_key(self):
        return self.A

    def gen_symmetric_key(self, B=None, private_key=None, p=None):
        if B is not None: self.set_public_key(B)
        if private_key is not None: self.set_private_key(private_key)
        if p is not None: self.set_modulus(p)
        if None not in (self.B, self.private_key, self.p):
            self.symmetric_key = fast_power(self.B, self.private_key, self.p)
            return self.symmetric_key
        else:
            return None
