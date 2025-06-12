class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxDiff = 0

        prev = nums[0]
        for i in range(1, len(nums)):
            diff = abs(nums[i] - prev)
            maxDiff = max(diff, maxDiff)
            prev = nums[i]

        edgeDiff = abs(nums[0] - nums[-1])
        maxDiff = max(maxDiff, edgeDiff)

        return maxDiff
