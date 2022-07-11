#!/usr/bin/python3
"""function that inserts a line of text to a file
   after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """append new string after each search string"""
    new_content = ""
    with open(filename, encoding="utf-8") as fd:
        for line in fd:
            new_content += line
            if search_string in line:
                new_content += new_string
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(new_content)
