'''Given the head of a singly linked list, reverse the list, 
and return the reversed list.
Definition for singly-linked list.'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        result = []
        node = self
        while node:
            result.append(str(node.val))
            node = node.next
        return " -> ".join(result)


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None

        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp

        return pre

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(Solution().reverseList(head))
