public class Solution {
    public void MoveZeroes(int[] nums) {
        if (nums.Length == 1) return;

        var i = 0;
        var j = 0;
        while (i < nums.Length)
        {
            var num = nums[i];
            if (num != 0)
            {
                i++;
                continue;
            }

            j = i;
            while (num == 0 && j < nums.Length)
            {
                num = nums[j];
                if (num != 0)
                {
                    nums[j] = 0;
                    nums[i] = num;
                    break;
                }
                j++;
            }

            i++;
        }
    }
}