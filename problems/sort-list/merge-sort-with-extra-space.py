# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        output = []
        current = head
        while current != None:
            output.append(current.val)
            current = current.next
        print(output)

        sortedOutput = self.mergeSort(output)
        #print(a)

        root = ListNode(sortedOutput[0])
        current = root
        for i in range(1, len(sortedOutput)):
            node = ListNode(sortedOutput[i])
            current.next = node
            current = node

        return root

    def mergeSort(self, nums: list[int]) -> list[int]:
        if len(nums) == 0 or len(nums) == 1:
            return nums

        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        return self.merge(left, right)

    def merge(self, left: list[int], right: list[int]) -> list[int]:
        output = []

        i = 0
        j = 0
        while i < len(left) and j < len(right):
            a = left[i]
            b = right[j]

            if a < b:
                output.append(a)
                i += 1
            else:
                output.append(b)
                j += 1

        while i < len(left):
            output.append(left[i])
            i += 1
        
        while j < len(right):
            output.append(right[j])
            j += 1
        #print(output)
        return output

