# Title: Elliptic Curve
# Creator: Austin Akerley
# Date Created: 12/25/2019
# Last Editor: Austin Akerley
# Date Last Edited:12/28/2019
# Associated Book Page Nuber: XXXXXXXX

from math import log2
import random
from crypto.src.mod_inv import mod_inv
from crypto.src.fast_power import fast_power
from crypto.src.mod_sqrt import mod_sqrt

class curve:
    def __init__(self, A, B, modulus = None): # Curve is y^2 = x^3 + A*x + B
        self.A = A
        self.B = B
        self.modulus = modulus
        self.divisor = None
        self.l = int(modulus.bit_length() / 2)
        self.max_msg = 0
        for _ in range(0, self.l):
            self.max_msg = (self.max_msg << 1) | 1
    
    def is_point_on_curve(self, P):
        if isinstance(P, int):
            P = self.get_point(P)
            if P is None:
                return False
        return (P[1] ** 2) == (fast_power(P[0], 3, self.modulus).get("result") + (self.A * P[0] % self.modulus) + self.B)

    def get_point(self, x):
        y2 = fast_power(x, 3, self.modulus).get("result") + (self.A * x % self.modulus) + self.B
        y = mod_sqrt(y2, self.modulus)
        if y is None: return None;
        return (x, y[0])
    
    def msg_to_point(self, m):
        if m > self.max_msg:
            return None
        P = None
        found_point = False
        while not found_point:
            r = random.randint(1, self.max_msg)
            r = (r << self.l) | m
            P = self.get_point(r)
            if P is not None and self.is_point_on_curve(P):
                found_point = True
        return P
    
    def point_to_msg(self, P):
        if isinstance(P, tuple):
            P = P[0]
        return P & self.max_msg;

    def slope(self, P, Q): # Where P and Q are tuples
        if P == Q:
            inv_2y_p = mod_inv(2*P[1], self.modulus)
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
