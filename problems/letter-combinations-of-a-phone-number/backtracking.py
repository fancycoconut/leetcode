class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        phoneMap = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        letters = ""
        for digit in digits:
            if digit not in phoneMap:
                continue
            letters += phoneMap[digit]
        #print(candidates)

        subset = []
        results = []
        visited = set()

        self.backtrack(0, digits, phoneMap, subset, results)

        return results

    def backtrack(self, index: int, digits, phoneMap: Dict[str, str], subset: List[str], results: List[str]):
        if len(subset) == len(digits):
            results.append("".join(subset))
            return

        if index >= len(digits):
            return

        digit = digits[index]
        letters = phoneMap[digit]
        for letter in letters:
            subset.append(letter)

            self.backtrack(index + 1, digits, phoneMap, subset, results)

            subset.pop()
