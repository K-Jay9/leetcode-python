#! /usr/bin/env python

def solution(array):
    diff = []
    indexer = 0
    for i in range(1, len(array)+1):
        diff.append(len(set(array[:indexer+1]))-len(set(array[i:])))
        indexer += 1
    return diff

if __name__ == "__main__":
    print(solution([1,2,3,4,5]))
