# -*- coding: utf-8 -*-

def sort_rule(item):
    rel = ["sibling", "parent", "cousin", "grandparent"]
    idx = rel.index(item[1])
    return (idx, item[0])

def genealogy(l):
    return sorted(l, key=sort_rule)