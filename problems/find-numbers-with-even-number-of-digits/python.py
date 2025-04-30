class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        numOfEvenDigits = 0

        for num in nums:
            numOfDigits = 0
            temp = num
            while temp > 0:
                temp = temp // 10
                numOfDigits += 1

            #print(str(num) + ' has ' + str(numOfDigits) + ' of digits')
            if numOfDigits % 2 == 0:
                numOfEvenDigits += 1
        
        return numOfEvenDigits