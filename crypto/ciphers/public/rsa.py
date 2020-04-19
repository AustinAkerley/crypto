# Title: RSA Public Key Encryption
# Creator: Austin Akerley
# Date Created: 03/07/2020
# Last Editor: Austin Akerley
# Date Last Edited: 04/19/2020
# Associated Book Page Nuber: 123


from crypto.src.fast_power import fast_power
from crypto.src.eea import eea
from crypto.src.mod_inv import mod_inv
import random

class rsa:
    def __init__(self, p = None, q = None, e = None, N = None):
        self.p = p
        self.q = q
        self.e = e
        self.N = N
        if None not in [self.p, self.q] and N is None:
            self.N = p * q

    def set_p(self, p):
        self.p = p

    def set_q(self, q):
        self.q = q

    def set_N(self, N):
        self.N = N

    def gen_e(self, p = None, q = None):
        if (p is not None):
            self.p = p
        if (q is not None):
            self.q = q
        e = 0
        while (e != 0 and eea(e, (self.p-1)*(self.q-1)).get("gcd") != 1):
            e = random.randint(3, (p-1)*(q-1))
        self.e = e
        return e

    def set_e(self, e):
        if self.q is None or self.p is None:
            raise ValueError("(self.) p and q cannot be None")
        if eea(e, (self.p-1)*(self.q-1)).get("gcd") == 1:
            self.e = e
        else:
            raise ValueError("Invalid e value, gcd of input e and (p-1)*(q-1) must be 1")

    def publish_public_info(self):
        print("e: "+str(self.e) + " | N: " + str(self.N))
        return [{"e" : self.e, "N" : self.N}]

    def encrypt(self, m, N = None, e = None):
        if N is not None:
            self.N = N
        if e is not None:
            self.e = e
        self.m = m
        if None in [self.N, self.e, self.m]:
            raise ValueError("m, e, or N is None")
        self.c = fast_power(self.m, self.e, self.N)
        return self.c

    def decrypt(self, c, p = None, q = None, e = None):
        if q is not None and p is not None:
            self.q = q
            self.p = p
            self. N = self.p * self.q
        if e is not None:
            self.e = e
        self.c = c
        if None in [self.N, self.p, self.q, self.e, self.c]:
            raise ValueError("c, e, p, q, or N is None")
        g = eea(self.p - 1, self.q-1).get("gcd")
        self.d = int(mod_inv(self.e % ((self.p-1)*(self.q-1)/g), (self.p-1)*(self.q-1)/g))
        self.m = fast_power(self.c, self.d, self.N)
        return self.m
