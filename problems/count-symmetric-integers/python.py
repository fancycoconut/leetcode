class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        numOfSymmetric = 0
        symmetricIntegers = []
        for n in range(low, high + 1):
            num = str(n)
            if len(num) % 2 == 1:
                continue

            mid = len(num) // 2
            left = num[:mid]
            right = num[mid:]
            leftSum = sum(int(x) for x in left)
            rightSum = sum(int(y) for y in right)
            if leftSum != rightSum:
                continue
            symmetricIntegers.append(n)

        return len(symmetricIntegers)
