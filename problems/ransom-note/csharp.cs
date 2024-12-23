public class Solution {
    public bool CanConstruct(string ransomNote, string magazine) {
        var map = new Dictionary<char, int>();

        foreach (var letter in magazine)
        {
            if (map.ContainsKey(letter))
            {
                map[letter]++;
            }
            else
            {
                map[letter] = 1;
            }
        }

        foreach (var letter in ransomNote)
        {
            if (!map.ContainsKey(letter)) return false;

            var numOfLettersLeft = map[letter];
            if (numOfLettersLeft - 1 < 0) return false;
            map[letter]--;
        }

        return true;
    }
}