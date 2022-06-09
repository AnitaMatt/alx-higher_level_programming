#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_dict = a_dictionary
    copy = a_dict.copy()
    for k, v in copy.items():
        if value in v:
            del a_dict[k]
    return a_dict
