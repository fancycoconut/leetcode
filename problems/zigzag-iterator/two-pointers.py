# Two Pointers
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vecs = [v1, v2]
        self.currentVecPosition = 0
        self.currentElementPosition = 0

        self.numOfElementsRead = 0
        self.totalNumOfElements = len(v1) + len(v2)

    def next(self) -> int:
        i = 0
        returnValue = None

        while i < len(self.vecs):
            vec = self.vecs[self.currentVecPosition]
            if self.currentElementPosition < len(vec):
                returnValue = vec[self.currentElementPosition]
            
            i += 1
            self.currentVecPosition = (self.currentVecPosition + 1) % len(self.vecs)
            # Increment the element pointer once iterating all vectors
            if self.currentVecPosition == 0:
                self.currentElementPosition += 1

            if returnValue is not None:
                self.numOfElementsRead += 1
                return returnValue
        
        raise Exception("No more elements to process")

    def hasNext(self) -> bool:
        return self.numOfElementsRead < self.totalNumOfElements

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())