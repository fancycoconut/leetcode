class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        uniquePermutations = set()
        subset = []
        visited = set()

        def backtrack(start: int) -> None:
            if len(subset) == len(nums):
                ans = subset[:]
                permutation = ",".join(str(x) for x in ans)
                if permutation in uniquePermutations:
                    return
                uniquePermutations.add(permutation)
                results.append(ans)
                return

            for i in range(len(nums)):
                num = nums[i]
                if i in visited:
                    continue

                visited.add(i)
                subset.append(num)
                
                backtrack(i + 1)

                visited.remove(i)
                subset.pop()
            
        backtrack(0)

        return results
