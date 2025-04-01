class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []

        for token in tokens:
            match token:
                case "+":
                    self.evalPlus(stack)
                case "-":
                    self.evalSubtract(stack)
                case "*":
                    self.evalMultiply(stack)
                case "/":
                    self.evalDivide(stack)
                case _:
                    stack.append(token)

        return stack.pop()

    def evalPlus(self, stack: List[str]):
        a = int(stack.pop())
        b = int(stack.pop())
        res = a + b
        stack.append(res)

    def evalMultiply(self, stack: List[str]):
        a = int(stack.pop())
        b = int(stack.pop())
        res = a * b
        stack.append(res)

    def evalSubtract(self, stack: List[str]):
        a = int(stack.pop())
        b = int(stack.pop())
        res = b - a
        stack.append(res)

    def evalDivide(self, stack: List[str]):
        a = int(stack.pop())
        b = int(stack.pop())
        res = int(b / a)
        stack.append(res)
