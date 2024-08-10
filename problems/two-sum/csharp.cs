public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var output = new List<int>();
        var map = new Dictionary<int, HashSet<int>>();
        for (var i = 0; i < nums.Length; i++)
        {
            var num = nums[i];
            if (map.ContainsKey(num))
            {
                map[num].Add(i);
            }
            else
            {
                map[num] = new HashSet<int> { i };
            }            
        }

        for (var i = 0; i < nums.Length; i++)
        {
            var num = nums[i];
            var complement = target - num;
            // If the current number and the complement is the same e.g. 3 & 3
            if (complement == num && map.ContainsKey(complement))
            {
                if (map[num].Count() == 1) continue;

                output.AddRange(map[complement]);
                break;
            }

            if (map.ContainsKey(complement))
            {
                output.Add(i);
                output.Add(map[complement].First());
                break;
            }
        } 

        return output.ToArray();
    }
}