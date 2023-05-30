#! /usr/bin/env python

def solution(a,b):
    total = bin(int(a,2) + int(b,2))
    return total[2:]

print(solution("11", "1"))
