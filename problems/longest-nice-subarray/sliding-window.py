class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        right = 0
        maxNiceSubArrayLength = 1

        temp = []
        while right < len(nums):
            temp.append(nums[right])
            #print(temp)
            if self.allElementsAreNice(temp):
                maxNiceSubArrayLength = max(maxNiceSubArrayLength, len(temp))
            else:
                temp.pop(0)
            right += 1

        return maxNiceSubArrayLength

    def allElementsAreNice(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                res = nums[i] & nums[j]
                if res != 0:
                    return False
        return True
