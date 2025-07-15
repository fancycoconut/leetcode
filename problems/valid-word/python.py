class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        if self.hasNumbers(word) == False and self.hasAlphabets(word) == False:
            return False

        print(self.getNumOfVowels(word))
        if self.getNumOfVowels(word) < 1:
            return False

        print(self.getNumOfConsonants(word))
        if self.getNumOfConsonants(word) < 1:
            return False

        if self.hasSpecialCharacters(word):
            return False

        return True

    def hasAlphabets(self, word: str) -> bool:
        hasAlphabets = False
        for letter in word:
            if letter.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                hasAlphabets = True
        return hasAlphabets

    def hasNumbers(self, word: str) -> bool:
        hasNumbers = False
        for letter in word:
            if letter in "0123456789":
                hasNumbers = True
        return hasNumbers

    def getNumOfVowels(self, word: str) -> int:
        numOfVowels = 0
        for letter in word:
            l = letter.upper()
            if l in "AEIOU" and l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                numOfVowels += 1
        return numOfVowels

    def getNumOfConsonants(self, word: str) -> int:
        numOfConsonants = 0
        for letter in word:
            l = letter.upper()
            if l not in "AEIOU" and l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                numOfConsonants += 1
        return numOfConsonants

    def hasSpecialCharacters(self, word: str) -> int:
        hasSpecial = False
        for letter in word:
            if letter in "@#$":
                hasSpecial = True
        return hasSpecial
