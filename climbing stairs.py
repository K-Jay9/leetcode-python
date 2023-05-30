#! /usr/bin/env python
# creates a fibonacci sequence inside a list and outputs the element at index n
def solution(n):
    res = [1,1]
    for i in range(n+1):
        res.append(res[-1]+res[-2])
    return res[n]


print(solution(2))
print(solution(3))
print(solution(45))
