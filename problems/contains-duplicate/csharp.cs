public class Solution {
    public bool HasDuplicate(int[] nums) {
        var map = new HashSet<int>();

        for (var i = 0; i < nums.Length; i++)
        {
            var num = nums[i];
            if (map.Contains(num)) return true;
            map.Add(num);
        }

        return false;
    }
}
