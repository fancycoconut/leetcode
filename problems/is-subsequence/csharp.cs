public class Solution {
    public bool IsSubsequence(string s, string t) {
        if (string.IsNullOrEmpty(s)) return true;
        if (s.Length == t.Length) return s == t;

        var lettersInS = s.AsSpan();
        var lettersInT = t.AsSpan();

        var j = 0;
        var buffer = new StringBuilder();
        for (var i = 0; i < lettersInT.Length; i++)
        {
            var letter = lettersInT[i];
            if (j < lettersInS.Length && letter == lettersInS[j])
            {
                j++;
                buffer.Append(letter);
            }
        }

        return buffer.ToString() == s;
    }
}