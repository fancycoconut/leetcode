class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDiagonalLength = 0
        ans = 0
        for dim in dimensions:
            diagonalLength = math.sqrt((dim[0] * dim[0]) + (dim[1] * dim[1]))
            #print(diagonalLength)

            area = dim[0] * dim[1]
            if diagonalLength == maxDiagonalLength:
                ans = max(ans, area)
                continue

            if diagonalLength > maxDiagonalLength:
                maxDiagonalLength = diagonalLength
                ans = area
        
        return ans
