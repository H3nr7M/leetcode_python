'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]

'''
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
    def deleteDuplicates(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head

# Función para imprimir una lista enlazada
def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()

# Lista de valores
values = [1, 1, 2, 3, 3]

# Crear los nodos de la lista enlazada
head = ListNode(values[0])
current = head
for val in values[1:]:
    current.next = ListNode(val)
    current = current.next

# Ejecutar el método deleteDuplicates y luego imprimir la lista resultante
f = Solution()
print("Lista de entrada: ", end="")
print_linked_list(head)
L = f.deleteDuplicates(head)
print("Lista de salida: ", end="")
print_linked_list(L)
