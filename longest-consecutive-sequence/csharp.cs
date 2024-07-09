public class Solution {
    public int LongestConsecutive(int[] nums) {
        var map = nums.ToHashSet();

        var longestConsecutive = 0;
        foreach (var num in nums)
        {
            var current = num;
            var currentLongestConsecutive = 0;
            if (!map.Contains(current - 1)) {
                while (map.Contains(current))
                {
                    currentLongestConsecutive++;
                    current++;
                }

                if (currentLongestConsecutive > longestConsecutive)
                {
                    longestConsecutive = currentLongestConsecutive;
                }
            }

        }

        return longestConsecutive;
    }
}