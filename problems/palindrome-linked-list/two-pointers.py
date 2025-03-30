# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = []
        current = head
        while current is not None:
            temp.append(current.val)
            current = current.next

        left = 0
        right = len(temp) - 1
        while left < len(temp) and right >= 0 and left != right:
            a = temp[left]
            b = temp[right]

            if a != b:
                return False

            left += 1
            right -= 1

        return True