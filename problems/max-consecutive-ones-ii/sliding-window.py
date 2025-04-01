class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxConsecutiveOnes = 0

        left = 0
        workingSum = 0
        length = 0

        for right in range(len(nums)):
            workingSum += nums[right]
            length += 1

            if length - workingSum > 1:
                workingSum -= nums[left]
                left += 1
                length -= 1
            maxConsecutiveOnes = max(maxConsecutiveOnes, length)

        return maxConsecutiveOnes
