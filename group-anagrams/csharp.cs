public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        var map = new Dictionary<string, List<int>>();

        var i = 0;
        foreach (var word in strs)
        {
            var rawWord = word.AsSpan().ToArray();
            Array.Sort(rawWord);
            var sortedWord = rawWord.AsSpan().ToString();
            //Console.WriteLine(sortedWord);

            if (map.ContainsKey(sortedWord))
            {
                map[sortedWord].Add(i);
            }
            else
            {
                map[sortedWord] = new List<int> { i };
            }

            i++;
        }

        List<IList<string>> results = new List<IList<string>>();
        foreach (var key in map.Keys)
        {
            var groupOfWords = new List<string>();
            foreach (var n in map[key])
            {
                groupOfWords.Add(strs[n]);
            }

            results.Add(groupOfWords);
        }

        return results;
    }
}