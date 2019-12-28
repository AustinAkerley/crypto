from crypto.ecc.curve import curve
import random
import math
def ecc_dlog_lsbs(P, Q, E):
    dict1 = {}
    dict2 = {}
    
    ji = None;
    ki = None;
    for _ in range(0, int(math.sqrt(E.modulus))+1):
        ji = random.randint(1, E.modulus);
        ki = random.randint(1, E.modulus);
        ji_P = E.multiply(P, ji)
        dict1.update({ji_P : ji});
        ki_P_Q = E.add(E.multiply(P, ki), Q)
        dict2.update({ki_P_Q: ki})
        
        if ji_P in dict2.keys():
            return (ji - dict2.get(ji_P)) % E.modulus
        elif ki_P_Q in dict1.keys():
            return (dict1.get(ki_P_Q) - ki) % E.modulus
    return None;