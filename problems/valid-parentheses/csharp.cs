public class Solution {
    public bool IsValid(string s) {
        if (s.Length == 1) return false;

        var stack = new Stack<char>();
        var closingBrackets = new List<char>();
        var symbols = s.AsSpan();

        for (var i = 0; i < symbols.Length; i++)
        {
            var symbol = symbols[i];
            if (IsValidOpening(symbol))
            {
                stack.Push(symbol);
                continue;
            }

            if (IsValidClosing(symbol))
            {
                var opening = GetOpening(symbol);

                if (stack.Count > 0 && opening == stack.Peek())
                {
                    stack.Pop();
                }
                else
                {
                    return false;
                }
            }
        }

        return stack.Count == 0;
    }

    private bool IsValidOpening(char symbol) => "({[".Contains(symbol);
    private bool IsValidClosing(char symbol) => ")}]".Contains(symbol);

    private char GetOpening(char closing)
    {
        return closing switch {
            ')' => '(',
            '}' => '{',
            ']' => '[',
            _ => '?'
        };
    }
}