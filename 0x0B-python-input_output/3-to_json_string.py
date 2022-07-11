#!/usr/bin/python3
""" function that returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """ serializes an object i.e python to JSON"""
    return json.dumps(my_obj)
