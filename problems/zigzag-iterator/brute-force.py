class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.queue = []
        vecs = []
        vecs.append(v1)
        vecs.append(v2)
        vecIndices = [0] * len(vecs)

        while self.canIterateVecs(vecs, vecIndices):
            for i in range(len(vecs)):
                vec = vecs[i]
                if vecIndices[i] >= len(vec):
                    continue
                val = vec[vecIndices[i]]
                vecIndices[i] += 1
                self.queue.append(val)

    def canIterateVecs(self, vecs: List[List[int]], vecIndices: List[int]) -> bool:
        canIterate = False

        for i in range(len(vecs)):
            vec = vecs[i]
            if vecIndices[i] < len(vec):
                canIterate = True

        return canIterate

    def next(self) -> int:
        return self.queue.pop(0)        

    def hasNext(self) -> bool:
        return len(self.queue) > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())