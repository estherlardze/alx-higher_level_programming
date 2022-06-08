#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    result1 = 0
    result2 = 0
    for a, b in my_list:
        result1 += a * b
        result2 += b
    return (result1 / result2)
