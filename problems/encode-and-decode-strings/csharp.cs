public class Codec {

    // Encodes a list of strings to a single string.
    public string encode(IList<string> strs) {
        var sb = new StringBuilder();
        const string stringsDeliminator = "-||-";
        const string letterDeliminators = "~|~";

        foreach (var str in strs)
        {
            if (string.IsNullOrEmpty(str))
            {
                sb.Append("!!EMPTY!!");
                sb.Append(stringsDeliminator);
                continue;
            }

            foreach (var letter in str)
            {
                sb.Append(letter);
                sb.Append(letterDeliminators);
            }

            sb.Append(stringsDeliminator);
        }

        return sb.ToString();
    }

    // Decodes a single string to a list of strings.
    public IList<string> decode(string s) {
        if (string.IsNullOrEmpty(s)) return new List<string>{ "" };

        var strings = new List<string>();
        const string stringsDeliminator = "-||-";
        const string letterDeliminators = "~|~";

        var sb = new StringBuilder();
        var parts = s.Split(stringsDeliminator);
        foreach (var part in parts)
        {
            sb.Clear();
            if (string.IsNullOrEmpty(part)) continue;

            if (part == "!!EMPTY!!")
            {
                strings.Add("");
                continue;
            }

            var letters = part.Split(letterDeliminators);
            foreach (var letter in letters)
            {
                sb.Append(letter);
            }

            strings.Add(sb.ToString());
        }

        return strings;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));