public class Solution {
    public IList<string> StringMatching(string[] words) {
        var output = new HashSet<string>();
        foreach (var word in words)
        {
            foreach (var word2 in words)
            {
                if (word != word2 && word.Contains(word2))
                {
                    output.Add(word2);
                }
            }
        }

        return output.ToList();
    }
}