#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    if length == 0:
        print("{:d} arguments.".format(length))
    elif length == 1:
        print("{:d} argument:".format(length))
    elif length > 1:
        print("{:d} arguments:".format(length))
    for i in range(length):
        print("{:d}: {}".format(i + 1, sys.argv[i + 1]))
