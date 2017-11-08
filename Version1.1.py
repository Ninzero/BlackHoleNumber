#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
import time
import random


def find_black_hole_number(num):

    def sort_digits(temp, biggest=True):  # To list the number, sort the list and turn it back into a number again.
        return reduce(lambda y, z: y*10+z, sorted(map(lambda x: int(x), list(str(temp))), reverse=biggest))

    path = [num]  # If we find a number in path, it means a black hole number(group) has occur.
    while True:  # Run until find black hole number
        largest_version = sort_digits(num)
        smallest_version = sort_digits(num, biggest=False)
        num = largest_version-smallest_version
        if not num:
            return 0
        elif num < start:
            num = num*10
        elif num in path:
            return num  # We have find a black hole number(group), at the same time break the loop.
        else:
            path.append(num)


if __name__ == '__main__':
    digits = int(input('Please enter the number of digits:'))
    time.clock()
    start = 10**(digits-1)  # For example, the start of three-digit number is 10**(3-1)=100
    end = 10**digits-1  # For example, the end of three-digit number is 10**3-1=999
    blackHoleNumbers = set()  # Use set means we don't have to deduplicate later.
    for x in range(100000):
        number = random.randint(start, end)
        blackHoleNumbers.add(find_black_hole_number(number))
    try:
        blackHoleNumbers.remove(0)  # Remove "fake" black hole number 0 caused by numbers with no different digits.
    except KeyError:
        pass
    timeSpend = time.clock()
    timeEstimate = timeSpend/100000*(end-start+1)
    print(timeSpend)
    print(timeEstimate)
