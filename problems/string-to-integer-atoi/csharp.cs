public class Solution {
    public int MyAtoi(string s) {
        var characters = s.AsSpan();
        var sb = new StringBuilder();

        var isNegative = false;
        var alreadyHasPrefix = false;
        for (var i = 0; i < characters.Length; i++)
        {
            var current = characters[i];
            if (current == ' ' && !alreadyHasPrefix && sb.Length == 0) continue;
            if (current == '-' && !alreadyHasPrefix && sb.Length == 0)
            {
                isNegative = true;
                alreadyHasPrefix = true;
                continue;
            }
            if (current == '+' && !alreadyHasPrefix && sb.Length == 0)
            {
                alreadyHasPrefix = true;
                continue;
            }

            if (IsAlphabetical(current) || !IsNumeric(current)) break;

            sb.Append(current);
        }

        var parsed = sb.ToString();
        if (string.IsNullOrEmpty(parsed)) return 0;
        //Console.WriteLine(parsed);

        var output = 0;
        try {
            output = int.Parse(parsed);
        }
        catch (OverflowException)
        {
            output = isNegative ? int.MinValue : int.MaxValue;
        }

        return isNegative ? output * -1 : output;
    }

    private bool IsNumeric(char letter) 
        => letter >= 48 && letter <= 57;

    private bool IsAlphabetical(char letter)
        => (letter >= 65 && letter <= 90) || (letter >= 97 && letter <= 122);
}