public class Solution {
    public int[] PlusOne(int[] digits) {
        var carry = 1;
        var output = new int[digits.Length];

        for (var i = digits.Length - 1; i >= 0; i--)
        {
            var num = digits[i];
            var result = num + carry;
            carry = (int)(result / 10);
            output[i] = result % 10;
        }

        if (carry != 0)
        {
            var temp = new int[digits.Length + 1];
            for (var i = digits.Length - 1; i > 0; i--)
            {
                temp[i] = output[i];
            }
            temp[0] = carry;
            output = temp;
        }

        return output;
    }
}