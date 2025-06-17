class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff = -1
        smallest = nums[0]

        for i in range(len(nums)):
            if nums[i] > smallest:
                maxDiff = max(maxDiff, nums[i] - smallest)
            else:
                smallest = nums[i]

        return maxDiff
