class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        results = []

        i = 0
        temp = ""
        for letter in s:
            if len(temp) % k == 0:
                results.append(temp)
                temp = ""
            temp += letter

        for i in range(k - len(temp)):
            temp += fill

        results.append(temp)
        
        return results[1:]
