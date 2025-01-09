// Solution using breadth first search approach
public class Solution {
    public int MaxAreaOfIsland(int[][] grid) {
       var visitedLocations = new HashSet<(int row, int col)>();

       var maxIslandSize = 0;
       for (var row = 0; row < grid.Length; row++)
       {
            for (var col = 0; col < grid[0].Length; col++)
            {
                var element = grid[row][col];
                if (element == 0) continue;

                var islandSize = BfsMaxIslandArea((row, col), grid, visitedLocations);
                maxIslandSize = Math.Max(maxIslandSize, islandSize);
            }
       }

       return maxIslandSize;
    }

    private int BfsMaxIslandArea((int row, int col) location, int[][] grid, HashSet<(int row, int col)> visitedLocations)
    {
        if (visitedLocations.Contains(location)) return -1;

        var queue = new Queue<(int row, int col)>();
        var rows = grid.Length;
        var cols = grid[0].Length;

        var islandSize = 0;
        queue.Enqueue(location);

        while (queue.Count > 0)
        {
            var position = queue.Dequeue();
            if (visitedLocations.Contains(position)) continue;

            var row = position.row;
            var col = position.col;
            var element = grid[row][col];
            if (element != 1) continue;
            
            islandSize++;
            visitedLocations.Add(position);

            if (row - 1 >= 0)
            {
                queue.Enqueue((row - 1, col));
            }

            if (row + 1 < rows)
            {
                queue.Enqueue((row + 1, col));
            }

            if (col - 1 >= 0)
            {
                queue.Enqueue((row, col - 1));
            }

            if (col + 1 < cols)
            {
                queue.Enqueue((row, col + 1));
            }
        }

        return islandSize;
    }
}