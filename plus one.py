#! /usr/bin/env python

def solution(nums):
    num =''.join(str(i)for i in nums)
    num_s = str(int(num) + 1)
    res = []
    for i in num_s:
        res.append(int(i))
    return res

print(solution([1,2,3]))
print(solution([1,3,9]))
