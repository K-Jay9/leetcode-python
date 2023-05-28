#! /usr/bin/env python

def singleNumber(nums):
    for i in range(len(nums)):
        if nums.count(nums[i]) != 2:
            return nums[i]


print(singleNumber([1,2,2]))
