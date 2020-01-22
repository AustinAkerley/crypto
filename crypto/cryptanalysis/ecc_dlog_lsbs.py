# Title: Little Step Big Step(lsbs) - Elliptic Curve Discrete Logarithm
# Creator: Daniel Gerthe
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/20/2020
# Associated Book Page Nuber: 310
# WARNING: Doesn't seem to fully work yet

# INPUT(s) -
# P - type: tuple, desc: Generator point on the curve
# R - type: tuple, desc: result of the multiplication
# E - type: curve, desc: The curve on which P and R were created

import random
import math
from crypto.ecc.curve import curve

def ecc_dlog_lsbs(P, R, E):
    dict1 = {}
    dict2 = {}
    n = None
    ji = None;
    ki = None;
    for i in range(0, int(math.sqrt(E.modulus))+1):
        ji = random.randint(1, E.modulus);
        ki = random.randint(1, E.modulus);
        ji_P = E.multiply(P, ji)
        dict1.update({ji_P : ji});
        ki_P_R = E.add(E.multiply(P, ki), R)
        dict2.update({ki_P_R: ki})
        #Check as you loop
        if ji_P in dict2.keys():
            n = (ji - dict2.get(ji_P)) % E.modulus
        elif ki_P_R in dict1.keys():
            n = (dict1.get(ki_P_R) - ki) % E.modulus

    return n

# OUTPUT - type: int
# n - type: int, desc: n where P*n = R on Elliptic Curve E
