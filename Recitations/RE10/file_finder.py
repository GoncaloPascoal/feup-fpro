# -*- coding: utf-8 -*-

def file_finder(dirs, file_name):
    path = dirs[0]
    if file_name in dirs[1:]:
        return path + "/" + file_name
    else:
        for item in dirs[1:]:
            if type(item) is list:
                subpath = file_finder(item, file_name)
                if subpath != None:
                    return path + "/" + subpath
    return
