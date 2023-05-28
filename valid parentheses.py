#! /usr/bin/env python


def solution(word):
    chars = list(word)
    if len(chars)%2 != 0:
        return False
    stack = []
    check = ["]", ")", "}"]
    for i in chars:
        if i in check and len(stack) == 0:
            return False
        if i not in check:
            stack.append(i)
        else:
            if i == ")" and stack[-1] == "(":
                stack.pop()
            elif i == "]" and stack[-1] == "[":
                stack.pop()
            elif i == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
    if len(stack) != 0:
        return False
    return True


print(solution("(){}[]"))
