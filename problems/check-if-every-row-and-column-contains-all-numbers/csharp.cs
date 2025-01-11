public class Solution {
    public bool CheckValid(int[][] matrix) {
        return AllColumnsAreInclusive(matrix) && AllRowsAreInclusive(matrix);
    }

    private bool AllColumnsAreInclusive(int[][] matrix)
    {
        var rows = matrix.Length;
        var cols = matrix[0].Length;

        for (var col = 0; col < cols; col++)
        {
            var set = new HashSet<int>();
            for (var row = 0; row < rows; row++)
            {
                var num = matrix[row][col];
                Console.WriteLine(num);
                if (set.Contains(num)) return false;
                set.Add(num);
            }
        }

        return true;
    }

    private bool AllRowsAreInclusive(int[][] matrix)
    {
        var rows = matrix.Length;
        for (var i = 0; i < rows; i++)
        {
            var row = matrix[i];
            var set = new HashSet<int>();
            foreach (var num in row)
            {
                if (set.Contains(num)) return false;
                set.Add(num);
            }
        }

        return true;
    }
}