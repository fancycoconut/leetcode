class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        numOfTimes = 0

        substring = word
        while sequence.find(substring) > -1:
            if sequence.find(substring) >= 0:
                numOfTimes += 1
                substring += word

        return numOfTimes