# Title: Fast Power Algorithm
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/19/2020
# Associated Book Page Nuber: 24

# INPUT(s) -
# x - type: int, desc: base of the exponentiation
# e - type: int, desc: exponent
# m - type: int, desc: modulus
# known_powers - type: dictionary, desc: sum of squares, mapped to values in the number field of m, this can be the input arg from an old running of this algorithm with a different exponent

from math import log2

def fast_power(x, e, m, known_powers=None): # solvivng x^e (mod m) = result
    # Fermatts little theorem check
    if e == m:
        return {"result":0, "known_powers":None}
    elif e == m-1:
        return {"result":1, "known_powers":{}}
    remainder = e
    sum_pwrs_2 = []
    while remainder != 0: # Build e via powers of 2, with the first element being the largest -> 345 ->sum_pwrs_2 = [log2(256), log2(64), ...]
        upper = int(log2(remainder)) # Floor log base 2
        sum_pwrs_2.append(upper)
        remainder = remainder-(2**upper)
    # The idea behind known powers is to not recompute powers that are already known this will benefit things such as iterating through x^e mod m where e={0,1,2,...n} for any large n
    if known_powers or known_powers is not None:
        result = 1
        for i in range(0, sum_pwrs_2[0]+1):
            if i in known_powers.keys(): # Added needed values to known powers
                #print("i: "+str(i))
                #print("square: " + str(known_powers.get(i)))
                if i in sum_pwrs_2:
                    result = (result*known_powers.get(i)) % m
            else:
                if i == 0:
                    known_powers.update({0:x})
                else:
                    last_i = known_powers.get(i-1)
                    last_i_squared = (last_i * last_i) % m
                    known_powers.update({i:last_i_squared})
                if i in sum_pwrs_2:
                    result = (result*known_powers.get(i)) % m
        return {"result":result, "known_powers":known_powers}
    else:
        known_powers = {}
        result = 1
        square = x
        for i in range(0, sum_pwrs_2[0]+1):
            if i in sum_pwrs_2:
                result = (result*square) % m
            known_powers.update({i:square})
            square = (square*square) % m
        return {"result":result, "known_powers":known_powers}

# OUTPUT - type: dictionary
# {
#     "result" - type: int, desc: this is the actual result of the exponentiation
#     "known_powers" - type: dictionary, desc: known_powers is a mapping of the log2 of the sum of squares representation, and the value of the sum of squares
# }
