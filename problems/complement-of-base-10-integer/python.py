class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        binary = self.toBinary(n)
        #print(binary)

        for i, bit in enumerate(binary):
            binary[i] = 1 if bit == 0 else 0

        #print(binary)
        ans = self.fromBinary(binary)
        #print(ans)

        return ans

    def fromBinary(self, binary: list[int]) -> int:
        ans = 0

        pos = 0
        for i in range(len(binary) - 1, -1, -1):
            bit = binary[i]
            n = pow(2, pos)
            pos += 1
            ans += (n * bit)
        return ans
        
    def toBinary(self, n: int) -> list[int]:
        output = []
        while n > 0:
            carry = n % 2
            n = n // 2
            output.append(carry)
        output.reverse()
        return output
