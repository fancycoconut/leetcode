public class Solution {
    public bool Exist(char[][] board, string word) {
        var found = false;
        var letters = word.AsSpan();

        var startingPoints = GetStartPositions(letters[0], board).ToList();
        if (!startingPoints.Any()) return false;

        foreach (var point in startingPoints)
        {
            //Console.WriteLine($"Start point: ({point.x}, {point.y})");
            if (ScanForWord(point, word, board))
            {
                found = true;
            }
        }

        return found;
    }

    private bool ScanForWord((int x, int y) startingPoint, string word, char[][] board)
    {
        var height = board.Length;
        var width = board[0].Length;

        var currentLetterPosition = 0;
        var wordLetters = word.AsSpan();

        var queue = new Queue<(int x, int y)>();
        var visitedLocations = new HashSet<(int x, int y)>();
        queue.Enqueue(startingPoint);

        var prevPosition = startingPoint;
        while (queue.Count > 0)
        {
            var position = queue.Dequeue();
            if (visitedLocations.Contains(position)) continue;

            var x = position.x;
            var y = position.y;
            var letter = board[y][x];
            var currentLetter = wordLetters[currentLetterPosition];

            currentLetterPosition += currentLetterPosition + 1 >= word.Length 
                ? 0
                : 1;
            
            var nextLetter = wordLetters[currentLetterPosition];

            if (CanMoveUp(position) && board[y-1][x] == nextLetter)
            {
                queue.Enqueue((x, y - 1));
            }

            if (CanMoveDown(position, height) && board[y+1][x] == nextLetter)
            {
                queue.Enqueue((x, y + 1));
            }

            if (CanMoveLeft(position) && board[y][x-1] == nextLetter)
            {
                queue.Enqueue((x - 1, y));
            }

            if (CanMoveRight(position, width) && board[y][x+1] == nextLetter)
            {
                queue.Enqueue((x + 1, y));
            }

            visitedLocations.Add(position);
            prevPosition = position;         
        }

        var foundWord = GetWordFromVisitedLocations(visitedLocations, board);
        Console.WriteLine($"Found word: {foundWord}");
        return foundWord == word;
    }

    private string GetWordFromVisitedLocations(HashSet<(int x, int y)> visitedLocations, char[][] board)
    {
        var sb = new StringBuilder();
        foreach (var location in visitedLocations)
        {
            var letter = board[location.y][location.x];
            sb.Append(letter);
        }

        return sb.ToString();
    }

    private bool CanMoveUp((int x, int y) current) => current.y - 1 >= 0;
    private bool CanMoveDown((int x, int y) current, int height) => current.y + 1 < height;
    private bool CanMoveLeft((int x, int y) current) => current.x - 1 >= 0;
    private bool CanMoveRight((int x, int y) current, int width) => current.x + 1 < width;

    private IEnumerable<(int x, int y)> GetStartPositions(char letter, char[][] board)
    {
        var height = board.Length;
        var width = board[0].Length;
        //Console.WriteLine($"Reading a {width} x {height} board");

        for (var x = 0; x < width; x++)
        {
            for (var y = 0; y < height; y++)
            {
                var currentLetter = board[y][x];
                if (currentLetter != letter) continue;
                yield return (x, y);
            }
        }
    }
}