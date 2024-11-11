public class Solution {
    public int LengthOfLongestSubstring(string s) {
        var characters = s.AsSpan();
        if (characters.Length == 1) return 1;

        var maxLongestLength = 0;
        var uniqueCharacters = new HashSet<char>();

        var left = 0;
        for (var right = 0; right < characters.Length; right++)
        {
            var currentCharacter = characters[right];
            if (!uniqueCharacters.Contains(currentCharacter))
            {
                uniqueCharacters.Add(currentCharacter);
                maxLongestLength = Math.Max(maxLongestLength, right - left + 1);
                continue;
            }

            while (characters[left] != characters[right])
            {
                uniqueCharacters.Remove(characters[left]);
                left++;
            }
            uniqueCharacters.Remove(characters[left]);
            left++;
            uniqueCharacters.Add(currentCharacter);
        }

        return maxLongestLength;
    }
}