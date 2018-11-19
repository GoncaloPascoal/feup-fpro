#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:32:33 2018

@author: exame
"""

names = ["bart", "marie", "jo"]
ages = [25, 75, 19]

pairs = ""

i = 0
for name in names:
    j = 0
    for age in ages:
        if (i == j):
            if (i != 0):
                pairs += " "
            pairs += name + "-" + str(age)
        j += 1
    i += 1

print(pairs)