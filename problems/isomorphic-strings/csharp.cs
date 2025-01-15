public class Solution {
    public bool IsIsomorphic(string s, string t) {
        if (s.Length != t.Length) return false;

        var a = s.AsSpan();
        var b = t.AsSpan();
        var uniqueCharacters = new HashSet<char>();
        var map = new Dictionary<char, char>();

        for (var i = 0; i < a.Length; i++)
        {
            var x = a[i];
            var y = b[i];
            if (uniqueCharacters.Contains(y)) continue;

            map[x] = y;
            uniqueCharacters.Add(y);         
        }

        var sb = new StringBuilder();
        for (var i = 0; i < a.Length; i++)
        {
            var x = a[i];
            if (!map.ContainsKey(x)) continue;
            sb.Append(map[x]);
        }

        Console.WriteLine(sb.ToString());
        return sb.ToString() == t;
    }
}