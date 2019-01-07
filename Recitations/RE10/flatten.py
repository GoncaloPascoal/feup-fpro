# -*- coding: utf-8 -*-

def flatten(alist):
    """
    Given a nested list, returns a single list with each of the non-list elements.
    """
    l = []
    for i in range(len(alist)):
        if type(alist[i]) is list:
            l += flatten(alist[i])
        else:
            l += [alist[i]]
    return l
