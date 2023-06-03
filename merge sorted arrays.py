#! /usr/bin/env python


def solution(nums1, nums2,m,n):
    nums1.sort()
    temp = 0
    for i in range(m+n):
        if nums1[i] == 0:
            nums1[i] = nums2[temp]
            temp += 1
        if temp == n:
            break
    nums1.sort()
    return nums1
a = [1,2,3,0,0,0]
b = [2,5,6]
m = len(a)
n = len(b)

print(solution(a,b,m,n))
