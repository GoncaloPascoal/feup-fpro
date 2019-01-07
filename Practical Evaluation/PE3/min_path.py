#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:10:25 2018

@author: exame
"""

def min_path(matrix, a, b, visited=[]):
    paths = []
    
    def generate_path(mx, start, end, vst):
        if start == end: # Base case
            paths.append(len(vst))
        else:
            new_vst = vst.copy()
            if start not in new_vst:
                new_vst.append(start)
            rows = list(filter(lambda x: x in range(len(mx)), range(start[0] - 1, start[0] + 2)))
            cols = list(filter(lambda x: x in range(len(mx[0])), range(start[1] - 1, start[1] + 2)))
            for i in rows:
                for j in cols:
                    if not(mx[i][j]) and (i, j) not in new_vst:
                        generate_path(mx, (i, j), b, new_vst)
            else:
                return
    
    generate_path(matrix, a, b, visited)
    
    return min(paths)

mx = [
[False, False, False, False],
[False, True, False, False],
[False, True, False, False],
[False, False, False, False]
]

print(min_path(mx, (2, 0), (0, 3)))