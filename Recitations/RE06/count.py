# -*- coding: utf-8 -*-

def count(word, phrase):
    word = word.lower()
    phrase = phrase.lower()
    
    word_list = phrase.split(" ")
    
    count = 0
    for w in word_list:
        if w == word:
            count += 1
    
    return count