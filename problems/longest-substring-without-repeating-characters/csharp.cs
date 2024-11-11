public class Solution {
    public int LengthOfLongestSubstring(string s) {
        var characters = s.AsSpan();

        var maxLongestLength = 0;
        var uniqueCharacters = new HashSet<char>();

        var left = 0;
        for (var right = 0; right < characters.Length; right++)
        {
            var currentCharacter = characters[right];
            while (uniqueCharacters.Contains(currentCharacter))
            {
                var leftCharacter = characters[left];
                uniqueCharacters.Remove(leftCharacter);
                left++;
            }

            uniqueCharacters.Add(currentCharacter);
            maxLongestLength = Math.Max(maxLongestLength, right - left + 1);
        }

        return maxLongestLength;
    }
}