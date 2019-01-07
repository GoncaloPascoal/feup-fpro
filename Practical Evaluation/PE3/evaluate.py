#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:10:24 2018

@author: exame
"""

def evaluate(a, x):
    return sum([a[i] * (x ** i) for i in range(len(a))])

print(evaluate([1, 2, 4], 5))