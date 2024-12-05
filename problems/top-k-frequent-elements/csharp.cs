public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        var map = new Dictionary<int, int>();
        var output = new HashSet<int>();

        foreach (var num in nums)
        {
            if (map.ContainsKey(num))
            {
                map[num]++;
            }
            else
            {
                map[num] = 1;
            }
        }

        var sortedElements = map.OrderByDescending(x => x.Value)
            .Select(x => x.Key)
            .Take(k);

        return sortedElements.ToArray();
    }
}