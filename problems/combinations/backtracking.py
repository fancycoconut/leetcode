class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        subset = []

        self.backtrack(1, n, k, subset, output)

        return output

    def backtrack(self, start: int, n: int, k: int, subset: List[int], results: List[List[int]]):
        if len(subset) == k:
            results.append([x for x in subset])
            return
        
        for i in range(start, n + 1):
            subset.append(i)

            self.backtrack(i + 1, n, k, subset, results)

            subset.pop()
        