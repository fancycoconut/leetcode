class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        numOfNegatives = 0
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols - 1, -1, -1):
                val = grid[row][col]
                if val >= 0:
                    break
                if val < 0:
                    numOfNegatives += 1
        
        return numOfNegatives
