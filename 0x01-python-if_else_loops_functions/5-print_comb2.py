#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i == 9 and j == 9:
            print("{:d}".format(i), end="")
            print("{:d}".format(j))
            break
        print("{:d}".format(i), end="")
        print("{:d}".format(j), end=", ")
