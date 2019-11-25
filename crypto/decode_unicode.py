# Author: Austin Akerley
# Date Last Edited: 10/31/2019
#
def decode_unicode(lst_of_ints):
    if isinstance(lst_of_ints, int):
        return chr(lst_of_ints)
    elif isinstance(lst_of_ints, list):
        result = ""
        for integer in lst_of_ints:
            result += chr(integer)
        return result
    else:
        print("Invalid type or None type given")
        return None
