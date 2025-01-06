public class Solution {
    public string Convert(string s, int numRows) {
        if (numRows == 1) return s;

        var letters = s.AsSpan();
        var rows = new StringBuilder[numRows];

        for (var i = 0; i < numRows; i++)
        {
            rows[i] = new StringBuilder();
        }

        var row = 0;
        var goingDown = true;
        foreach (var letter in letters)
        {
            rows[row].Append(letter);

            if (goingDown)
            {
                row++;
            }
            else
            {
                row--;
            }

            if (row == numRows - 1)
            {
                goingDown = false;
                continue;
            }
            if (row == 0)
            {
                goingDown = true;
            }
            
        }

        var sb = new StringBuilder();
        for (var i = 0; i < numRows; i++)
        {
            sb.Append(rows[i].ToString());
            //Console.WriteLine(rows[i].ToString());
        }

        return sb.ToString();
    }
}