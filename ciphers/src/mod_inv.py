def mod_inv(m, a): #Where a*b = 1 mod(m)
    from eea import eea
    inv = eea(a, m)
    return inv[3] % m
