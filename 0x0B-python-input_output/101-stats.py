#!/usr/bin/python3
import sys


def print_status():
    '''
        Printing the status of the request
    '''
    pro_counter = 0
    size_of_script = 0
    file_size = 0
    codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    for l in sys.stdin:
        line = l.split()
        try:
            size_of_script += int(line[-1])
            code = line[-2]
            codes[code] += 1
        except:
            continue
        if pro_counter == 9:
            print("File size: {}".format(size_of_script))
            for key, val in sorted(codes.items()):
                if (val != 0):
                    print("{}: {}".format(key, val))
            pro_counter = 0
        pro_counter += 1
    if pro_counter < 9:
        print("File size: {}".format(size_of_script))
        for key, val in sorted(codes.items()):
            if (val != 0):
                print("{}: {}".format(key, val))


if __name__ == "__main__":
    print_status()
