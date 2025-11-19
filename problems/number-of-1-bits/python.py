class Solution:
    def hammingWeight(self, n: int) -> int:
        numOfOnes = 0
        while n != 0:
            remainder = n % 2
            n //= 2
            numOfOnes += 1 if remainder == 1 else 0

        return numOfOnes
