from crypto.src.fast_power import fast_power

def mod_sqrt(a, modulus):
    
    if modulus % 2 == 0:
        print("suck a dick")
        return None
    
    if modulus % 8 == 1:
        print("1");
    elif modulus % 8 == 3 or modulus % 8 == 7:
        x0 = fast_power(a, (modulus + 1) / 4, modulus).get("result");
        x1 = fast_power(-a, (modulus + 1) / 4, modulus).get("result");
        return (x0, x1);
    elif modulus % 8 == 5:
        print("5");
    else: # bad
        return None;