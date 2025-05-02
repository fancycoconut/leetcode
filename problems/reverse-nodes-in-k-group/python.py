# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = []
        current = head
        while current is not None:
            temp.append(current.val)
            current = current.next
        #print(temp)

        for i in range(0, len(temp), k):
            if i + k > len(temp):
                break
            subarr = list(reversed(temp[i:i+k]))

            for j in range(k):
                temp[i + j] = subarr[j]
        #print(temp)

        root = ListNode(temp[0])
        current = root
        for i in range(1, len(temp)):
            num = temp[i]
            current.next = ListNode(num)
            current = current.next

        return root
        