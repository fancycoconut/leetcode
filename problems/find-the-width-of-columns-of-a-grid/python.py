class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])

        output = []
        for col in range(cols):
            maxColWidth = 0
            for row in range(rows):
                colWidth = len(str(grid[row][col]))
                maxColWidth = max(maxColWidth, colWidth)

            output.append(maxColWidth)
    
        #print(output)
        return output
