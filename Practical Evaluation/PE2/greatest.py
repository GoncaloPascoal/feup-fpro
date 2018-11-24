# -*- coding: utf-8 -*-

def greatest(num):
    return int("".join(sorted(str(num), key=int, reverse=True)))