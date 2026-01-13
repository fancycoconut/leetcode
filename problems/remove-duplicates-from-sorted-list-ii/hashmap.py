# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        numMap = {}
        current = head
        while current:
            count = numMap.get(current.val, 0)
            numMap[current.val] = count + 1
            current = current.next

        output = []
        current = head
        while current:
            if numMap[current.val] == 1:
                output.append(current.val)
            current = current.next

        if len(output) == 0:
            return None

        root = ListNode(output[0])
        current = root

        for i in range(1, len(output)):
            num = output[i]
            node = ListNode(num)
            current.next = node
            current = current.next

        return root
