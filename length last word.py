#! /usr/bin/env python

def solution(s):
    s = s.strip() # strip away trailing and leading whitespaces
    list_s = s.split(" ")
    return len(list_s[-1])


print(solution("Hello World"))
