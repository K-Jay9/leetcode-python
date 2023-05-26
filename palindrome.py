#!/usr/bin/env python



def solution(num):
    string = str(num)
    isOdd = (len(string)%2 != 0)
    if isOdd:
        second_half = string[len(string)//2+1:]
        first_half = string[:len(string)//2]
        return first_half == second_half[::-1]
    else:
        second_half = string[len(string)//2:]
        first_half = string[:len(string)//2]
        return first_half == second_half[::-1]



print(solution(1321))
print(solution(1221))
print(solution(121))
print(solution(11))
