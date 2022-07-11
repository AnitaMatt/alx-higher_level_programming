#!/usr/bin/python3
""" fn that writes an Object to a text file using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """ writing to txt files"""
    with open(filename, 'w', encoding="utf-8") as fd:
        json.dump(my_obj, fd)
