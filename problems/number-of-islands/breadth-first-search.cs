// Using breadth first search visualizing the islands as a connected graph
public class Solution {
    public int NumIslands(char[][] grid) {
        var numOfIslands = 0;
        var visitedLocations = new HashSet<(int row, int col)>();

        for (var row = 0; row < grid.Length; row++)
        {
            for (var col = 0; col < grid[0].Length; col++)
            {
                var element = grid[row][col];
                if (element != '1') continue;
                
                if (Bfs((row, col), visitedLocations, grid))
                {
                    numOfIslands++;
                }
            }
        }

        return numOfIslands;
    }

    private bool Bfs((int row, int col) position, HashSet<(int row, int col)> visitedLocations, char[][] grid)
    {
        var queue = new Queue<(int row, int col)>();
        if (visitedLocations.Contains(position)) return false;

        queue.Enqueue(position);

        var prevElement = grid[position.row][position.col];
        while (queue.Count > 0)
        {
            var currentPosition = queue.Dequeue();
            if (visitedLocations.Contains(currentPosition)) continue;

            var row = currentPosition.row;
            var col = currentPosition.col;
            var element = grid[row][col];
            if (element != prevElement) continue;

            visitedLocations.Add(currentPosition);

            if (row - 1 >= 0)
            {
                queue.Enqueue((row - 1, col));
            }

            if (row + 1 < grid.Length)
            {
                queue.Enqueue((row + 1, col));
            }

            if (col - 1 >= 0)
            {
                queue.Enqueue((row, col - 1));
            }

            if (col + 1 < grid[0].Length)
            {
                queue.Enqueue((row, col + 1));
            }

            prevElement = element;
        }

        return true;
    }
}