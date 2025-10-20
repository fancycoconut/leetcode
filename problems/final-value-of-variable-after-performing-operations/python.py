class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        output = 0
        for operation in operations:
            firstCharacter = operation[0]
            if firstCharacter == 'X':
                output = self.applyMathOperation(operation[1], output)
            else:
                output = self.applyMathOperation(operation[0], output)
        return output
            
    def applyMathOperation(self, operator: str, input: int) -> int:
        if operator == '+':
            return input + 1
        return input - 1
