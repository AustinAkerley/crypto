# Title: Extended Euclidean Algorithm
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited: 02/02/2020
# Associated Book Page Nuber: 16

# INPUT(s) -
# x - type: int, desc: one of the inputs for the extended euclidean algorithm, example: 12345
# y - type: int, desc: one of the inputs for the extended euclidean algorithm, example: 75232

# Formula: gcd(x,y) = ax + by

# Conditions:
#    1.) x must be smaller than y
#    2.) x and y not equal to 0

def eea(x, y):
    if x <= 0 or y <= 0:
        raise ValueError("x or y cannot be 0 or less")

    starting_x = x
    starting_y = y
    q_l = 0
    r_l = x
    s = 0
    s_l = 1
    s_l2 = None
    t = 1
    t_l = 0
    t_l2 = None
    quotient_remainder = (None, None)
    while quotient_remainder[1] != 0:
        quotient_remainder = divmod(y, x)
        y = x
        x = quotient_remainder[1]
        t_l2=t_l
        t_l = t
        s_l2=s_l
        s_l = s
        s = (s_l2-(s_l*q_l))
        t = (t_l2-(t_l*q_l))
        q_l = quotient_remainder[0]
    return {"gcd": y, "a":s, "x":starting_x, "b":t, "y":starting_y} # a is mod inv of x

# OUTPUT - type: dictionary or None
# {
#     "gcd" - type: int, desc: gcd(x, y),
#     "a" - type: int, desc: a,
#     "x" - type: int, desc: x,
#     "b" - type: int, desc: b,
#     "y" - type: int, desc: y
# }
