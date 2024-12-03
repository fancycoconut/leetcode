public class Solution {
    public string AddSpaces(string s, int[] spaces) {
        var sb = new StringBuilder();

        var lastPosition = 0;
        foreach (var space in spaces)
        {
            var endPosition = space;
            //Console.WriteLine(s[lastPosition..endPosition]);
            sb.Append(s[lastPosition..endPosition]);

            sb.Append(" ");
            lastPosition = endPosition;
        }

        sb.Append(s[lastPosition..]);

        return sb.ToString();
    }
}