public class Solution {
    public bool IsMatch(string s, string p) {
        var hasSingleCharacterMatch = p.Contains(".");
        var hasMultiCharacterMatch = p.Contains("*");
        var hasRegexMatch = hasSingleCharacterMatch || hasMultiCharacterMatch;

        if (!hasRegexMatch) return s == p;

        var i = 0;
        var j = 0;
        var sb = new StringBuilder();
        var patternCharacters = p.AsSpan();
        var characters = s.AsSpan();

        // Build the string with regex applied
        while (i < p.Length)
        {
            var character = characters[j];
            var regexCharacter = patternCharacters[i];
            if (regexCharacter == '.')
            {
                sb.Append(character);
                j++;
                i++;
                continue;
            }

            if (regexCharacter == '*')
            {
                var k = j;
                var l = i;
                while (l < characters.Length && k < patternCharacters.Length)
                {
                    var c = characters[l];
                    var nextCharacter = patternCharacters[k];
                    if (nextCharacter != '*') break;
                    sb.Append(c);
                    l++;
                    k++;
                }

                j = k;
                i = l;
                continue;
            }

            sb.Append(regexCharacter);
            j++;
            i++;
        }

        Console.WriteLine($"Built regex string: {sb.ToString()}");
        // Compare the built string and the original
        return s == sb.ToString();
    }
}