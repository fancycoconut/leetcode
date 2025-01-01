public class Solution {
    public bool IsValidSudoku(char[][] board) {
        var rowsIsValid = ValidateRows(board);
        var columnsIsValid = ValidateColumns(board);
        var subBoxsAreValid = ValidateSubBoxes(board);
        Console.WriteLine($"Rows valid: {rowsIsValid}");
        Console.WriteLine($"Columns valid: {columnsIsValid}");
        Console.WriteLine($"SubBoxes valid: {subBoxsAreValid}");

        return rowsIsValid && columnsIsValid && subBoxsAreValid;
    }

    private bool ValidateSubBoxes(char[][] board)
    {
        var rows = board.Length;
        var columns = board[0].Length;
        for (var i = 0; i < rows; i += 3)
        {
            var colOffset = 0;
            for (var j = 0; j < 3; j++)
            {
                // Construct sub boxes
                var subBox = new char[3][];
                var temp = board[i..(i+3)];
                for (var row = 0; row < temp.Length; row++)
                {
                    subBox[row] = new char[3];
                    for (var col = 0; col < 3; col++)
                    {
                        subBox[row][col] = temp[row][colOffset + col];
                    }
                }

                if (!ValidateSubBox(subBox)) return false;
                colOffset += 3;
            }                       
        }

        return true;
    }

    private bool ValidateSubBox(char[][] subBox)
    {
        var rows = subBox.Length;
        var columns = subBox[0].Length;
        //Console.WriteLine($"Validating a {rows} x {columns} box");
        var set = new HashSet<char>();
        
        for (var i = 0; i < rows; i++)
        {            
            for (var j = 0; j < columns; j++)
            {
                var cell = subBox[i][j];
                //Console.WriteLine(cell);

                if (cell == '.') continue;                
                if (set.Contains(cell)) return false;
                set.Add(cell);
            }
        }

        return true;
    }

    private bool ValidateColumns(char[][] board)
    {
        var rows = board.Length;
        var columns = board[0].Length;

        for (var i = 0; i < rows; i++)
        {
            var set = new HashSet<char>();
            for (var j = 0; j < columns; j++)
            {
                var cell = board[j][i];
                if (cell == '.') continue;
                if (set.Contains(cell)) return false;

                //Console.WriteLine(cell);
                set.Add(cell);
            }
        }

        return true;
    }

    private bool ValidateRows(char[][] board)
    {
        var rows = board.Length;
        var columns = board[0].Length;

        for (var i = 0; i < columns; i++)
        {
            var set = new HashSet<char>();
            for (var j = 0; j < rows; j++)
            {
                var cell = board[i][j];
                if (cell == '.') continue;
                if (set.Contains(cell)) return false;

                //Console.WriteLine(cell);
                set.Add(cell);
            }
        }

        return true;
    }
}