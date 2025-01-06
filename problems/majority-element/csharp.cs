public class Solution {
    public int MajorityElement(int[] nums) {
        var map = new Dictionary<int, int>();

        var maxOccurence = 0;
        var majorityElement = nums[0];
        for (var i = 0; i < nums.Length; i++)
        {
            var num = nums[i];
            if (map.ContainsKey(num))
            {
                map[num]++;
            }
            else
            {
                map[num] = 1;
            }

            if (map[num] > maxOccurence)
            {
                maxOccurence = map[num];
                majorityElement = num;
            }
        }

        return majorityElement;
    }
}