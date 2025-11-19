class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        numsMap = set()
        for num in nums:
            numsMap.add(num)
        
        n = original
        while n in numsMap:
            n = 2 * n
        return n
