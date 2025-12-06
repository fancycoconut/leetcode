class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")

        output = []
        for i in range(len(words) - 1, -1, -1):
            word = words[i].strip()
            if word == "":
                continue
            
            output.append(word)

        return " ".join(output)