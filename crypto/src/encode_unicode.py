# Title: Encode Unicode
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/19/2020
# Associated Book Page Nuber: 39
# Note: Not used anywhere, so neither should you.

# Input(s) -
# message - type: string, desc: string to convert to numerical representation

def encode_unicode(message): # Converts a string of text or a character of text to a list of integers or an integer in the case of 1 character
    encoded_text = []
    if message is None:
        encoded_text = None
    elif not isinstance(message, str):
        print("message is not of type string returning None")
        encoded_text = None
    else:
        for char in message:
            encoded_text.append(ord(char))
    return encoded_text

# OUTPUT - type: list
# encoded_text - type: list of ints, desc: numerical representation of the message
