class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSubArrayLength = float('inf')

        left = 0
        sumOfCurrentWindow = 0

        for right in range(0, len(nums)):
            sumOfCurrentWindow += nums[right]

            while sumOfCurrentWindow >= target:
                minSubArrayLength = min(minSubArrayLength, right - left + 1)
                sumOfCurrentWindow -= nums[left]
                left += 1

        # Return 0 if the target cannot be formed by all elements of the array
        return minSubArrayLength if minSubArrayLength != float('inf') else 0