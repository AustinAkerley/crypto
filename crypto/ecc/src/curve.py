# Title: Elliptic Curve
# Creator: Austin Akerley
# Date Created: 12/25/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/20/2020
# Associated Book Page Nuber: 299

# INPUT(s) -
# A - type: int, desc: coefficent of x
# B - type: int, desc: constant for the curve
# modulus - type: int, desc: modulus for the curve that defines the field it's in

import random
from math import log2
from crypto.src.mod_inv import mod_inv
from crypto.src.fast_power import fast_power
from crypto.src.mod_sqrt import mod_sqrt

class curve:
    def __init__(self, A, B, modulus): # Curve is of the mathematical form: y^2 = x^3 + A*x + B
        self.A = A
        self.B = B
        self.modulus = modulus
        self.divisor = None
        self.l = int(modulus.bit_length() / 2)
        self.max_msg = 0
        for _ in range(0, self.l):
            self.max_msg = (self.max_msg << 1) | 1

    def slope(self, P, Q): # Where P and Q are tuples
        if P == Q:
            inv_2y_p = mod_inv((2*P[1]) % self.modulus, self.modulus)
            if isinstance(inv_2y_p, tuple):
                d = inv_2y_p[1]
                return [None, None, d]
            slope = ((3*P[0]*P[0] + self.A) * inv_2y_p) % self.modulus
            return slope
        else:
            y_diff = (P[1]-Q[1])%self.modulus
            x_diff = (P[0]-Q[0])%self.modulus
            inv_x_diff  = mod_inv(x_diff, self.modulus)
            if isinstance(inv_x_diff,tuple):
                d = inv_x_diff[1]
                return [None, None, d]
            slope = (y_diff * inv_x_diff)%self.modulus
            return slope

    def add(self, P, Q): # Where P and Q are tuples
        if P[0] is None and P[1] is None:
            return Q
        elif Q[0] is None and Q[1] is None:
            return P
        elif P[0] == Q[0] and P[1] == -Q[1]:
            return (None, None)
        slope = self.slope(P,Q)
        if isinstance(slope, list):
            return slope
        xR = (slope * slope - P[0] - Q[0] ) % self.modulus
        yR = (slope * (P[0] - xR) - P[1]) % self.modulus
        return (xR, yR)

    def multiply(self, P, multiplier):
        if (multiplier == 1):
            return P
        elif (multiplier == 2):
            return self.add(P,P)
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
            if len(R) == 3:
                return R
            if i in ternary_expansion:
                if sum_pt is None:
                    sum_pt = R
                else:
                    sum_pt = self.add(sum_pt, R)
                    if len(sum_pt) == 3:
                        return sum_pt
        return sum_pt

    def calculate_y2(self, x):
        return (fast_power(x, 3, self.modulus) + (self.A*x) + self.B) % self.modulus

    def is_point_on_curve(self, P):
        y2 = self.calculate_y2(P[0])
        y = mod_sqrt(y2, self.modulus)
        if y is not (None, None):
            if y[0] == P[1] or y[1] == P[1]:
                return True
        return False

    def calculate_point(self, x):
        y2 = self.calculate_y2(x)
        y = mod_sqrt(y2)
        if y is (None, None):
            return None
        else:
            return [(x, y[0]), (x, y[1])]
