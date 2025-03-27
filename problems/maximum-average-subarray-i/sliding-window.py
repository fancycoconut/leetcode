class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAverage = float('-inf')

        i = 0
        length = 0
        workingAverage = 0
        while i < len(nums):
            workingAverage += nums[i]
            length += 1

            j = i + 1
            while True:
                if length >= k:
                    avg = workingAverage / k
                    maxAverage = max(maxAverage, avg)
                    workingAverage -= nums[j - k]
                    i = j - 1
                    break
                workingAverage += nums[j]
                length += 1
                j += 1
            i += 1

        return maxAverage
