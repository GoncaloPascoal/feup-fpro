#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:36:31 2019

@author: exame
"""

def histogram(alist, bins):
    result = []
    for i in range(len(bins) - 1):
        group = [n for n in alist if n >= bins[i] and n < bins[i + 1]]
        result.append(len(group))
    return result