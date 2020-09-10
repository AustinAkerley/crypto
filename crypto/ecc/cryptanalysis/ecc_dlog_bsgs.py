# Title: Baby Step Giant Step(bsgs) - Elliptic Curve Discrete Logarithm
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
from crypto.ecc.src.curve import curve

def ecc_dlog_bsgs(P, R, E):
    dict1 = {}
    dict2 = {}
    n = None
    ji = None;
    ki = None;
    for i in range(0, E.modulus):
        ji = random.randint(1, E.modulus-1);
        ki = random.randint(1, E.modulus-1);
        ji_P = E.multiply(P, ji)
        print("i: "+str(i))
        print("ji_P: "+str(ji_P) + "ji: " + str(ji))
        dict1.update({ji_P : ji});
        ki_P_R = E.add(E.multiply(P, ki), R)
        print("ki_P_R: "+str(ki_P_R) + "ki: " + str(ki) + "\n")
        dict2.update({ki_P_R: ki})
        #Check as you loop
        if ji_P in dict2.keys():
            n = (ji - dict2.get(ji_P)) % E.modulus
            print("ji_P: "+str(ji_P))
            break
        elif ki_P_R in dict1.keys():
            n = (dict1.get(ki_P_R) - ki) % E.modulus
            print("ki_P_R: "+str(ki_P_R))
            break
    print("\n\n\n\n")
    return n

# OUTPUT - type: int
# n - type: int, desc: n where P*n = R on Elliptic Curve E
