from crypto.src.mod_inv import mod_inv
from math import log2
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
        sum_pwrs_2 = []
        while remainder != 0: #Build e via powers of 2, with the first elemnet being the largest -> 345 ->sum_pwrs_2 = [256, 64, ...]
            upper = int(log2(remainder)) # floor log base 2
            sum_pwrs_2.append(upper)
            remainder = remainder-(2**upper)

        sum = None
        if 0 in sum_pwrs_2:
            sum = P
        R = P
        for i in range (1, int(log2(multiplier)) + 1):
            R = self.add(R,R)
            if i in sum_pwrs_2:
                if sum is None:
                    sum = R
                else:
                    sum = self.add(sum, R)
        return sum
