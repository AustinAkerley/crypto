# Title: Elliptic Cujrve El Gammal Cipher
# Creator: Austin Akerley
# Date Created: 12/30/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/20/2020
# Associated Book Page Nuber: 319

# INPUT(s) -
# E - type: curve, desc: the elliptic curve which to do the mathsss on
# P - type: tuple, desc: the shared public pointd

import random
from crypto.ecc.src.curve import curve
from crypto.src.mod_sqrt import mod_sqrt
from crypto.src.fast_power import fast_power

class ecc_el_gammal:
    def __init__(self, E, P):
        self.E = E
        self.style = ["whole point", "x only"]
        if isinstance(P, int):
            y2 = (fast_power(P, 3, self.E.modulus) + (P*self.E.A) + self.E.B) % self.E.modulus
            y = mod_sqrt(y2, self.E.modulus)[0]
            self.P = (P,mod_sqrt(y, self.E.modulus)[0])
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
            if isinstance(P, int):
                y2 = (fast_power(P, 3, self.E.modulus) + (P*self.E.A) + self.E.B) % self.E.modulus
                y = mod_sqrt(y2, self.E.modulus)[0]
                self.P = (P,mod_sqrt(y, self.E.modulus)[0])
            self.P = P
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

    def encrypt(self, plain_text, QB, E = None, P = None, output_type = "x only"):
        if E is not None:
            self.E = E
        if P is not None:
            if isinstance(P, int):
                y2 = (fast_power(P, 3, self.E.modulus) + (P*self.E.A) + self.E.B) % self.E.modulus
                y = mod_sqrt(y2, self.E.modulus)[0]
                self.P = (P,mod_sqrt(y, self.E.modulus)[0])
            self.P = P
        if QB is not None:
            if isinstance(QB, int):
                y2 = (fast_power(QB, 3, self.E.modulus) + (QB*self.E.A) + self.E.B) % self.E.modulus
                y = mod_sqrt(y2, self.E.modulus)[0]
                QB = (QB, mod_sqrt(y, self.E.modulus)[0])

        M = self.E.msg_to_point(plain_text)

        k = random.randint(1, self.E.modulus)

        C1 = self.E.multiply(k,P)
        C2 = self.E.add(M, E.multiply(k, QB))
        if output_type == self.style[0]:
            return (C1, C2)
        elif output_type == self.style[1]:
            return (C1[0], C2[0])
        else:
            print("Invalid type")
            return None

    def decrypt(self, c1, c2, QA = None):
        if QA is not None:
            self.QA = QA
        if isinstance(c1, int):
            y2 = (fast_power(c1, 3, self.E.modulus) + (c1*self.E.A) + self.E.B) % self.E.modulus
            y = mod_sqrt(y2, self.E.modulus)[0]
            c1 = (c1, y)
        if isinstance(c2, int):
            y2 = (fast_power(c2, 3, self.E.modulus) + (c2*self.E.A) + self.E.B) % self.E.modulus
            y = mod_sqrt(y2, self.E.modulus)[0]
            c2 = (c2, y)

        param2 =  self.E.multiply(self.private_key, c1)
        param2[1] = -param2[1]
        return self.E.point_to_msg(self.E.add(c2,param2))
