public class Solution {
    private Dictionary<(double, int), double> _resultMemo = new Dictionary<(double, int), double>();

    public double MyPow(double x, int n) {
        if (n == 0) return 1;
        if (n == 1) return x;
        if (_resultMemo.TryGetValue((x, n), out double result)) return result;

        if (n < 0)
        {
            //_resultMemo[(x, n)] = MyPow(x, n + 1);
            return 1 / MyPow(x, -n);
        }

        _resultMemo[(x, n)] = MyPow(x, n - 1);
        return x * _resultMemo[(x, n)];
    }
}