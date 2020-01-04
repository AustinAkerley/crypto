# Title: Brute Force Elliptic Curve Discrete Logarithm
# Creator: Daniel Gerthe
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited:12/28/2019
# Associated Book Page Nuber: XXXXXXXX

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
