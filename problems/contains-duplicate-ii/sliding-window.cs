public class Solution {
    public bool ContainsNearbyDuplicate(int[] nums, int k) {
        for (var i = 0; i < nums.Length; i++)
        {
            var num = nums[i];
            var j = i + 1;
            while (j - i <= k && j < nums.Length)
            {
                if (j >= nums.Length) break;
                var num2 = nums[j];
                if (num == num2) return true;
                j++;
            }
        }

        return false;
    }
}