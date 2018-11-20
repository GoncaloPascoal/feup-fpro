# -*- coding: utf-8 -*-

def unique(atuple):
    seen = ()
    for item in atuple:
        if item not in seen:
            seen += (item,)
        
    return tuple(sorted(seen))