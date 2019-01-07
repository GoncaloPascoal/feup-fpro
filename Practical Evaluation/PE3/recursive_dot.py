#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:10:24 2018

@author: exame
"""

def recursive_dot(l1, l2):
    dp = 0
    for i in range(len(l1)):
        if type(l1[i]) is list:
            dp += recursive_dot(l1[i], l2[i])
        else:
            dp += l1[i] * l2[i]
    return dp

print(recursive_dot([2], [1]))