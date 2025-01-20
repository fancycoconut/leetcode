public class Solution {
    public bool IsPowerOfThree(int n) {
        if (n <= 0) return false;
        if (n == 1) return true;
        return n % 3 == 0 && IsPowerOfThree(n / 3);
    }
}