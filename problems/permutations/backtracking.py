class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        subset = []
        visited = set()

        self.backtrack(0, nums, visited, subset, results)

        return results

    def backtrack(self, start: int, nums: List[int], visited: set, subset: List[int], results: List[List[int]]):
        if len(subset) == len(nums):
            results.append([x for x in subset])
            return

        for i in range(0, len(nums)):
            num = nums[i]
            if num in visited:
                continue
            
            subset.append(num)
            visited.add(num)

            self.backtrack(i, nums, visited, subset, results)

            subset.pop()
            visited.remove(num)