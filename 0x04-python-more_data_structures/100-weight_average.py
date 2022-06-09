#!/usr/bin/python3
def weight_average(my_list=[]):
    my_list = list(my_list)
    if len(my_list) == 0:
        return 0

    average = 0
    j_list = 0
    for i in my_list:
        j_list += i[0] * i[1]
        average += i[1]
    return j_list / average
