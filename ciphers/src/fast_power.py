# Author: Austin Akerley
# Date Last Edited: 10/31/2019
#
from math import log2
def fast_power(x, e, m, known_powers): #solivng for x^e (mod m) = result, where known_powers is a dictionary of powers and there result for the same x and m
    #Fermatts little theorem addition
    # TODO: Add a check to see if m is prime.
    if e == m:
        return 0
    elif e == m-1:
        return 1

    remainder = e
    sum_pwrs_2 = []
    while remainder != 0: #Build e via powers of 2, with the first elemnet being the largest -> 345 ->sum_pwrs_2 = [256, 64, ...]
        upper = int(log2(remainder)) # floor log base 2
        sum_pwrs_2.append(upper)
        remainder = remainder-(2**upper)

    if known_powers is not None:
        result = 1
        for i in range(0, sum_pwrs_2[0]+1):
            if i not in known_powers.keys(): #added needed values to known powers
                if i == 1:
                    known_powers.update({1:x})
                else:
                    j = i/2
                    not_in_known_powers = []
                    while j not in known_powers.keys():
                        not_in_known_powers.append(j)
                    y = known_powers.get(j)
                    for k in range(len(not_in_known_powers)-1, -1, -1):
                        known_powers.update({not_in_known_powers[k]:(y*y)%m)})

            #Values needed are already in known known_powers
            result = (result*known_powers.get(i)) % m
        return result, known_powers


    else:
        known_powers = {}
        result = 1
        square = x
        for i in range(0, sum_pwrs_2[0]+1):
            if i in sum_pwrs_2:
                known_powers.update({i})
                result = (result*square) % m
            square = (square*square) % m
        return result
