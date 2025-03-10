class Solution:
    def tribonacci(self, n: int) -> int:
        memo = []
        memo.append(0)
        memo.append(1)
        memo.append(1)
        for i in range(2, n):
            tribonacci = memo[i-2] + memo[i-1] + memo[i]
            print('i = ' + str(i) + ' n = ' + str(tribonacci))
            memo.append(tribonacci)
        return memo[n]
