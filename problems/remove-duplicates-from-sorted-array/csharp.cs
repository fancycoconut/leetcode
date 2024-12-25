// Brute force approach
public class Solution {
    public int RemoveDuplicates(int[] nums) {
        var map = new Dictionary<int, int>();
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

        var output = map.Select(x => x.Key).ToArray();

        for (var i = 0; i < nums.Length; i++)
        {
            var copiedValue = i >= output.Length
                ? -1
                : output[i];
            nums[i] = copiedValue;
        }

        return output.Length;
    }
}