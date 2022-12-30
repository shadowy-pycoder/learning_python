#!#!/usr/bin/env python3
# http://mathworld.wolfram.com/Factorial.html
# zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

# zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros


import math


def zeros(n: int) -> int:
    '''Calculates trailing zeroes of n!'''
    zero_num = 0
    if n == 0:
        return zero_num
    k_max = math.floor(math.log(n, 5)) + 1
    for k in range(1, k_max):
        zero_num += math.floor(n / math.pow(5, k))
    return zero_num


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
assert zeros(12) == 2
