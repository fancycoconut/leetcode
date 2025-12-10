class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            if num != prev:
                nums[slow] = num
                prev = num
                slow += 1
            
        return slow
