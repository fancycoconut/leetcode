class Solution:
    def reverseBits(self, n: int) -> int:
        bits = 32
        binary = ""
        quotient = n
        while quotient != 0:
            remainder = quotient % 2
            quotient = quotient // 2
            binary += str(remainder)
        
        final32BitBinary = binary.ljust(bits, "0")
        print(final32BitBinary)

        value = 0
        for i in range(len(final32BitBinary) - 1, -1, -1):
            bit = final32BitBinary[i]
            pos = abs(len(final32BitBinary) - i - 1)
            value += int(bit) * (2 ** pos)

        return value
