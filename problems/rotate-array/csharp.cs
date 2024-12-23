// Constant space solution
public class Solution {
    public void Rotate(int[] nums, int k) {
        if (nums.Length == 1) return;

        var output = new int[nums.Length];

        for (var i = 0; i < nums.Length; i++)
        {
            var target = (i + k) % nums.Length;

            output[target] = nums[i];
            //Console.WriteLine($"{nums[i]} new position is {target}");
        }

        for (var i = 0; i < nums.Length; i++)
        {
            nums[i] = output[i];
        }
    }
}