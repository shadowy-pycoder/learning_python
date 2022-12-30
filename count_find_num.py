#!#!/usr/bin/env python3

# primesL = [2, 5, 7]
# limit = 500
# List of Numbers Under 500          Prime Factorization
# ___________________________________________________________
#            70                         [2, 5, 7]
#           140                         [2, 2, 5, 7]
#           280                         [2, 2, 2, 5, 7]
#           350                         [2, 5, 5, 7]
#           490                         [2, 5, 7, 7]

# primesL = [2, 5, 7]
# limit = 500
# count_find_num(primesL, val) == [5, 490]
from functools import reduce
from operator import mul
from itertools import combinations_with_replacement


def count_find_num(primesL: list[int], limit: int) -> list[int]:
    '''
    Returns a number of possible numbers below a certain limit that can be 
    generated with given prime numbers and maximum number.
    '''
    primes = sorted(primesL)
    min_length = len(primes)
    results = list()
    shortest = primes[0]
    suffix = primes[1:]
    results.extend(suffix)
    product = reduce(mul, [prime for prime in suffix], 1)
    k = 1
    while True:
        result = shortest ** k * product
        if result < limit:
            results.append(shortest)
            k += 1
        else:
            max_length = len(results) + 1
            results.clear()
            break
    for i in range(min_length, max_length):
        for combo in combinations_with_replacement(primes, i):
            if len(set(combo)) >= min_length:
                result = reduce(mul, combo)
                if result <= limit:
                    results.append(result)
    return [len(results)] + [max(results)] if results else []


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
