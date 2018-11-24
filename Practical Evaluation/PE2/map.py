# -*- coding: utf-8 -*-

def map(pos, steps):
    l_steps = steps.split("-")
    
    for step in l_steps:
        if step == "up":
            pos = (pos[0], pos[1] + 1)
        elif step == "down":
            pos = (pos[0], pos[1] - 1)
        elif step == "right":
            pos = (pos[0] + 1, pos[1])
        elif step == "left":
            pos = (pos[0] - 1, pos[1])
    
    return pos