// This is a O(N) solution
public class Solution {
    public int[] SearchRange(int[] nums, int target) {
        if (nums.Length == 0) return new int[] { -1, -1 };

        var left = 0;
        var right = nums.Length - 1;
        while (left < nums.Length && right >= 0)
        {
            var num1 = nums[left];
            var num2 = nums[right];
            if (num1 == target && num2 == target) return new int[] { left, right };

            if (num1 != target)
            {
                left++;
                continue;
            }

            if (num2 != target)
            {
                right--;
                continue;
            }
        }


        return new int[] { -1, -1 };
    }
}