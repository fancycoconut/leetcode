public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        var prefix = strs[0];
        var prefixLength = prefix.Length;
        for (var i = 1; i < strs.Length; i++)
        {
            var str = strs[i];
            var safeLength = prefixLength >= str.Length ? str.Length : prefixLength;
            var currentPrefix = safeLength == 0
                ? ""
                : str.AsSpan()[0..safeLength].ToString();

            while (prefix != currentPrefix)
            {
                prefixLength--;
                safeLength = prefixLength >= str.Length ? str.Length : prefixLength;
                prefix = prefixLength == 0
                    ? ""
                    : prefix.AsSpan()[0..prefixLength].ToString();
                currentPrefix = str.AsSpan()[0..safeLength].ToString();
            }
        }

        return prefix;
    }
}