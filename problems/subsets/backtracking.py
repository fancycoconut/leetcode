class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        subset = []

        self.backtrack(0, nums, subset, results)

        return results

    def backtrack(self, start: int, nums: List[int], subset: List[int], results: List[List[int]]):
        results.append(subset[:])

        for i in range(start, len(nums)):
            subset.append(nums[i])

            self.backtrack(i + 1, nums, subset, results)

            subset.pop()