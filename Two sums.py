#! /usr/bin/env python

def solution(nums , target):
    original = nums.copy()
    indx, indy = 0,0
    for i in range(len(original)):
        indx = original[i]
        for j in range(len(original)):
            indy = original[j]
            total = indx + indy
            if total == target and i != j:
                return [i,j]
                break

    return []


b = [3,4,2]
print(solution(b, 6))



