#! /usr/bin/env python


def solution(string1, string2):
    if(len(string1) != len(string2)):
        return False
    string1 = list(string1)
    string2 = list(string2)
    string1.sort()
    string2.sort()
    return string1 == string2
print(solution('anagram', 'nagaram'))
