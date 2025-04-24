class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        print(maxHeap)

        while len(maxHeap) > 1:
            x = abs(heapq.heappop(maxHeap))
            y = abs(heapq.heappop(maxHeap))
            if x == y:
                continue
            
            z = y - x
            heapq.heappush(maxHeap, z)

        return abs(maxHeap[0]) if len(maxHeap) == 1 else 0
