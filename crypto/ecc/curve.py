# Title: Elliptic Curve
# Creator: Austin Akerley
# Date Created: 12/25/2019
# Last Editor: Austin Akerley
# Date Last Edited:12/28/2019
# Associated Book Page Nuber: XXXXXXXX

from math import log2
from crypto.src.mod_inv import mod_inv

class curve:
    def __init__(self, A, B, modulus = None): # Curve is y^2 = x^3 + A*x + B
        self.A = A
        self.B = B
        self.modulus = modulus

    def slope(self, P, Q): # Where P and Q are tuples
        if P == Q:
            slope = (3*P[0]*P[0] + self.A) * mod_inv(2*P[1], self.modulus)
            return slope
        else:
            y_diff = (P[1]-Q[1])%self.modulus
            x_diff = (P[0]-Q[0])%self.modulus
            slope = (y_diff * mod_inv(x_diff, self.modulus))%self.modulus
            return slope

    def add(self, P, Q): # Where P and Q are tuples
        if P[0] is None and P[1] is None:
            return Q
        elif Q[0] is None and Q[1] is None:
            return P
        elif P[0] == Q[0] and P[1] == -Q[1]:
            return (None, None)
        slope = self.slope(P,Q)
        xR = (slope * slope - P[0] - Q[0] ) % self.modulus
        yR = (slope * (P[0] - xR) - P[1]) % self.modulus
        return (xR, yR)

    def multiply(self, P, multiplier):
        multiplier = multiplier % self.modulus
        remainder = multiplier
        ternary_expansion = []
        while remainder != 0:
            upper = int(log2(remainder)) # floor log base 2
            ternary_expansion.append(upper)
            remainder = remainder-(2**upper)

        sum_pt = None
        if 0 in ternary_expansion:
            sum_pt = P
        R = P
        for i in range (1, int(log2(multiplier)) + 1):
            R = self.add(R,R)
            if i in ternary_expansion:
                if sum_pt is None:
                    sum_pt = R
                else:
                    sum_pt = self.add(sum_pt, R)
        return sum_pt
