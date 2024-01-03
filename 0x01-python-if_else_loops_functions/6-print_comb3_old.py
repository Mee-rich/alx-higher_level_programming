#!/usr/bin/python3
for num in range(0, 89):
    if num % 10 > num / 10:
        print("{:02d}, ".format(num), end='')
print("{:02d}".format(89))
