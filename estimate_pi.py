# -*- coding: utf-8 -*-

import random
import math
import statistics

random.seed()

done = False

area_square = 4
needles = 1000

while (not done):
    estimates = []
    
    for i in range(100):
        needles_in_circle = 0
        needles_in_square = needles
        
        for i in range(needles):
            # Generates x and y coordinates for the needle between -1 and 1, since the center is (0,0)
            x = (random.random() * 2) - 1
            y = (random.random() * 2) - 1
            # If the distance to the center is less than or equal to 1, the needle is inside the circle
            if (math.sqrt(x**2 + y**2) <= 1):
                needles_in_circle += 1
    
        area_circle = (area_square * needles_in_circle) / needles_in_square
        estimates.append(area_circle)
    
    average = sum(estimates) / 100
    print(average)
    standard_deviation = statistics.stdev(estimates)
    
    if (standard_deviation < 0.005):
        done = True
    else:
        needles *= 2

print("The estimated value for pi is ", average)
print(needles, " needles were used in the final estimation")