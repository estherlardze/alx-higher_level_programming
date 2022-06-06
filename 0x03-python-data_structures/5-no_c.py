#!/usr/bin/python3
def no_c(my_string):
    tmp_str = ""
    for i in my_string:
        if i is not 'c' and i is not 'C':
            tmp_str += i
    return (tmp_str)
# return my_string.translate({ord(c): None for c in "cC"})
