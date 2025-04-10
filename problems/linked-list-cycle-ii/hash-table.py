# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None

        nodes = []
        visited = set()
        current = head
        while current is not None and current not in visited:
            visited.add(current)
            nodes.append(current)
            current = current.next

        tail = nodes[-1]
        return tail.next