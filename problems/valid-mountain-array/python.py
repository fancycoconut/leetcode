class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        highestPoint = arr[0]
        highestPointIndex = 0
        for i in range(len(arr)):
            if arr[i] > highestPoint:
                highestPoint = arr[i]
                highestPointIndex = i

        if not (0 < highestPointIndex and highestPointIndex < len(arr) - 1):
            return False

        # Strictly increasing
        for i in range(1, highestPointIndex):
            if arr[i] <= arr[i - 1]:
                return False
        

        # Strictly decreasing
        for i in range(highestPointIndex + 1, len(arr)):
            if arr[i] >= arr[i - 1]:
                return False
        
        return True
