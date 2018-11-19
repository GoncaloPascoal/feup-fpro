#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:39:29 2018

@author: exame
"""

ts = int(input("Enter the swimming time, in hours:"))
tc = int(input("Enter the cycling time, in hours:"))
tr = int(input("Enter the running time, in hours:"))

if (ts + tc + tr) > 4:
    print("Time")
elif (1.5 / ts) < 2:
    print("Swimming")
elif (40 / tc) < 20:
    print("Cycling")
elif (10 / tr) < 8:
    print("Running")
else:
    print(ts + tc + tr)