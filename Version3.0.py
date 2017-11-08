#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
import time


def riddle(num_list):  # Calculate every number only once, that's why it is called riddle.
    return set(map(lambda x: sort_digits(x)-sort_digits(x, biggest=False), num_list))


def sort_digits(temp, biggest=True):  # To list the number, sort the list and turn it back into a number again.
    return reduce(lambda y, z: y*10+z, sorted(map(lambda x: int(x), list(str(temp))), reverse=biggest))


if __name__ == '__main__':
    digits = int(input('Please enter the number of digits:'))
    time.clock()
    start = 10**(digits-1)  # For example, the start of three-digit number is 10**(3-1)=100
    end = 10**digits-1  # For example, the end of three-digit number is 10**3-1=999
    blackHoleNumbers = range(start, end+1)  # Use set means we don't have to deduplicate later.
    while True:
        oldLength = len(blackHoleNumbers)
        blackHoleNumbers = riddle(blackHoleNumbers)
        newLength = len(blackHoleNumbers)
        if newLength == oldLength:
            break
    blackHoleNumbers.remove(0)  # Remove "fake" black hole number 0 caused by those numbers with no different digits.
    print(blackHoleNumbers, time.clock())
