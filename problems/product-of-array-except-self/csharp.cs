public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        var prefixProducts = new int[nums.Length];
        var suffixProducts = new int[nums.Length];
        var length = nums.Length;

        // Calculate prefix products
        prefixProducts[0] = 1;
        for (var i = 1; i < length; i++)
        {
            prefixProducts[i] = nums[i - 1] * prefixProducts[i - 1];
        }

        // Calculate suffix products
        suffixProducts[length - 1] = 1;
        for (var i = length - 2; i >= 0; i--)
        {
            suffixProducts[i] = suffixProducts[i + 1] * nums[i + 1];
        }

        // Multiply prefix * suffix
        for (var i = 0; i < length; i++)
        {
            nums[i] = prefixProducts[i] * suffixProducts[i];
        }

        Console.WriteLine($"prefix: [{string.Join(",", prefixProducts)}]");
        Console.WriteLine($"suffix: [{string.Join(",", suffixProducts)}]");

        return nums;
    }
}