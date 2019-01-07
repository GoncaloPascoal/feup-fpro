# -*- coding: utf-8 -*-

import string

def word_in_matrix(matrix, row, col, word):
    if word == "":
        return True
    else:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if row + i < len(matrix) and col + j < len(matrix[0]) and row + i >= 0 and col + j >= 0 and (i != 0 or j != 0):
                    if matrix[row + i][col + j] == word[0] and word_in_matrix(matrix, row + i, col + j, word[1:]):
                        return True
        else:
            return False

def soup(matrix, word):
    alpha = string.ascii_uppercase
    positions = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == word[0]:
                pos = alpha[i] + str(j + 1)
                if word_in_matrix(matrix, i, j, word[1:]):
                    positions.append(pos)
    
    return min(positions, key=lambda x: (x[0], int(x[1:]))) if (len(positions) != 0) else None