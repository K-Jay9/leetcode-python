#! /usr/bin/env python

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(a):
    res = []
    while a is not None:
        res.append(a.val)
        a = a.next
    half = len(res)//2
    if len(res)%2 == 0:
        return res[:half] == res[half:][::-1]
    return res[:half] == res[half+1:][::-1]


a = [1,2,2,1]
b = [1,2]
list_a = ListNode(-1)
list_b = ListNode(-1)
temp_a = list_a
temp_b = list_b

for i in a:
    list_a.next = ListNode(i)
    list_a = list_a.next
for i in b:
    list_b.next = ListNode(i)
    list_b = list_b.next

temp_a = temp_a.next
temp_b = temp_b.next

print(solution(temp_a))
print(solution(temp_b))
