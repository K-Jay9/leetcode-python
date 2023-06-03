#! /usr/bin/env python


def getRow(rowIndex):
    res = []
    for i in range(1, rowIndex+2):
        temp = []
        if i == 1:
            temp.append(1)
        else:
            adder = 0
            prev = res[-1]
            if len(prev) == 1:
                temp.append(1)
            else:
                for j in range(1,len(prev)):
                    if prev[j-1] == 1:
                        temp.append(1)
                    adder = prev[j] +prev[j-1]
                    temp.append(adder)
                    adder = 0
                    temp.append(1)
        res.append(temp)
        temp = []

    return res[rowIndex]

print(getRow(3))
