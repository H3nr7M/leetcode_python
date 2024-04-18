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
        if not head or not head.next:
            return

        # Encontrar la mitad de la lista
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Invertir la segunda mitad de la lista, tiene mas en numeros impares
        prev, curr = None, slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        second_half = prev

        # Fusionar las dos sublistas
        first_half = head
        while second_half.next: #porque la segunda mitad tiene mas en impares
            temp1 = first_half.next
            temp2 = second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half = temp1
            second_half = temp2

        return head

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
f=Solution()
f.reorderList(head)
print(head)