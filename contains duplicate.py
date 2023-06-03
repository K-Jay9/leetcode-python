#! /usr/bin/env python

def solution(nums):
    num_set = set(nums)
    return len(nums) != len(num_set)

print(solution([1,2,3,4,1]))
print(solution([5,6,4,7,8]))
