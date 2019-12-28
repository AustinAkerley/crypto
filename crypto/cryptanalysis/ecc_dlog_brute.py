from crypto.ecc.curve import curve

def ecc_dlog_brute(P, R, E):
    if P == R:
        return 1;
    Q = P;
    for i in range(2, E.modulus):
        Q = E.add(Q, P);
        if Q == R:
            return i;
    
    return None;