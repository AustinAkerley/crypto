# Title: Jacobi Symbol
# Creator: Austin Akerley
# Date Created: 09/09/2020
# Last Editor: Austin Akerley
# Date Last Edited: 09/09/2020
# Associated Book Page Nuber: 175

# INPUT(s) -
# a - type: int, desc: the number to see if there exists a square root
# b - type: int, desc: the modulus from which you want to know if input "a" has a square root

# Formula: (a/b) = {-1, 0, 1}  1: a is a quadratic residue b, -1: a is a quadratic non-residue, 0: p divides a

def jacobi_symbol(a, b):
    if b%2 == 0 or b<1:
        raise ValueError("b must be odd and greater than 0 | b: "+str(b))

    result = None
    negative = False
    while result is None:
        #(b-1/b)
        if a == b-1:
            if b%4==3:
                negative = not negative
            if negative:
                result = -1
                break
            else:
                result = 1
                break

        #(2/b) portion
        if a==2:
            if b%8 == 3 or b%8 == 5:
                negative = not negative
            if negative:
                result = -1
                break
            else:
                result = 1
                break
        pow_of_2 = 0
        while a%2 == 0:
            a = a/2
            pow_of_2+=1
        if (b%8 == 3 or b%8 == 5) and pow_of_2>0 and pow_of_2%2==0:
            negative = not negative

        #(a/b) portion
        if a%4==1 or b%4==1:
            new_a = b%a
            b = a
            a = new_a
        else:
            new_a = b%a
            b = a
            a = new_a
            negative = not negative
    return result
