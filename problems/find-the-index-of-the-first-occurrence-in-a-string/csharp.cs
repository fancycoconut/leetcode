// Using sliding window approach
// Where we keep adding to the right and checking and removing 
// from the left if the string does not match
public class Solution {
    public int StrStr(string haystack, string needle) {
        var left = 0;
        var right = 0;
        var sb = new StringBuilder();
        var needleLetters = needle.AsSpan();

        for (var i = 0; i < haystack.Length; i++)
        {
            var letter = haystack[i];
            sb.Append(letter);

            if (sb.ToString() == needle)
            {
                return (i + 1) - needle.Length;
            }

            if (sb.Length == needle.Length)
            {
                sb.Remove(0, 1);
                continue;
            }
        }

        //Console.WriteLine(sb.ToString());
        return -1;
    }
}