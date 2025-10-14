class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = nums[0]
        largestIndex = 0

        for i in range(1, len(nums)):
            num = nums[i]
            if num > largest:
                largest = num
                largestIndex = i
        
        for i in range(0, len(nums)):
            num = nums[i]
            if i == largestIndex:
                continue
            if num * 2 > largest:
                return -1
        return largestIndex