class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n + 1):
            res = self.numOfOnes(i)
            output.append(res)

        return output
    
    def numOfOnes(self, n: int) -> int:
        numOfOnes = 0
        while n != 0:
            remainder = n % 2
            n //= 2
            numOfOnes += 1 if remainder == 1 else 0
        return numOfOnes
