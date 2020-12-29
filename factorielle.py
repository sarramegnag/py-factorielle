#!/usr/bin/env python3

n = int(input('Type a number, and its factorial will be printed: '))

if n < 0:
    raise ValueError('You must enter a positive integer')

fact = 1
i = 2
while i <= n:
    fact *= i
    i += 1

print(fact)