class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)

        output = 0
        for i in range(0, k):
            output = -heapq.heappop(maxHeap)
            print(output)

        return output