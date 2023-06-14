#! /usr/bin/env python

def solution(n):
    if n == 1: # n shouldn't be 1
        return True
    if n == 0:
        return False
    if n%2 != 0: # Remove odd numbers 
        return False
    if n&(n-1) == 0:
        return True
    return False

if __name__ == "__main__":
    print(solution(16))
    print(solution(3))
    print(solution(2147483646))

'''
Time limit is the major constraint

'''
