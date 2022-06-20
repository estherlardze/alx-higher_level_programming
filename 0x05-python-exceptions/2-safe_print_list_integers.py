#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    num = printed_ints = 0
    while True:
        try:
            if num < x:
                print("{:d}".format(my_list[num]), end='')
                num += 1
                new_val += 1
            else:
                print()
                return new_val
        except (ValueError, TypeError):
            num += 1
