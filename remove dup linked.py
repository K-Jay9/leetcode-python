#! /usr/bin/env python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution(head):
    res = []
    while head is not None:
        res.append(head.val)
        head = head.next
    res_set = sorted(set(res))
    output = ListNode()
    result = output
    for i in res_set:
        output.next = ListNode(i)
        output = output.next
    result =result.next
    return result

'''
# alternative and elegant solution from leetcoders

def solution(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

'''


# Convert two ordinary lists into Linked Lists

a = [1,1,2,3,3]
b = [1,1,2]

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


print(solution(temp_a))
print(solution(temp_b))
