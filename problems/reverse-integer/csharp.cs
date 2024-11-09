public class Solution {
    public int Reverse(int x) {
        var characters = x.ToString().AsSpan();

        var sb = new StringBuilder();
        var isNegative = false;

        for (var i = characters.Length - 1; i >= 0; i--)
        {
            var currentChar = characters[i];
            if (currentChar == '-')
            {
                isNegative = true;
                break;
            }

            sb.Append(currentChar);
        }

        var reversed = sb.ToString();
        Console.WriteLine(reversed);

        if (!int.TryParse(reversed, out var output)) return 0;

        return isNegative ? output * -1 : output;
    }
}