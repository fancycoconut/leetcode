public class Solution {
    public int LengthOfLongestSubstring(string s) {
        var longestLength = 0;
        var characters = s.AsSpan();
        var uniqueCharacters = new HashSet<char>();

        var windowStart = 0;
        for (var windowEnd = 0; windowEnd < characters.Length; windowEnd++)
        {
            var currentCharacter = characters[windowEnd];
            while (uniqueCharacters.Contains(currentCharacter) && windowStart < windowEnd)
            {
                if (characters[windowStart] != currentCharacter)
                {
                    uniqueCharacters.Remove(characters[windowStart]);
                }
                
                windowStart++;
                currentCharacter = characters[windowStart];
            }

            uniqueCharacters.Add(currentCharacter);

            if (uniqueCharacters.Count > longestLength)
            {
                longestLength = uniqueCharacters.Count; 
            }    
        }

        return longestLength;
    }
}