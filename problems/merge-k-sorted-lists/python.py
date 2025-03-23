# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Convert them all to arrays
    # Merge all
    # Convert merged array to linked list
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None:
            return None
        
        arrays = []
        for head in lists:
            arr = []
            current = head
            while current is not None:
                arr.append(current.val)
                current = current.next
            arrays.append(arr)

        merged = []
        for arr in arrays:
            merged = self.mergeLists(merged, arr)

        if len(merged) == 0:
            return None

        root = ListNode(merged[0])
        current = root
        for i in range(1, len(merged)):
            next = ListNode(merged[i])
            current.next = next
            current = next

        return root

    def mergeLists(self, listA: List[int], listB: List[int]) -> List[int]:
        i = 0
        j = 0

        output = []
        while i < len(listA) and j < len(listB):
            a = listA[i]
            b = listB[j]

            if a < b:
                output.append(a)
                i += 1
            else:
                output.append(b)
                j += 1

        while i < len(listA):
            output.append(listA[i])
            i += 1

        while j < len(listB):
            output.append(listB[j])
            j += 1

        return output
