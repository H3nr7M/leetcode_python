'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(head, k):
            prev = None
            curr = head
            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev, head, curr
        
        dummy = ListNode(0)
        dummy.next = head
        prev_tail = dummy
        
        while True:
            curr_tail = prev_tail.next
            k_counter = 0
            while curr_tail and k_counter < k:
                curr_tail = curr_tail.next
                k_counter += 1
            if k_counter < k or not curr_tail:
                break
            prev_tail.next, prev_tail, next_head = reverse(prev_tail.next, k)
            prev_tail.next = next_head
        
        return dummy.next

# Código de prueba
# Crear una lista de nodos y probar la función reverseKGroup
nodes = [ListNode(i) for i in range(1, 11)]  # Crear 10 nodos con valores del 1 al 10
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]  # Enlazar los nodos
list_head = nodes[0]  # Nodo inicial de la lista

# Crear una instancia de Solution y probar la función reverseKGroup
solution = Solution()
k = 3  # Tamaño del grupo a revertir
reversed_head = solution.reverseKGroup(list_head, k)

# Imprimir los valores de los nodos en la lista revertida
while reversed_head:
    print(reversed_head.val, end=" -> ")
    reversed_head = reversed_head.next
