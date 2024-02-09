# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
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
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        def merge(l1, l2):
            dummy = ListNode(0)
            cur = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 if l1 else l2
            return dummy.next

        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists): # even elements in lists
                    merged.append(merge(lists[i], lists[i+1]))
                else:
                    merged.append(lists[i])
            lists = merged

        return lists[0]


lists = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
f = Solution()
L = f.mergeKLists(lists)
print(L)