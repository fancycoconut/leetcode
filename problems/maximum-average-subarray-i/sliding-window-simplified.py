class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        for i in range(0, k):
            sum += nums[i]

        maxSum = sum
        for i in range(k, len(nums)):
            sum += nums[i] - nums[i - k]
            maxSum = max(maxSum, sum)

        return maxSum / k