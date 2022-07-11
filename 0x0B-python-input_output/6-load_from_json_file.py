#!/usr/bin/python3
""" function that creates an Onject from a JSON file"""
import json


def load_from_json_file(filename):
    """ from json to object file"""
    with open(filename, encoding="utf-8") as fd:
        return json.load(fd)
