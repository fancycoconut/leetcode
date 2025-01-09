public class SnakeGame {
    private int _width;
    private int _height;
    private int _score;
    private (int x, int y) _currentPosition;

    private readonly HashSet<(int x, int y)> _snakeBodyPositions = new();
    private readonly Queue<(int x, int y)> _foodPositions = new();

    public SnakeGame(int width, int height, int[][] foods) {
        _score = 0;
        _width = width;
        _height = height;
        _currentPosition = (0, 0);
        InitializeFood(foods);

        _snakeBodyPositions.Add(_currentPosition);
    }
    
    public int Move(string direction) {
        switch (direction)
        {
            case "U":
                return MoveUp();
            case "D":
                return MoveDown();
            case "L":
                return MoveLeft();
            case "R":
                return MoveRight();
            default:
                throw new InvalidOperationException("Invalid direction specified!");
        }
    }

    private int MoveUp()
    {
        if (!CanMoveUp()) return -1;

        var newPosition = (_currentPosition.x, _currentPosition.y - 1);
        var score = TryConsumeFoodAtPosition(newPosition, "U");
        _currentPosition = newPosition;

        _snakeBodyPositions.Add(newPosition);

        return score;
    }

    private int MoveDown()
    {
        if (!CanMoveDown()) return -1;

        var newPosition = (_currentPosition.x, _currentPosition.y + 1);
        var score = TryConsumeFoodAtPosition(newPosition, "D");
        _currentPosition = newPosition;

        _snakeBodyPositions.Add(newPosition);

        return score;
    }

    private int MoveLeft()
    {
        if (!CanMoveLeft()) return -1;

        var newPosition = (_currentPosition.x - 1, _currentPosition.y);
        var score = TryConsumeFoodAtPosition(newPosition, "L");
        _currentPosition = newPosition;

        _snakeBodyPositions.Add(newPosition);

        return score;
    }

    private int MoveRight()
    {
        if (!CanMoveRight()) return -1;

        var newPosition = (_currentPosition.x + 1, _currentPosition.y);
        var score = TryConsumeFoodAtPosition(newPosition, "R");
        _currentPosition = newPosition;

        _snakeBodyPositions.Add(newPosition);

        return score;
    }

    private int TryConsumeFoodAtPosition((int x, int y) position, string direction)
    {
        if (_foodPositions.Count == 0) return _score;

        var currentFoodPosition = _foodPositions.Peek();
        if (position.x == currentFoodPosition.x && position.y == currentFoodPosition.y)
        {
            Console.WriteLine($"Found food at ({currentFoodPosition.x}, {currentFoodPosition.y})");
            // Remove the food that is already eaten
            _foodPositions.Dequeue();
            _score++;
        }

        return _score;
    }

    private void GrowSnake((int x, int y) foodPosition, string direction)
    {
        foreach (var bodyPosition in _snakeBodyPositions)
        {
            switch (direction)
            {
                case "U":
                    break;
                case "D":
                    break;
                case "L":
                    break;
                case "R":
                    break;
                default:
                    throw new InvalidOperationException("Invalid direction specified!");
            }
        }

        _snakeBodyPositions.Add(foodPosition);
    }

    private bool CanMoveUp() => _currentPosition.y - 1 >= 0;
    private bool CanMoveDown() => _currentPosition.y + 1 < _height;
    private bool CanMoveLeft() => _currentPosition.x - 1 >= 0;
    private bool CanMoveRight() => _currentPosition.x + 1 < _width;

    private void InitializeFood(int[][] foods)
    {
        foreach (var food in foods)
        {
            var y = food[0];
            var x = food[1];
            Console.WriteLine($"Food: ({x}, {y})");

            _foodPositions.Enqueue((x, y));
        }
    }
}

/**
 * Your SnakeGame object will be instantiated and called as such:
 * SnakeGame obj = new SnakeGame(width, height, food);
 * int param_1 = obj.Move(direction);
 */