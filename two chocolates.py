#! /usr/bin/env python


def solution(prices, money):
    prices = [i for i in prices if i < money]
    if len(prices) < 2:
        return money
    prices.sort()
    res = []
    for i in range(len(prices)-1):
        left = money - prices[i]
        del prices[i]
        res = [i for i in prices if left-i >= 0]
        if len(res) == 0:
            return money
        for j in res:
            if left-j >= 0:
                return left-j

print(solution([1,2,2], 3))
print(solution([3,2,3], 3))
