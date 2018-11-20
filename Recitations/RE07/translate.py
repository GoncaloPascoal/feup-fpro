# -*- coding: utf-8 -*-

def translate(astring, table):
    """
    Given a string and a tuple of pairs (a, b), replaces all occurrences of character a with b
    """
    translated = ""
    
    for char in astring:
        for pair in table:
            if char == str(pair[0]):
                translated += str(pair[1])
                break
        else:
            translated += char
    
    return translated