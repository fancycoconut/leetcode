public class Solution {
    public IList<string> SummaryRanges(int[] nums) {
        if (nums.Length == 0) return new List<string>();

        var summaryMap = new Dictionary<int, int>();

        var prev = nums[0];
        var intervalStart = prev;
        summaryMap[intervalStart] = prev;
        for (var i = 1; i < nums.Length; i++)
        {
            var current = nums[i];
            var diff = current - prev;
            if (diff != 1)
            {
                intervalStart = current;
            }

            summaryMap[intervalStart] = current;
            prev = current;
        }

        var output = new List<string>();
        foreach (var kvp in summaryMap)
        {
            var summary = kvp.Key == kvp.Value
                ? kvp.Key.ToString()
                : $"{kvp.Key}->{kvp.Value}";
            Console.WriteLine(summary);
            output.Add(summary);
        }

        return output;
    }
}