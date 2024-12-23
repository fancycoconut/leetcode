public class Solution {
    public int LengthOfLastWord(string s) {
        var sletters = s.TrimStart()
        .TrimEnd()
        .AsSpan();

        var lastIndex = -1;
        for (var i = 0; i < sletters.Length; i++)
        {
            var letter = sletters[i];
            if (letter != ' ') continue;
            lastIndex = i;
        }

        var lastWord = sletters[(lastIndex + 1)..];

        return lastWord.Length;
    }
}