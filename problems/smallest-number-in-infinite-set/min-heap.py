class SmallestInfiniteSet:
    numberSet = set()
    minHeap = []

    def __init__(self):
        self.minHeap.clear()
        for i in range(1, 1001):
            self.minHeap.append(i)
            self.numberSet.add(i)

        heapq.heapify(self.minHeap)

    def popSmallest(self) -> int:
        if len(self.minHeap) == 0:
            return 0

        smallest = heapq.heappop(self.minHeap)
        heapq.heapify(self.minHeap)
        if smallest in self.numberSet:
            self.numberSet.remove(smallest)

        return smallest

    def addBack(self, num: int) -> None:
        if num not in self.numberSet:
            self.numberSet.add(num)
            heapq.heappush(self.minHeap, num)
            heapq.heapify(self.minHeap)
        return None


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)