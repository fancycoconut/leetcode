public class Solution {
    public void ReverseString(char[] s) {
        var midpoint = s.Length / 2;

        var start = 0;
        var end = s.Length - 1;
        while (start < midpoint)
        {
            s[start] = (char)(s[start] ^ s[end]);
            s[end] = (char)(s[start] ^ s[end]);
            s[start] = (char)(s[start] ^ s[end]);

            start++;
            end--;
        }
    }
}