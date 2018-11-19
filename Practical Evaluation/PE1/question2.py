#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:22:27 2018

@author: exame
"""

d = int(input("Enter an integer with one digit:"))
num = int(input("Enter an integer:"))

sum_digits = 0

while num != 0:
    current_digit = num % 10
    if current_digit > d:
        sum_digits += current_digit
    num //= 10

print(2 * sum_digits)