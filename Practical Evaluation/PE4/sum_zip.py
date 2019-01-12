#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:36:32 2019

@author: exame
"""

def sum_zip(functions, arguments):
    for arg in arguments:
        results = [func(arg) for func in functions]
        yield (results, sum(results))