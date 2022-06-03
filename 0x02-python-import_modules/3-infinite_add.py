#!/usr/bin/python3
def add_arg(argv):
    n = len(argv) - 1
    if n == 0:
        print("{:d}".format(n))
        return
    else:
        i = 1
        addd = 0
        while i <= n:
            addd += int(argv[i])
            i += 1
        print("{:d}".format(addd))

if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
