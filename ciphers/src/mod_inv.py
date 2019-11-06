from eea import eea

def mod_inv(m, a): #Where a*b = 1 mod(m)
    inv = eea(a, m)
    return inv[3] % m
