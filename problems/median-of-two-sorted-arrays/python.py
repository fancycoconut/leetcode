class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i, j = 0, 0

        # Merge the 2 lists
        while i < len(nums1) and j < len(nums2):
            a = nums1[i]
            b = nums2[j]
            if a < b:
                merged.append(a)
                i += 1
            else:
                merged.append(b)
                j += 1

        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        print(merged)
        mid = len(merged) // 2

        # Find median
        median = 0
        if len(merged) % 2 == 0:
            median = (merged[mid] + merged[mid - 1]) / 2
        else:
            median = merged[mid]

        return median