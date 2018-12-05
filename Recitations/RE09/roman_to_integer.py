# -*- coding: utf-8 -*-

def roman_to_integer(astring):
    """
    Given a string in roman numerals, converts it to an integer in base 10
    """
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for (idx, char) in enumerate(astring):
        if idx < (len(astring) - 1) and d[char] < d[astring[idx + 1]]:
            total -= d[char]
        else:
            total += d[char]
    
    return total

print(roman_to_integer("LXXXIV")) #84
print(roman_to_integer("XLIII")) #43
print(roman_to_integer("MMMCMXCIX")) #3999
print(roman_to_integer("")) #0 (invalid?)