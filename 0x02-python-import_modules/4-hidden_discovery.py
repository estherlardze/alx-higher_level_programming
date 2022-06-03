#!/usr/bin/python3
import hidden_4


def discovr():
    names = dir(hidden_4)
    for i in names:
        if i[:2] != '__':
            print("{:s}".format(i))


if __names__ == "__main__":
    discovr()
