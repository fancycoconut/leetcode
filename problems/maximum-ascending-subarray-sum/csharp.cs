public class Solution {
    public int MaxAscendingSum(int[] nums) {
        var map = new Dictionary<List<int>, int>();

        var prev = 0;
        var max = 0;
        var currentList = new List<int>();
        foreach (var num in nums)
        {
            if (num - prev <= 0)
            {
                var sum = currentList.Sum();
                map.Add(currentList, sum);
                max = Math.Max(max, sum);
                Console.WriteLine(string.Join(",", currentList));
                currentList = new List<int>();
            }

            currentList.Add(num);
            prev = num;
        }

        map.Add(currentList, currentList.Sum());
        max = Math.Max(max, currentList.Sum());
        Console.WriteLine(string.Join(",", currentList));

        return max;
    }
}