class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for letter in s:
            if len(stack) > 0 and stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)

        print(stack)
        output = ""
        for letter in stack:
            output += letter

        return output