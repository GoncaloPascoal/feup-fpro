#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:36:31 2019

@author: exame
"""

def maximum_depth(l):
    list_depths = []
    
    def rec_depth(lst, ld, d=1):
        for item in lst:
            if type(item) is list:
                ld.append(d + 1)
                rec_depth(item, ld, d + 1)
        return d
    
    rec_depth(l, list_depths)
    
    try:
        return max(list_depths)
    except:
        return 1