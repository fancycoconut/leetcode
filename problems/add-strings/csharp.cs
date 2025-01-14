public class Solution {
    public string AddStrings(string num1, string num2) {
        var length = Math.Max(num1.Length, num2.Length);
        var num1Span = num1.PadLeft(length, '0').AsSpan();
        var num2Span = num2.PadLeft(length, '0').AsSpan();

        var output = new char[length];

        var remainingCarry = 0;
        for (var i = length - 1; i >= 0; i--)
        {
            var n = (int)char.GetNumericValue(num1Span[i]);
            var m = (int)char.GetNumericValue(num2Span[i]);
            var sum = n + m;
            sum += remainingCarry;

            var result = sum % 10;
            remainingCarry = sum / 10;

            output[i] = result.ToString().AsSpan()[0];
        }

        if (remainingCarry > 0)
        {
            var temp = new char[length + 1];
            for (var i = length - 1; i >= 0; i--)
            {
                temp[i + 1] = output[i];
            }

            temp[0] = remainingCarry.ToString().AsSpan()[0];
            output = temp;
        }

        return new string(output);
    }
}