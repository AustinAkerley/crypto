# Title: Decode Unicode
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/19/2020
# Associated Book Page Nuber: 39
# Note: Not used anywhere, so neither should you.

# Input(s) -
# encoded_text - type: list of ints, desc: numerical representation of the message

def decode_unicode(encoded_text):
    if isinstance(encoded_text, int):
        return chr(encoded_text)
    elif isinstance(encoded_text, list):
        message = ""
        for integer in encoded_text:
            message += chr(integer)
        return message
    else:
        print("Invalid type or None type given")
        return None

# OUTPUT - type: string
# message - type: string, desc: string to convert to numerical representation
