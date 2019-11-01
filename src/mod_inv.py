import eea

def mod_inv(a, m): #Where a*b = 1 mod(m)
    inv = eea.eea(m, a)
    return inv[3]
