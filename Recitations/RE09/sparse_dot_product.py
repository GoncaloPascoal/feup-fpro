# -*- coding: utf-8 -*-

def sparse_dot_product(dict1, dict2):
    """
    Calculates the dot product of two sparse vectors represented by dictionaries (pos: value). If a position does not appear in the dictionary, its value is 0.
    """
    result = 0
    
    for key in dict1:
        if key in dict2:
            result += dict1[key] * dict2[key]

    return result

print(sparse_dot_product({1: 3, 7: 1}, {1: 3, 7: 1})) #10