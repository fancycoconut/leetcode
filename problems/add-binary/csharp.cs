public class Solution {
    public string AddBinary(string a, string b) {
        var carry = 0;
        var maxLength = Math.Max(a.Length, b.Length);
        var paddedA = a.PadLeft(maxLength, '0');
        var paddedB = b.PadLeft(maxLength, '0');

        var abits = paddedA.AsSpan();
        var bbits = paddedB.AsSpan();
        var output = new char[maxLength];

        for (var i = maxLength - 1; i >= 0; i--)
        {
            var bitA = char.GetNumericValue(abits[i]);
            var bitB = char.GetNumericValue(bbits[i]);
            var sum = bitA + bitB;
            sum += carry;
            carry = (int)(sum / 2);
            var remainder = (int)(sum % 2);
            output[i] = remainder.ToString().AsSpan()[0];
        }

        if (carry != 0)
        {
            var temp = new char[maxLength + 1];
            for (var i = maxLength; i > 0; i--)
            {
                temp[i] = output[i-1];
            }
            temp[0] = carry.ToString().AsSpan()[0];
            output = temp;
        }

        return new string(output);
    }
}