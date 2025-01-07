public class Solution {
    public int CountAsterisks(string s) {
        var letters = s.AsSpan();
        var totalAsterisks = 0;
        var inVerticalBar = false;
        for (var i = 0; i < letters.Length; i++)
        {
            var letter = letters[i];
            if (letter == '|')
            {
                inVerticalBar = !inVerticalBar;
            }

            if (letter == '*' && !inVerticalBar)
            {
                totalAsterisks++;
            }
        }

        return totalAsterisks;
    }
}