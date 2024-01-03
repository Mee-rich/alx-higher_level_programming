#!/usr/bin/python3
for ascii_low in range(ord("a"), ord("z") + 1):
    if ascii_low != ord("e") and ascii_low != ord("q"):
        print("{}".format(chr(ascii_low)), end='')
