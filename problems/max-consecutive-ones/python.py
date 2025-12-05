class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        numOfOnes = 0
        maxConsecutiveOnes = 0
        for num in nums:
            if num != 1:
                numOfOnes = 0
            else:
                numOfOnes += 1
            
            maxConsecutiveOnes = max(maxConsecutiveOnes, numOfOnes)
        return maxConsecutiveOnes