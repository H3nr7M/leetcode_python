# Problem: Given an integer array nums of unique elements, return all possible subsets (the power set).
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

class Solution:
    def mergeKLists(self, lists: list[Node]) -> Node:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = Node()
        tail = dummy

        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next

f=Solution()
llist1 = LinkedList(Node('1',Node('2',Node('3'))))
llist2 = LinkedList(Node('6',Node('9',Node('10'))))
llist3 = LinkedList(Node('1',Node('3',Node('5'))))

lista=[llist1,llist2,llist3]


print(f.mergeKLists(lista))