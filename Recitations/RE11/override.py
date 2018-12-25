# -*- coding: utf-8 -*-

def override(l1, l2):
    """
    Performs the override operation on lists l1 and l2
    """
    atomic = [x[0] for x in l2]
    ovr = l2 + [x for x in l1 if x[0] not in atomic]
    return sorted(ovr)

print(override([('c','d'),('c','e'),('a','b'),('a', 'd')],[('a','c'),('b','d')]))