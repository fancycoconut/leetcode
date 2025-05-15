class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.currentVec = 0
        self.currentElementPosition = 0
        self.numOfElementsRead = 0
        self.totalNumOfElements = 0
        for v in vec:
            self.totalNumOfElements += len(v)

    def next(self) -> int:
        i = 0
        returnVal = None
        
        while i < len(self.vec):
            vec = self.vec[self.currentVec]
            if self.currentElementPosition < len(vec):
                returnVal = vec[self.currentElementPosition]
                self.currentElementPosition += 1
                self.numOfElementsRead += 1

            i += 1
            if self.currentElementPosition >= len(vec):
                self.currentElementPosition = 0
                self.currentVec += 1

            if returnVal is not None:
                return returnVal

        raise Exception("No more elements to read")

    def hasNext(self) -> bool:
        return self.numOfElementsRead < self.totalNumOfElements

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()