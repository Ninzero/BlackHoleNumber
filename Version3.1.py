#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
import time


def candidates():
    yield start
    candidate = [int(e) for e in str(start)]  # Turn start into a list of digits.
    while (candidate[0], candidate[-1]) != (9, 9):  # This means its the end of this generator, six-digit, 999999.
        for i in range(1, digits+1):
            if i == digits:  # At the first digit, no need to worry it's 9.
                candidate[-i] += 1
                for x in range(1, i):  # Change all the digits behind it to 0.
                    candidate[-x] = 0
            else:
                if candidate[-i]+1 > candidate[-i-1]:  # Make shall it's reverse order.
                    continue
                else:
                    candidate[-i] += 1
                    for x in range(1, i):
                        candidate[-x] = 0
                    break
        yield reduce(lambda y, z: y*10+z, candidate)  # Return an integer instead of a list.


def riddle(num_list):  # Calculate every number only once, that's why it is called riddle.
    return set(map(lambda x: sort_digits(x)-sort_digits(x, biggest=False), num_list))


def sort_digits(temp, biggest=True):  # To list the number, sort the list and turn it back into a number again.
    return reduce(lambda y, z: y*10+z, sorted(map(lambda x: int(x), list(str(temp))), reverse=biggest))


if __name__ == '__main__':
    digits = int(input('Please enter the number of digits:'))
    time.clock()
    start = 10**(digits-1)  # For example, the start of three-digit number is 10**(3-1)=100
    end = 10**digits-1  # For example, the end of three-digit number is 10**3-1=999
    blackHoleNumbers = candidates()
    oldLength = 0
    while True:
        blackHoleNumbers = riddle(blackHoleNumbers)
        newLength = len(blackHoleNumbers)
        if newLength == oldLength:
            if len(riddle(blackHoleNumbers)) == newLength:
                break
        oldLength = len(blackHoleNumbers)
    blackHoleNumbers.remove(0)  # Remove "fake" black hole number 0 caused by those numbers with no different digits.
    print(blackHoleNumbers, time.clock())
