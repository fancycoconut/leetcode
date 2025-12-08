class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for num in nums:
            if num != 0:
                nums[slow] = num
                slow += 1

        # Fill the rest with 0s
        for i in range(slow, len(nums)):
            nums[i] = 0
        print(nums)
