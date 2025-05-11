class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        hasThreeConsecutiveOdds = False
        numOfConsecutiveOdds = 0
        for num in arr:
            isOdd = num % 2 == 1

            if isOdd:
                numOfConsecutiveOdds += 1
            else:
                numOfConsecutiveOdds = 0

            if numOfConsecutiveOdds >= 3:
                hasThreeConsecutiveOdds = True

        return hasThreeConsecutiveOdds
