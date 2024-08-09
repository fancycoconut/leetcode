public class Solution {
    public int FirstMissingPositive(int[] nums) {
        if (nums.Length == 1 && nums[0] > 1) return 1;

        var min = 0;
        var max = 0;
        var map = new HashSet<int>();

        // Find min, max and store all numbers that appeared
        for (var i = 0; i < nums.Length; i++)
        {
            var num = nums[i];
            if (num < 0) continue;

            map.Add(num);
            if (num < min)
            {
                min = num;
            }

            if (num > max)
            {
                max = num;
            }
        }

        var smallestPositive = 1;
        for (var i = 0; i < max; i++)
        {
            if (!map.Contains(smallestPositive))
            {
                break;
            }

            smallestPositive++;
        }

        return smallestPositive;
    }
}