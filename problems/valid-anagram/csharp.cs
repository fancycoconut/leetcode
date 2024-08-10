public class Solution {
    public bool IsAnagram(string s, string t) {
        var sortedS = s.ToCharArray();
        var sortedT = t.ToCharArray();

        Array.Sort(sortedS);
        Array.Sort(sortedT);

        return string.Equals(new string(sortedS), new string(sortedT));
    }
}
