'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:
Input: head = [1], n = 1
Output: []
'''

# Definition for singly-linked list.
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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Reverse the linked list
        slow, fast = head, head
        while n:
            fast = fast.next
            n -= 1
        if not fast:
            return head.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return head
        



head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
f=Solution()
L=f.removeNthFromEnd(head, 2)
print(L)
