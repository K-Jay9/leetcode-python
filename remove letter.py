#! /usr/bin/env python


def solution(word):
    alpha = [*word]
    res = []
    placer = 0
    for i in range(len(alpha)):
        small = []
        letter = []
        for j in range(len(alpha)):
            if j != i:
                small.append(alpha[j])
        for k in range(len(small)):
            letter.append(small.count(small[k]))
        result = all(element == letter[0] for element in letter)
        if (result):
            return True
    return False

print(solution("abcc"))
print(solution("abc"))
print(solution("abcdcd"))
print(solution("abccccc"))
print(solution("abcc,mdshahnf"))
