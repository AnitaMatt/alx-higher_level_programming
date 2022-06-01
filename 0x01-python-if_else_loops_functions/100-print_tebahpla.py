#!/usr/bin/python3
for i in range(122,96, -1):
    s = i
    if i % 2 != 0:
        s = i - 32
    print("{}".format(chr(s)), end="")
