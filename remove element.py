#! /usr/bin/env python


def solution(nums, val):
    for i in range(nums.count(val)):
        nums.remove(val)
    return nums


print(solution([3,2,2,3], 3))
