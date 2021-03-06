#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce


class OrderSet(list):

    def add(self, num):
        self.append(num)
        self.sort()

    def binary_search(self, num):
        lo = 0
        hi = len(self)-1
        mid = (lo+hi) // 2
        while lo <= hi:
            if self[mid] > num:
                hi = mid-1
                mid = (lo + hi) // 2
            elif self[mid] < num:
                lo = mid+1
                mid = (lo + hi) // 2
            else:
                return True
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
            calculated.add(num)
        elif num in path:
            return num  # We have find a black hole number(group), at the same time break the loop.
        elif calculated.binary_search(num):
            return 0
        else:
            path.append(num)
            calculated.add(num)


if __name__ == '__main__':
    digits = int(input('Please enter the number of digits:'))
    start = 10**(digits-1)  # For example, the start of three-digit number is 10**(3-1)=100
    end = 10**digits-1  # For example, the end of three-digit number is 10**3-1=999
    blackHoleNumbers = set()  # Use set means we don't have to deduplicate later.
    calculated = OrderSet()
    for number in range(start, end+1):
        if not calculated.binary_search(number):
            blackHoleNumbers.add(find_black_hole_number(number))
            calculated.add(number)
    try:
        blackHoleNumbers.remove(0)  # Remove "fake" black hole number 0 caused by those no-different-digit numbers.
    except KeyError:
        pass
    print(blackHoleNumbers)
