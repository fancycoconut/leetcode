public class Solution {
    // Using 2 pointer approach
    public bool IsPalindrome(string s) {
        var characters = s.AsSpan().ToArray();

        var left = 0;
        var right = characters.Length - 1;

        while (left < characters.Length && right > 0)
        {
            var leftCharacter = characters[left];
            var rightCharacter = characters[right];

            if (!IsAlphaNumeric(leftCharacter))
            {
                left++;
                continue;
            }

            if (!IsAlphaNumeric(rightCharacter))
            {
                right--;
                continue;
            }

            if (char.ToUpper(characters[left++]) != char.ToUpper(characters[right--])) return false;
        }

        return true;
    }

    private bool IsAlphaNumeric(char letter)
    {
        return (letter >= 48 && letter <= 57) || (letter >= 65 && letter <= 90) || (letter >= 97 && letter <= 122);
    }
}