# Title: Elliptic Cujrve Diffie-Hellman Key Exchange
# Creator: Daniel Gerthe
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited:12/28/2019
# Associated Book Page Nuber: XXXXXXXX

import random
from crypto.ecc.curve import curve
from crypto.src.mod_sqrt import mod_sqrt

class ecc_diffie_hellman(object):
    def __init__(self, E = None, P = None):
        self.style = ["whole point", "x only"]
        self.E = E;
        if isinstance(P, int):
            y2 = (fast_power(P, 3, self.E.modulus).get("result") + (P*E.A) + E.B) % self.E.modulus
            y = mod_sqrt(y2, self.E.modulus)[0]
            P = (P,y)
        self.P = P

    def private_keygen(self):
        if self.E.modulus is None and self.E.modulus == 0:
            return None
        self.private_key = random.randint(1, self.E.modulus)
        print("Your Private Key: " + str(self.private_key))
        return self.private_key;

    def public_keygen(self, E = None, P = None, private_key = None, output_type = "x only"):
        if E is not None:
            self.E = E;
        if P is not None:
            self.P = P;
        if private_key is not None:
            self.private_key = private_key;
        if None in [self.E, self.P, self.private_key]:
            return None;
        self.QA = self.E.multiply(self.P, self.private_key);
        if output_type == self.style[0]:
            return self.QA
        elif output_type == self.style[1]:
            return self.QA[0]
        else:
            print("invalid type")
            return None

    def symmetric_keygen(self, QB = None, private_key = None, output_type = "x only" ):
        if private_key is not None:
            self.private_key = private_key
        if None in [self.E, self.private_key, QB]:
            return None;
        if isinstance(QB, int):
            y2 = (fast_power(QB, 3, self.E.modulus).get("result") + (QB*E.A) + E.B) % self.E.modulus
            y = mod_sqrt(y2, self.E.modulus)[0]
            self.QB = (QB, y)
        sym_point = self.E.multiply(QB, self.private_key)
        sym_key = sym_point[0]
        if output_type == self.style[0]:
            return sym_point
        elif output_type == self.style[1]:
            return sym_key;
        else:
            print("invalid output type")
            return None
