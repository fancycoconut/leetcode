public class Solution {
    public int[] GetFinalState(int[] nums, int k, int multiplier) {
        var currentMinimum = (nums[0], 0);
        for (var i = 0; i < k; i++) {
            for (var j = 0; j < nums.Length; j++)
            {
                var current = nums[j];
                if (current < currentMinimum.Item1)
                {
                    currentMinimum.Item1 = current;
                    currentMinimum.Item2 = j;
                }
            }

            nums[currentMinimum.Item2] = currentMinimum.Item1 * multiplier;
            currentMinimum = (nums[0], 0);
        }

        return nums;
    }
}