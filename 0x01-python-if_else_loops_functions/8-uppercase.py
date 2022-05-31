#!/usr/bin/python3
def uppercase(str):
    for i in str:
        s = ord(i)
        if ord(i) > 96 and ord(i) < 123:
            s = ord(i) - 32
        print("{}".format(chr(s)), end="")
    print()
