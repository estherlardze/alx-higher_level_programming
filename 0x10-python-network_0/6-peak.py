#!/usr/bin/python3

""" Finds a peak in list of unsorted integers """


def find_peak(list_of_integers):
    """ find highest value """
    my_list = list_of_integers
    if my_list:
        my_list.sort()
        return my_list[-1]
    else:
        return None
