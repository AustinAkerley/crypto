# Title: Brute Force Elliptic Curve Discrete Logarithm
# Creator: Daniel Gerthe
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/20/2020
# Associated Book Page Nuber: 310

# INPUT(s) -
# P - type: tuple, desc: Generator point on the curve
# R - type: tuple, desc: result of the multiplication
# E - type: curve, desc: The curve on which P and R were created

from crypto.ecc.src.curve import curve

def ecc_dlog_brute(P, R, E):
    n = None
    if P == R:
        n=1
    else:
        Q = P
        for i in range(2, E.modulus):
            Q = E.add(Q, P)
            if Q == R:
                n=i
                break
    return n

# OUTPUT - type: int
# n - type: int, desc: n where n is P*n = R, so given R and P solve backwards for n.
