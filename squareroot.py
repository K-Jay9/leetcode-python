#! /usr/bin/env python

# One should not use inbuilt functions: Re-Do it

from math import floor, sqrt

def solution(num):
    return floor(sqrt(num))

print(solution(8))
print(solution(1435643))
