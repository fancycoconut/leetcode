class MyStack:

    def __init__(self):
        self.queueA = []
        self.queueB = []

    def push(self, x: int) -> None:
        self.queueB.append(x)
        while len(self.queueA) > 0:
            self.queueB.append(self.queueA.pop(0))
        temp = self.queueA
        self.queueA = self.queueB
        self.queueB = temp

    def pop(self) -> int:
        return self.queueA.pop(0)

    def top(self) -> int:
        return self.queueA[0]

    def empty(self) -> bool:
        return len(self.queueA) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()