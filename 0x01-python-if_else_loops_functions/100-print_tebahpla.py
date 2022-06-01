#!/usr/bin/python3
j = 122
while j >= 97:
    flag = 0
    if j % 2 != 0:
        j = j - 32
        flag = 1
    print("{:s}".format(chr(i)), end="")
    if flag == 1:
        j = j + 32
    j = j - 1
