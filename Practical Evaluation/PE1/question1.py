#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:10:37 2018

@author: exame
"""

num = int(input("Enter a 3 digit number:"))
temp = num

sum_cubes = 0

for i in range(2, -1, -1):
    current_digit = temp // (10 ** i)
    sum_cubes += current_digit ** 3
    temp %= (10 ** i)

print(sum_cubes == num)