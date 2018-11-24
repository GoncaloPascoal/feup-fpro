# -*- coding: utf-8 -*-

def fibonacci(n):
    return int(((1 + 5 ** 0.5) ** n - (1 - 5 ** 0.5) ** n) / (2 ** n * 5 ** 0.5))

def caesar(message):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encoded = ""
    
    for i in range(len(message)):
        if message[i].isalpha():
            shift = fibonacci(i) % 26
            idx = alphabet.index(message[i])
            encoded += alphabet[idx - shift]
        else:
            encoded += message[i]
    
    return encoded