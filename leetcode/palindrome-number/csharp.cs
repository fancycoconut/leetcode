public class Solution {
    public bool IsPalindrome(int x) {
        var input = x.ToString().AsSpan();
        var midpoint = input.Length / 2;
        var evenLength = input.Length % 2 == 0;
        var stack = new Stack();

        for (var i = 0; i < input.Length; i++)
        {
            var current = input[i];
            if (i < midpoint)
            {
                stack.Push(current);
                continue;
            }
            if (i == midpoint && !evenLength) continue;

            if (current != (char)stack.Pop()) return false;
            
        }

        return true;
    }
}