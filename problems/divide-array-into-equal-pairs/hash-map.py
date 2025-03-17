class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        map = {}

        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        for key, value in map.items():
            if value % 2 != 0:
                return False

        return True
        