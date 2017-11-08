#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
import time


def whether_in_calculated(num):
    try:  # If calculated[num] does not exist, the interpreter will raise a KeyError.
        calculated[num]
        return True
    except KeyError:
        return False


def find_black_hole_number(num):

    def sort_digits(temp, biggest=True):  # To list the number, sort the list and turn it back into a number again.
        return reduce(lambda y, z: y*10+z, sorted(map(lambda x: int(x), list(str(temp))), reverse=biggest))

    global calculated
    path = [num]  # If we find a number in path, it means a black hole number(group) has occur.
    while True:  # Run until find black hole number
        largest_version = sort_digits(num)
        smallest_version = sort_digits(num, biggest=False)
        num = largest_version-smallest_version
        if not num:  # Deal with numbers such as 1111.
            return 0
        elif num < start:  # Four-digit number 1000, f(1000)=1000-1=999, not a four-digit number
            num = num*10
        elif num in path:
            return num  # We have find a black hole number(group), at the same time break the loop.
        elif whether_in_calculated(num):  # We have to detect whether num in path before calculated. Why?
            return 0
        else:
            path.append(num)
            calculated[num] = None


if __name__ == '__main__':
    digits = int(input('Please enter the number of digits:'))
    time.clock()
    start = 10**(digits-1)  # For example, the start of three-digit number is 10**(3-1)=100
    end = 10**digits-1  # For example, the end of three-digit number is 10**3-1=999
    blackHoleNumbers = set()  # Use set means we don't have to deduplicate later.
    calculated = dict()
    for number in range(start, end+1):
        if not whether_in_calculated(number):
            blackHoleNumbers.add(find_black_hole_number(number))
            calculated[number] = None
    blackHoleNumbers.remove(0)  # Remove "fake" black hole number 0 caused by those numbers with no different digits.
    print(blackHoleNumbers, time.clock())
