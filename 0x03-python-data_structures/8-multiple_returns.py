#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    firstCharacter = sentence[0]
    if length == 0:
        firstCharacter = None
    return length, firstCharacter
