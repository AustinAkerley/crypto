# Title: RSA Digital Signature
# Creator: Austin Akerley
# Date Created: 09/09/2020
# Last Editor: Austin Akerley
# Date Last Edited: 09/09/2020
# Associated Book Page Nuber: 197

from crypto.src.fast_power import fast_power
from crypto.src.eea import eea
from crypto.src.mod_inv import mod_inv
from crypto.src.random_prime import random_prime
import random

class rsa_sig:
    def __init__(self, p = None, q = None, e = None, N = None):
        self.p = p
        self.q = q
        self.e = e
        self.N = N
        if None not in [self.p, self.q] and N is None:
            self.N = p *

    def set_p(self, p):
        self.p = p

    def set_q(self, q):
        self.q = q

    def set_N(self, N):
        self.N = N

    def set_pub_key(self, N):
        self.N = N

    def get_N(self):
        return N

    def set_e(self, e):
        if self.q is None or self.p is None:
            raise ValueError("(self.) p and q cannot be None")
        if eea(e, (self.p-1)*(self.q-1)).get("gcd") == 1:
            self.e = e
        else:
            raise ValueError("Invalid e value, gcd of input e and (p-1)*(q-1) must be 1")

    def gen_keys(self, N_num_bits):
        self.p = random_prime(int(N_num_bits/2))
        self.q = random_prime(int(N_num_bits/2))
        self.N = self.p * self.q

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

    def gen_d(self):
        self.d = mod_inv(self.e % ((self.p-1)*(self.q-1)/g), (self.p-1)*(self.q-1)/g)

    def publish_public_info(self):
        print("e: "+str(self.e) + " | N: " + str(self.N))
        return {"e" : self.e, "N" : self.N}
