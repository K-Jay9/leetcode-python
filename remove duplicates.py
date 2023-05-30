#! /usr/bin/env python



def solution(nums):
    result = []
    for val in nums:
        for i in range(1,nums.count(val)):
            nums.remove(val)
    return len(nums)


print(solution([0,0,1,1,1,2,2,3,3,4]))
