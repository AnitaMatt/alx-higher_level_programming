#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        k = 0
        for j in i:
            k += 1
            print("{:d}".format(j), end="")
            if k < len(i):
                print(" ", end="")
        print()
