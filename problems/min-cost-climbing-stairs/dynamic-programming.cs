// 1. Define objective function:
// f(n) => min cost to reach the end of the array
// 2. Identity base cases:
// Sample: [10, 15, 20]
// f(n) = min(cost[i-2] + dp[i-2], cost[i-1] + dp[i-1])
// f(2) = min(0 + 15, 0 + 10) => 15
// f(1) = 0
// f(0) = 0
// 3. Recurrence relation:
// f(n) = min(cost[i-2] + dp[i-2], cost[i-1] + dp[i-1])
// 4. Order of computation
// bottom up?
// 5. Location of the answer
// n
public class Solution {
    public int MinCostClimbingStairs(int[] cost) {
        var n = cost.Length + 1;
        var dp = new int[n];
        for (var i = 2; i < n; i++)
        {
            var upOneStep = dp[i - 1] + cost[i - 1];
            var upTwoStep = dp[i - 2] + cost[i - 2];
            dp[i] = Math.Min(upOneStep, upTwoStep);
            Console.WriteLine(dp[i]);
        }

        return dp[n - 1];
    }


}