# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head

        if head.next == None:
            return head

        tail = head.next
        n = 1
        while tail.next != None:
            tail = tail.next
            n += 1
        n += 1

        #print(tail)
        #print(n)

        tail.next = head
        # Optimize number of rotations
        numOfRotations = k % n

        for i in range(0, abs(n - numOfRotations)):
            head = head.next
        
        tail = head
        for i in range(0, n - 1):
            tail = tail.next
        tail.next = None

        return head
