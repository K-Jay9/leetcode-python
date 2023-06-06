#! /usr/bin/env python

def solution(s):
    running = True
    while running:
        if "AB" in s:
            s = s.replace("AB", '')
        if "CD" in s:
            s = s.replace("CD", '')
        if "AB" not in s and "CD" not in s:
            running = False
    return len(s)

if __name__ == "__main__":
    print(solution("ABFCACDB"))
