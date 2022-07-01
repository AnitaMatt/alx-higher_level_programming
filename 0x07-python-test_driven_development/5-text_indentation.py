#!/usr/bin/python3
"""fn that prints a text with 2 new lines after each of these: ., ? and :"""
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    length = len(text)
    i = 0

    while i < length:
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            print("\n")
            i += 1
        i += 1
