class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        window = []
        maxConsecutiveOnes = 0
        for num in nums:
            if num != 1:
                window = []
            else:
                window.append(num)
            
            maxConsecutiveOnes = max(maxConsecutiveOnes, len(window))
        return maxConsecutiveOnes