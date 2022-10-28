#!/usr/bin/env python3
# Write a function named collatz() that has one parameter named number. If
# number is even, then collatz() should print number // 2 and return this value.

def collatz(number=None) -> list:
    if number == None or number <= 0:
        return [None]
    if number == 1:
        return [number]
    if number % 2 == 0:
        return [number] + collatz(number // 2)
    return [number] + collatz(3 * number + 1)

print(collatz(15) == [15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1])
print(collatz() == [None])
print(collatz(1) == [1])                                
print(collatz(0) == [None])
print(collatz(-2) == [None])
print(collatz(5) == [5, 16, 8, 4, 2, 1])  
try:
    value = int(input("Insert a number: "))   
except ValueError:
    print("This is not a number")
else:
    print(collatz(value))
