# -*- coding: utf-8 -*-

def triplet(atuple):
    indexes = ()
    triplets = ()
    
    lowest_idx = 0
    
    for a in range(len(atuple)):
        for b in range(len(atuple)):
            for c in range(len(atuple)):
                if a != b and b != c and a != c and atuple[a] + atuple[b] + atuple[c] == 0:
                    indexes = ((a, b, c),)
                    triplets += ((atuple[a], atuple[b], atuple[c]),)
    
    if len(triplets) == 0:
        return ()
    
    for i in range(len(indexes)):
        for j in range(len(indexes)):
            if i != j and indexes[i] < indexes[j]:
                lowest_idx = i
    
    return triplets[lowest_idx]