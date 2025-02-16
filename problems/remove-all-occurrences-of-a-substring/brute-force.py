class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        temp = s
        while temp.find(part) > -1:
            temp = temp.replace(part, "", 1)
            #print(temp)
        return temp
        