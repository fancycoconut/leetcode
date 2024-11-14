public class Solution {
    public int RomanToInt(string s) {
        var letters = s.AsSpan();

        var total = 0;
        char prev = ' ';
        foreach (var letter in letters)
        {
            var currentValue = GetAdjustedRomanNumeralsValue(prev, letter);

            total += currentValue;
            prev = letter;
        }

        return total;
    }

    private int GetAdjustedRomanNumeralsValue(char prev, char current)
    {
        var currentValue = ParseSingleRomanNumeral(current);
        // Value minus previously added value that is for a single digit
        // Basically the actual value of the letters minus the prev e.g. IV = 4 and prev is I which is 1
        // So we have to add 3 which is 4 - 1 to be clear
        return (prev, current) switch {
            ('I', 'V') => 4 - 1,
            ('I', 'X') => 9 - 1,
            ('X', 'L') => 40 - 10,
            ('X', 'C') => 90 - 10,
            ('C', 'D') => 400 - 100,
            ('C', 'M') => 900 - 100,
            _ => currentValue
        };
    }

    private int ParseSingleRomanNumeral(char c)
    {
        return c switch {
            'I' => 1,
            'V' => 5,
            'X' => 10,
            'L' => 50,
            'C' => 100,
            'D' => 500,
            'M' => 1000,
            _ => 0
        };
    }
}