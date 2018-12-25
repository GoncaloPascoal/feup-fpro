# -*- coding: utf-8 -*-

import functools

def reduce_map_filter(args):
    if type(args) is list: #Base case
        return args
    else:
        if args[0] == "reduce":
            return functools.reduce(args[1], reduce_map_filter(args[2]))
        elif args[0] == "map":
            return list(map(args[1], reduce_map_filter(args[2])))
        elif args[0] == "filter":
            return list(filter(args[1], reduce_map_filter(args[2])))

print(reduce_map_filter(("map", lambda x: 2*x, [1,2,3])))
print(reduce_map_filter(("map", lambda x: 2*x,("filter", lambda x: x%2 != 0,[1,2,3]))))
print(reduce_map_filter([1,2,3]))