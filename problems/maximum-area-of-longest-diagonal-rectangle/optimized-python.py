class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDiagonalSquare = 0
        ans = 0
        for dim in dimensions:
            diagonalSquare = (dim[0] * dim[0]) + (dim[1] * dim[1])
            #print(diagonalLength)

            area = dim[0] * dim[1]
            if diagonalSquare == maxDiagonalSquare:
                ans = max(ans, area)
                continue

            if diagonalSquare > maxDiagonalSquare:
                maxDiagonalSquare = diagonalSquare
                ans = area
        
        return ans
        