# -*- coding: utf-8 -*-

def calculator(expr):
    """
    Given an expression expr, represented by an integer or a nested tuple (tuple/integer, operation, tuple/integer), calculates the result of the expression.
    Valid operations are addition (+), subtraction (-) and multiplication (*).
    """
    if type(expr) is int: #Base case
        return expr
    else:
        if expr[1] == '+':
            return calculator(expr[0]) + calculator(expr[2])
        elif expr[1] == '-':
            return calculator(expr[0]) - calculator(expr[2])
        elif expr[1] == '*':
            return calculator(expr[0]) * calculator(expr[2])
