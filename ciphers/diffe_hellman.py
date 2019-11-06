from src.fast_power import fast_power

class diffe_hellman: #The major return value of this class is the symmetric_key which can be used in AES and DES
    g = None # generator
    private_key = None
    p = None # prime modulus
    A = None # Public domain key which is equal to g^private_key mod p
    B = None # PUblic domain key which is equal to g^(partners_private_key) mod p
    symmetric_key = None # Shared symmetric key B^a mod p

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
