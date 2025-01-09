public class Solution {
    public int PrefixCount(string[] words, string pref) {
        var numOfPrefixCount = 0;
        foreach (var word in words)
        {
            if (!word.StartsWith(pref)) continue;
            numOfPrefixCount++;
        }

        return numOfPrefixCount;
    }
}