class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subset = []
        total = [0]

        self.backtrack(0, nums, subset, total)

        return total[0]

    def backtrack(self, start: int, nums: List[int], subset: List[int], total: List[int]):
        print(subset)
        total[0] += self.getXORTotal(subset)

        for i in range(start, len(nums)):
            subset.append(nums[i])

            self.backtrack(i + 1, nums, subset, total)

            subset.pop()
        
    def getXORTotal(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        total = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            total ^= num
        return total