import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for point in points:
            a = pow(point[0], 2)
            b = pow(point[1], 2)
            c = math.sqrt(a + b)

            heapq.heappush(minHeap, (c, point[0], point[1]))

        output = []
        for i in range(k):
            item = heapq.heappop(minHeap)
            output.append((item[1], item[2]))

        return output
