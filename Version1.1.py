#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from CommonFunction import list2int, int2list
from CommonFunction import format_black_holes
from functools import reduce
import time
import random


def find_black_hole_number(num):
    path = [num]  # If we find a repeated number in this list, it means a black hole number(group) has occur.
    while True:
        maximum = list2int(sorted(int2list(num), reverse=True))
        minimum = list2int(sorted(int2list(num)))
        num = maximum - minimum
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
    black_hole_numbers = set()  # Use set means we don't have to deduplicate later.
    start_time = time.process_time()
    for x in range(100000):
        number = random.randint(start, end)
        black_hole_numbers.add(find_black_hole_number(number))
    try:
        black_hole_numbers.remove(0)  # Remove "fake" black hole number 0 caused by numbers with no different digits.
    except KeyError:
        pass
    stop_time = time.process_time()
    time_spent = stop_time - start_time
    estimate_time = time_spent/100000*(end-start+1)
    print(time_spent)
    print(estimate_time)
