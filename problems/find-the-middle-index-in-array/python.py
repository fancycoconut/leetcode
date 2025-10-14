class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        array1 = [0] * len(nums)
        array1[0] = nums[0]
        for i in range(1, len(nums)):
            array1[i] = nums[i] + array1[i - 1]
        print(array1)

        array2 = [0] * len(nums)
        array2[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            array2[i] = nums[i] + array2[i + 1]
        print(array2)

        for i in range(0, len(nums)):
            if array1[i] == array2[i]:
                return i

        return -1
