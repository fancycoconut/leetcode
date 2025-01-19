class Solution:
    def climbStairs(self, n: int) -> int:
        dp = []
        dp.append(1)
        dp.append(2)
        for i in range(2, n):
            ways = dp[i - 1] + dp[i - 2]
            dp.append(ways)
        return dp[n - 1]