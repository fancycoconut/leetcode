public class Solution {
    public int[] FinalPrices(int[] prices) {
        for (var i = 0; i < prices.Length; i++)
        {
            var currentPrice = prices[i];
            var discount = 0;
            var applyDiscount = false;
            var j = i + 1;
            while (j < prices.Length)
            {
                if (prices[j] <= currentPrice)
                {
                    applyDiscount = true;
                    discount = prices[j];
                    break;
                }

                j++;
            }

            if (applyDiscount)
            {
                prices[i] = currentPrice - discount;
            }
        }

        return prices;
    }
}