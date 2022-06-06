#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_ist = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            bool_ist[count] = True
        else:
            bool_ist[count] = False
    return(bool_ist)
