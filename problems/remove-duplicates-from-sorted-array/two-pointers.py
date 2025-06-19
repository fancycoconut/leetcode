class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueElements = 0
        i = 0

        prev = nums[0]
        while i < len(nums):
            num = nums[i]
            if num != prev:
                nums[uniqueElements] = prev
                uniqueElements += 1

            i += 1
            prev = num
        nums[uniqueElements] = prev
        uniqueElements += 1

        return uniqueElements
