# -*- coding: utf-8 -*-

def isomorphic(astring1, astring2):
    """
    Determines if two strings are isomorphic (characters in first string can be remapped to characters in second string).
    If true, returns a list of tuples with all remapped characters.
    """

    if len(astring1) != len(astring2):
        return "'{0}' and '{1}' are not isomorphic".format(astring1, astring2)
    else:
        d = {}
        for (idx, char) in enumerate(astring1):
            if char not in d:
                if astring2[idx] not in d.values():
                    d[char] = astring2[idx]
                else:
                    return "'{0}' and '{1}' are not isomorphic".format(astring1, astring2)
            elif astring2[idx] != d[char]:
                return "'{0}' and '{1}' are not isomorphic".format(astring1, astring2)
        
        return "'{0}' and '{1}' are isomorphic because we can map: {2}".format(astring1, astring2, list(d.items()))

print(isomorphic("ab", "aa"))
print(isomorphic("foo", "bar"))
print(isomorphic("paper", "title"))