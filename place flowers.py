#! /usr/bin/env python

def solution(flowerbed, n):
    positions = 0
    last = len(flowerbed)-1
        # return true if no flowers to be planted
    if n == 0:
        return True
    # hack using edge test cases
    if len(flowerbed) == 1 and flowerbed[0] == 0 or len(flowerbed) == 2 and flowerbed[0] == 0 and flowerbed[1] == 0:
            # can only accommodate 1 flower to be planted
        if n == 1:
            return True
        return False
    for i in range(1,len(flowerbed)-1):
            # deal with the first index
        if i == 1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
            flowerbed[i-1] = 1
            positions += 1
            # deal with the last index
        if i == last-1 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
            positions +=1
            flowerbed[i] = 1
                # deal with everything in between
        if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
            positions +=1
            flowerbed[i] = 1
    return n <= positions

print(solution([1,0,0,0,1],1))
print(solution([1,0,0,0,1],2))
