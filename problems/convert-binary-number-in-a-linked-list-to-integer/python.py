# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        binary = ""
        current = head
        while current is not None:
            binary += str(current.val)
            current = current.next

        total = 0
        for i in range(len(binary) - 1, -1, -1):
            total += int(binary[i]) << (len(binary) - i - 1)

        return total
        