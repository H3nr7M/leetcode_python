'''
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
'''

class ListNode:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        result = []
        node = self
        while node:
            result.append(str(node.val))
            node = node.next
        return " -> ".join(result)


class Solution:
    def copyRandomList(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
        if not head:
            return None
        
        # Paso 1: Crear nodos nuevos y almacenar referencias en un diccionario
        node_map = {}
        curr = head
        while curr:
            #mi llave es un nodo: value nuevo con el val
            node_map[curr] = ListNode(curr.val)
            curr = curr.next
        
        # Paso 2: Enlazar los nodos nuevos
        curr = head
        while curr:#obtengo valores de la llave y se los asigno a mis valores
            copy = node_map[curr]
            copy.next = node_map[curr.next]
            copy.random = node_map[curr.random]
            curr = curr.next
        
        return node_map[head]

# Código de prueba
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Instanciar la solución y llamar al método copyRandomList
solution = Solution()
copied_list = solution.copyRandomList(head)

# Imprimir la lista copiada
print("Lista original:", head)
print("Lista copiada:", copied_list)
