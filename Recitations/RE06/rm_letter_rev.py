# -*- coding: utf-8 -*-

def rm_letter_rev(l, astr):
    astr = astr.replace(l, "")
    return astr[::-1]