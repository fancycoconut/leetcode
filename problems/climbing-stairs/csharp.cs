public class Solution {
    private Dictionary<int, int> _cache = new();

    // Basically a subsets problem
    // Using dynamic programming
    public int ClimbStairs(int n) {
        if (_cache.ContainsKey(n)) return _cache[n];
        if (n == 0) return 1;
        if (n == 1) return 1;
        if (n == 2) return 2;

        var result = ClimbStairs(n-1) + ClimbStairs(n-2);
        _cache[n] = result;

        return result;
    }
}