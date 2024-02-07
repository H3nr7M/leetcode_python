'''
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
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
    def reorderList(self, head: ListNode) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next # it's the beginning of second half
        prev = slow.next = None # cut off the first half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # prev is the last node of second half
        # merge two halfs
        first, second = head, prev
        while second: # second half is always shorter or equal to first half
            tmp_first, tmp_sec = first.next, second.next
            first.next = second
            second.next = tmp_first
            first, second = tmp_first, tmp_sec # advance pointers

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
f=Solution()
f.reorderList(head)
print(head)