class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")

        output = []
        for word in words:
            output.append(self.reverseWord(word))
        #print(output)

        return " ".join(output)
        
    def reverseWord(self, s: str) -> str:
        output = []
        for letter in s:
            output.append(letter)
        return "".join(reversed(output))