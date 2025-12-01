class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        total = 0
        for i in range(1, (num // 2) + 1):
            remainder = num % i
            #print(str(i) + " - " + str(remainder))
            if remainder == 0:
                total += i
        #print(divisors)

        return total == num
