#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:36:21 2019

@author: exame
"""

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        while max(a, b) % min(a, b) != 0:
            if a == max(a, b):
                a = a % b
            else:
                b = b % a
    return min(a, b)