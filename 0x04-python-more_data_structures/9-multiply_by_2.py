#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    sim_dict = a_dictionary.copy()
    for x in sim_dict.keys():
        sim_dict[x] *= 2
    return (sim_dict)
