# -*- coding: utf-8 -*-

def formal(name):
    names = name.split(" ")
    
    formal_name = names[-1] + ", "
    
    for i in range(len(names) - 1):
        formal_name += (names[i])[:1] + ". "
    
    return formal_name.strip()