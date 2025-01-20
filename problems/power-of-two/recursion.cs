public class Solution {
    public bool IsPowerOfTwo(int n) {
        if (n == 0) return false;
        if (n == 1) return true;
        if (n == 3) return false;
        return n % 2 == 0 && IsPowerOfTwo(n / 2);
    }
}