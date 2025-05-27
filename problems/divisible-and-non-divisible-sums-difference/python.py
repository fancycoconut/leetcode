class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        a = 0
        for i in range(1, n + 1):
            if i % m != 0:
                a += i

        b = 0
        for j in range(1, n + 1):
            if j % m == 0:
                b += j

        return a - b
