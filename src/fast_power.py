import math
def fast_power(x, e, m):
    remainder = e
    sum_pwrs_2 = []
    while remainder != 0: #Build e via powers of 2
        upper = int(math.log2(remainder))
        sum_pwrs_2.append(upper)
        remainder = remainder-(2**upper)
    result = 1
    square = x
    for i in range(0, sum_pwrs_2[0]+1):
        if i in sum_pwrs_2:
            result = (result*square) % m
        square = (square*square) % m
    return result
