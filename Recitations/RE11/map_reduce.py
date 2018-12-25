# -*- coding: utf-8 -*-

import functools

def map_reduce(n1, n2):
    l = [x ** 2 for x in range(n1, n2 + 1) if x % 2 != 0]
    return functools.reduce(lambda x,y: x * y if x * y < 50 else x + y, l)

print(map_reduce(0, 10))
print(map_reduce(5, 100))