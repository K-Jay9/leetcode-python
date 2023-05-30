#! /usr/bin/env python

def solution(nums,target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)

print(solution([1,2,4,6],5))
