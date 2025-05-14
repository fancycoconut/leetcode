class MovingAverage:

    def __init__(self, size: int):
        self.window = []
        self.windowSize = size
        

    def next(self, val: int) -> float:
        if len(self.window) < self.windowSize:
            self.window.append(val)
        else:
            self.window.pop(0)
            self.window.append(val)

        #print(self.window)
        return sum(self.window) / len(self.window)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)