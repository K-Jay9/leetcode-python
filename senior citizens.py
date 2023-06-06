#! /usr/bin/env python

def solution(details):
    print(details[0][11:13])
    ages = 0
    for i in details:
        if int(i[11:13]) > 60:
            ages += 1
    return ages

if __name__ == "__main__":
    print(solution(["7868190130M7522","5303914400F9211","9273338290F4010"]))
