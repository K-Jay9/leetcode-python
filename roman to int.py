#! /usr/bin/env python

def solution(roman):
    romans = {
            "I" : 1,
            "IV" : 4,
            "V" : 5,
            "IX" : 9,
            "X": 10,
            "XL" : 40,
            "L" : 50,
            "XC": 90,
            "C" : 100,
            "CD": 400,
            "D": 500,
            "CM" : 900,
            "M" : 1000
        }
    res = 0
    roman_split = [i for i in roman]
    values = [romans[i] for i in roman_split]
    for i in range(len(values)):
        if i == len(values)-1:
            res += values[i]
        elif values[i+1] > values[i]:
            res -= values[i]
        else:
            res += values[i]

    return res


print(solution("MCMXCIX"))

