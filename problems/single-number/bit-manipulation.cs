// This approach uses Bit Manipulation
// Where:
// 0 XOR some bit will return that bit
// XOR of 2 same bits return 0
// XORing all bits together will return the unique number
public class Solution {
    public int SingleNumber(int[] nums) {
        var number = 0;
        for (var i = 0; i < nums.Length; i++)
        {
            var num = nums[i];
            number = number ^ num;
        }
        
        return number;
    }
}