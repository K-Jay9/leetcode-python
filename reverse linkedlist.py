#! /usr/bin/env python

class ListNode:
    def __init__(self, val = 0,next= None):
        self.next = next
        self.val = val

def solution(linked):
    temp =[]
    while linked is not None:
        temp.append(linked.val)
        linked = linked.next
    temp = temp[::-1]
    res = ListNode(-1)
    result = res
    for i in temp:
        res.next = ListNode(i)
        res = res.next
    result = result.next
    return result


a = [1,2,3,4,5]
list_a = ListNode(-1)
swap_a = list_a
for i in a:
    list_a.next = ListNode(i)
    list_a = list_a.next
swap_a = swap_a.next

print(solution(swap_a))

