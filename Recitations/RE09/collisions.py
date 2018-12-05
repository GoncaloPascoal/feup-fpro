# -*- coding: utf-8 -*-

def get_hash(n):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    return s % 8

def collisions(l):
    """
    Given a list of integers l, calculates the corresponding hashes (hash = sum_digits % 8) and returns a dictionary (hash: occurences)
    """
    hashes = {}

    for item in l:
        h = get_hash(item)
        if h not in hashes:
            hashes[h] = 0
        hashes[h] += 1
    
    return hashes

print(collisions([24, 42]))
print(collisions([1, 789, 100, 9807, 1208, 92, 101]))