#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:10:25 2018

@author: exame
"""

def interleave(alist1, alist2):
    result = []
    smallest = min(alist1, alist2, key=len)
    
    for i in range(len(smallest)):
        if type(smallest[i]) is list:
            result += interleave(alist1[i], alist2[i])
        else:
            result += [alist1[i], alist2[i]]
    
    return result

print(interleave(['a','b','c'], [1,2,3,4,5]))