#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    num = []
    for a in matrix:
        num.append(list(map(lambda a: a**2, a)))
    return (num)
