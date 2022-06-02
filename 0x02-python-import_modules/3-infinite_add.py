#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    s = 0
    for i in range(length):
        s += int(sys.argv[i + 1])
    print("{:d}".format(s))
