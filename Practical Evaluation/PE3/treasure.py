#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:10:23 2018

@author: exame
"""

def treasure(clues):
    pos = (0,0)
    
    while pos in clues:
        new_pos = clues[pos]
        del clues[pos]
        pos = new_pos
    
    return pos

print(treasure({(0,0): (1,0), (1,0): (2,0), (2,0): (3,0)}))