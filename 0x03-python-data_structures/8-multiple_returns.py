#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence[:1] == "":
        return None
    length = len(sentence)
    first = sentence[:1]

    return length, first
