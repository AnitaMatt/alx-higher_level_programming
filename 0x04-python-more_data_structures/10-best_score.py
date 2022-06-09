#!/usr/bin/python3
def best_score(a_dictionary):
    a_dict = a_dictionary
    return max(a_dict, key=a_dict.get) if a_dict else None
