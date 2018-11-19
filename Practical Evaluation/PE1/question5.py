#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:49:21 2018

@author: exame
"""

dec = int(input("Enter a decimal number:"))
octal = 0

highest_pow = 0

while dec // (8 ** highest_pow) != 0:
    highest_pow += 1

highest_pow -= 1

for i in range(highest_pow, -1, -1):
    octal_digit = dec // (8 ** i)
    octal += octal_digit * (10 ** i)
    dec -= octal_digit * (8 ** i)

print(octal)