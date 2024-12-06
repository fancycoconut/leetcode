public class Solution {
    public IList<int> FindDuplicates(int[] nums) {
        var map = new Dictionary<int, int>();

        foreach (var num in nums)
        {
            if (map.ContainsKey(num))
            {
                map[num] += 1;
            }
            else
            {
                map[num] = 1;
            }
        }

        var duplicates = map.Where(kv => kv.Value > 1)
            .Select(x => x.Key)
            .ToArray();

        return duplicates;
    }
}