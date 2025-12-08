class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i, num in enumerate(nums):
            if num != 0:
                continue
            
            j = i + 1
            while j < len(nums):
                if nums[j] != 0:
                    nums[i] = nums[j]
                    nums[j] = 0
                    break
                j += 1
        print(nums)
