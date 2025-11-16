class Solution:
    def numSub(self, s: str) -> int:
        substrings = []

        substring = ""
        for i in range(len(s)):
            letter = s[i]
            if letter == "1":
                substring += letter
                continue
            
            if len(substring) > 0:
                substrings.append(substring)
            substring = ""
        if len(substring) > 0:
                substrings.append(substring)
        #print(substrings)

        numOfSubstrings = 0
        for substring in substrings:
            length = len(substring)
            #print(length)
            total = self.getNumberOfOnes(length)
            # Modulus for large numbers
            total = total % (10**9 + 7)
            numOfSubstrings += total
        return numOfSubstrings

    def getNumberOfOnes(self, length: int) -> int:
        return (length  + 1) * length // 2
