#! /usr/bin/env python


def solution(string):
    string = "".join(i.lower() for i in string if i.isalnum())
    half = len(string)//2
    if len(string)%2 == 0:
        return string[:half] == string[half:][::-1]
    return string[:half] == string[half+1:][::-1]

print(solution("A man, a plan, a canal: Panama"))
print(solution('race car'))
