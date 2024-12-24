public class Solution {
    public int Divide(int dividend, int divisor) {
        try
        {
            return dividend / divisor;
        }
        catch (OverflowException ofe)
        {
            return int.MaxValue;
        }
    }
}