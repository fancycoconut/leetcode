class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = max(len(a), len(b))
        output = [''] * length
        paddedA = a.zfill(length)
        paddedB = b.zfill(length)

        carry = 0
        for i in range(length - 1, -1, -1):
            res = int(paddedA[i]) + int(paddedB[i]) + carry
            carry = res // 2
            output[i] = res % 2

        if carry == 1:
            return "1" + "".join(str(x) for x in output)

        return "".join(str(x) for x in output)
