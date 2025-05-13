class MyQueue:

    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, x: int) -> None:
        while len(self.stackA) > 0:
            self.stackB.append(self.stackA.pop(0))
        self.stackB.append(x)

        temp = self.stackB
        self.stackB = self.stackA
        self.stackA = temp

    def pop(self) -> int:
        return self.stackA.pop(0)

    def peek(self) -> int:
        return self.stackA[0]

    def empty(self) -> bool:
        return len(self.stackA) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()