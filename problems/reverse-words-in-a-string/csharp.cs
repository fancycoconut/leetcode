public class Solution {
    public string ReverseWords(string s) {
        var words = s.Trim().Split(" ");
        var output = new List<string>();

        for (var i = words.Length - 1; i >= 0; i--)
        {
            var word = words[i].Trim();
            if (string.IsNullOrWhiteSpace(word)) continue;
            Console.WriteLine(word);

            output.Add(word);
        }

        return string.Join(" ", output);
    }
}