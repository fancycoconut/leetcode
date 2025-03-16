class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        output = []

        i = 0
        j = 0
        while i < m and j < n:
            a = nums1[i]
            b = nums2[j]

            if a > b:
                output.append(b)
                j += 1
            else:
                output.append(a)
                i +=1

        while i < m:
            output.append(nums1[i])
            i += 1

        while j < n:
            output.append(nums2[j])
            j += 1

        print(output)
        
        for i in range(0, len(nums1)):
            nums1[i] = output[i]