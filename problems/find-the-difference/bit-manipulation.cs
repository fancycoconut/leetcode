// Using Bit Manipulation

public class Solution {
    public char FindTheDifference(string s, string t) {
        //if (string.IsNullOrEmpty(s)) return t[0];

        char result = '\0';
        foreach (var letter in s)
        {
            result = (char)(result ^ letter);
        }

        foreach (var letter in t)
        {
            result = (char)(result ^ letter);
        }

        return result;
    }
}