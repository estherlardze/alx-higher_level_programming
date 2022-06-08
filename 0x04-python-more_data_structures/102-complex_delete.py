#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    val = []
    for key, key_value in a_dictionary.items():
        if key_value is value:
            val.append(key)
    for x in val:
        del a_dictionary[x]
    return(a_dictionary)
