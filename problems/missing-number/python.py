class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxNum = 0
        visited = set()
        for num in nums:
            visited.add(num)
            maxNum = max(maxNum, num)

        #print(maxNum)
        for i in range(0, maxNum + 2):
            if i in visited:
                continue
            return i
        return -1
