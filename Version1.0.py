#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce


def find_black_hole_number(num):

    def list2int(a: list) -> int:
        return reduce(lambda x, y: x*10+y, a)

    def int2list(a: int) -> list:
        a = list(str(a))
        return map(lambda x: int(x), a)

    path = [num]  # If we find a repeated number in this list, it means a black hole number(group) has occur.
    while True:
        largest_combination = list2int(sorted(int2list(num), reverse=True))
        smallest_combination = list2int(sorted(int2list(num)))
        num = largest_combination - smallest_combination
        if not num:  # Deal with numbers such as 1111.
            return 0
        elif num < start:  # For example 1000, f(1000)=1000-1=999, not a four-digit number anymore.
            num *= 10
        elif num in path:
            return num  # We have found a black hole number(group).
        else:
            path.append(num)


if __name__ == '__main__':
    digits = int(input('Please enter the number of digits:'))
    start = 10**(digits-1)  # For example, the start of three-digit number is 10**(3-1)=100
    end = 10**digits-1  # For example, the end of three-digit number is 10**3-1=999
    blackHoleNumbers = set()  # Use set means we don't have to deduplicate later.
    for number in range(start, end+1):
        blackHoleNumbers.add(find_black_hole_number(number))
    blackHoleNumbers.remove(0)  # Remove "fake" black hole number 0 caused by those numbers with no different digits.
    print(blackHoleNumbers)
