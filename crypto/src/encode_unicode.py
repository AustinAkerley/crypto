# Title: Encode Unicode
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited:12/28/2019
# Associated Book Page Nuber: XXXXXXXX

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
