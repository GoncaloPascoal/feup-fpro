# -*- coding: utf-8 -*-

def sort_rule(item):
    return (-(sum(item[2]) / len(item[2])), item[0], item[1])

def sort_grades(records):
    return tuple(sorted(records, key=sort_rule))