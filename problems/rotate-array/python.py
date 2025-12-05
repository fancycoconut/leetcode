class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        output = [0] * len(nums)

        for i,num in enumerate(nums):       
            new_pos = new_pos = (i + k) % len(nums)
            output[new_pos] = num
       
        for i in range(len(nums)):
            nums[i] = output[i]