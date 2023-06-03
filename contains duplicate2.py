#! /usr/bin/env python

def solution(nums):
    if len(set(nums)) == len(nums):
        return False
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] and abs(i - j) <= k and i != j:
                return True
    return False

