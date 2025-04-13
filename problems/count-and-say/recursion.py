class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        digits = self.countAndSay(n - 1)
        rle = self.getRunLengthEncoding(digits)
        return rle
        
    def getRunLengthEncoding(self, digits: str) -> str:
        frequencies = [ [ digits[0], 1 ] ]

        for i in range(1, len(digits)):
            digit = digits[i]
            # If the last frequency pair in the array is equal to the current digit
            # increment the value
            if frequencies[-1][0] == digit:
                frequencies[-1][1] += 1
            else:
                # Add a new frequency for a new digit
                frequencies.append([digit, 1])
        
        output = ""
        for freq in frequencies:
            output += str(freq[1]) + freq[0]
        #print(output)

        return output
