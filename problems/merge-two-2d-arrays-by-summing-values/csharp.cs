public class Solution {
    public int[][] MergeArrays(int[][] nums1, int[][] nums2) {
        var map = new Dictionary<int, int>();

        foreach (var pair in nums1)
        {
            var key = pair[0];
            var val = pair[1];
            map[key] = val;
        }

        foreach (var pair in nums2)
        {
            var key = pair[0];
            var val = pair[1];

            if (map.ContainsKey(key))
            {
                map[key] += val;
            }
            else
            {
                map[key] = val;
            }
        }

        return map.OrderBy(x => x.Key)
            .Select(kvp => new [] { kvp.Key, kvp.Value })
            .ToArray();
    }
}