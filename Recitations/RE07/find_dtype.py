# -*- coding: utf-8 -*-

def find_dtype(atuple, data_type):
    tpl = ()
    
    for i in range(len(atuple)):
        if type(atuple[i]).__name__ == data_type:
            tpl += (atuple[i],)
    
    return tpl