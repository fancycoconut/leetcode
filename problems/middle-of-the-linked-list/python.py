# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next is None:
            return head

        length = 0
        current = head
        while current != None:
            current = current.next
            length += 1
        
        mid = (length // 2)

        midNode = head
        for i in range(0, mid):
            midNode = midNode.next
        return midNode
