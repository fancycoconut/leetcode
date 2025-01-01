public class Solution {
    public int LongestPalindrome(string s) {
        var map = new Dictionary<char, int>();

        var characters = s.AsSpan();
        foreach (var character in characters)
        {
            if (map.ContainsKey(character))
            {
                map[character] += 1;
            }
            else
            {
                map[character] = 1;
            }
        }

        var totalLength = 0;
        var hasOddFrequency = false;

        foreach (var kvp in map)
        {
            var isEven = (kvp.Value % 2) == 0;
            if (isEven)
            {
                totalLength += kvp.Value;
                continue;
            }
            
            totalLength += kvp.Value - 1;
            hasOddFrequency = true;
        }

        return hasOddFrequency
            ? totalLength + 1
            : totalLength;
    }
}