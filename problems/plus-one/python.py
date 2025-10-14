class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        numberAsString = ""
        for digit in digits:
            numberAsString += str(digit)
        print(numberAsString)

        num = int(numberAsString)
        res = str(num + 1)

        return [ int(letter) for letter in res ]
