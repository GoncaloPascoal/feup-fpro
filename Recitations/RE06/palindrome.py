# -*- coding: utf-8 -*-

def palindrome(astring):
    num = 0
    for i in range(2, len(astring) + 1): # Length of substring
        for j in range(len(astring) - i + 1): # Maximum starting index
            substr = astring[j:j+i]
            if substr == substr[::-1]: # Substring is a palindrome
                num += 1
    return "For string '{0}': {1} palindrome substrings".format(astring, num)