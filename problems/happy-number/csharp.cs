public class Solution {
    public bool IsHappy(int n) {
        var visitedNumbers = new HashSet<int>();

        var current = n;
        while (!visitedNumbers.Contains(current))
        {
            visitedNumbers.Add(current);
            var sum = 0;
            var currentCharacters = current.ToString().AsSpan();
            foreach (var character in currentCharacters)
            {
                var num = int.Parse(character.ToString());
                var square = num * num;
                Console.WriteLine($"{num} ^ 2 = {square}");

                sum += square;
            }

            if (sum == 1) return true;
            current = sum;
        }

        return false;
    }
}