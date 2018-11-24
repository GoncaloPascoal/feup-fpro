# -*- coding: utf-8 -*-

def exactly(s):
    pairs = ()
    
    for (idx1, char1) in enumerate(s):
        if char1.isdecimal():
            for (idx2, char2) in enumerate(s):
                if char2.isdecimal() and int(char1) + int(char2) == 10 and idx1 < idx2:
                    if s[idx1+1:idx2].count("?") == 3:
                        pairs += (char1 + char2,)
                    else:
                        return "The sequence {0} is NOT OK with first violation with pair: {1}".format(s, (char1 + char2,))
    
    return "The sequence {0} is OK with the pairs: {1}".format(s, pairs)