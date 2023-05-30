#! /usr/bin/env python



# A singly linked list in the most basic form
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# Merging two sorted singly linked lists
def solution(list1,list2):
    res = []
    while list1 is not None:
        res.append(list1.val)
        list1 = list1.next
    while list2 is not None:
        res.append(list2.val)
        list2 = list2.next
    res.sort()
    result = ListNode(-1)
    output = result
    for i in range(len(res)):
        result.next = ListNode(res[i])
        result = result.next
    output.next

    return output.next



# Convert two ordinary lists into Linked Lists

a = [1,2,4]
b = [1,3,4]

# Create the link node and tie them to a temporary variable
a_node = ListNode(-1)
b_node = ListNode(-1)
temp_b = b_node
temp_a = a_node


# Loop through the lists as you create a node from every list element
for i in range(len(b)):
    b_node.next = ListNode(b[i])
    b_node = b_node.next

for i in range(len(a)):
    a_node.next = ListNode(a[i])
    a_node = a_node.next

# Link the nodes together to form linked list
temp_a = temp_a.next
temp_b = temp_b.next

print(solution(temp_a, temp_b))
