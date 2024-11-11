public class Solution {
  public int MaxProfit(int[] prices) {
    var left = 0;
    var right = 1;
    var maxProfit = 0;

    while (right < prices.Length)
    {
      if (prices[right] > prices[left])
      {
        var profit = prices[right] - prices[left];
        maxProfit = Math.Max(maxProfit, profit);
      }
      else
      {
        left = right;
      }

      right++;
    }

    return maxProfit;
  }
}