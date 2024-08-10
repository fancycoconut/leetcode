public class Solution {

    public bool ContainsDuplicate(int[] nums) {
        var map = new Dictionary<int, int>();
        foreach (var num in nums)
        {
            if (map.ContainsKey(num))
            {
                return true;
            }

            map[num] = 1;
        }

        return false;
    }
}