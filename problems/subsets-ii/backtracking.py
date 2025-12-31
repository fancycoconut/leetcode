class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        results = []
        subset = []
        uniqueAnswers = set()

        def backtrack(start: int) -> None:
            ans = subset[:]
            uniqueAns = ",".join(str(x) for x in ans)
            if uniqueAns not in uniqueAnswers:
                uniqueAnswers.add(uniqueAns)
                results.append(ans)

            for i in range(start, len(sortedNums)):
                num = sortedNums[i]
                subset.append(num)

                backtrack(i + 1)

                subset.pop()

        backtrack(0)

        return results
