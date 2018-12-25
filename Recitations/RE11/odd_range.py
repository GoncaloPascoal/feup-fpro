# -*- coding: utf-8 -*-

def odd_range(start, stop, step):
    if start % 2 == 0:
        start += 1
    for x in range(start, stop, step * 2):
        yield x

print([i for i in odd_range(100, 150, 5)])