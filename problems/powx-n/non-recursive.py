class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x

        k = x if n > 0 else (1 / x)
        memo = k

        total = abs(n) - 1
        while total > 0:
            memo = memo * k

            total -= 1

        return memo