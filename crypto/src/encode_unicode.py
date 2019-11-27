# Author: Austin Akerley
# Date Last Edited: 10/31/2019
#
def encode_unicode(message): # Converts a string of text or a character of text to a list of integers or an integer in the case of 1 character
    encoded_text= []
    if message is None:
        return None
    if not isinstance(message, str):
        print("message is not of type string returning None")
        return None
    for char in message:
        encoded_text.append(ord(char))
    if len(encoded_text) == 1:
        return encoded_text[0]
    else:
        return encoded_text
