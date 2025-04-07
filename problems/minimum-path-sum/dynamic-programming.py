class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])

        dp = []
        for y in range(0, height):
            dp.append([float('inf')] * width)
        dp[0][0] = grid[0][0]

        for x in range(0, width):
            res = grid[0][x] + dp[0][x - 1]
            dp[0][x] = min(dp[0][x], res)

        for y in range(1, height):
            for x in range(0, width):
                dp[y][x] = grid[y][x] + min(dp[y - 1][x], dp[y][x - 1])

        #print(dp)
        return dp[-1][-1]