class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        values = Counter(arr)
        for num in arr:
            if num == 0 and values[0] == 1:
                continue
            if num * 2 in values:
                return True

        return False
