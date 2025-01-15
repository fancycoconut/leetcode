public class Solution {
    public bool WordPattern(string pattern, string s) {
        var words = s.Split(" ").ToArray();
        if (pattern.Length != words.Length) return false;

        var patternTokens = pattern.AsSpan();
        var addedWords = new HashSet<string>();
        var map = new Dictionary<char, string>();
        for(var i = 0; i < words.Length; i++)
        {
            var token = patternTokens[i];
            var word = words[i];
            if (addedWords.Contains(word)) continue;
            map[token] = word;
            addedWords.Add(word);
        }

        var output = new List<string>();
        for (var i = 0; i < patternTokens.Length; i++)
        {
            var token = patternTokens[i];
            if (!map.ContainsKey(token)) continue;
            var word = map[token];
            output.Add(word);
        }

        Console.WriteLine(string.Join(" ", output));
        return string.Join(" ", output) == s;
    }
}